#method overiding ->overiding parent class ...same signature as parent class

class Bike:
    def start(self):
        print("Kicker start")

    def breaking(self):
        print("drum break")

class HeroHondaSplender:
    def start(self):
        print("self start")

    def breaking(self):
        print("abs breaking")

hobj=HeroHondaSplender()
hobj.start()
hobj.breaking()