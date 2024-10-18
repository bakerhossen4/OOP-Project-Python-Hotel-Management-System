
from rooms import Rooms

class HotelManager:
    def __init__(self):
        self.roomlist = []
        self.bookinglists = []
    def add_room( self, roomob ) :
        self.roomlist.append( roomob )
        print(f"Room Id : {roomob.id} Room No: {roomob.no} added Successfully")
    def show_available_rooms( self ):
        print("-----------------------------")
        print("-----Show Available Rooms----")
        print("ID\t\tRoomNo\t\tBookStatus")
        for i in self.roomlist :
            if i.booked == False :
                print(f"{i.id}\t\t{i.no}\t\t{i.booked}")
        print("-----------------------------")
    def show_booked_rooms( self ):
        print("-----------------------------")
        print("-----Show Booked Rooms----")
        print("ID\t\tRoomNo\t\tBookStatus")
        for i in self.roomlist :
            if i.booked == True :
                print(f"{i.id}\t\t{i.no}\t\t{i.booked}")
        print("-----------------------------")
    def reserve_room( self, roomid, bookob ) :
        print("-----------------------------")
        for i in self.roomlist :
            if i.booked == False:
                if i.id == roomid :
                    i.booked = True
                    self.bookinglists.append(bookob)
                    print(f"ID: {i.id}, Room No - {i.no} Booked Successfully")
            else:
               print(f"ID: {i.id}, Room No - {i.no} Booked Already. Unable to book now !")
        print("-----------------------------")
    def bookinglist( self ):
        print("-----------------------------")
        print("----- Show Booked Rooms of all customers ----")
        print("ID\t\tCustomerName")
        for i in self.bookinglists :
            print(f"{i.rid}\t\t{i.cusname}")
        print("-----------------------------")