num = int( input() )
if num < 11 or num > 99:
    print('Input must be 11-99')
else:
    while True:
        print(num)
        
        left_digit = num // 10 
        right_digit = num % 10 

        if left_digit == right_digit:
            break
        else:
            num = num - 1 