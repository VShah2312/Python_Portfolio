f len(my_string) % 2 == 0:
        # If you pass a string to reversed(), you get an iterator that yields characters in reverse order:
        # So you need to use join
        result = "".join(reversed(my_string))  # OR my_string[::-1]
        return result
    else:
        return my_string.swapcase()


user_input = input("Enter a string: ")

print(function(user_input))
