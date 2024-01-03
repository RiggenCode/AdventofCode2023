class Solution:
    def Solution():
        numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        count = 0 #initialize a total count to return

        with open("Advent2023/Day1/input1.txt") as file:
            
            for line in file:
                numString = ""
                for x in list(line):

                    if x in numList:
                        numString += x

                if (len(numString) == 1):
                    count += int(numString) * 11
                else:
                    count += int(str(numString[0] + numString[-1]))

        return count
    
print(Solution.Solution())

