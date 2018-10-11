import math

homer = (12,178,54,88,90)
homer_nome = "Homer"

bart = (44,76,44,900,5)
bart_nome = "Bart"

pessoa = (123,543,45,21,4)
pessoa_nome = "Individuo"

distancia_Euclidiana_1 = 0
distancia_Euclidiana_2 = 0

for posicao in range(0,5):

	distancia_Euclidiana_1 = distancia_Euclidiana_1 + ((homer[posicao] - pessoa[posicao])**2)
	distancia_Euclidiana_2 = distancia_Euclidiana_2 + ((bart[posicao] - pessoa[posicao])**2)

distancia_Euclidiana_1 = math.sqrt(distancia_Euclidiana_1)
distancia_Euclidiana_2 = math.sqrt(distancia_Euclidiana_2)

if(distancia_Euclidiana_1 < distancia_Euclidiana_2):
	print("Individuo + proximo do %s -> Distancia = %f" %(homer_nome, distancia_Euclidiana_1))
	
if(distancia_Euclidiana_2 < distancia_Euclidiana_1):
	print("%s + proximo do %s -> Distancia = %f\n" %(pessoa_nome, bart_nome, distancia_Euclidiana_2))

	