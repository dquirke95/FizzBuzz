# FizzBuzz Test

for FizzBuzz in range(100):
    # if the number is divisible by both 3 and 5
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print("FizzBuzz")
        continue
    # if the number is divisible by 3 only
    elif FizzBuzz % 3 == 0:
        print("Fizz")
        continue
    # if the number is divisible by 5 only
    elif FizzBuzz % 5 == 0:
        print("Buzz")
        continue
    # if the number is divisible by neither 3 nor 5
    print(FizzBuzz)
