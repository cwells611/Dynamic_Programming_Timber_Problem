import random

random_num_segments = 11

#generates a list of random segment lengts between 1 and 1000
#based on the number of segments 
log = []
for i in range(random_num_segments):
    random_length = random.randint(1,1000)
    log.append(str(random_length))
num_segments = str(random_num_segments)

#write to input file for recursive algorithm 
with open('test.txt', 'w') as file:
    file.write(num_segments + '\n')
    for line in log:
        file.write(line + " ")