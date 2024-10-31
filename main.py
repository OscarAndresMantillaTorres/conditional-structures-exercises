
quantity = int(input("How many numbers do you want to enter? "))


numbers = []
for i in range(quantity):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)


sorted_numbers = sorted(numbers)
print("Sorted numbers:", " ".join(map(str, sorted_numbers)))
