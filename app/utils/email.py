import yagmail
import os

def enviar_correo(destinatario, usuario, contrasena):
    try:
        remitente = os.getenv("EMAIL_REMITENTE")
        clave = os.getenv("EMAIL_CLAVE")

        if not remitente or not clave:
            raise ValueError("Faltan variables de entorno EMAIL_REMITENTE o EMAIL_CLAVE")

        yag = yagmail.SMTP(remitente, clave)

        asunto = "Credenciales de acceso - Plataforma SENA"
        contenido = f"""
        Hola, has sido registrado exitosamente en la plataforma de guías SENA.
        
        Tus credenciales de acceso son:
        Usuario: {usuario}
        Contraseña: {contrasena}
        
        Puedes iniciar sesión en la aplicación.
        """

        yag.send(to=destinatario, subject=asunto, contents=contenido)
        print(f"Correo enviado a {destinatario}")

    except Exception as e:
        print("Error al enviar correo:", e)
