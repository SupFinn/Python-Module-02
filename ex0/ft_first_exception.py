#!/usr/bin/python3

def check_temperature(temp_str: str):
    try:
        value = int(temp_str)
        if value >= 0 and value <= 40:
            print(f"Temperature {value}°C is perfect for plants!")
            return value
        elif value < 0:
            print(f"Error: {value}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {value}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    return None


if __name__ == "__main__":

    print("=== Garden Temperature Checker ===")

    print("\nTesting temperature: 25")
    check_temperature("25")

    print("\nTesting temperature: abc")
    check_temperature("abc")

    print("\nTesting temperature: 100")
    check_temperature("100")

    print("\nTesting temperature: -50")
    check_temperature("-50")

    print("\nAll tests completed - program didn't crash!")
