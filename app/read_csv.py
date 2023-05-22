import csv # modulo nativo para leer archivos scv

def read_csv(path): # se le envia la direccion de donde se va a leer
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",") # la coma es un limitador de cada dato, en algunos casos vienen con ;
    header = next(reader) #aqui se lee la primer fila manualmente, el cual contiene el nombre de las columnas y posteriormente utilizaremos este dato de filas para unirlas con las columnas y asi poder crear una lista de diccionarios
    data = [] #creamos una lista vacia donde posteriormente guardaremos los diccionarios
    for row in reader: #aqui leemos fila a fila el archivo csv
      iterable = zip(header, row) #utilizamos la funcion zip para hacer match entre los keys y el valor de cada fila
      country_dict = {key: value for key, value in iterable} #aqui convertimos en diccionarios lo que obtenemos de hacer el match entre las filas y columnas
      data.append(country_dict) #añadimos el diccionario a la lista vacia que se declaro anteriormente, la asignacion se hara en automatico mediante la iteracion que ejecuta la funcion for
    return data
    
#para poder ejecutarlo desde la consoloa como script utilizamos lo siguiente

if __name__ == "__main__":
  data = read_csv("./app/data.csv") #la funcion retorna una lista de diccionarios la cual debemos de guardar en una variable
  print(data[0]) #leemos el primer diccionario de la lista
  print("*" * 10)
 
  
  











###playground

#def read_csv(path):
   # Tu código aquí 👇
  
#   with open(path, "r") as csvfile:
#      reader = csv.reader(csvfile, delimiter = ",")
#      suma = 0
#      for row in reader:
#         gasto = int(row[1]) 
#         suma += gasto
#      total = suma
#      return total

#response = read_csv('./data.csv')
#print(response)

#Administration,200
#Marketing,201
#Purchasing,114
#Human Resources,203
#Shipping,121
#IT,103
#Public Relations,204
#Sales,145
#Executive,100
#Finance,108


