class FILM:
    def __init__(self, name, producer, enterprise, money, year):
        self.name = name
        self.producer = producer
        self.enterprise = enterprise
        self.money = money
        self.year = year
    def add_money(self, amount):
        self.money += amount
    def show(self):
        print(f"Назва: {self.name}")
        print(f"Режисер: {self.producer}")
        print(f"Кіностудія: {self.enterprise}")
        print(f"Прибуток від прокату: {self.money} $")
        print(f"Рік випуску: {self.year}")
