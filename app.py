import sys
from arraysearch import algorithms
from arraysearch import execution_time_gathering
import matplotlib.pyplot as plt

def graphicsAlgorithms():
    minimum_size = 100000
    maximum_size = 200000
    step = 10000
    samples_by_size = 5
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | Linear Search | Binary Search | Ternary Search")
    for row in table:
        print(row)


    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[1][0] for row in table]
    y2 = [row[2][0] for row in table]
    y3 = [row[3][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Linear", color='blue')
    plt.plot(x, y2, label="Binary", color='green')
    plt.plot(x, y3, label="Ternary", color='red')

    plt.title('Comparation Search in Array algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[1][1] for row in table]
    y2 = [row[2][1] for row in table]
    y3 = [row[3][1] for row in table]

    plt.plot(x, y1, label="Linear", color='blue')
    plt.plot(x, y2, label="Binary", color='green')
    plt.plot(x, y3, label="Ternary", color='red')

    plt.title('Comparation Search in Array algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()

def graphicsBinaryTernary():
    minimum_size = 200000
    maximum_size = 1000000
    step = 100000
    samples_by_size = 5
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, True)
    print("Size | Binary Search | Ternary Search")
    for row in table:
        print(row)

    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[1][0] for row in table]
    y2 = [row[2][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Binary", color='blue')
    plt.plot(x, y2, label="Ternary", color='green')

    plt.title('Comparation Search in Array algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[1][1] for row in table]
    y2 = [row[2][1] for row in table]

    plt.plot(x, y1, label="Binary", color='blue')
    plt.plot(x, y2, label="Ternary", color='green')

    plt.title('Comparation Sorting algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    graphicsAlgorithms()
    graphicsBinaryTernary()
