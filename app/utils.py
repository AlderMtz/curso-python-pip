#cualquier archivo con terminacion .py se concidera un modulo
def obtencion_poblacion(data):
  labels = []
  values = []
  
  i = 0;
  for key, value in data.items():
    if i >= 5 and i<= 12:
      print("clave => ", key, "value", value)
      labels.append(key)
      values.append(int(value))
    i += 1 

  return labels, values



def get_population(data):
  population_dict = {
    "2022" : int(data["2022 Population"]),
    "2020" : int(data["2020 Population"]),
    "2015" : int(data["2015 Population"]),
    "2010" : int(data["2010 Population"]),
    "2000" : int(data["2000 Population"]),
    "1990" : int(data["1990 Population"]),
    "1980" : int(data["1980 Population"]),
    "1970" : int(data["1970 Population"])
  }
  labels = population_dict.keys()
 
  values = population_dict.values()
  
  return labels, values

def population_by_country(data, country):
  result = list(filter(lambda item: item["Country/Territory"] == country, data))
  return result
  #esta funcion obtiene un lista de diccionarios(data) y filtra buscando la ciudad (country)


def obtencion_columna(data):
  countrys = list(map(lambda item : item["Country/Territory"], data))
  values = list(map(lambda item: item["World Population Percentage"], data))
  return countrys, values   











A = "Hola"
