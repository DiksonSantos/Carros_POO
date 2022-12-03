
from Car_son import Car
from __Modulo_CAR import Batery, ElectricCar





#"This Car has a " + str(self.Nivel_Bateria()) + "KWh"
Meu_Tesla = ElectricCar("Tesla", "Model-S", 2016)
print(Meu_Tesla.get_descriptive_name())
Meu_Tesla.descrever_BATERIA()

Carro_Pilha = ElectricCar("Raiovac", "Alcalino", 2019)
print("\n"+Carro_Pilha.get_descriptive_name())
Carro_Pilha.Nivel_Bateria = 90  #Fui eu quem fiz esta Linha :0
Carro_Pilha.descrever_BATERIA()

print("\n")

# Usamos aqui neste carro a combustão, funções herdadas da classe "Car", que contem carros a combustão:
Smoke = Car("Ford","S-10",1986)
print(Smoke.get_descriptive_name())
Smoke.increment_odometer(10)
Smoke.read_odometer()

