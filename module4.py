#The program asks the user for input N (positive integer) and reads it
while True:
    pos_int=input('Please input a positive integer: ')
    try:
        n_number = int(pos_int)
        print('Your input is', n_number)
        break
    except:
        print('try again')

#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
num_list =[]
while len(num_list) < n_number:
    while True:
        num_q = input('Please provide a number:')
        try: 
            flo_num = float(num_q)
            print(flo_num)
            num_list.append(flo_num)
            break
        except:
            print('wrong input, try again')

#In the end, the program asks the user for input X (integer) and outputs: "-1" 
#if there were no such X among N read numbers, 
#or the index (from 1 to N) of this X if the user inputed it before.
mat_q = input('Please a number X for matching up: ')
mat_num = float(mat_q)
if mat_num in num_list:
    print('The index number is: ',num_list.index(mat_num))
else:
    print('-1')