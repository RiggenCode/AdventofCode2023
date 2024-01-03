class Solution:
    def Solution():
        sum = 0
        with open("Advent2023/Day2/input1.txt") as file:
            for line in file:
                redMax = 0
                greenMax = 0
                blueMax = 0
                for x in line.split(":")[1].split(";"):
                    i = 0
                    x = x.strip().split(" ")
                    while i < len(x):

                        if i % 2 == 0:

                            if ((x[i + 1] == 'red' or x[i + 1] == 'red,') and int(x[i]) > redMax):
                                redMax = int(x[i])

                            if ((x[i + 1] == 'green' or x[i + 1] == 'green,') and int(x[i]) > greenMax):
                                greenMax = int(x[i])

                            if ((x[i + 1] == 'blue' or x[i + 1] == 'blue,') and int(x[i]) > blueMax):
                                blueMax = int(x[i])    

                        i += 1

                sum += (redMax * greenMax * blueMax)

        return sum
    
print(Solution.Solution())