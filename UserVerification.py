import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def send_passcode_email(email: str, passcode: str):
    sender_email = "tuemail@gmail.com"  # Reemplaza con tu correo
    receiver_email = email
    password = "tu_contraseña"  # Reemplaza con tu contraseña de correo

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

def generate_and_send_passcode(email: str):
    passcode = str(random.randint(100000, 999999))  # Generar passcode aleatorio
    send_passcode_email(email, passcode)
    return passcode
