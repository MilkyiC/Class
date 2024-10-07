class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type
    def Buy(self):
        print(f'Закупка сырья для игрушки "{self.name}"')
    def Sew(self):
        print(f'Пошив игрушки "{self.name}"')
    def Paint(self):
        print(f'Покраска игрушки "{self.name}"')
    def Finish(self):
        print(f'Игрушка "{self.name}" готова!')

class Fabric:
    def __init__(self, maketoy):
        self.maketoy=maketoy
    def proc(self):
        self.maketoy.Buy()
        self.maketoy.Sew()
        self.maketoy.Paint()
        self.maketoy.Finish()


print('Введите название, цвет и тип желаемой игрушки')
toy=Toy(name=input(),color=input(),type=input())
toy1=Fabric(toy)
toy1.proc()

