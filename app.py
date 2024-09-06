from flask import Flask, render_template, request, session, redirect, url_for
import bcrypt
import sqlite3
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


        if check==True:
            return render_template('index.html')
        
        else:
            return render_template('registrazione.html')


@app.route('/login', methods=['POST', 'GET'])
def accesso():
    if request.method=='POST':
        utente=request.form['user']
        passwd=request.form['pass'].encode('UTF-8')

        
        db=qDb.db()
        check=qUsers.login(db, utente, passwd)    
        
        if check==False:
            return render_template('errore.html')
        
        else:
            session['userId']=check
            return redirect(url_for('home'))
        


@app.route('/home', methods=['POST', 'GET'])
def home():
    
    return render_template('home.html')

@app.route('/visualizzaTask', methods=['POST', 'GET'])
def visualizzaTask():
    
    db=qDb.db()
    
    rep=qTask.recuperaRepartoUtente(db, session['userId'])
    task=qTask.visualizzaTuttePerReparto(db, rep)
    
    return render_template("vis.html", task=task)


if __name__ == "__main__":
    # Run the app server on localhost:4449
    app.run(host='0.0.0.0', port=5000)