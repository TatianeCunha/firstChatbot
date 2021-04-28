def validaIdade(idade): 
	if idade > 115 or idade < 0:
		while idade > 115 or idade < 0:
			print("Insira uma idade válida.")
			idade=int(input())
		if idade > 65:
			return True

def validaSexo(sexo): 
	if sexo != 'FEMININO' or sexo != 'MASCULINO':
		#TODO
		print("Insira Feminino ou Masculino")
		sexo=input()
