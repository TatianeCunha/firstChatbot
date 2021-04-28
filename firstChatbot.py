import mysql.connector
import psycopg2
import validateData

#connection to the database
mydb = psycopg2.connect(
    host="tuffi.db.elephantsql.com",
    database="uevnqhtj",
    user="uevnqhtj",
    password="RqAmmvdUX0q2vR_cJh9pnQ9uAkfLW213",
    port='5432')

cursor = mydb.cursor()

#chatbot

grupoRisco = False

print("Chatbot: Oi! Seja bem-vindo! Para começarmos, preciso de algumas informações suas.")
print("Chatbot: Pode me informar seu nome?")
nome = input()

print("Chatbot: Certo, e qual a sua idade?")
idade=int(input())
if idade > 115 or idade < 0:
    while idade > 115 or idade < 0:
        print("Insira um valor válido")
        idade=int(input())
if idade > 65:
    grupoRisco = True


#Idade > 65  ---> risco

print("Chatbot: Qual o seu sexo? Feminino ou masculino?")
sexo=input()
if sexo != "Feminino" or sexo != "Masculino":
     while idade > 115:
        print("Insira um valor válido")
        idade=int(input())

print("Chatbot: Pode nos contar um pouco mais sobre você? Possui alguma doença crônica?")
doencaCronica=input()

#doença cronica ---> risco

print("Chatbot: Possui alguma alergia?")
alergia=input()

print("Chatbot: e histórico de cirurgias?")
cirurgia=input()

#verificar se é pessoa de risco
#se maior de certa idade
#instanciar variavel grupo de risco=0
#se possui alguma das situações previstas


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
