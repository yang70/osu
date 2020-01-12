from exception_test import OutOfRangeError

def mult3(num1, num2, num3):
    if num1 == 4:
        try:
            raise OutOfRangeError
        except:
            print("4 is not allowed")
        else:
            return num1 * num2 * num3