import math
import sympy

def prima():
    # 2**63 sampai 2**64 9223372036854775837 (5 menit 30 detik)
    # 2**31 sampai 2**32 2147483659

    lower = 2**63
    upper = 2**64

    num = sympy.randprime(lower,upper)
    print(num)

    # ketiga
    # for num in range(upper + 1, lower, -1):
    #     if num % 2 == 0:
    #         pass
    #     else:
    #         prime = True
    #         pmax = int(math.sqrt(num))
    #         for p in range(3, pmax + 1, 2):
    #             if (num % p) == 0:
    #                 prime = False
    #                 break
    #         if prime:
    #             print(num)
    #             break

        # pertama
        # for num in range(lower, upper + 1):
        #     if num > 1:
        #         for p in range(2, num):
        #             if (num % p) == 0:
        #                 break
        #         else:
        #             result = str(num)
        #             break

        # kedua
        # if num > 1:
        #     test = int (math.sqrt(num))
        #     for p in range(2, test):
        #         if (num % p) == 0:
        #             break
        #     else:
        #         print(num)
        #         break
prima()