def ptl(): #print list function
    return ", ".join((str(i) for i in l))

l = [5, 4, 3, 2, 1] #the list to be sorted

print("original list:              " + ptl()) #for comparison, the unsorted
                                              #list is printed first
print("\nbubble sort:") #loop which actually runs the sort algorthim
for itr in range(ln :=  len(l) - 1):
    for itr2 in range(ln):
        if (l[itr2] > l[itr2 + 1]):
            l[itr2], l[itr2 + 1] = l[itr2 + 1], l[itr2]
    print(f"iteration {itr + 1} of bubble sort: " + ptl()) #displays what
    #the list looks like in its current state, at some time during the alg

print("\nbubble sorted list:         " + ptl()) #displays the sorted list
