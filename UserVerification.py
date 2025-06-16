import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()  # Asegúrate de tener un archivo .env con las variables de entorno

# Usar un diccionario para almacenar passcodes temporales (esto debería ser reemplazado por una base de datos en producción)
passcodes = {}

# Función para enviar el passcode al correo electrónico
def send_passcode_email(email: str, passcode: str):
    sender_email = os.getenv("bssdatos@gmail.com")  # Correo desde una variable de entorno
    password = os.getenv("password123/")  # Contraseña del correo desde una variable de entorno
    receiver_email = email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Verificación de correo electrónico"

    body = f"Tu passcode es: {passcode}. Por favor, ingrésalo para completar la verificación."
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
    except Exception as e:
        raise Exception(f"Error al enviar el correo: {str(e)}")

# Función para generar y enviar el passcode
def generate_and_send_passcode(email: str):
    passcode = str(random.randint(100000, 999999))  # Genera un passcode aleatorio
    passcodes[email] = passcode  # Almacena el passcode generado para la verificación
    send_passcode_email(email, passcode)  # Enviar el passcode por correo
    return passcode

# Función para verificar el passcode ingresado
def verify_passcode(entered_passcode: str, email: str):
    stored_passcode = passcodes.get(email)  # Obtiene el passcode almacenado para ese correo
    if stored_passcode and stored_passcode == entered_passcode:
        del passcodes[email]  # Elimina el passcode después de la verificación
        return True
    return False
