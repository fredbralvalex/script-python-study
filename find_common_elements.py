def find_common_elements(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                result.append(item1)
    return result

common = find_common_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8])
print(common)
#BigO n^2