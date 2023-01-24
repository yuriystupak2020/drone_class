class Drone:
    """Just a train for classes in sample drone"""
    print("It's a class of drones")
    variable_class = 4

    def __init__(self):
        self.x = 10

    def f1(self):
        print(self.x)

d = Drone()
d.f1()
print(d.x)
setattr(d, "x", 45)
print(getattr(d, "x"))
print(getattr(d, "a", 56))#если нет то 56 даст

Drone.lenth = 50
d.width = 25
print(d.width, d.lenth)
d2 = Drone()
print(d2.lenth*3)

Drone.variable_class = 17
d.variable_class = 18
print(d.variable_class)
print(d2.variable_class)

print(dir(Drone))
print(dir(d))