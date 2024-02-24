import enum

class Gender(enum.Enum):            #Create ENUM for gender (Female or Male)
    Female = 1
    Male = 2

class PassengerDetail:              #Class #1
    '''Class to represent Passenger Details'''
    def __init__(self, firstName, lastName, age, gender, passportNum, nationality):
        '''Initialize the attributes of the class'''
        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__gender = gender
        self.__passportNum = passportNum
        self.__nationality = nationality

    def setFirstName(self, firstName = " "):          # Set the first Name of the passenger
        self.__lfirstName = firstName

    def getFirstName(self):                          # Get the first Name of the passenger
        return self.__firstName

    def setLastName(self, lastName = " "):          # Set the Last name of the passenger
        self.__lastName = lastName

    def getLastName(self):                      # Get the Last name of the passenger
        return self.__lastName

    def setAge(self, age = 0):                #Set the age of the passenger
        self.__age = age

    def getAge(self):                      #Get the age of the passenger
        return self.__age

    def setGender(self, gender = None):         #Set the gender of the passenger
        self.__gender = gender

    def getGender(self):                   #Get the gender of the passenger
        return self.__gender

    def setPassportNum(self, passportNum = " "):   #Set the passport number of the passenger
        self.__passportNum = passportNum

    def getPassportNum(self):                 #Get the passport number of the passenger
        return self.__passportNum

    def setNationality(self, nationality = " "):     #Set the nationality of the passenger
        self.__nationality = nationality

    def getNationality(self):                  #Get the nationality of the passenger
        return self.__nationality

    def illegal(self):
        '''Check if the passenger is legal or illegal to fly'''
        if self.__age < 18:
            return False  # Passenger is illegal and can't fly
        else:
            return True  # Passenger is legal and can fly


import enum

class ClassType(enum.Enum):                   #Create ENUM for the passengers class type
    FirstClass = 1
    BusinessClass = 2
    EconomyClass = 3

class Passenger:              #Class #2
    '''Class to represent Passenger'''

    def __init__(self,luggageNum, classType, date, fromDestiny, toDestiny):
        '''Initialize the attributes of the class'''
        self.__luggageNum = luggageNum
        self.__classType = classType
        self.__date = date
        self.__fromDestiny = fromDestiny
        self.__toDestiny = toDestiny

    def setLuggageNum(self, luggageNum = 0):       #Set the number of luggages of the passenger
        self.__luggageNum = luggageNum

    def getLuggageNum(self):                  #Get the number of luggages of the passenger
        return self.__luggageNum

    def setClassType(self, classType):                 #Set the Class type of the passenger
        self.__classType = classType

    def getClassType(self):                 #Get the Class type of the passenger
        return self.__classType

    def setDate(self, date = " "):  # Set the date of the flight
        self.__date = date

    def getDate(self):  # Get the date of the flight
        return self.__date

    def setFromDestiny(self, fromDestiny = " "):                #Set the Destiny from of the passenger
        self.__fromDestiny = fromDestiny

    def getFromDestiny(self):                       #Get the Destiny from of the passenger
        return self.__fromDestiny

    def setToDestiny(self, toDestiny = " "):                #Set the Destiny to of the passenger
        self.__toDestiny = toDestiny

    def getToDestiny(self):                       #Get the Destiny to of the passenger
        return self.__toDestiny


class Flight:              #Class #3
    '''Class to represent Passenger Flight Detail'''
    def __init__(self, flightNumber, seatNumber, departureTime, boardingTime, arrivalTime):
        ''''Initialize the attributes of the class'''
        self.__flightNumber = flightNumber
        self.__seatNumber = seatNumber
        self.__departureTime = departureTime
        self.__boardingTime = boardingTime
        self.__arrivalTime = arrivalTime

    def setFlightNumber(self, flightNumber = " "):  # Set the flight number of the flight
        self.__flightNumber = flightNumber

    def getFlightNumber(self):  # Get the flight number of the flight
        return self.__flightNumber

    def setSeatNumber(self, seatNumber = " "):                 #Set the Seat Number of the passenger
        self.__seatNumber = seatNumber

    def getSeatNumber(self):                 #Get the Seat Number of the passenger
        return self.__seatNumber

    def setDepartureTime(self, departureTime = " "):  # Set the departure time of the flight
        self.__departureTime = departureTime

    def getDepartureTime(self):  # Get the departure time of the flight
        return self.__departureTime

    def setBoardingTime(self, boardingTime = " "):  # Set the boarding time of the flight
        self.__boardingTime = boardingTime

    def getBoardingTime(self):                # Get the boarding time of the flight
        return self.__boardingTime

    def setArrivalTime(self, arrivalTime = " "):         # Set the arrival time of the flight
        self.__arrivalTime = arrivalTime

    def getArrivalTime(self):              # Get the arrival time of the flight
        return self.__arrivalTime


import enum
class TransportService(enum.Enum):              #Type of transportation service to reach the terminal, gate, (Train, Car, or Bus)
    Train = 1
    GulfCar = 2

class Enterance(enum.Enum):              #Type of entrence when entering the airport (VIP, or Regular enterence)
    VIP = 1
    Regular = 2


