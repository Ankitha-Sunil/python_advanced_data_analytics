try:
    inp1=input("Enter a name:")
    inp2=int(input("Enter age:"))
    print(f"Name:{inp1}, Age:{inp2}")

except ValueError as e:
    print(f"This is a ValueError: {e}.Please enter a valid integer for age")

except TypeError as e:
    print(f"This is a TypeError: {e}.Please enter a valid input")

else:
    print("Input is valid.No exception occured")

finally:
    print("Program execution completed")