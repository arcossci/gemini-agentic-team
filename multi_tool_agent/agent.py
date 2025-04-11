import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

def obtener_clima(ciudad: str) -> dict:
    """Obtiene el reporte del clima actual para una ciudad específica.
    Args:
        ciudad (str): El nombre de la ciudad para la cual se obtendrá el reporte del clima.
    Returns:
        dict: estado y resultado o mensaje de error.
    """
    if ciudad.lower() == "new york":
        return {
            "estado": "éxito",
            "reporte": (
                "El clima en Nueva York es soleado con una temperatura de 25 grados"
                " Celsius (41 grados Fahrenheit)."
            ),
        }
    elif ciudad.lower() == "Pasto":
        return {
            "estado": "éxito",
            "reporte": (
                "El clima en Nueva York es soleado con una temperatura de 17 grados"
            ),
        }
    else:
        return {
            "estado": "error",
            "mensaje_error": f"La información del clima para '{ciudad}' no está disponible.",
        }


def obtener_hora_actual(ciudad: str) -> dict:
    """Devuelve la hora actual en una ciudad específica.
    Args:
        ciudad (str): El nombre de la ciudad para la cual se obtendrá la hora actual.
    Returns:
        dict: estado y resultado o mensaje de error.
    """

    if ciudad.lower() == "new york":
        identificador_zona_horaria = "America/New_York"
    else:
        return {
            "estado": "error",
            "mensaje_error": (
                f"Lo siento, no tengo información de la zona horaria para {ciudad}."
            ),
        }

    zona_horaria = ZoneInfo(identificador_zona_horaria)
    ahora = datetime.datetime.now(zona_horaria)
    reporte = (
        f'La hora actual en {ciudad} es {ahora.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"estado": "éxito", "reporte": reporte}


root_agent = Agent(
    name="agente_clima_hora",
    model="gemini-2.0-flash-exp",
    description=(
        "Agente para responder preguntas sobre la hora y el clima en una ciudad"
    ),
    instruction=(
        "Responde preguntas sobre la hora y el clima en una ciudad"
    ),
    tools=[obtener_clima, obtener_hora_actual],
)