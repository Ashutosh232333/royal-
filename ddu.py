# number = (int(input("take a number")))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
n=int(input("Enter A positive number: "))
total=0
for number in range(1,n+1):
    total+=number
print(f"Total: {total}")
