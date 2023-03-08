class Student():
    def __init__(self, name):
        self.name = name
        # __ means private
        self.__scores = {'math':90, 'English': 78}
    def showName(self):
        return self.name
    def showScores(self):
        return self.__scores

ming = Student('ming')
print(ming.name)
print(ming.showName())
print(ming.showScores())
print(ming._Student__scores)# read private property = =?
