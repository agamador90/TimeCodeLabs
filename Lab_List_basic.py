#Instructions
#In this lab, you complete a partially pre-written Python program that uses a list.
 #The program prompts the user to interactively enter eight batting averages, which the program stores in a list.
 #It should then find the minimum and maximum batting averages stored in the list, as well as the average of
 #the eight batting averages. The data file provided for this lab includes the input statement and some variable 
 #initializations. Comments are included in the file to help you write the remainder of the program.





# Initialize an integer for list size here.
size = 0
# Initialize list here.
averages = list()
# Write a loop to get batting averages from user and add to list.
while size < 8:
    
    # String version of batting average input by user.

 averageString = input("Enter a batting average: ")

    # Use this variable to store the batting average input by user.

 battingAverage = float(averageString)

    # add value to list.
 averages.append(battingAverage)
 size += 1
# Use these variables to store the minimum and maximum batting averages.

# Assign the first element in the list to be the minimum and the maximum.

min = averages[0]

max = averages[0]

# Start out your total initialized to 0.
total = 0
sum_ave = 0
# Write a loop here to access list values starting with averages[1]
for i in range(len(averages)): #I also tried starting at index in [1] like this: for i in range(1,len(averages)):
     # Within the loop test for minimum and maximum batting averages.
 if averages[i] > max:
  max = averages[i]
 if averages[i]< min:
  min = averages[i] 
    # Also accumulate a total of all batting averages.
 total += 1
 sum_ave += averages[i]  
# Calculate the average of the 8 averages.
suma = float()
suma = sum_ave/total

# Print the averages stored in the averages list.
for f in range(len(averages)):
 print(f"averages[{f}] is:{averages[f]}")


# Print the maximum batting average, minimum batting average, and average batting average.
print(f"Maximun batting average is {max}")
print(f"Minimum batting average is {min}")
print(f"Average batting average is {suma:.4f}")



#An example of the program is shown below:

#Enter a batting average: .299
#Enter a batting average: .157
#Enter a batting average: .242
#Enter a batting average: .203
#Enter a batting average: .198
#Enter a batting average: .333
#Enter a batting average: .270
#Enter a batting average: .190
#averages[0] is: 0.299
#averages[1] is: 0.157
#averages[2] is: 0.242
#averages[3] is: 0.203
#averages[4] is: 0.198
#averages[5] is: 0.333
#averages[6] is: 0.27
#averages[7] is: 0.19
#Minimum batting average is 0.157
#Maximum batting average is 0.333
#Average batting average is 0.2365