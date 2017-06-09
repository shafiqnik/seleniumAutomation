class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def make_car_sound():
        print('vroooooom')

   
        
mustang = Car('Ford', 'Mustang')
print (mustang.wheels)

#Car.make_car_sound()
