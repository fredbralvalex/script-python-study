def find_max(my_array):
    max = 0
    for item in my_array:
        if item > max:
            max = item
    return max

max = find_max([13, 2, 33, 40, 25, 16, 27, 8, 19])
print(max)
#bigO n