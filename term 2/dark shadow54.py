def average(numbers):
    sums = 0
    for n in numbers:
        sums += n
        print(sums/len(numbers))