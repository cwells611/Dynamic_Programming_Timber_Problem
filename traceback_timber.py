#Given Recurrence Relation
#T(i,j) = max(l_i + min[T(i+2,j), T(i+1, j-1)], l_j + min[T(i+1,j-1), T(i,j-2)])
#Base Cases:
    #T(i,j) = l_i -> j = i
    #T(i,j) = max(l_i,l_j) -> j = i+1

#imports 
import sys

#read in input file 
input_file = open(sys.argv[1])

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
    logs = num_logs
    #DP table will be 2-dimensional with dimensions nxn, initialized with 0s 
    #parent pointer table will be same size as DP table, and initialized with 0s
    rows = logs
    cols = logs
    dp_table = [[0 for i in range(logs)] for j in range(logs)]
    parent_table = [[0 for i in range(logs)] for j in range(logs)]
    #fill in table 
    for diagonal in range(rows):
        for i in range(cols - diagonal):
            j = i + diagonal
            #base cases
            if i == j:
                dp_table[i][j] = log[i]
            if j == (i+1):
                dp_table[i][j] = max(log[i],log[j])
                if (dp_table[i][j] == log[i]) or (log[i] == log[j]):
                    my_choice = i
                    opponent_choice = j
                else:
                    my_choice = j
                    opponent_choice = i
                parent_table[i][j] = (my_choice, opponent_choice)
            #general case 
            if dp_table[i][j] == 0:
                condition1 = log[i] + min(dp_table[i+2][j], dp_table[i+1][j-1])
                condition2 = log[j] + min(dp_table[i+1][j-1], dp_table[i][j-2])
                dp_table[i][j] = max(condition1, condition2)
                if dp_table[i][j] == condition1:
                    my_choice = i 
                    if dp_table[i+2][j] == dp_table[i+1][j-1]:
                        opponent_choice = my_choice + 1
                    else:
                        if dp_table[i][j] == log[i] + dp_table[i+2][j]:
                            opponent_choice = my_choice + 1
                        else:
                            opponent_choice = j
                    parent_table[i][j] = (my_choice, opponent_choice)
                elif dp_table[i][j] == condition2:
                    my_choice = j
                    if dp_table[i+1][j-1] == dp_table[i][j-2]:
                        opponent_choice = i
                    else:
                        if dp_table[i][j] == log[j] + dp_table[i+1][j-1]:
                            opponent_choice = i
                        else:
                            opponent_choice = my_choice - 1
                    parent_table[i][j] = (my_choice, opponent_choice)
    
    #print out max length of wood 
    print(dp_table[0][logs-1])

    #account for case when n = 1
    if num_logs == 1:
        print(num_logs)
        return 
    
    #start traceback with values in top right corner of parent table
    my_choice = parent_table[0][logs-1][0]
    opponent_choice = parent_table[0][logs-1][1]
    traceback = [my_choice+1,opponent_choice+1]
    my_old_choice = my_choice
    opponent_old_choice = opponent_choice
    if opponent_old_choice == 0:
        first_segment = opponent_old_choice
    else:
        first_segment = -1
    while len(traceback) < num_logs:
        #account for case when n in odd 
        if (num_logs - len(traceback)) == 1:
            for i in range(1, num_logs+1):
                if i in traceback:
                    continue
                else:
                    traceback.append(i)
            break
        #I take first segment, opponent takes second segment 
        if opponent_old_choice == (my_old_choice + 1):
            my_choice = parent_table[opponent_old_choice+1][logs-1][0]
            opponent_choice = parent_table[opponent_old_choice+1][logs-1][1]
            traceback.append(my_choice+1)
            traceback.append(opponent_choice+1)
            first_segment = opponent_old_choice
        #I take first segment, opponent takes last segment 
        elif opponent_old_choice > my_old_choice:
            my_choice = parent_table[my_old_choice+1][opponent_old_choice-1][0]
            opponent_choice = parent_table[my_old_choice+1][opponent_old_choice-1][1]
            traceback.append(my_choice+1)
            traceback.append(opponent_choice+1)
            first_segment = my_old_choice
            logs = logs - 1
        #I take last segment, opponent takes second to last segment 
        elif opponent_old_choice == (my_old_choice - 1):
            my_choice = parent_table[first_segment+1][opponent_old_choice-1][0]
            opponent_choice = parent_table[first_segment+1][opponent_old_choice-1][1]
            traceback.append(my_choice+1)
            traceback.append(opponent_choice+1)
            logs = logs - 2
        #I take last segment, opponent takes first segment 
        else:
            my_choice = parent_table[opponent_old_choice+1][my_old_choice-1][0]
            opponent_choice = parent_table[opponent_old_choice+1][my_old_choice-1][1]
            traceback.append(my_choice+1)
            traceback.append(opponent_choice+1)
            first_segment = opponent_old_choice
            logs = logs - 1
        #update old choices before next iteration 
        my_old_choice = my_choice
        opponent_old_choice = opponent_choice

    for i in range(len(traceback)):
        print(traceback[i], end=' ')

#print output
T(0,num_logs,log)
