
class Rectangle:
    def __init__(self,vertical,horizontal,height):
        self.vertical = vertical
        self.horizontal = horizontal
        self.height = height
    
    def calc_area(self):
        return self.vertical * self.horizontal
        

class Rectangular(Rectangle):
    def __init__(self,vertical,horizontal,height):
        super().__init__(vertical,horizontal,height)
    def calc_volume(self):
        return self.calc_area() * self.height
        

def create_instance():
    global squares
    squares = []
    dimensions=[
     (3,4,5),
     (50,60,70),
      (333,444,555)
    ]
    for vertical,horizontal,height in dimensions:
       dimension = Rectangular(vertical,horizontal,height)
       squares.append(dimension)
    

def play():
    create_instance()
    for i in squares:
        print(f"Area: {i.calc_area()}")
        print(f"Volume: {i.calc_volume()}")
        print('-' * 30)
play()