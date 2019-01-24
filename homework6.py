"""
Homework 6.

Create class representing money in different currencies.
"""

RATES = {
    ('BYN', 'USD'): 0.47,
    ('BYN', 'EUR'): 0.41,
    ('BYN', 'JPY'): 51.07,

    ('USD', 'BYN'): 2.15,
    ('USD', 'EUR'): 0.88,
    ('USD', 'JPY'): 109.75,

    ('EUR', 'BYN'): 2.44,
    ('EUR', 'USD'): 1.13,
    ('EUR', 'JPY'): 124.48,

    ('JPY', 'BYN'): 0.020,
    ('JPY', 'USD'): 0.0091,
    ('JPY', 'EUR'): 0.0080
}


class Money(object):
    """Money class."""

    def __init__(self, value, currency='USD'):
        """Init method."""
        self.value = value
        self.currency = currency

    def convert(self, to_cur):
        """Currencies converting method."""
        if self.currency != to_cur:
            rate = RATES[(self.currency, to_cur)]
            return self.value * rate
        else:
            return self.value

    def __add__(self, other):
        """+ operation method."""
        if isinstance(other, Money):
            if other.currency != self.currency:
                other.value = other.convert(self.currency)
                other.currency = self.currency
            return self.__class__(self.value + other.value, self.currency)

    def __radd__(self, other):
        """Reversed + operation method."""
        if isinstance(other, Money):
            if self.currency != other.currency:
                other.value = other.convert(self.currency)
                self.currency = other.currency
        return self.__class__(self.value + other, self.currency)

    def __mul__(self, other):
        """* operation method."""
        amount = self.value * other
        return self.__class__(amount, self.currency)

    def __rmul__(self, other):
        """Reversed * operation method."""
        return self.__mul__(other)

    def __repr__(self):
        """Representation method."""
        return "{} {}".format(str(self.value), self.currency)


if __name__ == '__main__':
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")

    print(z + 3.11 * x + y * 0.8)

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]

    s = sum(lst)

    print(s)
