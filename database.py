import mysql.connector
import psycopg2

#connection to the database
mydb = psycopg2.connect(
    host="tuffi.db.elephantsql.com",
    database="uevnqhtj",
    user="uevnqhtj",
    password="RqAmmvdUX0q2vR_cJh9pnQ9uAkfLW213",
    port='5432')

cursor = mydb.cursor()

def insertPaciente (nome, idade, sexo, alergia, cirurgia):
	cursor.execute("insert into paciente values (nextval('seq_paciente'), '"
    +str(nome)+"','"
    +str(idade)+"','"    
    +str(sexo)+"','"
    +str(alergia)+"','"
    +str(cirurgia)+ "') returning id")
	mydb.commit()

	lastId=cursor.fetchone()
	return lastId[0]

def insertSintoma (pacienteID, sintoma):
	cursor.execute("insert into sintomas values (nextval('seq_sintoma'), '"
    +str(pacienteID)+"','"
    +str(sintoma)+"')")
	mydb.commit()

def insertGrupo (pacienteID, grupo):
	cursor.execute("insert into grupo values (nextval('seq_grupo'), '"
    +str(pacienteID)+"','"
    +str(grupo)+"')")
	mydb.commit()