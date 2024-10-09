import time, os, subprocess, random
from curses.ascii import isdigit, isalpha
from datetime import datetime
from select import select


class TimeInterval:

    def __init__(self, h, m, s, d):
        d = 0
        if (s == 60):
            m += 1

        if (m == 60):
            h += 1

        if (h >= 24):
            h = (h % 24)



        if not isinstance(h, int) or not isinstance(h, int) or not isinstance(s, int):
            raise TypeError("Hours, minutes, and seconds must be integers.")

        elif (s < 60) and (m < 60):
            self.horas = h
            self.minutos = m
            self.segundos = s
        else:
            raise TypeError("Digite um horário válido.")

    def secondTransform(self):
        return (self.horas * 3600) + (self.minutos * 60) + self.segundos

    def secondToTime(s):
        h, rest = divmod(s, 3600)
        m,s = divmod(rest,60)
        return TimeInterval(h,m,s)


  #  def __add__(self,other):
  #          total_segundos = self.secondTransform() + other.secondTransform()
  #          return TimeInterval.secondToTime(total_segundos)

    def __add__(self, s):

        total_segundos = self.secondTransform() + s
        return TimeInterval.secondToTime(total_segundos)

  #  def __sub__(self,other):
   #     total_segundos = self.secondTransform() - other.secondTransform()
   #         return TimeInterval.secondToTime(total_segundos)

    def __sub__(self, s):
        total_segundos = self.secondTransform() - s
        return TimeInterval.secondToTime(total_segundos)

    def __mul__(self,other):
            total_segundos = self.secondTransform() * other.secondTransform()
            return TimeInterval.secondToTime(total_segundos)

    def __str__(self):

        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"


    def counter(self):

        x = self.secondTransform()
        for x in range (x,-1,-1):
            self = TimeInterval.secondToTime(x)
            print(f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}")
            time.sleep(1)
            subprocess.run('clear', shell = True)




#contador



#t1 = TimeInterval(12, 35, 15)
#t2 = TimeInterval(00, 2, 5)

#t2.counter()
#t3 = (t1 * t2)
#print(str(t3))

#try:
 #   element.melt()
#except AttributeError:4
 #   print('No melt() method')
