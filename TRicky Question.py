#question: for number 135,  1**1 + 3**2 + 5**3 = 135

def get_digits(n):
    result = []
    while n > 0:
        result.insert(0, n % 10)
        n //= 10
    return result

def sum_dig_pow(a, b):
    result = []
    for n in range(a,b+1):
        s = 0
        for index, digit in enumerate(get_digits(n)):
            s += digit**(index+1)
        if s == n:
            result.append(n)
    print(result)

sum_dig_pow(1,135)

# code for same question
# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#     res = []
#     for number in range(a, b+1):
#         digits = [int(i) for i in str(number)]
#         s = 0
#         for idx, val in enumerate(digits):
#             s += val ** (idx + 1)
#         if s == number:
#             res.append(number)
#     return res