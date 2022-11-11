from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    """hello_world Saludo de inicio

    :return: Devuelve el saludo de inicio de la api
    :rtype: str
    """
    return 'Pagina Inicio!'


@app.route('/logs')
def mostrar_logs() -> list:
    """mostrar_logs Devuelve los registros del archivo error_logging.log

    :return: Lista de errores registrados
    :rtype: list
    """

    with open(r"logs/error_loggin.log", "r") as f:
        return f.read().split("\n")
