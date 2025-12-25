class ClinicAppointment:
    def __init__(self):
        # Fixed time slots
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.appointments = []

    # ---------- Helper methods ----------
    def _find_appointment_by_mobile(self, mobile):
        for appt in self.appointments:
            if appt["mobile"] == mobile:
                return appt
        return None

    def _is_slot_available(self, doctor, slot):
        count = 0
        for appt in self.appointments:
            if appt["doctor"].lower() == doctor.lower() and appt["slot"] == slot:
                count += 1
        return count < 3  # <-- return after loop, not inside it

    def _show_time_slots(self):
        print("\nAvailable time slots:")
        for idx, tslot in enumerate(self.time_slots, start=1):
            print(f"{idx}. {tslot}")

    # ---------- Core functionalities ----------
    def book_appointment(self):
        print("\n--- Book Appointment ---")
        name = input("Enter patient name: ")
        age = input("Enter patient age: ")
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor name: ")

        if self._find_appointment_by_mobile(mobile):
            print("You already have an appointment booked with this mobile number.")
            return

        self._show_time_slots()
        try:
            choice = int(input("Choose a time slot (1-5): "))
            if choice < 1 or choice > len(self.time_slots):
                print("Invalid time slot choice.")
                return
        except ValueError:
            print("Please enter a valid number for time slot.")
            return

        selected_slot = self.time_slots[choice - 1]

        if not self._is_slot_available(doctor, selected_slot):
            print(f"Sorry, {doctor} is fully booked at {selected_slot}. Try another time slot or doctor.")
            return

        appointment = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "doctor": doctor,
            "slot": selected_slot,
        }
        self.appointments.append(appointment)
        print("\nAppointment booked successfully!")
        print(f"Patient: {name}")
        print(f"Doctor: {doctor}")
        print(f"Time Slot: {selected_slot}")
        print(f"Mobile: {mobile}")

    def view_appointment(self, mobile):
        print("\n--- View Appointment ---")
        appt = self._find_appointment_by_mobile(mobile)
        if not appt:
            print("No appointment found for this mobile number.")
            return

        print("Appointment Details:")
        print(f"Patient Name : {appt['name']}")
        print(f"Age          : {appt['age']}")
        print(f"Mobile       : {appt['mobile']}")
        print(f"Doctor       : {appt['doctor']}")
        print(f"Time Slot    : {appt['slot']}")

    def cancel_appointment(self, mobile):
        print("\n--- Cancel Appointment ---")
        for appt in self.appointments:
            if appt["mobile"] == mobile:
                print("Cancelling this appointment:")
                print(f"Patient: {appt['name']} | Doctor: {appt['doctor']} | Slot: {appt['slot']}")
                confirm = input("Are you sure you want to cancel? (y/n): ").lower()
                if confirm == "y":
                    self.appointments.remove(appt)
                    print("Appointment cancelled successfully.")
                else:
                    print("Cancellation aborted.")
                return
        print("No appointment found with this mobile number.")

    # ---------- Optional: Menu ----------
    def run(self):
        while True:
            print("\n===== Clinic Appointment System =====")
            print("1. Book Appointment")
            print("2. View Appointment")
            print("3. Cancel Appointment")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                mobile = input("Enter mobile number to view appointment: ")
                self.view_appointment(mobile)
            elif choice == "3":
                mobile = input("Enter mobile number to cancel appointment: ")
                self.cancel_appointment(mobile)
            elif choice == "4":
                print("Exiting Clinic Appointment System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


clinic = ClinicAppointment()
clinic.run()
