from collections import Counter
from typing import List, Union


def find_unique_value(some_list: List[Union[int, float]]) -> Union[int, float, None]:

    count = Counter(some_list)
    for number, freq in count.items():
        if freq == 1:
            return number
    return None


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
