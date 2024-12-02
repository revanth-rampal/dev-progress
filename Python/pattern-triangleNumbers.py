for i in range(5):
    for j in range(1,5-i+1):
        print(" ", end='')
    for j in range(1,i+2):
        print(f'{j} ',end='')
    print()