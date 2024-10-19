import yagmail
class GestioneMessaggi:
    
    def __init__(self, mailDiInvio, passwordMail):
        self.mailDiInvio=mailDiInvio
        self.passwordMail=passwordMail
        

    def inviaAvviso(self, oggetto, testo, mailDestinatario):

        # Creazione dell'oggetto yagmail
        yag = yagmail.SMTP(self.mailDiInvio, self.passwordMail)

        # Invio dell'email
        yag.send(to=mailDestinatario, oggetto='Oggetto dell\'email', testo='Questo è il corpo dell\'email.')
        print('Email inviata con successo!')
