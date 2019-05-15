

# properties are an excellent addition to python as they help with encapsulation of instance data and have a
# great way to avoid breaking code when modifications are made later.  This is demonstrated through example, see below:
# Note: if you come from something like java, getters and setters are absolutely everywhere!
class BankBalance:
    def __init__(self, pounds: int, pence: int):
        self.pounds = pounds
        self.pence = pence


# Now here comes a user, who uses our code in v1 of our api
balance = BankBalance(50, 90)
print(f"I have {balance.pounds} pounds and {balance.pence}")

# Now we need to make changes to our Bank Balance code, the requirements have changed :(


class BankBalance:
    def __init__(self, pounds: int, pence: int):
        self.total = pence * 100 + pounds  # we only care about total pence now


# The users code will now be broken...
# balance.pounds no longer exists, 'AttributeError' will be raised here
# AttributeError: 'BankBalance' object has no attribute 'pounds:
balance = BankBalance(50, 90)
print(f"I have {balance.pounds} pounds and {balance.pence}")

#  Here is where python is cool and how we should handle this scenario:


class BankBalance:
    def __init__(self, pounds: int, pence: int):
        self.total = pence * 100 + pounds

    @property
    def pounds(self):
        return self.total // 100

    @pounds.setter
    def pounds(self, new_pounds):
        self.total = 100 * new_pounds + self.pence

    @property
    def pence(self):
        return self.total % 100

    @pence.setter
    def pence(self, new_pence):
        self.total = 100 * self.pounds + new_pence


# The takeaway? They make it possible to refactor and make change(s) to your code without breaking everyone elses!


class TheProperties:
    def __init__(self):
        self._x: int = 25

    # @property is used as an accessor, or 'getter' for the property in question, note the name of the method
    # matches that of the property (without the _)
    @property
    def x(self):
        print('Getter for _x')
        return self._x

    # note here; the property name (again without _) as the method name
    # instance variable (dot .) setter
    @x.setter
    def x(self, new_value):
        print('Setter for _x')
        self._x = new_value

    @x.deleter
    def x(self):
        print('Runs before deleting _x')
        del self._x


