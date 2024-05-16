#bikes = ['trek', 'redline', 'giant']
#bikes = []
#bikes.append('trek')
#bikes.append('redline')
#bikes.append('giant')
#for bike in bikes:
# print(bike)
squares = []
for x in range(1, 11):
 squares.append(x**2) 
 print (x)
 squares = [x**2 for x in range(1, 11)]
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]
print(first_two)
alien = {'color': 'green', 'points': 5}
print(f"The alien's color is {alien['color']}")
alien['x_position'] = 0
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
 print(f"{name} loves {number}")
for name in fav_numbers.keys():
 print(f"{name} loves a number")
