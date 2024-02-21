year = int(input("Enter a year: "))
if year %4==0: 
    if year%400==0: 
        print(f"Year {year} is a leap year.")
    elif year %100==0: 
        print(f"Year {year} is NOT a leap year.")
    else: 
        print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is NOT a leap year.")