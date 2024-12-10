# Question 1
aoc1 = open("H:\\manims\\aoc1.txt", "r") # Must open directory directly from files "use \\ to specify subfolders"
list1 = [] # from list 1
list2 = [] # from list 2

# for loop for each line of aoc1
for line in aoc1: 
    entry = line.split() # split values as array (vals[0] is num in first list, vals[1] is num in 2nd list)

    list1.append(int(entry[0])) # add all first entries into first list
    list2.append(int(entry[1])) # add all second entries into 2nd list

# sort lists
list1.sort()
list2.sort()

# calculate distance
dist = 0
for i in range(0, len(list1)): # loop through lists
    diff = abs(list1[i] - list2[i]) # take positive difference between lists
    dist += diff # add to sum --> total distance

print(dist)