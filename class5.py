class commodity():
    name = "Water"
    price = 100
    stock = 2000

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, stock: {self.stock}"

a = commodity()
print(a)