#-----------------------------------------API----------------------------------
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pickle
import re
import os.path
import os
import array as arr
import requests

#-----------------------------------------Flask--------------------------------
from flask import Flask, request, redirect
from flask import render_template
#-----------------------------------------Clases-------------------------------
        

class GoogleCalendar:
        def __init__(self):
                print('Class Calendario Iniciada')
                print('Acceso Google Calendar')
                self.Matricula="1730505"
                permiso = ['https://www.googleapis.com/auth/calendar']
                Credencial = None
                if os.path.exists(self.Matricula+'.pkl'):
                   with open(self.Matricula+'.pkl', "rb") as token:
                        Credencial = pickle.load(token)
                if not Credencial or not Credencial.valid:
                        if Credencial and Credencial.expired and Credencial.refresh_token:
                                Credencial.refresh(Request())
                        else:
                                IDOAuth = InstalledAppFlow.from_client_secrets_file("secreto_cliente.json", scopes=permiso)
                                Credencial = IDOAuth.run_local_server(port=5000)
                                with open(self.Matricula+'.pkl', 'wb') as token:
                                        pickle.dump(Credencial, token)
                self.Servicio=build("calendar", "v3", credentials=Credencial)

                
        def CrearEvento(self, Nombre, Ubicacion, Describcion, year, mes, dia, hora, minu):
                self.year=int(year)
                self.mes=int(mes)
                self.dia=int(dia)
                self.hora=int(hora)
                self.minu=int(minu)
                print('Crear evento')
                result = self.Servicio.calendarList().list().execute()
                calendar_id = result['items'][0]['id']
                timezone =result['items'][0]['timeZone']
                result = self.Servicio.events().list(calendarId=calendar_id, timeZone=timezone)
                Hora_inicio = datetime(year, mes, dia, hora, minu, 0)
                Hora_final = Hora_inicio + timedelta(hours=4)
                event = {
                  'summary': Nombre,
                  'location': Ubicacion,
                  'description': Describcion,
                  'start': {
                    'dateTime': Hora_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                    'timeZone': timezone,
                  },
                  'end': {
                    'dateTime': Hora_final.strftime("%Y-%m-%dT%H:%M:%S"),
                    'timeZone': timezone,
                  },
                  'reminders': {
                    'useDefault': False,
                    'overrides': [
                      {'method': 'email', 'minutes': 24 * 60},
                      {'method': 'popup', 'minutes': 10},
                   ],
                  },
                }
                self.Servicio.events().insert(calendarId=calendar_id, body=event, sendNotifications=True).execute()

        def ConsultarEventos(self):
                result = self.Servicio.calendarList().list().execute()
                calendar_id = result['items'][0]['id']
                Pagina = None
                result =self.Servicio.events().list(calendarId=calendar_id, pageToken=Pagina).execute()
                BAND=True
                try:
                        arr_event = []
                        while BAND==True:
                         for Eventos in result['items']:
                             arr_event.append(Eventos['summary'])
                             prueba=Eventos.get('nextPageToken')
                             if not prueba:
                               BAND=False
                except:
                       return "No hay eventos"
                return arr_event

        def ServiciosExtras(self):
                return self.Servicio

class Gmail(GoogleCalendar):
         def __init__(self):
                print('Class Gmail Iniciada')
                Conexion=GoogleCalendar()
                self.Servicio=Conexion.ServiciosExtras()
                print('Acceso Gmail')
                self.ServicioG=smtplib.SMTP_SSL(host='smtp.gmail.com', port=465 )               
        
         def CrearMensaje(self, Hacia, Mensaje, Contra):
                print('Crear Mensaje')
                result = self.Servicio.calendarList().list().execute()
                Correo =result['items'][0]['summary']
                print(Correo)
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',Correo.lower()):
                        print("Correo correcto")
                        self.ServicioG.ehlo()
                        self.ServicioG.login(Correo, Contra)
                else:
                        print("Correo incorrecto")
                Msg = MIMEMultipart()
                print('Enviado por: ',Correo)
                Msg['From']=Correo
                if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',Hacia.lower()):
                        print("Correo correcto")
                        Msg['To']= Hacia
                        Msg['Subject']='Invitacion'
                        Msg.attach(MIMEText(Mensaje, 'plain'))
                        self.ServicioG.send_message(Msg)
                        del Msg
                        self.ServicioG.quit()
                        (print("Enviado !!!"))
                else:
                        print("Correo incorrecto")

#--------------------------------------Main------------------------------------
    
                        
app = Flask(__name__, template_folder = 'template',static_folder = 'template/static')

@app.route('/', methods = ['GET', 'POST', 'DELETE'])

def index():
    api=GoogleCalendar()
    api=Gmail()
    if request.method == 'POST':
        if request.form.get('Event')=='Evento':
                Nombre=str(request.form.get('nEvento'))
                Ubicacion=str(request.form.get('uEvento'))
                Describcion=str(request.form.get('dEvento'))
                year=int(request.form.get('year'))
                mes=int(request.form.get('mes'))
                dia=int(request.form.get('dia'))
                hora=int(request.form.get('hora'))
                minu=int(request.form.get('minutos'))
                print(Nombre ,' ', Ubicacion ,' ', Describcion ,' ', year ,' ', mes ,' ', dia ,' ', hora ,' ', minu)
                api.CrearEvento(Nombre, Ubicacion, Describcion, year, mes, dia, hora, minu)
                api.ConsultarEventos()
        if request.form.get('messenger')=='Enviar':
                Hacia=str(request.form.get('correo'))
                Contra=str(request.form.get('pass'))
                Mensaje=str(request.form.get('Mensaje'))
                api.CrearMensaje( Hacia, Mensaje, Contra)
    return render_template('index.php')
        
if __name__ == '__main__':
        app.run(debug=True)
