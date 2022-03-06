
print('\t\t\tWELCOME TO VEHICLE RENTAL MANAGING APP')
print('=================EMPLOYEE LOGIN PAGE================')
email=input('Email : ')
password=input('Password : ')
if email == 'shrutiepawar@gmail.com' and 'password ==app@123!':
    print('Welcome to Vehicle Rental Managing Application ')
else:
    print('Please check the email id and password you have entered. ')
print('===============================================================')
print('\tMenu')
class customer():
    def __init__(self,CustomerName,PhoneNumber,Email):
        self.CustomerName=CustomerName
        self.PhoneNumber=PhoneNumber
        self.Email=Email
    def display(self):
        print("{0}\t{1}\t{2}".format(self.CustomerName,self.PhoneNumber,self.Email))

class rental():
    def __init__(self,name,rentaldate,returndate,vehicletype):
        if(vehicletype in vlist):
            self.CustomerName=name
            self.rentaldate=rentaldate
            self.returndate=returndate
            self.vehicletype=vehicletype
        else:
            print("Vehicle not available")
    def show(self):
        print("{0}\t{1}\t{2}\t{3}".format(CustomerName,rentaldate,returndate,vehicletype))

vlist = ["bike", "cycle", "car", "boat"]
count=[2,3,1,2]
custlist=[]
rentlist=[]
while(1):
    print("1. Add customer*")
    print("2. Add rental booking")
    print("3. See customer list")
    print("4. See rental booking list")
    print("5. See inventory of vehicles available")
    print("6. Exit")
    print('-----------------------------------------')

    choice=eval(input("Please enter choice : "))
    if(choice==1):
        CustomerName = input("Please enter Customer Name : ")
        PhoneNumber = eval(input("Please enetr Mobile Number :"))
        Email = input("Please enter Customer Email Address : ")
        n=customer('shruti',9008530619,'shrutiepawar@gmail.com')
        custlist.append(n)
    if(choice==2):
        print("Please add rental booking")
        name=input("Please enter customer name : ")
        for x in custlist:
            if(x.CustomerName==name):
                rentaldate=input("Enter rental start Date(ddmmyyyy) : ")
                returndate=input("Enter return end date(ddmmyyyy) : ")
                vehicletype=input("Enter vehicle from ['bike,cycle,car,boat'] : ")
                print('Reserved your Ride')
                print("We hope that you will enjoy our service!")
                print('-------------------------------------------')
                for i in range(4):
                    if(vlist[i]==vehicletype and count[i]>0):
                        a = rental(name, rentaldate, returndate, vehicletype)
                        rentlist.append(a)
                        count[i]=count[i]-1
                        break
                else:
                    print("{0} cannot be rented as it is already booked Please check Availability".format(vehicletype))
                break
        else:
            print("customer not available")

    if(choice==3):
        print("--------------------------------")
        print("---------Customer Names---------")
        print("--------------------------------")
        for x in custlist:
            x.display()

    if (choice == 4):
        print("--------------------------------")
        print("--------Rental list Names--------")
        print("--------------------------------")
        for x in rentlist:
            x.show()

    if(choice==5):
        print("--------------------------------")
        print("--------Available Rental vehicles--------")
        print("--------------------------------")
        for i in range(4):
            print("{0} = {1}".format(vlist[i],count[i]))

    if(choice==6):
        break
