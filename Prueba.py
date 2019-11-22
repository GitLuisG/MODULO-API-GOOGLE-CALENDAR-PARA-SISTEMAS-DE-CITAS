from EstanciaI import *
# json file leer

Hacia='estanciaupv@gmail.com'
Mensaje="Hola a todos y muchos Saludos"
Nombre ='Vida salvaje'
Ubicacion ='Mexico'
Describcion ='Solo para gatos'
year =int('2019')
mes =int('10')
dia =int('28')
hora =int('12')
minu=int('00')


con=GoogleCalendar()
con.CrearEvento(Nombre, Ubicacion, Describcion, year, mes, dia, hora, minu)
con.ConsultarEventos()
