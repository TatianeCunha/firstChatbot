import mysql.connector
import psycopg2
import validateData
from validateData import validaIdade, validaSexo, validaCronica
from database import insertPaciente, insertSintoma

#chatbot
print("Chatbot: Oi! Seja bem-vindo! Para começarmos, preciso de algumas informações suas.")
print("Chatbot: Pode me informar seu nome?")
nome = input().upper()

print("Chatbot: Certo, e qual a sua idade?")
idade=int(input())

#Idade > 65  ---> risco
grupoRisco= validaIdade(idade)

print("Chatbot: Qual o seu sexo? 1 - Feminino ou 2 - Masculino?")
sexo=int(input())
validaSexo(sexo)

print("""Chatbot: Pode nos contar um pouco mais sobre você? Você pode ser inserido em algum destes grupos?
	1 - Hipertensão
	2 - Asma
	3 - Diabetes
	4 - Fumantes
	5 - Obesidade
	6 - Doença renal crônica
	7 - Doença pulmonar
	8 - Cardiopatia
	9 - Gestante ou lactante
	10 - Fumante
	0 - Encerrar""")
doencasCronicas = []
doencaCronica=input()
validaCronica(doencaCronica)

print("Chatbot: Possui alguma alergia?")
alergia=input()

print("Chatbot: e histórico de cirurgias?")
cirurgia=input()

#insert paciente into database
pacienteID=insertPaciente (nome, str(idade), sexo, doencaCronica, alergia, cirurgia)

print("""Chatbot: Você está apresentando algum dos seguintes sintomas:",
    1-Fadiga
    2-Dor de cabeça
    3-Tosse
    4-Febre
    5-Dor de garganta
    6-Náusea
    7-Vômito
    8-Dor no peito
    9-Diarreia
    10-Dificuldade para respirar
    11-Perda do paladar
    12-Perda do olfato
    0-Encerrar"""
    )

#print("Chatbot: Estou procurando o especialista que possa melhor te atender")

sintoma=int(input())

cont=0
while sintoma!=0:
    insertSintoma (pacienteID, sintoma)
    sintoma=int(input())
    cont=cont+1
    if sintoma==10: print("Numa escala de 0 a 10, qual o nível da sua dificuldade de respirar?")
    dificuldadeRespiratoria=int(input())


if cont>5 or dificuldadeRespiratoria != None : 
    print("Você apresenta um quadro suspeito de COVID-19. Aguarde no chat até que o médico possa te atender.")
    suspeitaCovid='S'