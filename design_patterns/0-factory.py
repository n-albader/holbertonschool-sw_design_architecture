#!/usr/bin/python3
"""Factory pattern with a vehicle registry"""


class Bus:
    """Represent a bus"""

    def mode(self):
        """Return the bus mode"""
        return "road"


class Train:
    """Represent a train"""

    def mode(self):
        """Return the train mode"""
        return "rails"


class Bike:
    """Represent a bike"""

    def mode(self):
        """Return the bike mode"""
        return "lane"


class Scooter:
    """Represent a scooter"""

    def mode(self):
        """Return the scooter mode"""
        return "scooter_lane"


class VehicleFactory:
    """Factory that creates vehicles using a registry"""

    _registry = {
            "bus": Bus,
            "train": Train,
            "bice": Bike
    }

    @classmethod
    def register_kind(cls, name, vehicle_cls):
        """Register a new vehicle type"""
        cls._registry[name] = vehicle_cls

    @classmethod
    def create(cls, kind):
        """Create a vehicle from the registry"""
        vehicle_cls = cls._registry[kind]
        return vehicle_cls


def main():
    """Demonstrate the vehicle factory"""
    factory = VehicleFactory()

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bice").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
