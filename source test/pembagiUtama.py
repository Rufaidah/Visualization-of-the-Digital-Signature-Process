import math

from sympy.ntheory import factorint
import sympy

def isPrime(num):
    prime = sympy.isprime(num)
    return prime

def pfactors():
    prime = 3497165743

    q = prime - 1
    upper = int(q/100)
    # upper = int(math.sqrt(q))


    for num in range(2, upper):
        if (q % num == 0):
            if (isPrime(num)):
                print(num)
    #             result = num
    #
    # print(result)

    # num = factorint(q)
    # print(num)
pfactors()

# def isPrime(num):
#     if num > 3:
#         if num % 2 == 0:
#             return False
#         else:
#             pmax = int(math.sqrt(num))
#             for p in range(3, pmax + 1, 2):
#                 if (num % p) == 0:
#                     return False
#             else:
#                 return True
#     else:
#         return True
#
# def pfactors():
#     prime = 283
#
#     upper = prime - 1
#
#     for num in range(2, upper):
#         if (upper % num == 0):
#             if (isPrime(num)):
#                 print(num)
#
# pfactors()

# def komputasi():
#     k = open('../output/nilaihash.txt', 'r').read()
#     j = 8
#
#     num = k*j
#
#     print(num)
# komputasi()

# def modinv():
#     s = 30
#     q = 47
#
#     w = sympy.mod_inverse(s, q)
#     print(w)
# modinv()