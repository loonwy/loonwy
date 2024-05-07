
with open('mas.txt', 'r') as f:
    line = f.read()

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst [j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
print(bubble_sort(list(map(int, line.split(',')))))
'''Принцип: Сравнивает соседние элементы и меняет их местами, если они не в порядке. Повторяет этот процесс до тех пор, пока весь список не будет отсортирован.
Область применения: Простые списки небольшого размера.
351.99856758117676 миллисекунд'''

def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i-1
        while (j >= 0 and temp <alist[j]):
            alist[j+1] = alist[j]
            j = j - 1
        alist[j + 1] = temp
    return alist
print(insertion_sort(list(map(int, line.split(',')))))
'''Принцип: Вставляет каждый элемент в правильную позицию в уже отсортированной части списка.
Область применения: Списки, которые уже частично отсортированы или почти отсортированы.
51.03349685668945 миллисекунд'''

def merge_sort(lst):
    if len(lst) <=1:
        return lst
    mid = len(lst)//2
    left_list = lst[:mid]
    right_list = lst[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append((left_half[0]))
            left_half.remove((left_half[0]))
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res += right_half
    else:
        res += left_half
    return res

print(merge_sort(list(map(int, line.split(',')))))
'''Принцип: Делит список на две части, сортирует каждую часть рекурсивно, а затем сливает отсортированные части воедино.
Область применения: Большие списки, особенно когда память ограничена.
8.028268814086914 миллисекунд'''

def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [i for i in s if i == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort(list(map(int, line.split(',')))))
''' Принцип: Выбирает опорный элемент, делит список на два подсписка (элементы меньше и больше опорного элемента) и рекурсивно применяет ту же процедуру к подспискам.
Область применения: Большие списки, когда память не ограничена.
13.997554779052734 миллисекунд'''

def counting_sort(alist, largest):
    c = [0] * (largest + 1)
    for i in range(len(alist)):
        c[alist[i]] += 1
    for i in range(1, largest + 1):
        c[i] += c[i - 1]
    res = [None] * len(alist)
    for x in reversed(alist):
        if c[x] < len(res):
            res[c[x]] = x
        c[x] -= 1
    return res

largest = max(list(map(int, line.split(','))))
print(counting_sort(list(map(int, line.split(','))), largest))
''' Принцип: Работает только для списков с ограниченным набором значений. Создаёт массив частот для каждого возможного значения, а затем использует эти частоты для определения позиции каждого элемента в отсортированном списке.
Область применения: Списки с небольшим набором значений, например, подсчёт букв в тексте.
5.0029754638671875 миллисекунд'''

f.close()

'''В ходе посчета времени оказалось, что для этого списка самая эффектиивная сортировка была - сортировка подсчетом'''