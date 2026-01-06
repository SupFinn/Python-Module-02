#!/usr/bin/python3

def garden_operations(mode: str):
    if mode == "value":
        try:
            int("abc")
        except ValueError:
            print("Caught ValueError: invalid literal for int()")

    elif mode == "zero":
        try:
            10 / 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")

    elif mode == "file":
        try:
            open("missing.txt", "r")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")

    elif mode == "key":
        try:
            data = {"rose": 5}
            data["sunflower"]
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'")

    elif mode == "multiple":
        try:
            int("abc")
            10 / 0
            open("missing.txt", "r")
            {}["x"]
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    garden_operations("value")

    print("\nTesting ZeroDivisionError...")
    garden_operations("zero")

    print("\nTesting FileNotFoundError...")
    garden_operations("file")

    print("\nTesting KeyError...")
    garden_operations("key")

    print("\nTesting multiple errors together...")
    garden_operations("multiple")


if __name__ == "__main__":
    test_error_types()
