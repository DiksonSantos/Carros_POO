

class Car():
    #Uma tentativa simples de representar um carro.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title() #Nem precisou do PRINT Usando o Return

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Representa aspectos específicos de veículos elétricos."""
    def __init__(self, make, model, year):
        """Inicializa os atributos da classe pai.
        Em seguida, inicializa os atributos específicos de um carro elétrico"""
        super().__init__(make, model, year) #Herdados
        self.Nivel_Bateria = 70  #Atrib Exclusivo

    def descrever_BATERIA(self):
        '''Capacidade da Batera'''
        print("This Car has a " + str(self.Nivel_Bateria) + "-kWhbattery")


"""O IF a baixo serve para manter estes testes (das linhas a baixo) aqui. Ou, se este arquivo "Car_son"
For importado em outro script, estes testes aqui a baixo não vão rodar lá """
if __name__ == "__main__":

            # "Montamos/descrevemos" o carro:
            Carro_eletrico = ElectricCar("Tesla_01", "Prototipo", 2014)
            # Mostramos as caracteristicas dele:
            print(Carro_eletrico.get_descriptive_name())
            # Fornecemos um nivel de bateria:
            Carro_eletrico.Nivel_Bateria = 105
            # Apresentamos o nivel de bateria fornecido:
            Carro_eletrico.descrever_BATERIA()
            print("\n") 


            #"This Car has a " + str(self.Nivel_Bateria()) + "KWh"
            Meu_Tesla = ElectricCar("Tesla", "Model-S", 2016)
            print(Meu_Tesla.get_descriptive_name())
            Meu_Tesla.descrever_BATERIA()

            
# Usamos aqui neste carro a combustão, funções herdadas da classe "Car", que contem carros a combustão:
            Fumaça = Car("Ford","S-10",1986)
            print(Fumaça.get_descriptive_name())
            Fumaça.increment_odometer(10)
            Fumaça.read_odometer()

            
