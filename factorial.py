def factorial(max_number):
    for each in range(max_number):
        print(each)
        factorial(max_number - 1)
    print('..')

factorial(3)
#bigO n!