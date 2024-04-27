def find_division_index(a):
    left, right = 0, len(a) - 1
    while left <= right:
        center = left + (right - left) // 2
        if a[center] == 1 and a[center - 1] == 0:
            return center
        elif a[center] == 0:
            left = center + 1
        else:
            right = center - 1
    return -1

a = list(map(int, input("Введите массив из 0 и 1: ").split()))
a.sort()
result = find_division_index(a)
print(a)

if result != -1:
    print(f"Index {result}")
else:
    print("Разделение не обнаружено")
