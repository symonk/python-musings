# The built in `filter` keyword is used for passing an iterable through a function, collecting only
# the return values of that function which are `True`.
from functools import wraps
from typing import Any


def meta_data(f):
    # Utility decorator for printing the executing func
    @wraps(f)
    def wrapper(*args, **kw):
        print(f"Executing: -----> {f.__name__} <-----")
        return f(*args, **kw)
    return wrapper


@meta_data
def basic_example() -> None:
    def divisible_by_five(item: Any) -> bool:
        return item % 5 == 0

    one_to_one_thousand = range(1000)
    filter_obj: filter = filter(divisible_by_five, one_to_one_thousand)  # returns a <class 'filter'>
    casted_to_list = list(filter_obj)
    print(casted_to_list)  # 0..5..10..15...990..995


@meta_data
def basic_example_lambda() -> None:
    # The same example as above concise with an anonymous function <lambda>
    print(list(filter(lambda x: x % 5 == 0, range(1000))))


@meta_data
def false_filter_example() -> None:
    # itertools can offer a predicate (False) alternative, this is displayed below:
    from itertools import filterfalse
    numbers_not_divisible_by_five = list(filter(lambda x: x % 5 != 0, range(1000)))
    print(numbers_not_divisible_by_five)


if __name__ == '__main__':
    basic_example()
    basic_example_lambda()
    false_filter_example()


