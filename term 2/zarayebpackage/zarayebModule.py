def zarayeb(input_number):
    n = input_number
    file = open(f'multiples{n}.txt', 'w')
    file.write(f'Multiple numbers of {n}\n')
    while n < 1000:
        print(n)
        n += input_number
    file.close()
    