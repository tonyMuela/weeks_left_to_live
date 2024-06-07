age = input("How old are you? ")
die = input("How old do you think you'll live to be? ")

years = int(die) - int(age)
weeks = years * 52
days = weeks * 7

print(f"If you live to be 90 you have about {weeks} weeks left.")
print(f"That's about {days} more days.")
