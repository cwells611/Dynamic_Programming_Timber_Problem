#Given Recurrence Relation
#T(i,j) = max(l_i + min[T(i+2,j), T(i+1, j-1)], l_j + min[T(i+1,j-1), T(i,j-2)])
#Base Cases:
    #T(i,j) = l_i -> j = i
    #T(i,j) = max(l_i,l_j) -> j = i+1

#imports 
import sys
import time

start = time.time()
#read in input file 
input_file = open('test.txt')

#lines from input file
num_logs = int(input_file.readline())
log_lengths = input_file.readline().split()

#poulate array with log lengths
log = []
for i in range(num_logs):
    length = int(log_lengths[i])
    log.append(length)

#bottom-up DP implementation
def T(i,j,log):
    #DP table will be 2-dimensional with dimensions nxn, initialized with 0s 
    rows = num_logs
    cols = num_logs
    dp_table = [[0 for i in range(num_logs)] for j in range(num_logs)]
    #fill in table 
    for diagonal in range(rows):
        for i in range(cols - diagonal):
            j = i + diagonal
            #base cases
            if i == j:
                dp_table[i][j] = log[i]
            if j == (i+1):
                dp_table[i][j] = max(log[i],log[j])
            #general case 
            if dp_table[i][j] == 0:
                condition1 = log[i] + min(dp_table[i+2][j], dp_table[i+1][j-1])
                condition2 = log[j] + min(dp_table[i+1][j-1], dp_table[i][j-2])
                dp_table[i][j] = max(condition1, condition2)
    for row in dp_table:
        for element in row:
            print(element, end=' ')
        print()
    print()
    print(log[10]+dp_table[4][9])
    print(log[10]+dp_table[3][8])
            

#print function result
T(0,num_logs,log)