Smartphones = []

class Phones:
    def __init__(self, type, Size, color):
        self.type = type
        self.Size = Size
        self.color = color

    def info(self):
        return f"type:{self.type}  size:{self.Size}  color:{self.color}"

data = [
    ("Android", 60, "red"),
    ("iPhone", 50, "blue"),
    ("Android", 70, "white"),
    ("Android", 50, "black"),
    ("Android", 60, "purple"),
    ("iPhone", 60, "black"),
    ("Android", 50, "green"),
    ("iPhone", 70, "yellow"),
    ("iPhone", 80, "purple"),
    ("Android", 60, "yellow")
]


for type, Size, color in data:
    smartphone = Phones(type, Size, color)
    Smartphones.append(smartphone)


for smartphone in Smartphones:
    print(smartphone.info())
