print("SMART SCHOOL DAY PLANNER")
day=input("tell the day today.(mon-sun):")
weather=input("weather today?(sunny/rainy/cloudy)")
homework=input("hw done?(yes/no)")
print()
print("-" *20)

#topic 1
if day in ("saturday","sunday"):
    print("enjoy your free time!!!")
elif day=="monday":
    print("first school day of the week.")
elif day=="friday": 
    print('last school day!')
elif day in ("tuesday","wednesday","thursday"):
    print("regular school day.")        
else:
    print("day not recognised")

#topic 2
if weather == "sunny" and homework == "yes":
    print("go to the park-great weather and hw is done")

#topic 3
if weather=="rainy" or "cloudy":
    print("take an umbrella with you")

#topic 4
if not homework=="yes":
    print("finish hw before going out")

#topic 5
if weather=="rainy" and not homework=="yes":
    print("stay at home and finish hw.")
elif weather=="sunny" and homework=="yes" and day=="monday":
    print("have a great school day.")
else:
    print("take one step at a time")

print()
print("**HAVE A WONDERFUL DAY!**")