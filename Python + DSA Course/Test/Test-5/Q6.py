"""
Question 6: Write a Python program to convert string values of a given dictionary
into integer/float data types.
Original list:[{'x': '10','y': '20','z': '30'}, {'p': '40','q': '50','r': '60'}]
Output:[{'x': 10,'y': 20,'z': 30}, {'p': 40,'q': 50,'r': 60}]
"""


def convert(my_list: list[dict]) -> list[dict]:
    for i in my_list:
        for key, value in i.items():
            if "." in value:
                i[key] = float(value)
            else:
                i[key] = int(value)
    return my_list


my_list = [{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}]
print(convert(my_list))
