import math
#from pprint import pprint

seats = [
    [{"available": True, "name": None, "fare": 0} for _ in range(8)], # First Class
    [{"available": True, "name": None, "fare": 0} for _ in range(40)] # Coach Class
]

def accept_input(msg: str, data_type: str, min_value=0, max_value=0):
    while True:
        try:
            choice_str = input(msg)
            if data_type == "int":
                choice = int(choice_str)
                if choice not in range(min_value, max_value):
                    print(f"You put in an invalid value, expecting a(n) {data_type} between {min_value} and {max_value - 1}.  You entered: {choice_str}")
                    continue
            elif data_type == "float":
                choice = float(choice_str)
                if choice < float(min_value) or choice > float(max_value):
                    print(f"You put in an invalid value, expecting a(n) {data_type} between {min_value} and {max_value - 1}.  You entered: {choice_str}")
                    continue
            else:
                choice = choice_str
            break
        except:
            print(f"You put in an invalid value, expecting a(n) {data_type}.  You entered: {choice_str}")

    return choice

def calculate_fare(base_price, age):
    if age <= 7 or age >= 65:
        price = round(base_price * (1 - .2), 2)
    else:
        price = base_price
    return price


def calculate_change(amount_paid, fare):
    change = amount_paid - fare
    denominations = {
        "$100 bills": 100, 
        "$20 bills": 20, 
        "$5 bills": 5,
        "$1 bills": 1, 
        "Quarters": 0.25, 
        "Dimes": 0.10,
        "Nickels": 0.05, 
        "Pennies": 0.01
    }

    change_breakdown = {}
    for name, value in denominations.items():
        count = math.floor(change // value)
        change -= count * value
        change_breakdown[name] = count
    return change_breakdown

def make_reservation(class_type, base_price):
    print_seats(class_type)
    if class_type == 0:
        print("First Class")
        seat_num = accept_input("Enter seat number: ", "int", 1, 9) - 1
    else:
        seat_num = accept_input("Enter seat number: ", "int", 1, 41) - 1
    if seats[class_type][seat_num]["available"]:
        name = accept_input("Enter passenger name: ", "str")
        age = accept_input("Enter passenger age: ", "int", 1, 134)
        fare = calculate_fare(base_price, age)
        print(f"Fare: ${fare:.2f}")
        amount_paid = accept_input("Enter amount paid: ", "float", 1, 1001)
        if amount_paid >= fare:
            change = calculate_change(amount_paid, fare)
            seats[class_type][seat_num] = {"available": False, "name": name, "fare": fare}
            print(f"Reservation successful! Change: ${amount_paid - fare:.2f}")
            print("Change breakdown:", change)
        else:
            print("Insufficient funds. Reservation canceled.")
    else:
        print("Seat not available.")


def change_reservation():
    class_type = accept_input("Enter 1 for First Class or 2 for Coach: ", "int", 1, 3) - 1
    print_seats(class_type)
    if class_type == "1":
        current_seat = accept_input("Enter current seat number: ", "int", 1, 9) - 1
        new_seat = accept_input("Enter new seat number: ", "int", 1, 9) - 1
    else:
        current_seat = accept_input("Enter current seat number: ", "int", 1, 41) - 1
        new_seat = accept_input("Enter new seat number: ", "int", 1, 41) - 1
    if seats[class_type][current_seat]["available"] == False:
        if seats[class_type][new_seat]["available"]:
            seats[class_type][new_seat] = seats[class_type][current_seat]
            seats[class_type][current_seat] = {"available": True, "name": None, "fare": 0}
            print("Reservation changed successfully.")
        else:
            print("New seat is not available.")
    else:
        print("Current seat is not booked.")


def print_seats(class_type):
    compartment = "First Class" if class_type == 0 else "Coach Class"
    print(f"\n{compartment} Seating:")
    for idx, seat in enumerate(seats[class_type]):
        status = "Available" if seat["available"] else f"Booked by {seat['name'][:12]}"
        print(f"Seat {idx + 1}: {status}")


def main():
    while True:
        print("\n1. New First Class Reservation")
        print("2. New Coach Class Reservation")
        print("3. Change Existing Reservation")
        print("4. Print Listing of Seats")
        print("5. Quit")
        choice = accept_input("Choose an option: ", "int", 1, 6)

        if choice == 1:
            make_reservation(0, 500)
        elif choice == 2:
            make_reservation(1, 199)
        elif choice == 3:
            change_reservation()
        elif choice == 4:
            for i in range(2):
                print_seats(i)
        elif choice == 5:
            print("Exiting program. Thank you!")
            exit()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
