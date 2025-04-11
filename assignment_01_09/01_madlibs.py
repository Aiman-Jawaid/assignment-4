
print("Let's play Mad Libs!")
print("Please provide the following words:\n")


adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb (past tense): ")
place = input("Place: ")
food = input("Food: ")


mad_lib = f"""
Today I went to the zoo. I saw a(n) {adjective} {animal} jumping up and down in its tree.
It {verb} through the large tunnel that led to its {place}.
I got hungry and bought some {food} to eat.
It was a wild day!
"""


print("\nHere's your Mad Lib story:")
print(mad_lib)
