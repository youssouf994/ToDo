#from crypt import methods
from dataclasses import dataclass
from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import datetime
from functools import wraps

from algoritmi.queryDb import qDb
from algoritmi.queryUsers import qUsers
from algoritmi.queryTask import qTask

app= Flask(__name__)
app.config['SECRET_KEY']='super_secret_key'

def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if 'userId' in session:
            return view_func(*args, **kwargs)
        else:
            return redirect(url_for('crea_utente'))
    return wrapped_view


@app.route('/')
@app.route('/main')
def main():
    
    return render_template('index.html')



@app.route('/registrazione', methods=['POST', 'GET'])
def crea_utente():
    if request.method=='POST':
        nome=request.form['nome']
        cognome=request.form['cognome']
        azienda=request.form['azienda']
        mail=request.form['mail']
        reparto=request.form['reparto']
        passw=request.form['pass']

        db=qDb.db()
       
        check=qUsers.confrontoMail(db, nome, cognome, azienda, mail, passw, reparto)
        db.close()

        if check==True:
            return render_template('index.html')
        
        else:           
            return render_template('errore.html')


@app.route('/login', methods=['POST', 'GET'])
def accesso():
    if request.method=='POST':
        utente=request.form['user']
        passwd=request.form['pass'].encode('UTF-8')

        
        db=qDb.db()
        check=qUsers.login(db, utente, passwd)    
        db.close()
        
        if check==False:
            return render_template('errore.html')
        
        else:
            session['userId']=check
            return redirect(url_for('home'))
        
        

@app.route('/home', methods=['POST', 'GET'])
def home():
    
    return render_template('home.html')

@app.route('/visualizzaTask/<stato>')
def visualizzaTask(stato):
    db=qDb.db()
    
    if stato == 'da_fare':
        task=qTask.visualizzaTutteDaCompletare(db, session['userId'])
        
    elif stato == 'in_sospeso':
        task=qTask.visualizzaTutteSospese(db, session['userId'])
        
    elif stato == 'chiuse':
        task=qTask.visualizzaTutteCompletate(db, session['userId'])
        
    elif stato == 'da_fareB':
        task=qTask.visualizzaTutteDaCompletareAssegnatemi(db, session['userId'])
        
    elif stato == 'in_sospesoB':
        task=qTask.visualizzaTutteSospeseAssegnatemi(db, session['userId'])
        
    elif stato == 'chiuseB':
        task=qTask.visualizzaTutteCompletateAssegnatemi(db, session['userId'])
    

    db.close()
    return render_template('vis.html', task=task, stato=stato)

@app.route('/aggiungi', methods=['POST', 'GET'])
def aggiunta():
    db=qDb.db()
    
    utenti=qUsers.recuperaUtenti(db)
    
    db.close()
    
    return render_template("aggiungiTask.html", utenti=utenti)

@app.route('/aggiungiTasks', methods=['POST', 'GET'])
def nuovoTask():
    if request.method == 'POST':    
        db=qDb.db()
    
        now = datetime.datetime.now()
    
        titolo=request.form['titolo']
        descrizione=request.form['descrizione']
        priorità=request.form['priorita']
        assegnatoA=request.form['assegnatoA']
        stato=request.form['stato']
        luogo=request.form['luogo']
        data=now.strftime('%d-%m-%Y')
        ora=now.strftime('%H:%M:%S')
      
    qTask.aggiungiTask(db, titolo, descrizione, priorità, session['userId'], assegnatoA, stato, luogo, data, ora)
    rep=qTask.recuperaRepartoUtente(db, session['userId'])
    task=qTask.visualizzaTuttePerReparto(db, rep)
    utenti=qUsers.recuperaUtenti(db)
    
    db.close()
    
    return render_template("aggiungiTask.html", task=task, utenti=utenti)


if __name__ == "__main__":
    # Run the app server on localhost:4449
    app.run(host='0.0.0.0', port=5000)