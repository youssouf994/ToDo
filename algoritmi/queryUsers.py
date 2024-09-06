import sqlite3
import bcrypt

class qUsers:
    def confrontoMail(db,nome, cognome, azienda, mail, passw, reparto):
        cursore=db.cursor()
        

        cursore.execute('SELECT * FROM users WHERE mail=?', (mail,))
        
        if cursore.fetchone() is not None:
           return False
        
        else:
            #-----------CODIFICA VALORI INSERITI--------------
            pass_codificata=bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt())
            #-----------------------------------------------------------

            cursore.execute('INSERT INTO users (nome, cognome, azienda, mail, passw, reparto) VALUES (?, ?, ?, ?, ?, ?)', (nome, cognome, azienda, mail, pass_codificata, reparto))
            
            db.commit()
            db.close()
            
            return True
        

    def login(db, mail, passwd):
        cursore=db.cursor()

        cursore.execute('SELECT * FROM users WHERE mail=?', (mail,))
        trovato_nome=cursore.fetchone()
        
        db.close()
        

        if trovato_nome is not None and bcrypt.checkpw(passwd, trovato_nome[5]):
            sessione=trovato_nome[0]      
            return sessione
           
        else:
            trovato_nome=None
            return False