if __name__ == "__main__":
  # How to Find the Index of an Element in a List

  cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]
  print(cities)
  print(cities.index("Mumbai"))

  # cities.index('Osaka')
  # ValueError

  cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]
  city = "Osaka"

  if city in cities:
    index = cities.index(city)
    print(f"The {city} has an index of {index}.")
  else:
    print(f"The {city} doesn't exist in the list.")
