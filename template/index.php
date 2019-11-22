<!DOCTYPE HTML>
<html>
	<head>
		<title>Python Web</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link  href="{{ url_for('static', filename='style.css') }}"  rel="stylesheet">
                <link  rel="stylesheet" href="{{ url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css') }}" >
          
                <script src="{{ url_for('static', filename='jquery.min.js') }}" ></script>
                <script src="{{ url_for('static', filename='jquery.poptrox.min.js') }}"></script>
                <script src="{{ url_for('static', filename='browser.min.js') }}"></script>
                <script src="{{ url_for('static', filename='breakpoints.min.js') }}"></script>
                <script src="{{ url_for('static', filename='util.js') }}"></script>
                <script src="{{ url_for('static', filename='main.js') }}"></script>
                <script src="{{ url_for('static', filename='vendor/jquery/jquery.min.js') }}"></script>
                <script src="{{ url_for('static', filename='vendor/bootstrap/js/bootstrap.bundle.min.js') }}"></script>
        </head>               
	<body class="is-preload">
            <!-- Button trigger modal -->


		<!-- Header -->
			<header id="header">
					<a href="#" class="image avatar"><img src="{{ url_for('static', filename='images/avatar.png') }}" alt="" /></a>
					<h1><strong>Estancias I: </strong>, Nuesto Proyecto<br>
					Es un sitio web desarrollado en python para<br>
                                        <a>El Sistema de citas de la Universidad Politecnica</a>.</h1>
				</div>
			</header>

		<!-- Main -->
			<div id="main">
				<!-- One -->
					<section id="one">
						<header class="major">
							<h2>Proyecto Implementacion de un Modulo-Api GoogleCalendar Para Sistemas de Citas.</h2>
						</header>
						<p>
                            cd C:\Users\Luis\AppData\Local\Programs\Python\Python37<br>
                                                </p>
                           <h1> Librerias instaladas</h1><br><p>
                            
                            pip install requests<br>

                            python -m pip install --upgrade pip<br>

                            pip3 install requests<br>

                            pip install google-api-python-client<br>

                            actualizar pip install --upgrade google-api-python-client<br>

                            pip install google-auth-oauthlib<br>

                            pip install --upgrade google-auth-oauthlib<br>

                            pip install datefinder<br>

                            pip install oauth2client<br>
                            <h1>
                                instalacion de libreria para correo</h1><p><br>
                            pip install smtplib<br>


                            ---------------------------------------------------<br>
                            uso de la libreria flask<br>

                            py -m venv nombre de Carpeta o Proyecto<br>

                            cd nombre de Carpeta o Proyecto\Scripts<br>

                            ACTIVATE<br>

                            pip  install flask<br>

                            Set FLASK_APP=nombre de archivo.py<br>

                            flask run<br>

                            entrar al servidor 127.0.0.1:5000<br>

                            api en flask<br></p><p>
                            <h1>--instalaciones</h1><br>
                            pip install -U Flask<br>
                            pip install flask_restful<br>
                            <h1>---librerias</h1><br>
                            from flask import Flask<br>
                            from flask_restful import Resource, Api.<br>
					</section>
                                <div class="inner">
                                    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#Agregar">Eventos</button>
                                    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#EnviarGmail">Gmail</button>
                                </div>
				<!-- Two -->
                                
                                   
                                
</div>
                               
			<div class="modal fade" id="EnviarGmail" tabindex="-1" role="dialog" aria-labelledby="EnviarGmail" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="EnviarGmail">Enviar Gmail</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <label>
              
          </label>
        <br>
        <form method="POST">
            <input type="email" name="correo" placeholder="Email Destino" />
            <input type="password" name="pass" placeholder="Contraseña" />
                 <textarea name="Mensaje" placeholder="Mensaje" rows="10"></textarea>
                 <input class="btn btn-secondary" type="submit" name="messenger" value="Enviar" />
              
        </form>
        
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
      </div>
    
      
    </div>
  </div>
</div>
                        </div>             
      
                <div class="modal fade" id="Agregar" tabindex="-1" role="dialog" aria-labelledby="Agregar" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="Agregar">Agregar un Evento</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <label>
              
          </label>
        <br>
        <form method="POST">
            <div class="form-group">
            <input type="text"  name="nEvento" placeholder="Nombre del evento" />
                                                                                   
            <input type="text" name="uEvento" placeholder="Ubicacion del evento" />
            <textarea name="dEvento" placeholder="Descripcion" rows="10"></textarea>
            <input type="text" name="year" placeholder="Ano">
            <input type="text" name="mes" placeholder="Mes" >
            <input type="text" name="dia" placeholder="Dia">
            <input class="form-control" type="number" min="0" max="24" name="hora" placeholder="Hora">
            <input class="form-control" type="number" min="0" max="59" name="minutos" placeholder="Minutos">
                                                                                    
            </div>
        
                 <input class="btn btn-secondary" type="submit" name="Event" value="Evento" />
        </form>                   
    <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
      </div>
      </div>
      
    </div>
  </div>
</div>
	
	</body>
</html>
                                                                   