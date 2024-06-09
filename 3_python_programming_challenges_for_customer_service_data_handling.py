# Task 1 Customer Service Ticket Tracker

def open_ticket(ticket_dict, ticket_id, name, issue):
    ticket_dict[ticket_id] = {}
    ticket_dict[ticket_id].update({"Customer": name.title()})
    ticket_dict[ticket_id].update({"Issue": issue})
    ticket_dict[ticket_id].update({"Status": "open"})
    print(f"Ticket ID {ticket_id} has been opened for customer, {name.title()}, who is experiencing issues with {issue}")

'''
This function, open_tickets works with parameters for the ticket dictionary we are feeding into the function, and then 
strings for ticket_id, name and issue. The ticket_id becomes the key for the outer dictionary that will be assigned a value of a dictinary full of that ticket's details.
This value starts off as an assignment of an empty dictionary. We then assign customer name and issue with the arguments we will feed in by using the .update() method after directing through the outer dictionary's key.
Lastly when we use that same meth to assign status insted of taking in an argument/parameter we default to open because when opening a ticket it will never start off as closed.
'''

def update_status(ticket_dict, ticket_id, status):
    try:
        ticket_dict[ticket_id].update({"Status": status})
        print(f"Ticket ID {ticket_id} has had its status updated to {status}")
    except KeyError:
        print("Please enter valid ticket number to update.")

'''
I decided to have update_status work by taking 3 parameters, one for the dictionary we are working with, one for the ticket id we are adjusting (the key in the outer dictionary),
and then the new status we are assigning to the ticket. I decided to take this third parameter so our function could not just close an open ticket,
but reopen a ticket if an addressed issue suddenly re-emerges. I used a similar structure to my open_ticket function however for this function we do not need to modify name or issue,
just the status of the ticket and then reflect this through a print statement. I also put this in a try/except block to pick up any key errors.
'''

#import copy

def display_tickets(ticket_dict, status_filter):
    status_filter = status_filter.lower()
    if status_filter.lower() == "all tickets":
        print("Service Tickets:")
        for ticket, ticket_details in ticket_dict.items():
            print(f"Ticket ID: {ticket}\nCustomer: {ticket_details["Customer"]}\nIssue: {ticket_details["Issue"]}\nStatus: {ticket_details["Status"]}")
    elif status_filter.lower() == "open tickets":
        print("Service Tickets:")
        for ticket, ticket_details in ticket_dict.items():
            if ticket_dict[ticket]["Status"] == "open":
                print(f"Ticket ID: {ticket}\nCustomer: {ticket_details["Customer"]}\nIssue: {ticket_details["Issue"]}\nStatus: {ticket_details["Status"]}")
    elif status_filter.lower() == "closed tickets":
        print("Service Tickets:")
        for ticket, ticket_details in ticket_dict.items():
            if ticket_dict[ticket]["Status"] == "closed":
                print(f"Ticket ID: {ticket}\nCustomer: {ticket_details["Customer"]}\nIssue: {ticket_details["Issue"]}\nStatus: {ticket_details["Status"]}")
    else:
        print("Incorrect status filter input. Please use a specified option.")

def display_tickets2(ticket_dict, status_filter):
    status_filter = status_filter.lower()
    for ticket, ticket_details in ticket_dict.items():
        if ticket_dict[ticket]["Status"] in status_filter:
            print(f"Ticket ID: {ticket}\nCustomer: {ticket_details["Customer"]}\nIssue: {ticket_details["Issue"]}\nStatus: {ticket_details["Status"]}")
        else:
            print(f"Ticket ID: {ticket}\nCustomer: {ticket_details["Customer"]}\nIssue: {ticket_details["Issue"]}\nStatus: {ticket_details["Status"]}")
'''
Refactored during tutoring with Daniel
'''


'''
This function works by showing either all tickets, open tickets, or closed tickets by using an if/elif/elif/else block to compare the filter entered
to each of those three options. For the all block no further comparison is needed and we can just loop through all of the keys and values for all of the tickets.
To essentially filter for open or closed though a nested if statement is inside each elif block that navigates to the inner dictionary and looks for either a closed or open status
printing off each ticket ID and its details that match that specific status. The else block specifies if an unexpected filter was listed that doesn't entail open or closed. 
'''
service_tickets= {}

open_ticket(service_tickets, "Ticket001", "Ben G", "Keyboard Error")
open_ticket(service_tickets, "Ticket002", "Matt G", "Slow Internet")
open_ticket(service_tickets, "Ticket003", "Alyssa W", "Login problem")
#update_status(service_tickets, "Ticket002", "closed")
#display_tickets(service_tickets, "all tickets")
#display_tickets(service_tickets, "closed tickets")

while True:
    main_menu_input = input("1.) Open New Ticket \n2.) Update Ticket Status \n3.) Display Tickets \n4.) Quit \nChoose Option (1-4): ")
    if main_menu_input == "1":
        ticket_id_input = input("Enter ticket ID: ")
        customer_name_input = input("Enter customer name: ")
        issue_input = input("Enter issue: ")
        open_ticket(service_tickets, ticket_id_input, customer_name_input, issue_input)
        continue
    elif main_menu_input == "2":
        id_update_input = input("Enter ticket ID: ")
        status_update_input = input("Enter new status (open or closed): ")
        update_status(service_tickets, id_update_input, status_update_input)
        continue
    elif main_menu_input == "3":
        status_filter_input = input("Which types of tickets would you like to display (all tickets, open tickets, closed tickets): ")
        display_tickets(service_tickets, status_filter_input)
        continue
    elif main_menu_input == "4":
        print("Thank you for using our app.")
        break
    else:
        print("Please enter a valid digit 1-4 to navigate menu")
        continue

'''
I built a simple while loop that allows a user to access through terminal inputs all three functions I wrote and takes further inputs to give those functions its needed arguments
The 4th oprtion in the menu breaks the loop and quits the application and the else statement catches any invalid input.
'''