class AirPort:                      #Class #4
    '''Class to represent Passenger AirPort Details'''
    def __init__(self, airlineComp, gateNum, terminalNum, transportServ, enterance):
        '''Initialize the attributes of the class'''
        self.__airlineComp = airlineComp
        self.__gateNum = gateNum
        self.__terminalNum = terminalNum
        self.__transportServ = transportServ
        self.__enterance = enterance

    def setAirlineComp(self, airlineComp = " "):          #Set the airline company name
        self.__airlineComp = airlineComp

    def getAirlineComp(self):                    #Get the airline company name
        return self.__airlineComp

    def setGateNum(self, gateNum = " "):                #Set the gate number
        self.__gateNum = gateNum

    def getGateNum(self):                       #Get the gate number
        return self.__gateNum

    def setTerminalNum(self, terminalNum = 0):                #Set the terminal number
        self.__terminalNum = terminalNum

    def getTerminalNum(self):                     #Get the terminal number
        return self.__terminalNum

    def setTransportService(self, transportServ):        #Set the transportation service (train, gulf car, car)
        self.__transportServ = transportServ

    def getTransportService(self):               #Get the transportation service
        return self.__transportServ

    def setEnterance(self, enterance):           #Set the enterance type (VIP, Business)
        self.__enterance = enterance

    def getEnterance(self):             #Get the enterance type
        return self.__enterance



import enum

class YorN(enum.Enum):
    '''Create ENUM class for 2 options Yes or No'''
    Yes = 1
    No = 2

class Ticket:                    #Class #5
    '''Class to represent Passenger Ticket Details'''
    def __init__(self, elecTicketNum, price, deskNumber, seatUpgrade, boardingPassCode, boardingPass):
        ''''Initialize the attributes of the class'''
        self.__elecTicketNum = elecTicketNum
        self.__price = price
        self.__deskNumber = deskNumber
        self.__seatUpgrade = seatUpgrade
        self.__boardingPassCode = boardingPassCode
        self.__boardingPass = boardingPass

    def setElecTicketNum(self, elecTicketNum = 0):               #Set the electronic ticket number
        self.__elecTicketNum = elecTicketNum

    def getElecTicketNum(self):                      #Get the electronic ticket number
        return self.__elecTicketNum

    def setPrice(self, price = " "):               #Set the price of the ticket
        self.__price = price

    def getPrice(self):                             #Get the price of the ticket
        return self.__price

    def setDeskNumber(self, deskNumber = " "):              #Set the desk number where the ticket was issued
        self.__deskNumber = deskNumber

    def getDeskNumber(self):                  #Get the desk number where the ticket was issued
        return self.__deskNumber

    def setYorN(self, seatUpgrade):                #Set the seat upgrade status
        self.__seatUpgrade = seatUpgrade

    def getYorN(self):                         #Get the seat upgrade status
        return self.__seatUpgrade

    def setBoardingPassCode(self, boardingPassCode = " "):          #Set the Boarding Pass code
        self.__boardingPassCode = boardingPassCode

    def getBoardingPassCode(self):                       #Get the Boarding Pass code
        return self.__boardingPassCode

    def setBoardingPass(self, boardingPass = " "):              #Set the Boarding Pass
        self.__boardingPass = boardingPass

    def getBoardingPass(self):                           #Get the Boarding Pass
        return self.__boardingPass



passenger1 = PassengerDetail( "James", "Smith", 26, Gender.Male, "US76294", "USA")
'''Created an object by filling the first passenger detail in PassengerDetail Class'''

passenger2 = Passenger(2, ClassType.FirstClass, "06 Dec 20", "Chicago ORD", "New York JFK")
'''Created an object by filling the first passenger detail in Passenger Class'''

passenger3 = Flight("NA4321", "09A", "11:40", "11:20", "13:30")
'''Created an object by filling the first passenger detail in Flight Class'''

passenger4= AirPort("National Airline", "03", 2, TransportService.GulfCar, Enterance.VIP)
'''Created an object by filling the first passenger detail in Airline Class'''

passenger5= Ticket(629, "598.9$", "24A" , YorN.Yes, "5A6BCD78", "Passenger ticket and Baggage check")
'''Created an object by filling the first passenger detail in Ticket Class'''



#Display ALL Passengers Data in the Boarding pass
print("Boarding Pass:", passenger5.getBoardingPass())
print("Passenger Name:", passenger1.getFirstName(), passenger1.getLastName())
print("Passenger Age:", passenger1.getAge())
print("Passenger Gender:", passenger1.getGender())
print("Passenger Passport Number:", passenger1.getPassportNum())
print("Passenger Nationality:", passenger1.getNationality())

print("Number of Luggages:", passenger2.getLuggageNum())
print("Class Type:", passenger2.getClassType())
print("Date of Flight:", passenger2.getDate())
print("From Destination:", passenger2.getFromDestiny())
print("To Destination:", passenger2.getToDestiny())

print("Flight Number:", passenger3.getFlightNumber())
print("Seat Number:", passenger3.getSeatNumber())
print("Departure Time:", passenger3.getDepartureTime())
print("Boarding Time:", passenger3.getBoardingTime())
print("Arrival Time:", passenger3.getArrivalTime())

print("Airline Company:", passenger4.getAirlineComp())
print("Gate Number:", passenger4.getGateNum())
print("Terminal Number:", passenger4.getTerminalNum())
print("Transport Service:", passenger4.getTransportService())
print("Entrance Type:", passenger4.getEnterance())

print("Electronic Ticket Number:", passenger5.getElecTicketNum())
print("Ticket Price:", passenger5.getPrice())
print("Desk Number:", passenger5.getDeskNumber())
print("Seat Upgrade:", passenger5.getYorN())
print("Boarding Pass Code:", passenger5.getBoardingPassCode())
print("Seat Upgrade:", passenger5.getYorN())
print("Boarding Pass Code:", passenger5.getBoardingPassCode())