DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS commenti;

CREATE TABLE users
(
	id_utente INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	cognome TEXT,
	azienda TEXT,
	mail TEXT,
	passw VARCHAR[255],
	reparto TEXT
);

CREATE TABLE task
(
	id_task INTEGER PRIMARY KEY AUTOINCREMENT,
	titolo  TEXT,
	descrizione TEXT,
	priorità INTEGER,
	inseritoDa INTEGER,
	etichetta INTEGER,
	luogo TEXT,
	data DATE,
	ora TIME,
	FOREIGN KEY (inseritoDa) REFERENCES users (id_utente)

);

CREATE TABLE commenti
(
	id_commento INTEGER PRIMARY KEY AUTOINCREMENT,
	testo TEXT,
	data DATE,
	ora TIME,
	daInserito INTEGER,
	id_task INTEGER,
	FOREIGN KEY (daInserito) REFERENCES users (id_utente),
    FOREIGN KEY (id_task) REFERENCES task (id_task)    
);