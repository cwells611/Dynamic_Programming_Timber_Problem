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
input_file = open("test.txt")

#lines from input file
num_logs = int(input_file.readline())
log_lengths = input_file.readline().split()

#poulate array with log lengths
log = []
for i in range(num_logs):
    length = int(log_lengths[i])
    log.append(length)

#recursive algorithm
#parameters: bottom-most segment of log, top-most segment of log
#and list that including the lengths of each segment of the log
def T(i,j,log):
    #base cases 
    if j == i:
        return log[j]
    if j == (i+1):
        return max(log[i], log[j])
    #recursive call 
    condition1 = log[i] + min(T(i+2,j,log), T(i+1,j-1,log))
    condition2 = log[j] + min(T(i+1,j-1,log), T(i,j-2,log))
    return max(condition1, condition2)
  

#print function result
print(T(0,num_logs-1,log))

end = time.time()
print(end-start)