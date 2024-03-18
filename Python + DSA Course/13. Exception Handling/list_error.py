# Exception Handling:

# Example 1: IndexError
try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list[99])
except:
    print("Some error occured")

# Example 2: ZeroDivisionEror
try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list[0] / my_list[-1])
except:
    print("Some error occured")

# Example 3:
# Above codes handles all kind of error. But what if we want to handle a specific error in specific manner.
try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list[0] / my_list[-1])
except ZeroDivisionError or ValueError:  # Type of errors
    print("Cannot divide by Zero, please check values again")
except IndexError:
    print("Index is out of range")
except (
    Exception
) as e:  # Always have to go last. It handle all error that are not specified above block.
    # But we are unable to tell what type of error has occured. E tells the error message.
    print(type(e).__name__)  # Gets us name of the error
    print(f"{e} : error message")
    print(" Some unknown error occured.")
else:  # Runs if no error.
    print("Everything works fine")
    print(my_list)
finally:  # Runs always irrespective of the error. You can use it without else clause.
    # Usually used for cleaned up process. If you are writing finally and else, else goes first then finally.
    print("This is finally clause")

# Question:
# Try Clause 1:
try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list[99])
    try:
        my_list = [34, 55, 63, 78, 94, 0]
        print(my_list[0] / my_list[-1])
    except:
        print("Try Clause 2")
except:
    print("Try Clause 1")

# Try Clause 2:
try:
    my_list = [34, 55, 63, 78, 94, 0]
    try:
        my_list = [34, 55, 63, 78, 94, 0]
        print(my_list[0] / my_list[-1])
    except:  # Handles the error for try clause 2. Thus we no longer have error for try clause 1
        # Thus no need for except clause for try clause 1 to run.
        print("Try Clause 2")
except:
    print("Try Clause 1")
