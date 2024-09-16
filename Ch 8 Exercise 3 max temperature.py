#Program name: Ch 8 Exercise 3 max temperature.py
#Finds the maximum average daily temperature in a week

days = ["Sunday","Monday","Tuesday","Wednesday",\
        "Thursday","Friday","Saturday"]   # Creating a list called 'days' with the days of the week

def maxTemp(temps):
    maxTemp = temps[0] # List with one value '0'
    maxDay = 0 # maxday being assigned the value 0
    for day in range(7): # This for loop keeps going through each value in the list and if the value is bigger than the previous one it gets replaces the previosu value in the 'temps' list.
        if temps[day] > maxTemp: # Both maxDay and maxTemp have been assigned to 0 so whatever the first value entered by the user will straight away replace the '0's
            maxTemp = temps[day]
            maxDay = day
    return maxTemp, maxDay

#main program
temperatures = [None]*7 # This is creating a list with 7 null values, if i printed this out it would print [0,0,0,0,0,0,0]
                        # It means this list will have seven values and at the moment they are set to null or no value
                        
for day in range(7): # This for loop goes through the 'days' list and adds the inputted value to the temperatures list
    temperatures[day] = int(input("Enter temperature on "+days[day]+": ")) # temperature is an int value
# The plus before and after +days[day]+ concatonates the string, basically it adds it all together, it needs to be there or else you get a syntax error                       
            
maxTemp, day = maxTemp(temperatures) # calling on the function, 'maxTemp, day' will be assigned the return values
                                     # temperatures as the input to the function will be the list of inputted temperatures
print("\nMaximum temperature was " + str(maxTemp) + " on "+ days[day])

input("Press Enter to exit ")
