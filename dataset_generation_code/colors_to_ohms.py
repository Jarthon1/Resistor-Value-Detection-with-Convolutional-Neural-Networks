# Takes in colors as a string and returns Ohms as a searchable string
from matplotlib import colors

def colors_to_ohms(input: str):
    listInput = input.split()
    res = 0
    # get a list of nums
    nums = colors_to_nums(listInput)
    length = len(nums)

    # convert list to string of search query
    if length  == 3:
        ohm = (nums[0]*10 + nums[1])*10**(nums[2])
        tol = 20
    elif length == 4:
        ohm = (nums[0]*10 + nums[1])*10**(nums[2])
        tol = nums[3]
    elif length == 5:
        ohm = (nums[0]*10 + nums[1] + nums[2])*10**(nums[3])
        tol = nums[4]
    elif length == 6:
        ohm = (nums[0]*10 + nums[1] + nums[2])*10**(nums[3])
        tol = nums[4]
        tmp = nums[5]
    res =  str(ohm) + " Ohm Resistor with Tolerance " + str(tol) + " and Temperature" + str(tmp)
    return res

# store the numbers in a list
def colors_to_nums(listInput):
    nums = []
    for i in range(len(listInput)):
        if listInput[i] == "none" and i == len(listInput) - 1:
            nums.append(20)
        elif listInput[i] == "none": 
            pass
        elif listInput[i] == "black":
            nums.append(0)
        elif listInput[i] == "brown":
            nums.append(1)
        elif listInput[i] == "red":
            nums.append(2)
        elif listInput[i] == "orange":
            nums.append(3)
        elif listInput[i] == "yellow":
            nums.append(4)
        elif listInput[i] == "green":
            nums.append(5)
        elif listInput[i] == "blue":
            nums.append(6)
        elif listInput[i] == "violet":
            nums.append(7)
        elif listInput[i] == "grey":
            nums.append(8)
        elif listInput[i] == "white":
            nums.append(9)
        elif listInput[i] == "gold":
            nums.append(5)
        elif listInput[i] == "silver":
            nums.append(10)
    return nums