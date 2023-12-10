class Car():
    __private_prop = 10
    public_prop = 20

car = Car()
print(car.public_prop)
# print(car.__private_prop) Exception when private prop