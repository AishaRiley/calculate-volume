##Write program to calculate volume of pyramid

##Have user give the base and the height of the pyramid
def main():
    print("Volume:",pyramidVolume(5, 9))
    print("Expected: 300")
    print("Volume:",pyramidVolume(9, 10))
    print("Expected: 0")

def pyramidVolume(baseLength, height):
    baseArea = baseLength * baseLength
    return height * baseArea / 3

##Start program
main()

