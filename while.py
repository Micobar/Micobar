num = 0
numbers = []
while num >= 0:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    else:
        numbers.append(num)

print(f"You have entered: {numbers}")

average = sum(numbers) / len(numbers)
print(f"Average of entered numbers is: {average}")
