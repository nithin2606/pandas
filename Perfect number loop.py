per_list = []
def perfect(n):
    total = 0
    for num in range(1, n):
        if n % num == 0:
            total = total + num
    if total == n:
        per_list.append(total)


def perfect1(a):
    for n in range(1, a):
        perfect(n)
    print(per_list)


perfect1(100)
