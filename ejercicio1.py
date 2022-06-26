# Ingresar N personas, en cada uno tiene que ingresar su respectivo valores en Talla, Peso,
# considere decimales.
# Calcular su Índice Masa Corporal. Aplique la formula del IMC.
# Validar el resultado del IMC, represente su condición
# IMC<18,5;"Bajo peso";
# IMC>=18,5 AND IMC<=24,9;"Normal";
# IMC>=25 AND IMC <=29,9"Sobrepeso";
# IMC>=30 AND IMC <=34,9)"Obesidad Grado I
# IMC>=35 AND IMC<=39,9)"Obesidad Grado II"
# IMC>=40;"Obesidad Grado III"
# Una vez validado contar los respectivos resultados, Se pide mostrar los resultados en cada 
# criterio o validación. Utilice las respectivas senescencias, funciones en Python 

def calcularIMC(estatura:float, peso:float) -> dict:
  """
  Funcion que calcula el IMC de una persona
  Parametros:
    estatura: Es la altura de la persona en metros
    peso: Es el peso de la persona en kilogramos
  Retorna:
    Diccionario con el imc y el estado
  """
  resultado = {}
  imc = peso / estatura**2

  if imc < 18.5:
    resultado['estado'] = 'Bajo peso'
  elif imc < 25:
    resultado['estado'] = 'Normal'
  elif imc < 30:
    resultado['estado'] = 'Sobrepeso'
  elif imc < 35:
    resultado['estado'] = 'Obesidad grado I'
  elif imc < 40:
    resultado['estado'] = 'Obesidad grado II'
  else:
    resultado['estado'] = 'Obesidad grado III'

  resultado['imc'] = round(imc, 2)

  return resultado

def ingresarPersonas() -> list:
  """
  Funcion que ingresa n cantidad de personas a una lista
  Retorna:
    Una lista con la estatura y peso de cada persona
  """
  personas = []

  cantidadPersonas = int(input('Ingrese la cantidad de personas que va a ingresar: '))
  while cantidadPersonas <= 0:
    print('ERROR, debe ingresar una cantidad positiva')
    cantidadPersonas = int(input('Ingrese la cantidad de personas que va a ingresar: '))
  

  for i in range(cantidadPersonas):
    print(f'** Datos de la persona {i+1} **')

    estatura = float(input('Ingrese la estatura(m): '))
    while estatura <= 0.50:
      print('ERROR, la estatura debe ser mayor a 0.50m')
      estatura = float(input('Ingrese la estatura(metros): '))
    
    peso = float(input('Ingrese el peso(kg): '))
    while peso <= 20:
      print("ERROR, debe ingresar un peso superior a 20kg")
      peso = float(input('Ingrese el peso(kg): '))
    
    personas.append([estatura,peso])
    
  return personas


if __name__ == "__main__":
  personas = ingresarPersonas()

  for i in range(len(personas)):
    
    resultado = calcularIMC(personas[i][0], personas[i][1])
    
    print(f'Persona {i+1}: ')
    print(f'\tIMC: {resultado["imc"]}')
    print(f'\tEstado: {resultado["estado"]}')
