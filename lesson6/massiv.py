def find_division_index(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        midpoint = left + (right - left) // 2
        if arr[midpoint] == 1 and arr[midpoint - 1] == 0:
            return midpoint
        elif arr[midpoint] == 0:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return -1

arr = list(map(int, input("Введите упорядоченный массив из 0 и 1 через пробел: ").split()))
result = find_division_index(arr)

if result != -1:
    print(f"Место разделения: Индекс {result}")
else:
    print("Разделение не найдено.")
print (arr)
