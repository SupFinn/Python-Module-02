#!/usr/bin/python3

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
