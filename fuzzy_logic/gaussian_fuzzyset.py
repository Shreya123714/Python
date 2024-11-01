"""
By @Shreya123714

https://en.wikipedia.org/wiki/Fuzzy_set
https://en.wikipedia.org/wiki/Fuzzy_set_operations
https://en.wikipedia.org/wiki/Membership_function_(mathematics)
"""

from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class GaussianFuzzySet:
    """
    A class for representing and manipulating Gaussian fuzzy sets.

    Attributes:
        name: The name or label of the fuzzy set.
        mean: The mean value (center) of the Gaussianfuzzy set.
        std_dev: The standard deviation (controls the spread) of
        the Gaussian fuzzy set.
        is_complement: Indicates whether this is the complement
        of the original fuzzy set.
    Methods:
        membership(member): Calculate the membership value of
        an input 'member'in the fuzzy set.
        complement(): Create a new GaussianFuzzySet instance representing
        the complement.
        plot(): Plot the membership function of the fuzzy set.

    >>> fuzzy_set = GaussianFuzzySet("Medium Temperature", mean=25, std_dev=5)
    >>> fuzzy_set.membership(25)
    1.0
    >>> fuzzy_set.membership(30)
    0.6065306597126334
    >>> fuzzy_set.complement().membership(25)
    0.0
    """

    name: str
    mean: float
    std_dev: float
    is_complement: bool = False  # This flag indicates if it's the complement set

    def membership(self, member: float) -> float:
        """
        Calculate the membership value of an input 'member' in the Gaussian fuzzy set.
        If it's a complement set, returns 1 - the Gaussian membership.

        >>> GaussianFuzzySet("Medium", 0, 1).membership(0)
        1.0
        >>> GaussianFuzzySet("Medium", 0, 1).membership(1)
        0.6065306597126334
        """

        membership_value = np.exp(-0.5 * ((member - self.mean) / self.std_dev) ** 2)
        # Directly return for non-complement or return 1 - membership for complement
        return (
            float(membership_value)
            if not self.is_complement
            else 1 - float(membership_value)
        )

    def complement(self) -> GaussianFuzzySet:
        """
        Create a new GaussianFuzzySet instance representing the complement.

        >>> GaussianFuzzySet("Medium", 0, 1).complement().membership(0)
        0.0
        """
        return GaussianFuzzySet(
            f"¬{self.name}",
            self.mean,
            self.std_dev,
            is_complement=not self.is_complement,
        )

    def plot(self) -> None:
        """
        Plot the membership function of the Gaussian fuzzy set.
        """
        x = np.linspace(
            self.mean - 3 * self.std_dev, self.mean + 3 * self.std_dev, 1000
        )
        y = [self.membership(xi) for xi in x]
        plt.plot(x, y, label=self.name)
        plt.xlabel("x")
        plt.ylabel("Membership")
        plt.legend()


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Create an instance of GaussianFuzzySet
    fuzzy_set = GaussianFuzzySet("Medium Temperature", mean=25, std_dev=5)

    # Display some membership values
    print(f"Membership at mean (25): {fuzzy_set.membership(25)}")
    print(f"Membership at 30: {fuzzy_set.membership(30)}")
    print(
        f"Complement Membership at mean (25): {fuzzy_set.complement().membership(25)}"
    )

    # Plot the Gaussian Fuzzy Set and its complement
    fuzzy_set.plot()
    fuzzy_set.complement().plot()
    plt.title("Gaussian Fuzzy Set and its Complement")
    plt.show()
