# Se pide como proceso SUMAR Y CALCULAR EL PROMEDIO de los valores que contiene el 
# vector, en posiciones impares. Se pide como proceso SUMAR Y CALCULAR EL PROMEDIO los 
# valores que contiene el vector en posiciones pares.
# c.- Realice una estructura Switch con las opciones
# 1.- Ingreso de N trabajadores con sus respectivos nombre, cargo, sueldo en un vector
# 2.- Suma de los valores (columna sueldo) y mostrar el promedio
# 3.- Sueldo mínimo y máximo (identificar el sueldo con sus respectivos datos (nombre, Cargo, 
# Sueldo)
# 4.- Mostrar los resultados (Número de personas ingresados con sus datos, promedio de los 
# sueldos, Sueldo mínimo, máximo con sus datos)
# 5.- Salir

def ingresarTrabajadores()->list:
  """
  Funcion para ingresar los datos de los trabajadores
  Retorna:
    Lista de trabajadores
  """
  trabajadores = []
  
  cantidaTrabajadores = int(input('Cantidad de trabajadores a ingresar: '))
  while cantidaTrabajadores <= 0:
    print('ERROR, la cantidad debe ser positiva')
    cantidaTrabajadores = int(input('Cantidad de trabajadores a ingresar: '))
    
  for i in range(cantidaTrabajadores):
    print(f'** Trabajador {i+1}: ')

    nombre = input('Nombre: ')
    while len(nombre) == 0:
      print('ERROR, Debe ingresar un nombre!')
      nombre = input('Nombre: ')

    cargo = input('Cargo: ')
    while len(cargo) == 0:
      print('ERROR, Debe ingresar un cargo!')
      cargo = input('Cargo: ')

    sueldo = float(input('Sueldo: '))
    while sueldo <= 0:
      print('ERROR, Debe ingresar un sueldo positivo!')
      sueldo = float(input('Sueldo: '))

    trabajadores.append([nombre,cargo,sueldo])

  return trabajadores

def promedioSueldos(trabajadores:list) -> float:
  """
  Funcion que calcula el sueldo promedio
  """
  sumaImpar = 0;sumaPar = 0
  contadorImpar = 0;contadorPar = 0
  for i in range(len(trabajadores)):
    if i%2 == 0:
      sumaImpar += trabajadores[i][2]
      contadorImpar += 1
    else:
      sumaPar += trabajadores[i][2]
      contadorPar += 1
  
  promedioImpar = sumaImpar / contadorImpar
  promedioPar = sumaPar / contadorPar

  return [round(promedioImpar, 2), round(promedioPar, 2)]

def minimoYMaximo(trabajadores:list)->dict:
  """
  Funcion que retorna caclula el sueldo minimo y maximo
    con sus respectivos valores
  """
  minimo = trabajadores[0][2]
  indiceMinimo = 0
  maximo = trabajadores[0][2]
  indiceMaximo = 0

  for i in range(len(trabajadores)):
    if minimo > trabajadores[i][2]:
      minimo  = trabajadores[i][2]
      indiceMinimo = i
    
    if maximo < trabajadores[i][2]:
      maximo  = trabajadores[i][2]
      indiceMaximo = i

  resultado = {}
  resultado['minimo'] = trabajadores[indiceMinimo]
  resultado['maximo'] = trabajadores[indiceMaximo]

  return resultado

if __name__ == '__main__':
  trabajadores = []
  opcion = 1
  while opcion != 0:
    print('==== MENU ====')
    print('[1] Ingreso de N trabajadores')
    print('[2] Promedio sueldos')
    print('[3] Sueldo minimo y maximo')
    print('[0] Salir')  
    opcion = int(input('Opcion: '))

    if opcion == 1:
      trabajadores = ingresarTrabajadores()

    elif opcion == 2:
      if len(trabajadores) > 0:
        resultado = promedioSueldos(trabajadores)
        print(f'Promedio Impar: {resultado[0]}')
        print(f'Promedio Par: {resultado[1]}')
      else:
        print('Ingrese trabajadores!')
    
    elif opcion == 3:
      if len(trabajadores) > 0:
        resultado = minimoYMaximo(trabajadores)
        print(f"Sueldo minimo: {resultado['minimo'][0]} - {resultado['minimo'][1]} - {resultado['minimo'][2]}")
        print(f"Sueldo maximo: {resultado['maximo'][0]} - {resultado['maximo'][1]} - {resultado['maximo'][2]}")

      else:
        print('Ingrese trabajadores!')


  