'''

x = int(input())
y = int(input())

for s in range(x):
    for t in range(y):
        if ((t==0) or (t == y-1)):
            print("|", end="")
        elif (s != 0) and (s != x-1):
            print(" ", end = "")

        if(s==0) and (t < y-2):
            print("-", end = "")
        elif (s==x-1) and (t < y-2):
            print("_", end ="")

    print()
    
def printTimeStamp(function):
    timestamp = datetime.now()
    micro = timestamp.microsecond
    def wrapper(*args, **kwargs):
        print(timestamp.strftime("%d-%m-%Y %H:%M:%S"))
        name = (format(function.__name__))
        print(f"\n\t\tCalculando: {name.upper()}...")
        print('\n\t{}\t{}\n'.format(args, kwargs))
        time.sleep(3)
        function(*args, **kwargs)
        print(f"\nExecution time: {datetime.now().microsecond - micro} microseconds")
        #return function (*args, **kwargs)

    return wrapper

@printTimeStamp
def imc(p,a, peso, altura):
    print(f"{p/(pow(2,a)):.2f}")

@printTimeStamp
def percentual(n, nt, numero, total):
    print(f"{(n/nt)*100:.2f}%")


#imc(85, 1.75, peso = 85, altura = 1.75)
#ercentual(90,230,numero = 90, total = 230)


class RelogioLuxo:

    numero_relogios = 0

    def __init__(self):
        RelogioLuxo.numero_relogios += 1

    @classmethod
    def getNumeroRelogios(cls):
        return cls.numero_relogios

    @classmethod
    def gravarNoRelogio(cls, texto):
        incorretos = ""
        if (len(texto) <= 40) and (texto.isdigit() or texto.isalpha()):
            RelogioLuxo()
            print(f"Texto {texto} gravado")
        elif len(texto) < 40:
            for i in texto:
                if (not isdigit(i)) and (not isalpha(i)):
                    if (i == " "):
                        i = ('" "')
                    incorretos  += i
            print(f"Digito(s) {incorretos} incorreto(s)")
        else:
            print("O texto ultrapassou o numero de caracteres")


#RelogioLuxo.gravarNoRelogio("uidhjaidjduhasiuhduiashda")
#print(RelogioLuxo.getNumeroRelogios())

import abc

class Scanner(abc.ABC):
    max_resolution = 0
    sn = None

    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    max_resolution = 0
    sn = None

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD(Scanner, Printer):

    def __init__(self, sn):
        Scanner.sn = sn
        Printer.sn = sn

    def scan_document(self):
        print("----------The document has been scanned!----------\n")

    def get_scanner_status(self):
        return Scanner.max_resolution, self.sn

    def print_document(self):
        print("----------The document has been printed!----------\n")

    def get_printer_status(self):
        return Printer.max_resolution, self.sn

    def status(self):
        res, s = self.get_scanner_status()
        print(f"Scanner SN: {s} \tResolução: {res}")
        res, s = self.get_printer_status()
        print(f"Impressora SN: {s} \tResolução: {res}")




class MFD1(MFD):

    def __init__(self, sn):
        Scanner.max_resolution = 250
        Printer.max_resolution = 250
        super().__init__(sn)

    def scan(self):
        self.scan_document()

    def print(self):
        self.print_document()

    def status(self):
        super().status()
        print()


class MFD2(MFD):

    def __init__(self, s):
        Scanner.max_resolution = 600
        Printer.max_resolution = 600
        self.operationH = 0
        super().__init__(s)


    def scan(self):
        self.scan_document()

    def print(self):
        self.operationH += 1
        self.print_document()

    def status(self):
        super().status()
        print(f"Numero de impressões realizadas: {self.operationH}\n")


class MFD3(MFD):

    def __init__(self, sn, n):
        self.operationH = 0
        Scanner.max_resolution = 1200
        Printer.max_resolution = 1200
        super().__init__(sn)
        self.numFax = n
        self.fax = True


    def scan(self):
        self.scan_document()

    def print(self):
        self.print_document()
        self.operationH += 1

    def status(self):
        super().status()
        print(f"Numero de impressões realizadas: {self.operationH}")
        print(f"Fax numero: {self.numFax}")
        if(self.fax):
            print(f"Status Fax: Ligado\n")
        else:
            print(f"Status Fax: Desligado\n")

    def desligarFax(self):
        print("----------Desligando Fax----------")
        time.sleep(2)
        self.fax = False
        print("----------Fax Desligado---------\n")



m1 = MFD1("123123123")
m1.print()
m1.scan()
m1.status()

m2 = MFD2("sadasfsfsda")
i = 0
while (i!=10):
    m2.print()
    i+=1
m2.scan()
m2.status()

m3 = MFD3("s11111111a", "(45) 98412-4576")
m3.print()
m3.scan()
m3.status()
m3.desligarFax()
m3.status()


class AccountError(Exception):
    pass


class BankAcount:

    def __init__(self):
        self.__number = random.randint(1, 400000)
        self.__balance = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, n):
        raise AccountError("No permision for change account number")

    @number.deleter
    def number(self):
        if (self.__balance == 0):
            self.__number = 0
        else:
            raise AccountError("No permission to delete account number")

    @property
    def balance(self):
        return balance.__number

    @balance.setter
    def balance(self, b):
        if (b >= 0):
            if (b > 100000):
                print("You've set a balance greater than $ 100.000")
            self.__balance = b
        else:
            raise AccountError("You can't set a negative balance")


ba = BankAcount()
ba.balance = 1000.00
try:
    ba.balance = -200.00
except AccountError as e:
    print(e)

try:
    ba.number = 231297986
except AccountError as e:
    print(e)

ba.balance = 1000000.00

try:
    del ba.number
except AccountError as e:
    print(e)


class Tire:

    def __init__(self, size, max_pressure, current_pressure):
        self.size = size
        self.max_pressure = max_pressure
        self.current_pressure = current_pressure


class CityTire(Tire):

    def __init__(self, current_pressure):
        size = 15
        max_pressure = 40
        super().__init__(size, max_pressure, current_pressure)

    def get_pressure(self):
        print(f"City Tire maximum pressure:\t {self.max_pressure} lbs")
        print(f"City tire current pressure is:\t{self.current_pressure} lbs")

    def pump(self, n):
        print("Pumping City Tire...")
        if (self.current_pressure + n <= self.max_pressure):
            self.current_pressure += n
        else:
            (f"Current City Tire achive maximum pressure {self.max_pressure} lbs!!")
            self.current_pressure = self.max_pressure


class RoadTire(Tire):

    def __init__(self, current_pressure):
        size = 18
        max_pressure = 60
        super().__init__(size, max_pressure, current_pressure)

    def get_pressure(self):
        print(f"Road Tire maximum pressure:\t {self.max_pressure} lbs")
        print(f"Road Tire current pressure is:\t{self.current_pressure} lbs")

    def pump(self, n):
        print("Pumping Road Tire...")
        if (self.current_pressure + n <= self.max_pressure):
            self.current_pressure += n
        else:
            (f"Current Road Tire achive maximum pressure {self.max_pressure} lbs!!")
            self.current_pressure = self.max_pressure


class Engine:

    def __init__(self, fueltype):
        self.fuel_type = fueltype
        self.started = False

    def start(self):
        print("Engine started!!!")
        self.started = True

    def stop(self):
        print("Engine stoped!!!")
        self.started = False

    def getState(self):
        if (self.started):
            print("Engine is ON")
            print(f"Fuel Type: {self.fuel_type}")
        else:
            print("Engine is OFF")


class EletricEngine(Engine):

    def __init__(self):
        super().__init__("Eletric")


class PetrolEngine(Engine):

    def __init__(self):
        super().__init__("Petrol")


class Car:

    def __init__(self, VIN, engine, tire):
        self.VIN = VIN
        self.engine = engine
        self.tire = tire

    def get_engine_status(self):
        self.engine.getState()

    def turn_on_engine(self):
        self.engine.start()

    def turn_off_engine(self):
        self.engine.stop()

    def get_tire_pressure(self):
        self.tire.get_pressure()

    def pump_tire(self, lbs):
        self.tire.pump(lbs)


t1 = CityTire(32)
t2 = RoadTire(28)
e1 = EletricEngine()
e2 = PetrolEngine()

c1 = Car("abc1234", e1, t1)
c2 = Car("tuv8765", e2, t2)

c1.turn_on_engine()
c1.get_engine_status()
c1.get_tire_pressure()
c1.pump_tire(10)
c1.get_tire_pressure()
c1.turn_off_engine()
c1.get_engine_status()
print("\n\n")

c2.turn_on_engine()
c2.get_engine_status()
c2.get_tire_pressure()
c2.pump_tire(40)
c2.get_tire_pressure()
c2.turn_off_engine()
c2.get_engine_status()


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp('MonitoredDict created')

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp('value for key [{}] retrieved'.format(key))
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp('value for key [{}] set'.format(key))

    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append('{} {}'.format(timestampStr, message))


kk = MonitoredDict()
kk[10] = 15
kk[20] = 5

print('Element kk[10]:', kk[10])
print('Whole dictionary:', kk)
print('Our log book:\n')
print('\n'.join(kk.log))

'''

print(divmod(47,24))
