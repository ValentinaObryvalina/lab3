import random
error_count = 0
count = 0
while error_count < 3:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if int(input(f"{a} + {b} = ")) == a + b:
        count += 1
        print('Правильно!')
    else:
        error_count += 1
        print('Неправильно!')
print(f"Игра окончена. Правильных ответов {count}")