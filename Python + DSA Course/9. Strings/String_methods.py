"""
String Methods:

1. joining
2. split
3. lower : Return a copy of the string converted to lowercase. 
4. upper : Return a copy of the string converted to uppercase.
5. casefold : 
6. swapcase : Convert uppercase characters to lowercase and lowercase characters to uppercase.
7. title :  Return a version of the string where each word is titlecased.
            More specifically, words start with uppercased characters 
            and all remaining cased characters have lower case. 
8. capitalize : Return a capitalized version of the string.
                More specifically, make the first character have upper case and the rest lower case.
9. islower : Return True if the string is a lowercase string, False otherwise.
10. isupper : Return True if the string is an uppercase string, False otherwise.
11. isdigit : Return True if the string is a digit string, False otherwise.
12. isalpha : Return True if the string is an alphabetic string, False otherwise.
13. isalnum : Return True if the string is an alpha-numeric string, False otherwise.
14. count : Return the number of non-overlapping occurrences of substring sub in
15. endswith : Return True if S ends with the specified suffix, False otherwise.
16. startswith : Return True if S starts with the specified prefix, False otherwise.
17. find and index : 
        Find : Return the lowest index in S where substring sub is found, Return -1 on failure.
        index : Return the lowest index in S where substring sub is found, Raises ValueError when the substring is not found.
19. replace : Return a copy with all occurrences of substring old replaced by new.
20. strip : Return a copy of the string with leading and trailing whitespace removed.
21. rstrip, lstrip: 
        rstrip: Return a copy of the string with trailing whitespace removed.
        lstrip: Return a copy of the string with leading whitespace removed.
22. rfind : Return the highest index in S where substring sub is found,
"""

my_string = " great1212 "
print(my_string.rfind("g"))
