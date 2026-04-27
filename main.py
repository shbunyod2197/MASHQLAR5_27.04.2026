##1-masala
class Shaxs:
    def __init__(self, ism):
        self.ism = ism

    def salom(self):
        print(self.ism)

class Oqituvchi(Shaxs):
    def __init__(self, ism, fan):
        super().__init__(ism)
        self.fan = fan


    def salom(self):
        super().salom()
        print(self.ism)
        print(self.fan)


o = Oqituvchi("Dilnoza", "Matematika")
o.salom()


## 2-masala
class Kitob:
    def __init__(self, nomi):
        self.nomi = nomi

    def info(self):
        print(self.nomi)

class Darslik(Kitob):
    def __init__(self, nomi, fan):
        super().__init__(nomi)
        self.fan = fan

    def info(self):
        super().info()
        print(self.fan)

d = Darslik("Algebra", "Matematika")
d.info()

# 3
class Avto:
    def __init__(self, nomi):
        self.nomi = nomi

    def yurish(self):
        print(self.nomi)

class ElektroAvto(Avto):
    def __init__(self, nomi, quvvat):
        super().__init__(nomi)
        self.quvvat = quvvat

    def yurish(self):
        super().yurish()
        print(self.quvvat)

e = ElektroAvto("kgkhwgakg", 123)
e.yurish()

## 4-masala
class Kompyuter:
    def __init__(self, cpu):
        self.cpu = cpu

    def info(self):
        print(self.cpu)

class Noutbuk(Kompyuter):
    def __init__(self, cpu, batareya):
        super().__init__(cpu)
        self.batareya = batareya

    def info(self):
        super().info()
        print(self.batareya)

n = Noutbuk("i7", "5 soat")
n.info()

## 5-masala
class Oyinchi:
    def __init__(self, ism):
        self.ism = ism

    def info(self):
        print(self.ism)

class ProOyinchi(Oyinchi):
    def __init__(self, ism, reyting):
        super().__init__(ism)
        self.reyting = reyting

    def info(self):
        super().info()
        print(self.reyting)

p = ProOyinchi("Ali", 2500)
p.info()
