class Calculator():   
    def plus(self, a, b) -> int:
        return a + b
    def total(self, a: []) -> int:
        return self.plus(a[0], a[1])

calculator = Calculator()
print(calculator.plus(1,2))
print(calculator.total([1,2]))