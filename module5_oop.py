class Data_processing():
    def __init__(self):
        while True:
            input_N = input('Please input a positive integer: ')
            try:
                n_number = int(input_N)
                print('Your input is', n_number)
                break
            except:
                print('Wrong input, please try again')


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
                    print('wrong input, please try again')

        mat_q = input('Please a number X for matching up: ')
        try:
            mat_num = float(mat_q)
            if mat_num in num_list:
                print('The index number is: ',num_list.index(mat_num)+1)
            else:
                print('-1')
        except:
            print('-1')
            
Data_processing()