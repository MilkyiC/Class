class Car:
    def __init__(self,speed, color, name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(self.name,'поехал')
    def stop(self):
        print(self.name,'остановился')
    def turn(self,direction):
        print(self.name,'повернул',direction)

class Towncar(Car):
    def __init__(self,speed, color, name, passability):
        super().__init__(speed,color,name,is_police=False)
        self.passability = passability

class Sportcar(Car):
    def __init__(self,speed, color, name,transfers):
        super().__init__(speed,color,name,is_police=False)
        self.transfers = transfers

class Workcar(Car):
    def __init__(self,speed, color, name,weight):
        super().__init__(speed,color,name,is_police=False)
        self.weight = weight

class Policecar(Car):
    def __init__(self,speed, color, name,capacity):
        super().__init__(speed,color,name,is_police=True)
        self.capacity = capacity

town_car = Towncar(60, "синий", "Городской автомобиль","Высокая")
town_car.go()
town_car.turn('назад')
