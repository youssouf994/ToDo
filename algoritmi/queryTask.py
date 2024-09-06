class qTask:
    def visualizzaTuttePerReparto(db, repartoU):
          cursore = db.cursor()
          tabella="task"

          cursore.execute(f"SELECT * FROM {tabella} WHERE luogo=?", (repartoU,))
          taskReparto = cursore.fetchall()
          
          return taskReparto
    
    def recuperaRepartoUtente(db, idU):
        cursore=db.cursor()
         
        tabella="users"
         
        cursore.execute(f"SELECT * FROM {tabella} WHERE id_utente=?", (idU,))
        idRep=cursore.fetchone()
         
        return idRep    