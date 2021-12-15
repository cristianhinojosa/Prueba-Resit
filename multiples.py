class Multiples:
    # Constructor que ayuda a settiar el inicio y el fin del loop
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Metodo que selecciona los divisibles y los no divisibles
    def divisible(self, number):     
        divisible_dict = {15:"INTEGRACIONES", 5:"IT", 3:"RESIT"}
        for clave, valor in divisible_dict.items():
            if number % clave == 0:
                return(valor)
        return(number)

    # Metodo que ayuda a realizar la operacion 
    def operation(self):
        string = ""
        for i in range(self.start, self.end):
            string += str(self.divisible(i))

        return string 


# Creamos una instancia de la clase Multiples
#multiples = Multiples(1, 101)

# Ejecutamos e imprimimos los resultados del metodo operation 
#print(multiples.operation())
