import Pyro4

# Obtain the URI of the server
uri = input("Enter the URI of the ticket server: ")

# Connect to the ticket server
ticket_booking = Pyro4.Proxy(uri)

# Book a ticket
concert = input("Enter the concert name: ")
result = ticket_booking.book_ticket(concert)

# Print the booking result
print(result)
