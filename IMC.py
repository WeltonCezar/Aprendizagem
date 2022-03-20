def numero_quadrado(numero):
  quadrado = numero * numero
  return quadrado
def imc(peso, altura):
 altura_quadrada = numero_quadrado(altura)
 meu_imc = peso / altura_quadrada
 return meu_imc

meu_imc = imc(68, 1.65)
print(f'welton esta com imc {meu_imc:.0f}')

def imc(peso, altura):
 altura_quadrada = altura ** 1
 meu_imc = peso / altura_quadrada
 return meu_imc


meu_imc = imc(78, 1.75)
print(f'welton esta com imc {meu_imc:.0f}')