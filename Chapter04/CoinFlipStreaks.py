#Radnom coin flip simulation
import random
numberOfStreaks = 0

#Run the experiment 10000 times (100 flips per experiment)
allExperiments = []
for experimentNumber in range(10000):
    experiment = []
    for coinFlip in range(100):
        experiment.append(random.randint(0,1))
    allExperiments.append(experiment)

print('Checking for streaks of six flips the same in a row...')

for x in range(len(allExperiments)):
    counter = 0
    for y in range(len(allExperiments[x])):
        if y == 0:
            continue
        elif allExperiments[x][y] == allExperiments[x][y-1]:
            counter += 1
            if counter == 6:
                numberOfStreaks += 1
                counter = 0
        else:
            counter = 0

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
