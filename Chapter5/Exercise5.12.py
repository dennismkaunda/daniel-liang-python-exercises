number = 100
count_per_line = 1
limit = 10

print("The integers that are divisible by 5 and 6 from 100 to 1,000 are:")
while number <= 1000:
    if number % 5 == 0 and number % 6 == 0:
        print(str(number), end=' ')
        if count_per_line % limit == 0:
            print()
        count_per_line += 1
    number += 1
