from database import insertGrupo

def validaIdade(idade): 
	if idade > 115 or idade < 0:
		while idade > 115 or idade < 0:
			print("Chatbot: Insira uma idade válida.")
			idade=int(input())
		if idade > 65:
			return True

def validaSexo(sexo): 
	while sexo != 1 and sexo != 2:
		print("Chatbot: Insira 1 para feminino e 2 para masculino.")
		sexo=int(input())


def validaCronica(doencaCronica, pacienteID):
	doencasCronicas = []
	doencasCronicas.append(doencaCronica)
	while doencaCronica != '0':
		insertGrupo (pacienteID, doencaCronica)
		doencasCronicas.append(doencaCronica)
		doencaCronica = input("Chatbot: Algo mais? \n")
		grupoRisco = True

		if doencaCronica == '0': 
			break

		