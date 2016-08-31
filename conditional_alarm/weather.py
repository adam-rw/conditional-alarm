import sys
import os

class Weather:

    def __init__(self):
        self.get_user_location()

    def closest_station(self):
        pass

    def get_user_location(self):
        with open('location.txt', 'r+') as location_file:
            location_string = location_file.read()

        if location_string:
            self.location = location_string
        else:
            self.location = str(input("What is your current location? "))
            if len(self.location) == 0:
                self.get_user_location()
            with open('location.txt', 'r+') as location_file:
                location_file.write(self.location)

    def get_location_weather(self, for_when):
        pass