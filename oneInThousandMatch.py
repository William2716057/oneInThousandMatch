
import random
import time
#Generate first number between one and one thousand
firstNumber = random.randint(1, 1000)
print("Original number: ", firstNumber)

#record start time
startTime = time.time()

while True:
    nextNumber = random.randint(1, 10000)
    if nextNumber == firstNumber:
        print("Match found!", nextNumber)
        #calculate time
        endTime = time.time()
        duration = endTime - startTime
        print("duration: ", duration)
        break