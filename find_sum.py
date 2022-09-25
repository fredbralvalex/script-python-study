def find_sum(my_array):
    sum = 0
    for item in my_array:
        sum += item
    return sum

sum = find_sum([13, 2, 33, 40])
print(sum)
#BigO n