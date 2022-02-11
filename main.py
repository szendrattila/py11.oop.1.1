'''
1.1 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
'''

class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def kerulet(self):
        return self.oldalhossz * 4
    def terulet(self):
        return self.oldalhossz ** 2


negyzet_01 = Negyzet(7)
print(f"A neégyzet területe: {negyzet_01.terulet()}")
print(f"A neégyzet kerülete: {negyzet_01.kerulet()}")

