
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))


quotient = dividend // divisor
remainder = dividend % divisor


if remainder == 0:
    print("The division is exact.")
else:
    print("The division is not exact.")


print("Quotient:", quotient)
print("Remainder:", remainder)
