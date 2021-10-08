class Employee:
    def __init__(self, namn, kontonummer, age, 
            monthlySalary, timeHourly):
        self._namn = namn
        self._kontonummer = kontonummer
        self._age = age
        self._monthlySalary = monthlySalary
        self._timeHourly = timeHourly
        self._hoursWorked  = 0

    def calculateSalary(self):
        if self._hoursWorked > 0:
            return self._hoursWorked * self._timeHourly 
        salary = self._monthlySalary 
        if self._age > 48:
            salary = salary + 50
        return salary

    def setWorkedHours(self,timmar):
        self._hoursWorked = timmar

    def sendToBank(self, belopp):
        print(f"{self._kontonummer} {belopp}")



listOfEmployees = []

listOfEmployees.append(Employee("Stefan", "11123", 49, 15000,0))
n = Employee("Oliver", "22211",13, 12000,0)
listOfEmployees.append(n)

josefine = Employee("Josefine", "555599", 19, 0,120)
listOfEmployees.append(josefine)
josefine.setWorkedHours(18)


for emp in listOfEmployees:
    belopp = emp.calculateSalary()
    emp.sendToBank(belopp)

