"""
Assert Keyword: It a way of showing error.  
Assert only runs when condition is not met. 
It bascially crashes as soon as assertion condition is FALSE. Assertion conditions (age>18) has to be bool. 
Assert conditions are the one that needs to be satisfied. 
"""

age = int(input("Enter your age: "))

assert age > 18, "You should be atleast 18 age"  # You customized error message

vote_id = int(input("Enter voting ID: "))
vote_party = input("Enter party to vote: ")

# Example 1:
try:
    age = int(input("Enter your age: "))
    assert age > 18, "You should be atleast 18 age"  # You customized error message
    vote_id = int(input("Enter voting ID: "))
    vote_party = input("Enter party to vote: ")
except AssertionError as e:
    print(e)
except:
    print("Some error occured.")


# Example 2:

try:
    my_list = [54, 12, 15, 178, 162, 158]
    index = int(input("Enter index numer: "))
    assert 0 <= index < len(my_list), "Index is out of range"
    print(my_list[index])
except AssertionError as e:
    print(e)
except:
    print("Some unknown error has occured.")
