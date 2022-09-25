# if number[i] == 0 count --
# if count < 0 and number[i0]==0 count ++
# move i0i
def windowSlider(numbers, k):
    count = k
    i0 = 0
    for i in range(len(numbers)):        
        if numbers[i] == 0: #count = count - (1 - numbers[i])
            count = count - 1

        if count < 0:
            if numbers[i0] == 0: #count = count + (1 - numbers[i0])
                count = count + 1
            i0 = i0 + 1
            
    return i - i0 + 1

val = windowSlider( [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], 0)
print(val)