# file read line for all problems:
# aoc[problem #] = open("H:\\Pytons\\Advent-of-Code-2024\\[FILENAME].txt", "r")

# Question 2
aoc2 = open("H:\\Pytons\\Advent-of-Code-2024\\input.txt", "r") # file reading
safe_reports = 0 # tracks # of safe reports

for line in aoc2: # loop through each possible report
    report = line.split() # turn into array 
    report = [int(x) for x in report] # make all elements integers instead of string
    for i in range(0, len(report)): # loop through each element in report, remove one to test 'problem dampener'
        tolerate = report.copy() # copy of report that will remove element
        tolerate.pop(i) # remove element (problem dampener)

        # same idea as with first part but with adjusted report list
        if all(tolerate[i] < tolerate[i+1] for i in range(len(tolerate)-1)) or all(tolerate[i] > tolerate[i+1] for i in range(len(tolerate)-1)): # check if all increasing/decreasing
            valid_diff = True # flag that checks if the difference is between 1 and 3
            for j in range(0, len(tolerate)-1): 
                diff = abs(tolerate[j+1] - tolerate[j]) # take difference
                if diff < 1 or diff > 3: # if not valid, set flag to false and end loop for that report
                    valid_diff = False
                    break 
            
            if valid_diff == True: # only add if no invalid differences and end outer loop so it does not continue to check possible safe lists
                safe_reports+=1
                break
        
print(safe_reports)