class Konto:
    def __init__(self, kontonr, pin):
        self._saldo = 0
        self._kontonr = kontonr
        self._pinkod = pin
    
    def withdraw(self,belopp):
        if self._saldo < belopp:
            return False
        self._saldo = self._saldo - belopp
        return True

v = input("Ange kontonr")
a = input("Ange pinkod")
stefansKonto = Konto(v,a)        
if stefansKonto.withdraw(100) == False:
    print("Inga pengar")
else:    
    print("Uttaget lyckades")

