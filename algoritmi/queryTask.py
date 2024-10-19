class qTask:
    def visualizzaTuttePerReparto(db, idU):
          cursore = db.cursor()
          tabella="task"

          query="SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE u_creatore.id_utente=?;"
          cursore.execute(query, (idU,))
          taskReparto = cursore.fetchall()
          
          return taskReparto
    
    def visualizzaTutteCompletate(db, idU):
          cursore = db.cursor()

          query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=1 AND u_creatore.id_utente=?;")
          cursore.execute(query, (idU,))
          taskCompletate = cursore.fetchall()
          
          return taskCompletate
    
    def visualizzaTutteDaCompletare(db, idU):
          cursore = db.cursor()

          query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=0 AND u_creatore.id_utente=?;")
          cursore.execute(query, (idU,))
          taskDaCompletare = cursore.fetchall()
          
          return taskDaCompletare
    
    def visualizzaTutteSospese(db, idU):
          cursore = db.cursor()

          query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=2 AND u_creatore.id_utente=?;")
          cursore.execute(query, (idU,))
          taskSospese = cursore.fetchall()
          
          return taskSospese

    def visualizzaTutteAssegnatemi(db, idU):
              cursore = db.cursor()
              tabella="task"

              query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=1 AND t.assegnatoA= ? AND t.id_utente!= ?;")
              cursore.execute(query, (idU, idU, ))
              taskReparto = cursore.fetchall()
          
              return taskReparto
    
    def visualizzaTutteCompletateAssegnatemi(db, idU):
          cursore = db.cursor()

          query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=1 AND t.assegnatoA= ? AND t.id_utente!= ?;")
          cursore.execute(query, (idU, idU, ))
          taskCompletate = cursore.fetchall()
          
          return taskCompletate
    
    def visualizzaTutteDaCompletareAssegnatemi(db, idU):
          cursore = db.cursor()

          query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=0 AND t.assegnatoA= ? AND t.id_utente!= ?;")
          cursore.execute(query, (idU, idU, ))
          taskDaCompletare = cursore.fetchall()
          
          return taskDaCompletare
    
    def visualizzaTutteSospeseAssegnatemi(db, idU):
          cursore = db.cursor()

          query=(f"SELECT t.id_task, t.titolo, t.descrizione, t.priorità, u_creatore.nome AS daNome, u_creatore.cognome AS daCognome, u_creatore.reparto AS daReparto, u_assegnato.nome AS aNome, u_assegnato.cognome AS aCognome, u_assegnato.reparto AS aReparto, t.data, t.ora, t.stato, t.luogo FROM task t JOIN users u_creatore ON t.id_utente = u_creatore.id_utente LEFT JOIN users u_assegnato ON t.assegnatoA= u_assegnato.id_utente WHERE t.stato=2 AND t.assegnatoA= ? AND t.id_utente!= ?;")
          cursore.execute(query, (idU, idU, ))
          taskSospese = cursore.fetchall()
          
          return taskSospese
    
    def recuperaRepartoUtente(db, idU):
        cursore=db.cursor()
         
        tabella="users"
         
        cursore.execute(f"SELECT * FROM {tabella} WHERE id_utente=?", (idU,))
        idRep=cursore.fetchone()
         
        return idRep[6]   
    
    def aggiungiTask(db, titolo, descrizione, priorità, inseritoDa, assegnatoA, stato, luogo, data, ora):
        cursore=db.cursor()
        
        tabella="task"
        
        cursore.execute(f"INSERT INTO {tabella} (titolo, descrizione, priorità, id_utente, assegnatoA, stato, luogo, data, ora) VALUES (?,?,?,?,?,?,?,?,?)", (titolo, descrizione, priorità, inseritoDa, assegnatoA, stato, luogo, data, ora))
        db.commit()
    

    def modificaCampo(db, idUser, nuovo, tabella, colonna, idVecchio):
        # Costruire la query di aggiornamento in modo dinamico
        query = (f"UPDATE {tabella} SET {colonna} = ? WHERE id_utente = ?", (colonna, idVecchio))

        # Eseguire l'aggiornamento con parametri
        db.execute(query, (nuovo, idUser, idVecchio))
        db.commit()
        print(f"Campo {colonna} aggiornato correttamente in {tabella}.")
        
