class Train:
    def __init__(self,name,fair,seats):
        self.name= name 
        self.fair = fair
        self.seats = seats
    
    def getstatus(self):
        print(f"The name of the train is {self.name}.")
        print(f"The seats available in the train is : Rs. {self.seats}.")

    def fairinfo(self):
        print(f"The price of the ticket is : {self.fair}.")

    def bookticket(self):
        if self.seats>0:
            print(f"Your tickets has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, No sets left")
    
a = Train("Intercity Express:110022",115,2)
a.getstatus()
a.fairinfo()
a.bookticket()

