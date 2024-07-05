import array
# Input the number of days
numDays = int(input("How many days' temperature? "))
# Initialize the total sum of temperatures
total = 0
# Create an array to store the temperatures
temp = array.array('i')
# Input temperatures for each day
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) + "'s high temp: "))
    temp.append(nextDay)
    total += temp[i]
    
# Calculate the average temperature
avg = round(total / numDays, 2)
print("\nAverage = " + str(avg))

# Count the number of days with temperatures above the average
above = 0
for t in temp:
    if t > avg:
        above += 1

print(str(above) + " day(s) above average")
