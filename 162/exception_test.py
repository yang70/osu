class OutOfRangeError(Exception):
    pass

def numberName():
    num = int(input("Input an integer: "))

    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    else:
        raise OutOfRangeError

def main():
    try:
        numberName()
    except OutOfRangeError:
        print("That's not one of the allowed values!")

if __name__ == '__main__':
    main();

