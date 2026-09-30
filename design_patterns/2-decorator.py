#!/usr/bin/env python3
"""Decorator pattern for adding beverage toppings."""


class Beverage:
    """Base beverage interface."""

    def cost(self):
        """Return the cost of the beverage."""
        raise NotImplementedError

    def description(self):
        """Return the beverage description."""
        raise NotImplementedError


class Coffee(Beverage):
    """Concrete coffee beverage."""

    def cost(self):
        """Return the coffee cost."""
        return 50

    def description(self):
        """Return the coffee description."""
        return "Coffee"


class BeverageDecorator(Beverage):
    """Base decorator for beverages."""

    def __init__(self, beverage):
        """Initialize the decorator."""
        self._inner = beverage


class MilkDecorator(BeverageDecorator):
    """Add milk to a beverage."""

    def cost(self):
        """Return the cost including milk."""
        return self._inner.cost() + 10

    def description(self):
        """Return the description including milk."""
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    """Add sugar to a beverage."""

    def cost(self):
        """Return the cost including sugar."""
        return self._inner.cost() + 5

    def description(self):
        """Return the description including sugar."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    """Add caramel to a beverage."""

    def cost(self):
        """Return the cost including caramel."""
        return self._inner.cost() + 15

    def description(self):
        """Return the description including caramel."""
        return self._inner.description() + " + caramel"


def main():
    """Run the decorator example."""
    coffee = Coffee()
    print(
        MilkDecorator(coffee).description(),
        MilkDecorator(coffee).cost()
    )

    coffee_with_sugar = SugarDecorator(Coffee())
    coffee_with_sugar_and_milk = MilkDecorator(coffee_with_sugar)

    print(
        coffee_with_sugar_and_milk.description(),
        coffee_with_sugar_and_milk.cost()
    )

    coffee_with_all = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(
                Coffee()
            )
        )
    )

    print(
        coffee_with_all.description(),
        coffee_with_all.cost()
    )


if __name__ == "__main__":
    main()
