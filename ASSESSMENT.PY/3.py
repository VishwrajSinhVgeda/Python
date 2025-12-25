class BusTicketingSystem:
    def __init__(self):
        self.bus_routes = {
            1: "Ahmedabad to Mumbai : 500",
            2: "Ahmedabd to Delhi : 1200",
            3: "Ahmedabd to Bangalore : 1500",
            4: "Ahmedabd to Chennai : 1400"
        }
        # Store bookings as a dict: {passenger_id: booking_data}
        self.bookings = {}
        self.next_passenger_id = 1
        self.next_seat_number = 1

    def show_routes(self):
        print("\n--- Available Bus Routes ---")
        for key, value in self.bus_routes.items():
            print(f"{key}. {value}")

    def seat_number(self):
        seat_number_id = self.next_seat_number
        if seat_number_id <= 40:
            self.next_seat_number += 1
            return seat_number_id
        else:
            return None  # No seats left

    def _generate_passenger_id(self):
        passenger_id = self.next_passenger_id
        self.next_passenger_id += 1
        return passenger_id

    def booking(self):
        print("\n=== Book Ticket ===")
        print("Enter the details below: ")

        # Get passenger details
        name = input("Enter your name: ").strip()

        try:
            age = int(input("Enter your age: ").strip())
        except ValueError:
            print("Invalid age. Please enter a number.")
            return

        if age <= 0:
            print("Age must be a positive number.")
            return

        mobile = input("Enter your mobile number (10 digits): ").strip()
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Invalid mobile number. It must be 10 digits.")
            return

        # Assign seat
        seat = self.seat_number()
        if seat is None:
            print("Sorry, no seats available.")
            return

        # Show routes using a list so we can index by choice - 1
        routes_list = list(self.bus_routes.values())

        print("\nAvailable bus routes:")
        for idx, route in enumerate(routes_list, start=1):
            print(f"{idx}. {route}")

        print("Choose the bus route from the above.")
        try:
            choice = int(input(f"Enter your choice (1 - {len(routes_list)}): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if choice < 1 or choice > len(routes_list):
            print("Invalid number. Please enter a valid number.")
            return

        selected_route = routes_list[choice - 1]

        # Generate passenger ID and save booking
        passenger_id = self._generate_passenger_id()

        self.bookings[passenger_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": selected_route,
            "seat": seat
        }

        print("\nTicket booked successfully!")
        print(f"Passenger ID : {passenger_id}")
        print(f"Name         : {name}")
        print(f"Age          : {age}")
        print(f"Mobile       : {mobile}")
        print(f"Route        : {selected_route}")
        print(f"Seat Number  : {seat}")

    def view_booking(self):
        print("\n--- View Passenger Details ---")
        try:
            passenger_id = int(input("Enter Passenger ID: ").strip())
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        passenger = self.bookings.get(passenger_id)
        if not passenger:
            print("No Passenger found with this ID.")
            return

        print(f"\nDetails for Passenger ID {passenger_id}:")
        print(f"Name          : {passenger['name']}")
        print(f"Age           : {passenger['age']}")
        print(f"Route         : {passenger['route']}")
        print(f"Mobile Number : {passenger['mobile']}")
        print(f"Seat Number   : {passenger['seat']}")

    def cancel_booking(self, mobile):
        print("\n--- Cancel Booking ---")

        # Find booking by mobile
        found_id = None
        for pid, data in self.bookings.items():
            if data["mobile"] == mobile:
                found_id = pid
                print("Cancelling this ticket:")
                print(f"Passenger: {data['name']} | Mobile: {data['mobile']} | Route: {data['route']} | Seat: {data['seat']}")
                confirm = input("Are you sure you want to cancel? (y/n): ").lower()
                if confirm == "y":
                    del self.bookings[pid]
                    print("Booking cancelled successfully.")
                else:
                    print("Cancellation aborted.")
                return  # Stop after handling this booking

        print("No booking found with this mobile number.")

    def run(self):
        """Simple menu loop to interact with the bus ticketing system."""
        while True:
            print("\n===== Bus Ticketing System =====")
            print("1. Book Ticket")
            print("2. View Ticket")
            print("3. Cancel Ticket")
            print("4. Show Routes")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.booking()
            elif choice == "2":
                self.view_booking()
            elif choice == "3":
                mobile = input("Enter mobile number to cancel ticket: ").strip()
                self.cancel_booking(mobile)
            elif choice == "4":
                self.show_routes()
            elif choice == "5":
                print("Exiting Bus Ticketing System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


busbooking = BusTicketingSystem()
busbooking.run()