from typing import List


def convert(numbers: List[int]) -> List[int]:
        
    new_list: List[int] = []
    for x in numbers:
        if new_list and new_list[-1][0] == x:
            new_list[-1].append(x)
        else:
            new_list.append([x])
    return new_list


print(convert([1, 1, 1, 1, 2]))
