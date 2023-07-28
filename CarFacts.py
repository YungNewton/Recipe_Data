class Car:
    def __init__(self,color, wheels, model):
        self.color = color
        self.wheels = wheels
        self.model = model

    def isDriving(self, isDrive):
        if isDrive == True:
            print('car is driving')
        else:
            print('car is not driving')
            pass