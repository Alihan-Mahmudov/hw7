class Bank:
    def __init__(self, money:int, name):
        self.__money=money
        self.__name=name
    def setmoney(self, money):
        self.__money=money
    def getmoney(self):
        return self.__money
    def setname(self, name):
        self.__name=name
    def getname(self):
        return self.__name
    def moneyX(self):
        self.__money+=int(input("Введите сумму:"))
    def _kill(self):
        self.__money=0
    def __jackpot(self):
        self.__money*=10
user=Bank(100,'Alihan')
user.moneyX()
print(f"moneX:{user._Bank__money}")
user._Bank__jackpot()
print(f"jackpot:{user._Bank__money}")
user._kill()
print(f"kill:{user._Bank__money}")
