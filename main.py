from customer import Customer
from rooms import Rooms
from hotelmanager import HotelManager
from booking import Booking
id = 1
no = 200
hotelob = HotelManager()

def cus_menu() :
    name = input("Enter Customer Name : ")
    cusob = Customer( name )
    while True :
        print("------------------------------------")
        print("2: Reserve a Room ")
        print("3: Show available Rooms")
        print("4: Show Booked Rooms")
        print("5: Show Booking List of all customers ")
        print("6: Go to Admin Panel")
        print("------------------------------------")
        data = int(input("Enter Input : "))
        if data == 2: 
            roomid = int(input("Enter Room Id : "))
            bookob = Booking( roomid, name )
            hotelob.reserve_room(roomid, bookob)
        elif data == 3: 
            hotelob.show_available_rooms()
        elif data == 4:
            hotelob.show_booked_rooms()
        elif data == 5:
            hotelob.bookinglist()
        elif data == 6:
            break
while True :
    print("------------------------------------")
    print("******* Admin Panel ********")
    print("1: Add room")
    print("2: Login as Customer")
    print("------------------------------------")
    data = int(input("Enter Input : "))
    if data == 1 :
        roomob = Rooms( id, no )
        id = id + 1
        no = no + 1
        hotelob.add_room( roomob )
    elif data == 2:
        cus_menu()
    else :
        break
        

