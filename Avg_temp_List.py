#Calculate Average Temperature
numDays = int(input("How many day's temperature? "))
total = 0 #use this variable to store sum of temperature
temp=[] #0 1 this is list
for i in range(numDays):
    nextDay = int(input("Day " +str(i+1)+"'s high temp: "))
    temp.append(nextDay) #0 index has 1st day temp or 1 has 2nd day temp etc.
    total += temp[i] # 0+43 = 43, 43+45= 88

avg= round(total/numDays,2) # 88/2 = 44
print("\nAverage = "+str(avg))
above= 0
for i in temp: # 43
    if i > avg: # 43> 44
        above += 1
        print(above)

print(str(above) + " day(s) above average")