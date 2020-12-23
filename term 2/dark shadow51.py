number = input("Enter Number: ")
counter = 0
numbers = []
sums = 0
while number != '0':
    if number.isdigit():
        numbers.append(number)
        counter += 1
    number = input("Enter Number: ")
for n in numbers:
    sums += int(n)
print(f"Your numbers{numbers}")
print(f"Average of your numbers {sums/counter}")
