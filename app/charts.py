# graficos #
import matplotlib.pyplot as plt #paquete que no viene incorporado en python, tenemos que cargarlo
#se utiliza as plt para etiquetarlo y sea mas facil ejecutarlo

def generate_bar_chart(name, labels, values): #creamos la funcion para la grafica
  #fig = forma
  #ax = coordenadas para graficar
  fig, ax = plt.subplots() #declaramos los tipos de datos para graficar
  ax.bar(labels, values) #indicamos que se hará una grafica de barras con los valores de labels y values
  #plt.show()
  plt.savefig(f'./imgs/{name}bar.png')
  plt.close()


def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis("equal")
  #plt.show()
  plt.savefig(f'./imgs/{name}pie.png')
  plt.close()
  


#creamos un script para poder ejecutarlo desde la consola
if __name__ == "__main__":
  labels = ["a", "b", "c"]
  values = [10, 40, 800]
  #generate_bar_chart(labels, values) #invocamos a la funcion graficadora
  generate_pie_chart(labels, values)
