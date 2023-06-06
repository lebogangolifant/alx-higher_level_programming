#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        print(
            "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
            "Fizz" if num % 3 == 0 else
            "Buzz" if num % 5 == 0 else
            num,
            end=" "
        )
