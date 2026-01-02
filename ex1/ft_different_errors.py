#!/usr/bin/python3

def garden_operations(str_value: str):
    # ValueError
    try:
        value = int(str_value)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        value = 0
        return
    # ZeroDivisionError
    try:
        result = 10 / value
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        return
    # FileNotFoundError
    try:
        open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
        return
    # KeyError
    plants = {"rose": 5}
    try:
        plant = plants["sunflower"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
        return
    try:
        value = int(str_value)
        result = 10 / value
        open("missing.txt", "r")
        plant = plants["sunflower"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")
    
    print("\nTesting ValueError...")
    garden_operations("abc")

    print("\nTesting ZeroDivisionError...")
    garden_operations("0")
    
    # print("\nTesting FileNotFoundError...")
    
    # print("\nTesting KeyError...")

    # print("\nTesting multiple errors together...")


if __name__ == "__main__":

    test_error_types()