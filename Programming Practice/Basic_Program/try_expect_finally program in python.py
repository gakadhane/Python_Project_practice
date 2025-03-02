class error_test():
    @staticmethod
    def try_block(a, b):
        try:
            result = a / b

        # The first except block catches ZeroDivisionError and prints an error message.
        except ZeroDivisionError:
            print("error: can not divided by zero.")
            result = None

        # The second except block catches TypeError and prints an error message.
        except TypeError:
            print("error: both argument must be number")
            result = None

        # The code inside the else block is executed if no exceptions occur in the try block. It prints a success message.
        else:
            print("Division successful!")

        # The code inside the finally block is always executed
        finally:
            print("Execution of the divide_numbers function is complete.")
        return result


num1 = 10
num2 = 2  # Change this value to test different cases

result = error_test.try_block(num1, num2)
print(f"Result: {result}")
