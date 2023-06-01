# I produced this work from the knowledge I have acquired from this bootcamp
# Ask user to choose destination
# only 3 destinations are offered and so it is mandatory to select one
# user can only proceed when one of the above has been entered
while True:
    try:
        city_flight = str(input('''what is your destination? PLease choose one of the following:
                    1. London
                    2. Birmingham
                    3. Manchester\n
                    \t'''))
        if city_flight == 'London' or city_flight == 'Birmingham' or city_flight == 'Manchester':
            print(
                f'Thank you dear traveller!, your holiday destination is {city_flight}\n')
            break
    except ValueError:
        print('Sorry you have typed the wrong destination\n')

# secondly, number of nights spent at a hotel of choice
# This will ensure the user enters a number before proceeding
while True:
    try:
        num_nights = int(
            input('How many nights are you spending at the hotel?: '))
        if num_nights == int(num_nights):
            print(
                f'Thank you valued customer, you have decided to spend {num_nights} nights\n')
            break
    except ValueError:
        print('Sorry, you have not entered a number\n')

# Duration of car rent
while True:
    try:
        rental_days = int(input('how many days would you rent a car?: '))
        if rental_days == int(rental_days):
            print(
                f'Thank you valued customer, you are renting a car for {rental_days} days\n')
            break
    except ValueError:
        print('Sorry, you have not entered a number\n')

# now unto a pack of functions
# the hotel cost calculation


def hotel_cost(nights_spent):
    # hotel charge
    cost_per_night = 76
    total_cost = cost_per_night * nights_spent
    return total_cost


# Display the hotel cost
print(f'Thanks you, your hotel charge is £{hotel_cost(num_nights)}\n')

# calculating the plane cost


def plane_cost(destination):
    plane_ticket = None
    # charge is based on holiday destination selected
    if destination == 'London':
        plane_ticket = 100
    elif destination == 'Birmingham':
        plane_ticket = 80
    else:
        if destination == 'Manchester':
            plane_ticket = 70

    return plane_ticket


# Display fare
print(f'Great!, Your plane ticket will cost you £{plane_cost(city_flight)}.\n')


# calculating the rental cost
def car_rental(days_of_rent):
    daily_charge = 30
    total_cost = daily_charge * days_of_rent
    return total_cost


# display rental cost here
print(
    f'Congratulations!, You have rented a car for £{car_rental(rental_days)}\n')


# holiday calculation
# Sum of all expenses
def holiday_cost(nights, place, rental_duration):
    overall_cost_of_holiday = hotel_cost(
        nights) + plane_cost(place) + car_rental(rental_duration)
    return overall_cost_of_holiday


# overall cost of holiday
print(
    f'Best Wishes, The total cost of your holiday is £{holiday_cost(num_nights, city_flight, rental_days)},')
