# Alkemy-Unidad17
Acceso a otros origenes de datos


Se siguen los pasos para una primer App con flask
- Los pasos se remiten a :
https://j2logo.com/leccion-1-la-primera-aplicacion-flask/

Como ejemplo se define una api con 2 funciones
1) Saludo inicial de la api
2) Apertura de un archivo de log y muestra del mismo en la interfaz web

##PASOS PARA SIMULAR LA PRUEBA

1) Crear un entorno virtual (venv)
2) Modificar el archivo activate de nuestro entorno agregando:
export FLASK_APP="Alkemy-Unidad17/app.py"   
> Hay que tener en cuenta que la ruta puede cambiar en funcion de donde se cree el entorno virtual
3) Se debe instalar Flask , se puede conseguir mediante 
pip install -r requirements.txt
4) Ejecutamos flask run

Podremos visualizar en :
http://127.0.0.1:5000/
El mensaje de bienvenida

http://127.0.0.1:5000/logs
Los errores loggeados



