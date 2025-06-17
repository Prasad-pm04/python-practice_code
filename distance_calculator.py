# Calculate the distance between the pick-up location and the drop location

import geopy.distance
import math

class Maps:

    def __init__(self):
        pass

    def get_distance(self, location_1, location_2):

        try:
            distance = geopy.distance.distance(location_1, location_2).km
        except:
            distance = math.sqrt((location_1[0]-location_2[0])^2 + (location_1[1]-location_2[1])^2)

        return distance



class SurgePricing:

    def __init__(self):
        pass

    def get_price_per_km(self, hour):

        try:

            if (hour > 8) & (hour < 11):
                price_per_km = 20
            elif (hour > 18) & (hour < 21):
                price_per_km = 15
            else:
                price_per_km = 10

        except:

            price_per_km = 10

        return price_per_km


def get_final_price(location_1, location_2, booking_hour):

    maps = Maps()
    surge = SurgePricing()

    total_distance = maps.get_distance(location_1, location_2)
    actual_price_per_km = surge.get_price_per_km(booking_hour)

    final_price = round(total_distance * actual_price_per_km, 2)

    return final_price
