# total =0
# for i in range(1,11):
#     total += i
# print(f"Sum of numbers from 1 to 10 is: {total}")

input = int(input("Enter a number: "))
total = 0
for i in range(1, input + 1):
    total += i
print(f"Sum of numbers from 1 to {input} is: {total}")
