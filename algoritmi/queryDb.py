from flask import g, render_template
import sqlite3


class qDb:
     @staticmethod
     def db():
        """
        Funzione per ottenere la connessione al database SQLite.
        Se la connessione non esiste, viene creata e memorizzata nell'oggetto globale g.
        
        Returns:
            db (sqlite3.Connection): Connessione al QueryDatabase.
        """
        DATABASE = 'dati.db'
        db = getattr(g, 'database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db
    