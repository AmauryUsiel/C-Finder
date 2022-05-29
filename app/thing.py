from curses.ascii import HT
from django.http import HttpResponse

# Primera vista, devolver una respuesta

def vistalogin(request):

    documento = """<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>C-Finder</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    </head>
    <body  style="height: 100px; background:linear-gradient(96deg, rgba(90, 226, 250, 0.637), rgba(111, 0, 255, 0.671), rgba(221, 82, 221, 0.726));" >
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

        <div class="container"> p
                <div class="row m">

                    <!--Espaciado-->
                    <div class="col">
                        
                    </div>

                    <!--Formulario-->
                    <div class="col">
                        <div class="text-end">

                            <h2 class="fw-bold text-center py-4">Login</h2>

                            <!--Login-->
                            <form action="#">
                                <!--Correo-->
                                <div class="md-5 text-start">
                                    <label for="correo" class="form-label fw-bold">
                                        Correo Electronico
                                    </label>
                                    <input type="correo" class="form-control" name="correo" placeholder="Ingrese el correo electronico">
                                </div>
                                
                                <!--Contraseña-->
                                <div class="md-5 text-start">
                                    <label for="contraseña" class="form-label fw-bold">
                                        Contraseña
                                    </label>
                                    <input type="contraseña" class="form-control" name="contraseña" placeholder="Ingrese su contraseña">
                                </div>

                                <!--Conexion-->
                                <div class="ms-5">
                                    <input type="checkbox" name="conectado" class="form-check-input">
                                    <label for="conectado" class="form-check-label">
                                        Mantenerme Conectado <br>
                                    </label>
                                </div>
                                
                                <!--Boton de inicio-->
                                <div class="d-grid">
                                    <button type="submit" class="btn btn-primary text-center"> 
                                        Iniciar Sesion <br><br>
                                    </button>                                
                                </div>

                                <!--Extras-->
                                <div class="my-3">
                                    <!--Contraseña olvidada-->
                                    <span class="fw-bold">
                                        <a href="#" style="color: black ;">
                                            Olvide mi contraseña <br>
                                        </a>
                                    </span>
                                

                                    <!--No tengo cuenta-->
                                    <span class="fw-bold">
                                        ¿No tienes cuenta?
                                        <a href="#" style="color: black ;">
                                            Registrate aqui <br><br>
                                        </a>
                                    </span>

                                    <!--Iniciar como invitado-->
                                    <span class="btn btn-sm">
                                        <a href="#" style="color: black ;">
                                            Iniciar como invitado 
                                        </a>
                                    </span>
                                </div>
                                
                            </form>
                        </div>
                    </div>
                </div>
        </div>
    </body>
</html>"""

    return HttpResponse(documento)

def vistaprofesor(request):

    documento = """<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>C-Finder</title>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <link rel="shortcut icon" href="C-Finder_vector_logo.png">
    </head>
    <body  style="height: 100px; background:linear-gradient(160deg, rgba(158, 158, 158, 0.24), rgba(136, 196, 252, 0.664));" >
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

        <div class="container">
                <div class="row align-items-center">

                    <!--Vista Previa-->
                    <div class="col align-items-center">
                        <!--Titulo-->
                        <h3 class="fw-bold text-center py-4">Vista previa</h3>

                        <!--Vista-->
                        <div class="card">
                            <h5 class="card-header">Titulo</h5>
                            <div class="card-body">
                              <h5 class="card-title">Tema </h5>
                              <p class="card-text">En este curso podremos apreciar...</p>
                              <img src="login_botrep.jpg" width="500" alt="">
                            </div>
                        </div>

                        <div class="mb-4 text-start">
                            <label for="videocomp" class="form-label fw-bold">Sube la imagen de previsualizacion de tu video</label>
                            <input class="form-control" type="file" id="videocomp" accept=".jpg, .png">
                        </div>
                    </div>

                    <!--Formulario-->
                    <div class="col">
                        <div class="text-end">
                            <img src="logpng.png" width="40" height="40" alt="">
                            <label for="" class="fw-bold">Usuario</label>
                            <img src="C-Finder_vector_logo.png" width="120" alt="" >

                            <h2 class="fw-bold text-center py-4">Subida de Cursos</h2>

                            <form action="#">

                                <!--Informacion General-->

                                <!--Titulo-->
                                <div class="md-4 text-start">
                                    <label for="vidname" class="form-label fw-bold">
                                        Titulo del Video
                                    </label>
                                    <input type="vidname" class="form-control" name="vidname" placeholder="Ingrese el titulo del video">
                                </div>

                                <!--Temas-->
                                <div class="md-4 text-start">
                                    <label for="vidtem" class="form-label fw-bold">
                                        Temas del video
                                    </label>
                                    <input type="vidtem" class="form-control" name="vidtem" placeholder="Ingrese los temas vistos en el video">
                                </div>

                                <!--Descipcion-->
                                <div class="md-4 text-start"> 
                                    <label for="viddesc" class="form-label fw-bold">Descripcion del video</label>
                                    <textarea class="form-control" rows="5" id="viddesc" placeholder="Ingrese una breve descripcion del video"></textarea>
                                  </div>

                                <!--Seleccionar archivo-->
                                <div class="mb-4 text-start">
                                    <label for="videocomp" class="form-label fw-bold">Sube tu archivo</label>
                                    <input class="form-control" type="file" id="videocomp" accept=".mp4, .mov, .avi">
                                </div>

                                <!--Boton de subida-->
                                <div class="d-grid">
                                    <button type="submit" class="btn btn-primary text-center"> 
                                        Publicar
                                    </button>                                
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
        </div>
    </body>
</html>"""

    return HttpResponse(documento)
