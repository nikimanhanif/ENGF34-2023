for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
        continue # continue statement needed to break the loop
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0: 
        print("Buzz")
        continue
    print(fizzbuzz)