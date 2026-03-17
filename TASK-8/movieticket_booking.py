user_age=int(input("enter the age:"))
seat_availability=10

if user_age>=18:
    user_seat=int(input("enter the seats:"))

    if user_seat<=seat_availability:
        print("Ticket booked")

    else:
        print("House full")

else:
    print("not eligible to watch the movie")            

