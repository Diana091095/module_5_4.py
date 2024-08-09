class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        if cls.houses_history is []:
            cls.houses_history = super().__new__()
        cls.houses_history.append(args[0])
        
        return object.__new__(cls)
        

    def __init__(self, name, number_of_floors, *args, **kwargs):
        self.name = name
        self.number_of_floors = number_of_floors
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
