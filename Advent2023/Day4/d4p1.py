import math as m
class Solution:
    def Solution():
        sum = 0
        with open("Advent2023/Day4/input1.txt") as file:
            for line in file:
                expon = -1
                winingNums = set(line.strip().split("|")[0].split(":")[1].split(" "))
                winingNums.remove('')
                winingNums = list(map(int, list(winingNums)))
                
                ourNums = set(line.strip().split("|")[1].split(" "))
                ourNums.remove('')
                ourNums = list(map(int, list(ourNums)))

                for i in range(0, len(ourNums)):
                    if ourNums[i] in winingNums:
                        expon += 1
                if expon < 0:
                    continue
                sum += int(m.pow(2, expon))
        return sum





print(Solution.Solution())
