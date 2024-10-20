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
    
    def recuperaId(db, idU, dato, tabella, colonna):
        cursore=db.cursor()
         
         
        cursore.execute(f"SELECT * FROM {tabella} WHERE {colonna}=? AND {dato}=?", (tabella, colonna, dato,))
        idTrovato=cursore.fetchone()
         
        return idTrovato[0]
    
    def aggiungiTask(db, titolo, descrizione, priorità, inseritoDa, assegnatoA, stato, luogo, data, ora):
        cursore=db.cursor()
        
        tabella="task"
        
        cursore.execute(f"INSERT INTO {tabella} (titolo, descrizione, priorità, id_utente, assegnatoA, stato, luogo, data, ora) VALUES (?,?,?,?,?,?,?,?,?)", (titolo, descrizione, priorità, inseritoDa, assegnatoA, stato, luogo, data, ora))
        db.commit()
    

    def modificaCampo(db, idUser, nuovi_valori, tabella, colonne):
        for colonna, nuovo_valore in zip(colonne, nuovi_valori):
            # Ottieni il valore corrente dal database per confronto
            query_select = f"SELECT {colonna} FROM {tabella} WHERE id_utente = ?;"
            risultato = db.execute(query_select, (idUser,)).fetchone()

            if risultato is not None:
                valore_corrente = risultato[0]
            
                # Aggiorna solo se il nuovo valore è diverso dal valore corrente
                if nuovo_valore != valore_corrente:
                    query_update = f"UPDATE {tabella} SET {colonna} = ? WHERE id_utente = ?;"
                    db.execute(query_update, (nuovo_valore, idUser))
                    print(f"Eseguendo query: {query_update} con valori: ({nuovo_valore}, {idUser})")
    
    # Conferma le modifiche una volta che tutte le operazioni sono eseguite
        db.commit()

       
    def eliminaRiga(db, tabella, idRiga):
    # Determina il nome della colonna chiave primaria in base alla tabella
        if tabella == 'task':
            nomeUser = 'id_task'
        elif tabella == 'user':
            nomeUser = 'id_user'
        else:
            raise ValueError("Tabella non supportata")
    
        # Prepara la query SQL per eliminare solo la riga con l'id specificato
        query = f"DELETE FROM {tabella} WHERE {nomeUser} = ?;"
    
        # Esegui la query passando l'id della riga come parametro
        db.execute(query, (idRiga,))
        db.commit()
    
        print(f"Eseguendo query: {query} con valore: {idRiga} {nomeUser}")

        

         

        
