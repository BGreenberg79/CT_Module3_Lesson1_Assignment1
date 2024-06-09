# Task 1 Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(hotel, room, name):
    room = str(room)
    if room in hotel and hotel[room]["status"] == "available":
        hotel[room]["status"] = "booked"
        hotel[room]["customer"] = name.title()
        print(f"Room number {room} has been marked as {hotel[room]["status"]} for customer {name.title()}")
    elif room in hotel and hotel[room]["status"] == "booked":
        print(f"Sorry, room number {room} has already been booked.")
    else:
        print("It appear you have entered an invalid room number or hotel dictionary.")

book_room(hotel_rooms, 101, "Ben Greenberg")
#print(hotel_rooms)

'''
The book_room function works through three parameters, the first being the hotel dictionary we are working off of, and then the room number we are trying to book and the name of the customer
we are assigning the room to. first we ensure that room is converted to string as our initial dictionary lists the room keys as strings.
then in an if block we check if the room is in the hotel dictionary and if hthe status of the hotel room we are trying to book is available.
If it is we reassign the status to booked and assign a customer name in title case. Then we print an f-string saying what the program did to the dictionary.
That is followed by an elif statement that checks if we are trying to book an already occupied room and an else statement that will catch any attempts to book an invalid room number.
'''

def checkout(hotel, room):
    room = str(room)
    if room in hotel and hotel[room]["status"] == "booked":
        print(f"Customer, {hotel[room]["customer"].title()}, is checking out of room number {room}.")
        hotel[room]["status"] = "available"
        hotel[room]["customer"] = ""
    elif room in hotel and hotel[room]["status"] == "available":
        print("Cannot check-out an unoccupied room.")
    else:
        print("It appears you have entered an invalid room number or hotel dictionary.")

checkout(hotel_rooms, 101)
#checkout(hotel_rooms, 101)

'''
The checkout function uses a very similar logic structure and if/elif/else block as the previously defined book_room function
Here I once again convert room number to string and follow it with an if statement that checks if the room is in the hotel and if the room is booked.
If the room is booked I print an f-string stating the customer that is checking out and which room they are checking out of. I then mark that room as available and assign the name function a value of empty string ""
The elif statement checks an invalid checkout where the user tries to check out of a room that isn't occupied and the else statement picks up invalid entries with a wrong hotel dictionary or a non-existant room number
'''

def display_status(hotel):
    print("Hotel Room Status Report")
    for room, details in hotel.items():
        print(f"Room Numer: {room}") 
        print(f"Room Status: {details["status"].title()}, Guest Name: {details["customer"].title()}")
    
display_status(hotel_rooms)

'''
The Display_status function works with print statments and by usinga for loop paired with the .items() method to run through each hotel room in the dictionary and cleanly print the room's details and status.
The first variable created for the for loop is room and that pairs with the keys of the outer dictionary. We print that before going into the different values of the inner dictionary we need to report.
The f-string set up makes the keys from the inner dictionary redundant so we do not need to access them when printing. This is the reason we don't need a second for loop nested inside the first one, even though admittedly I was making that mistake initially.
As details (the values from the outer dictionary) is a dictionary itself, to unpack it we need to reference which keys we are pulling data from when printing the inner values. That is why we use the notation of details["status"] and details["customer"] to unpack the inner dictionary when accessing the second variable our for loop creates.
'''