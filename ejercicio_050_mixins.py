class Invitado:
    def __init__(self, nombre, email, numero_telefono):
        self.nombre = nombre
        self.email = email
        self.numero_telefono = numero_telefono

class EmailManager:
    def send_email(self, destino, asunto, mensaje):
        pass

class WhatsAppManager:
    def send_whatsapp(self, numero_telefono, mensaje):
        pass

class InvitacionBoda(EmailManager, WhatsAppManager):
    def __init__(self, invitado : Invitado, texto, numero_cuenta):
        self.invitado = invitado

invitacion = InvitacionBoda(Invitado('Abel','abel@gmail.com','630881100'), 'Abel, estamos encantados...', 'IBAN383-3838-8383')
invitacion.send_email(invitacion.invitado.email, 'Invitación a mi boda', 'Bla, bla, bla...')
invitacion.send_whatsapp(invitacion.invitado.numero_telefono, 'Te invito, lo siento...')