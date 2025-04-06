
earth_weight = float(input("Enter a weight on Earth: "))


planet = input("Enter a planet: ")


if planet == "Mercury":
    factor = 0.376
elif planet == "Venus":
    factor = 0.889
elif planet == "Mars":
    factor = 0.378
elif planet == "Jupiter":
    factor = 2.36
elif planet == "Saturn":
    factor = 1.081
elif planet == "Uranus":
    factor = 0.815
elif planet == "Neptune":
    factor = 1.14


planet_weight = round(earth_weight * factor, 2)


print(f"The equivalent weight on {planet}: {planet_weight}")
