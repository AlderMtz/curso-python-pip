#aqui podemos importar los modulos creados anteriormente y esten en la misma carpeta
#modularizacion reutilizacion de otros modulos-archivos
import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv("./data.csv") #obtenemos el archivo csv
  country = input("Ingrese la ciudad:\n".lower())
  #country = country.lower() #minimizar
  country = country.capitalize() #hacer mayuscula la primer letra
  print(country)
  result = utils.population_by_country(data, country)
  result_2 = dict(result[0])
  
  
  if len(result) > 0:
    country = result[0] #como result es una lista, se le indica la posicion en donde se guardo el diccionario buscado, meramente por formalidad, ya que una lista de diccionarios puede tener uno o mas diccionarios dentro.
    #print(result[0].values())
    keys, values = utils.get_population(country) #llamamos la funcion definida en el modulo mod
    print(keys, values)

    keys_2, values_2 = utils.obtencion_poblacion(result_2)
    print(keys_2, values_2) 

    charts.generate_bar_chart(country['Country/Territory'] ,keys_2, values_2)
    charts.generate_pie_chart(country['Country/Territory'] ,keys_2, values_2)

  







  #text = utils.A #y asi llamamos a las varibales definidas en el modulo mod

  #print(text)
  #print(utils.A)

if __name__ == "__main__":##Se le llama: Entry point #esta condicion lo que hace es ejecutar el "main" sin la nececidad de llamar a a la funcion run, esto desde la terminal. Se ejecuta como script y tambien se puede llamar datos en main sin que se ejecute run(), dualidad
  run()
