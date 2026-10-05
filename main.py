class Cafe:
    def __init__(self, nomi, manzil, taom, narx):
        self.nomi = nomi
        self.manzil = manzil
        self.taom = taom
        self.narx = narx

    def info(self):
        print("Cafe:", self.nomi)
        print("Manzil:", self.manzil)
        print("Taom:", self.taom)
        print("Narx:", self.narx)

    def buyurtma(self):
        print(self.taom, "buyurtma qilindi")


cafe1 = Cafe("Bella Cafe", "Samarqand", "Burger", 30000)

cafe1.info()
cafe1.buyurtma()
