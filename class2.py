class Car():
    def __init__(self):
        self.name = "car"
    def getName(self) -> dict:
        return self.name
    def getType(self):
        raise NotImplementedError()
    
class Tesla(Car):
    def __init__(self):
        super().__init__()

class Toyota(Car):
    def __init__(self):
        self.name = "Toyota"

tesla = Tesla()
print(tesla.getName())
toyota = Toyota()
print(toyota.getName())