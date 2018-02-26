i = 1
while i < 101:
    if i % 15 == 0:
        print("Fizz buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("buzz!")
    else:
        print(i)
    
    i += 1