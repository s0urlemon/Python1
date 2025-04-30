def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(place):
    if "mumbai"==place:
        return 183
    elif "delhi"==place:
        return 220
    elif "chennai"==place:
        return 222
    elif "bangalore"==place:
        return 475
    
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
    
def trip_cost(place,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(place)+spending_money

print("Cost of car rental:",rental_car_cost(5))
print("Cost of plane ride:",plane_ride_cost("mumbai"))
print("Cost of hotel room:",hotel_cost(7))
print("Total cost of trip",trip_cost("mumbai",7,550))
print(trip_cost("delhi",6,550))