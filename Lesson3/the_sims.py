import  human as h
import  auto as a

dima = h.Human(1, "Dima")
roma = h.Human(1, "Roma")
igor =h.Human(1, "Igor")
eva = h.Human(0, "Eva")

humans = [dima, roma, igor, eva]
bmw = a.Auto(brand = "BMW")
for human in humans:
    if (human.role != 0):
        bmw.addPassengers(human)
    if (human.role == 0):
        bmw.addDriver(human)
print(f"Passengers: {bmw.passengers}")
print(f"Driver: {bmw.driver}")

