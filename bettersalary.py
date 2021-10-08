class Employee:
    def __init__(self, namn, kontonummer):
        self._namn = namn
        self._kontonummer = kontonummer

    def calculateSalary(self):
        return 0

    def sendToBank(self, belopp):
        print(f"{self._kontonummer} {belopp}")

class MonthlyEmployee (Employee):
    def __init__(self, namn, kontonummer, monthlySalary):
        super().__init__(namn, kontonummer)
        self._monthlySalary = monthlySalary

    def calculateSalary(self):
        return self._monthlySalary

class HourlyEmployee (Employee):
    def __init__(self, namn, kontonummer, hourlySalary,hoursWorked):
        super().__init__(namn, kontonummer)
        self._hourlySalary = hourlySalary
        self._hoursWorked = hoursWorked

    def calculateSalary(self):
        return self._hourlySalary * self._hoursWorked        

a = MonthlyEmployee("Stefan", "999111222",15000)
b = MonthlyEmployee("Oliver", "111454545",12000)
c = HourlyEmployee("Josefine", "111454545",120, 181)
listOfEmployees = [a,b,c]

for emp in listOfEmployees:
    belopp = emp.calculateSalary()
    emp.sendToBank(belopp)

