import Pyro4

@Pyro4.expose
class TicketBooking:
    def book_ticket(self, concert):
        # Implement your ticket booking logic here
        # You can add code to process the concert ticket, handle availability, etc.
        # Return the result of the booking process, e.g., a booking confirmation or status

        return "Ticket booked successfully for concert: {}".format(concert)

# Start the Pyro4 Daemon
daemon = Pyro4.Daemon()

# Register the TicketBooking class as a Pyro4 object
ticket_booking = TicketBooking()
uri = daemon.register(ticket_booking)

# Print the URI for clients to use
print("URI:", uri)

# Start the event loop for the server
daemon.requestLoop()
