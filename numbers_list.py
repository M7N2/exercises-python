numbers = [15, 8, 23, 15, 42, 8, 15, 7, 31, 15, 23, 8, 42, 15, 7]

print(sum(numbers))
print(max(numbers))
print(min(numbers))

count15 = 0
count8 = 0

for i in numbers:
    if i == 15:
        count15 += 1
    if i == 8:
        count8 += 1
print(f"чисел 15: {count15}, чисел 8: {count8}\n")    

#без повторений
numbers_set = list(set(numbers)) #чтобы сохранился порядок и список
print(numbers_set)

#среднее арифметическое
summ = sum(numbers)
count = len(numbers)
average = summ/count
print(f"Среднее арифметическое = {average:.2f}")
