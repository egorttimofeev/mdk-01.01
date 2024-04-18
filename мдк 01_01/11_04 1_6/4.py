import random

def count_even_odd(numbers):

    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

numbers = [random.randint(1, 100) for _ in range(100)]

even, odd = count_even_odd(numbers)

print("Кол-во четных чисел:", even)
print("Кол-во нечетных чисел:", odd)