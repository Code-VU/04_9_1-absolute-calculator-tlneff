def calculateAbsolute():

    # This first line is provided for you
    in_num = input("Enter a number: ")
    try:
        in_num = int(in_num)
    except:
        print("Not valid!")
        quit()

    result = abs(21 - in_num)
    if in_num > 21:
        result = result * 2
    print("Result:", result)
    # end assignment

# If you want to test locally run > python payCalculator.py


if __name__ == "__main__":
    calculateAbsolute()
