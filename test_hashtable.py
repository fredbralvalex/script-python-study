my_list = []
my_list.append('test') 
my_list.append('test2') 
my_list
['test', 'test2']
my_list[0] 
'test'
my_list[1] 
'test2'
my_dict = {}
my_dict['test'] = 123
my_dict['test2'] = 456
my_dict['abd'] = 789   
my_dict['def'] = 789 
my_dict['abd'] = 789 
my_dict['abc'] = 789 
my_dict['abc']      
789
'abc'.__hash__()
6055571010658266631
my_dict
{'test': 123, 'test2': 456, 'abd': 789, 'def': 789, 'abc': 789}


def solution_n(numbers, target_sum):
    if not numbers:
        return []
    
    my_dic = {}
    for num in numbers:
        val = target_sum - num
        if val in my_dic:
            return [val, num]
        else:
            my_dic[num] = val
        print(my_dic)
    
    return []

solution_n([4, 1, 2, -2, 11, 15, 1, -1, -6, -4], 9 )