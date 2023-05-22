import utils
import read_csv
import charts

def run():
  result, a, b = sum(1,2)
  data = read_csv.read_csv("./app/data.csv") #obtenemos el archivo csv
  continente = input("Ingrese el continente:\n".lower())
  #country = country.lower() #minimizar
  continente = continente.title() #hacer mayuscula la primer letra
  print(continente)
  data_1 = list(filter(lambda item : item["Continent"] == continente , data ))
  
  keys, values = utils.obtencion_columna(data_1)
  print(keys, values)
  charts.generate_pie_chart(keys, values)

if __name__ == "__main__":##Se le llama: Entry point #esta condicion lo que hace es ejecutar el "main" sin la nececidad de llamar a a la funcion run, esto desde la terminal. Se ejecuta como script y tambien se puede llamar datos en main sin que se ejecute run(), dualidad
  run()
  