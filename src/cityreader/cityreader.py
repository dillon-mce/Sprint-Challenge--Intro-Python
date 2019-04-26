# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.
class City:
  def __init__(self, name, latitude, longitude):
    self.name = name
    self.lat = latitude
    self.lon = longitude

  def __str__(self):
    return f'City(name: {self.name}, lat: {self.lat}, lon: {self.lon})'

  def falls_within(self, square):
    point = Point(self.lon, self.lat)
    return square.contains(point)

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

import csv
def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  cities = []
  with open('cities.csv') as cities_file:
    reader = csv.DictReader(cities_file)
    for row in reader:
      name = row['city']
      lat = float(row['lat'])
      lon = float(row['lng'])
      city = City(name, lat, lon)
      cities.append(city)
    
  return cities

cities = cityreader()
# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
print("\n\n")
lat1 = float(input("First Latitude: "))
lon1 = float(input("First Longitude: "))
lat2 = float(input("Secong Latitude: "))
lon2 = float(input("Secong Longitude: "))

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Square:
  def __init__(self, point1, point2):
    self.point1 = Point(min(point1.x, point2.x), max(point1.y, point2.y))
    self.point2 = Point(max(point1.x, point2.x), min(point1.y, point2.y))

  def contains(self, point):
    return point.x > self.point1.x and point.x < self.point2.x and point.y < self.point1.y and point.y > self.point2.y

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  square = Square(Point(lon1, lat1), Point(lon2, lat2))
  within = [city for city in cities if city.falls_within(square)]

  return within

result = cityreader_stretch(lat1, lon1, lat2, lon2, cities)
print("\nResults:\n")
for city in result:
  print(city)