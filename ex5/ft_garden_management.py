#!/usr/bin/python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class SunError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name: str, water: int, sun: int):
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            new_plant = Plant(name, water, sun)
            self.plants += [new_plant]
            print(f"Added {name} successfully")

        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        for plant in self.plants:
            try:
                if plant.water > 10:
                    raise WaterError(
                        f"Water level {plant.water} is too high (max 10)"
                        )
                if plant.water < 1:
                    raise WaterError(
                        f"Water level {plant.water} is too low (min 1)"
                        )
                if plant.sun > 12:
                    raise SunError(
                        f"Sunlight hours {plant.sun} is too high (max 12)"
                        )
                if plant.sun < 2:
                    raise SunError(
                        f"Sunlight hours {plant.sun} is too low (min 2)"
                        )

                print(
                    f"{plant.name}: healthy "
                    f"(water: {plant.water}, sun: {plant.sun})"
                    )

            except GardenError as e:
                print(f"Error checking {plant.name}: {e}")


def test_garden_manager():
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 9)
    manager.add_plant("", 3, 5)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health()

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_manager()
    print("\nGarden management system test complete!")
