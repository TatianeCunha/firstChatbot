def validaIdade(idade): 
	if idade > 115 or idade < 0:
		while idade > 115 or idade < 0:
			print("Insira uma idade válida.")
			idade=int(input())
		if idade > 65:
			return True

def validaSexo(sexo): 
	while sexo != 1 and sexo != 2:
		print("Insira um valor válido")
		sexo=int(input())


def validaCronica(doencaCronica):
	doencasCronicas = []
	doencaCronica=input()
	doencasCronicas.append(doencaCronica)
	while doencaCronica != '0':
		doencasCronicas.append(doencaCronica)
		doencaCronica = input("Algo mais? ")
		grupoRisco = True
		if doencaCronica == '0': 
			break