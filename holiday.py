''' make a holiday calculator that will sum up 
cost of the plane(city_flight), 
hotel(num_nights),
and renting a car(rental_days). 
Ask user where are they flying to(each city different cost),
how many days they stay at the hotel,
and how many days they want to rent their car for. 
so 3 inputs - city_flight, num_nights, rental_days,

4 functions:
plane_cost - assign cost of the flight from the users choice
hotel_cost - make up price per night, and multiply by number of nights using num_nights input,
car_rental - make up price per day, multiply per number of days
holiday_cost - sum up hotel_cost, plane_cost, and car_rental to output final holiday cost,
 '''

print("You can fly to: \n (a) Warsaw (£156), \n (b) Amsterdam (£58), \n (c) Cape Town (£364),")
# user choosing flight
while True:
    city_flight = input("Where are you flying to? (please enter 'Warsaw', 'Amsterdam' or 'Cape Town'): ")
    city_flight = city_flight.lower() # lowering the variable to ensure different input can be accepted
    if city_flight == "warsaw": 
        print("You are going to Warsaw!\n") # prints the choice
        break # breaks the loop
    elif city_flight == "amsterdam":
        print("You are going to Amsterdam!\n")
        break
    elif city_flight == "cape town":
        print("You are going to Cape Town!\n") 
        break
    else:
        print("Wrong input!!!")
# Getting cost of the flight
def plane_cost(city_flight): # defining function plane_cost
    if city_flight == "warsaw":
        city_flight = 156
        return city_flight # returning cost of the flight
    elif city_flight == "amsterdam":
        return 58
    elif city_flight == "cape town":
        return 364
    else:
        return 0 # return like this will never happen, done for esthetics
cost = plane_cost(city_flight) # assigning function to variable "cost", so I can use it with ease
# Calculating cost of stay
num_nights = 0

while num_nights == 0:
    try:
        num_nights = int(input("How many nights are you staying?: "))
        print("Thank You!\n")
    except ValueError:
        print("Wrong input, please enter a number!\n")

per_night = 90

def hotel_cost(num_nights,per_night): # defining hotel_cost function to calculate the cost of the hotel
    total_stay_cost = num_nights * per_night
    return total_stay_cost
hcost = hotel_cost(num_nights,per_night)

# Calculating cost of the car

rental_days = 0

while rental_days == 0:
    try:
        rental_days = int(input("How many days are you renting a car for?: "))
        print("Thank You!\n")
    except ValueError:
        print("Wrong input, please enter a number!\n")

per_day = 69

def car_rental(rental_days,per_day): # this function calculates car rental costs
    rental_cost = rental_days * per_day
    return rental_cost
rcost = car_rental(rental_days,per_day)


# Calculating the cost of the holiday

def holiday_cost(plane_cost,hotel_cost,car_rental):
    final_cost = plane_cost + hotel_cost + car_rental
    return final_cost
xfinal_cost = holiday_cost(cost,hcost,rcost)
city_flight = city_flight.capitalize() # capitalising for esthetics

# final output of the costs
print(f"Your trip to {city_flight} will cost you £{cost}")
print(f"You want to stay {num_nights} days in {city_flight}, this is £{per_night} per night, in total it will cost you £{hcost}")
print(f"You are renting a car for {rental_days} days, this will sum up to £{rcost}")
print(f"Your trip in total will cost you £{xfinal_cost}, good luck!")