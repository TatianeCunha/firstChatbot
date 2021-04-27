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

#chatbot

print("Chatbot: Oi! Seja bem-vindo! Para começarmos, preciso de algumas informações suas.")
print("Chatbot: Pode me informar seu nome?")
nome = input()

print("Chatbot: Certo, e qual a sua idade?")
idade=input()

print("Chatbot: Qual o seu sexo? Feminino ou masculino?")
sexo=input()

print("Chatbot: Pode nos contar um pouco mais sobre você? Possui alguma doença crônica?")
doencaCronica=input()

print("Chatbot: Possui alguma alergia?")
alergia=input()

print("Chatbot: e histórico de cirurgias?")
cirurgia=input()

print("Chatbot: Estou procurando o especialista que possa melhor te atender")


cursor.execute("insert into paciente values (nextval('seq_paciente'), '"
    +nome+"','"
    +idade+"','"
    +sexo+"','"
    +doencaCronica+"','"
    +alergia+"','"
    +cirurgia+ "')")
mydb.commit()

print(cursor.rowcount, "was inserted.")
