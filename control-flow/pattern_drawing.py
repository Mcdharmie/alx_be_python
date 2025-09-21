number = int(input(f"Enter the size of the pattern: "))

i = 0

while i < number:
    i+=1
    for number in range(1, number+1):
        print("*", end="")
    print()
         
