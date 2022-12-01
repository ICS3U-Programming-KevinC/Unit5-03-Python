# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Dec. 1, 2022
# This program prints "Hello, World!" and has comments

# finds the percentage corresponding with the grade
def getPercentage(grade):
    match grade:
        case "4+":
            return 98
        case "4":
            return 91
        case "4-":
            return 83
        case "3+":
            return 78
        case "3":
            return 75
        case "3-":
            return 71
        case "2+":
            return 68
        case "2":
            return 65
        case "2-":
            return 61
        case "1+":
            return 58
        case "1":
            return 55
        case "1-":
            return 51
        case "0":
            return 0
        case _:
            return -1


def main():
    # gets user input for the level grade
    user_grade = input("Please enter a level grade: ")

    # calls getPercentage with the user input
    percentage = getPercentage(user_grade)

    # checks if the grade inputted was 0
    if percentage == 0:
        print("The percentage of 0 is less than 50%")

    # checks if the grade inputted was invalid
    elif percentage == -1:
        print(f'"{user_grade}" is not a valid grade')

    # displays the correct percentage
    else:
        print(f"The percentage of {user_grade} is {percentage}%")


if __name__ == "__main__":
    main()
