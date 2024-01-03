class Solution:
    def Solution():
        ID = 0
        sum = 0
        with open("Advent2023/Day2/input1.txt") as file:
            for line in file:
                ID = int(line.split(" ")[1].strip(":"))
                addBool = True
                for x in line.split(":")[1].split(";"):
                    if not addBool:
                        break
                    i = 0
                    x = x.strip().split(" ")
                    while i < len(x) / 2:
                        colorChecker = Solution.ColorChecker(x[(i * 2) + 1], int(x[i * 2]))
                        if not colorChecker:
                            addBool = False
                            break
                        i += 1
                if not addBool:
                    continue
                sum += ID

        return sum
    
    def ColorChecker(color, num):
        if ((color == 'red' or color == 'red,') and num > 12):
            return False
        if ((color == 'green' or color == 'green,') and num > 13):
            return False
        if ((color == 'blue' or color == 'blue,') and num > 14):
            return False
        return True

print(Solution.Solution())