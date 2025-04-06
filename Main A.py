#this class contains all the functions of the system
class FlightSeatManager:
    def __init__(self):
        self.sitting_plan = [] #list to initialize seats
        self.seat_states = [] #list for seat status
        seat_rows = ["A", "B", "C", "X", "D", "E", "F"] #6 compartments of seats
        for letter in seat_rows:
            for number in range(1, 81): # each section has 80 seats
                self.sitting_plan.append(f"{number}{letter}")
                self.seat_states.append("F") #initially all seats are free thus marked F

        # initializing aisle parts
        for aisle_index in range(240, 320):
            self.sitting_plan[aisle_index] = "X"
            self.seat_states[aisle_index] = "N" #status , Not available (only for backend)

        #initializing storage seats
        for store_index in [396, 397, 476, 477, 556, 557]:
            self.sitting_plan[store_index] = "S"
            self.seat_states[store_index] = "N"

    #this function provides the functionality no.4 Show Booking Status
    def display_seating_chart(self):
        for idx in range(len(self.sitting_plan)):
            label = self.sitting_plan[idx]
            state = self.seat_states[idx]
            if label in ["X","S"]:
                print(f"   {label}   ",end="  ") #no need to print status of aisle and storage seats

            else:
                print(f"[{label}/{state}]", end="  ")
            if (idx + 1) % 80 == 0:
                print()


    #this function provides the functionality no.1  Check availability of Seat
    def show_available_seats(self):
        for idx in range(len(self.sitting_plan)):
            label = self.sitting_plan[idx]
            state = self.seat_states[idx]
            if label in ["X", "S"]: # printing empty space for aisle and storage area
                print("     ", end="  ")
            elif state == "F":
                print(f"[{label}]", end="  ")
            else:
                temp = len(f"[{label}]")
                print(" " * temp, end="  ") #if the seat is reserved an empty space is printed
            if (idx + 1) % 80 == 0:
                print()
                if (idx + 1) in [240, 320]:
                    print()


    #this function provides the functionality no. 2 Books a seat
    def reserve_seats(self):
        self.show_available_seats()

        seat_input = input("Enter seat number: ")
        if seat_input not in self.sitting_plan:
            print("Invalid seat number. Try again.")
            return

        idx = self.sitting_plan.index(seat_input)

        if self.sitting_plan[idx] in ["X", "S"]: # check for aisle and storage area
            print(f"Seat {seat_input} cannot be booked.")
            return
        elif self.seat_states[idx] == "R": # check for already reserved seat
            print(f"Seat {seat_input} is already reserved.")
            return

        self.seat_states[idx] = "R" #if booking is successful, changing the status of seat
        print(f"Seat {seat_input} booked successfully!")


    #this function will provide the functionality no. 3
    def release_seat(self):
        seat_input = input("Enter seat number to free: ").strip()

        if seat_input not in self.sitting_plan:
            print("Invalid seat number.")
            return

        idx = self.sitting_plan.index(seat_input)

        if self.seat_states[idx] == "R":
            self.seat_states[idx] = "F" #changing the status of the seat
            print(f"Seat {seat_input} is now available.")
        else:
            print(f"Seat {seat_input} is not currently reserved.")

    #this is additional feature I implemented, most real.world airline booking systems have this feature
    #that they display the summary of sitting plan, this function displays the summary of booked, availed and unavailable seats
    def display_summary(self):
        total = len(self.sitting_plan)
        booked = self.seat_states.count("R")
        free = self.seat_states.count("F")
        blocked = self.seat_states.count("N")

        print("--- Seat Summary Report ---")
        print(f"Total Seats:       {total}")
        print(f"Booked Seats:      {booked}")
        print(f"Available Seats:   {free}")
        print(f"Non-bookable Seats:{blocked}")
        print("---------------------------")
    # this function will run the program
    def run(self):
        print("\n!!==!!-- WELCOME TO BURAK757 --!!==!!")
        while True:
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking status")
            print("5. Display seat summary")
            print("6. Exit program")
            selection = input("Enter your choice (1-5): ").strip()
            print()
            if selection == "1":
                self.show_available_seats()
            elif selection == "2":
                self.reserve_seats()
            elif selection == "3":
                self.release_seat()
            elif selection == "4":
                self.display_seating_chart()
            elif selection == "5":
                self.display_summary()
            elif selection == "6":
                print("Thanks for using our booking system.")
                break
            else:
                print("Invalid input. Choose a number between 1 and 5.")
            print()

if __name__ == "__main__":
    flight_system = FlightSeatManager()
    flight_system.run()
