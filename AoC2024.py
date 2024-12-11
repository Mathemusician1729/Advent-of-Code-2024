# file read line for all problems:
# aoc1 = open("H:\\Pytons\\Advent-of-Code-2024\\[FILENAME].txt", "r")

# Question 2
aoc1 = open("H:\\Pytons\\Advent-of-Code-2024\\input.txt", "r") # file reading
safe_reports = 0 # tracks # of safe reports

for line in aoc1: # loop through each possible report
    report = line.split() # turn into array 
    report = [int(x) for x in report] # list comprehension (turns all vals into integer)
    if all(report[i] < report[i+1] for i in range(len(report)-1)) or all(report[i] > report[i+1] for i in range(len(report)-1)): # check if all increasing/decreasing
        valid_diff = True # flag that checks if the difference is between 1 and 3
        for i in range(0, len(report)-1): # check if difference between values is between 1 and 3 
            diff = abs(report[i+1] - report[i]) # take difference
            if diff < 1 or diff > 3: # if not valid, set flag to false and end loop for that report
                valid_diff = False
                break
        
        if valid_diff == True: # only add if no invalid differences
            safe_reports+=1
        
print(safe_reports)