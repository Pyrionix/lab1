import math

def search_min_fun(x, fx):
    min = fx[0]
    min_x = x[0]
    for i in range(len(fx)):
        if fx[i] < min:
            min = fx[i]
            min_x = x[i]
    return min_x, min

def passive_search_N(a, b, Eps):
    return math.ceil((b - a) / Eps - 1)

def passive_search_count(N, a, b):
    x, fx = [], []
    for i in range(N):
        x.append(a + ((b - a) / N) * (i + 1))
        fx.append(-2 * math.sqrt(x[i]) * math.sin(0.5 * x[i]))
    return x , fx
    
def input_Eps():
    Eps = input()
    while str(Eps).isdigit == False:
        print("Type Eps (float)")
        Eps = input()
    return float(Eps)

def golnden_search_count(Eps, a, b):
    i, lk = 1, b - a
    x1 = a + (1 - 1 / tau) * lk
    x2 = a + 1 / tau * lk
    fx1 = -2 * math.sqrt(x1) * math.sin(0.5 * x1)
    fx2 = -2 * math.sqrt(x2) * math.sin(0.5 * x2)
    print("x" + str(i) + ",1 = " + str(x1),"x" + str(i) + ",2 = " + str(x2))
    print("f(x" + str(i) + ",1) = " + str(fx1), "f(x" + str(i) + ",2) = " + str(fx2))
    i += 1

    while lk > Eps:

        if fx1 > fx2:
            a, b = x1, b 
            lk = b - a
            x1 = x2
            x2 = a + 1 / tau * lk
            fx2 = -2 * math.sqrt(x2) * math.sin(0.5 * x2)
            print("x" + str(i) + ",1 = " + str(x1),"x" + str(i) + ",2 = " + str(x2))
            print("f(x" + str(i) + ",1) = " + str(fx1), "f(x" + str(i) + ",2) = " + str(fx2))

        else:
            a, b = a, x2
            lk = b - a
            x2 = x1
            x1 = a + (1 - 1 / tau) * lk
            fx1 = -2 * math.sqrt(x1) * math.sin(0.5 * x1)
            print("x" + str(i) + ",1 = " + str(x1),"x" + str(i) + ",2 = " + str(x2))
            print("f(x" + str(i) + ",1) = " + str(fx1), "f(x" + str(i) + ",2) = " + str(fx2))

        print(lk)
        i += 1

    return i 


# def golnden_search_count(Eps, a, b):
#     i, lk = 1, b - a
#     while lk > Eps:
#         lk = b - a
#         x1 = a + (1 - 1 / tau) * lk
#         x2 = a + 1 / tau * lk
#         fx1 = -2 * math.sqrt(x1) * math.sin(0.5 * x1)
#         fx2 = -2 * math.sqrt(x2) * math.sin(0.5 * x2)
#         if fx1 > fx2:
#             a, b = x1, b
#         else:
#             a, b = a, x2

#         print("x" + str(i) + ",1 = " + str(x1),"x" + str(i) + ",2 = " + str(x2))
#         print("f(x" + str(i) + ",1) = " + str(fx1), "f(x" + str(i) + ",2) = " + str(fx2))

#         i += 1

#     return i 



# f = -2 * math.sqrt(x) * math.sin(0.5 * x)
a, b = 2, 6
tau = (1 + math.sqrt(5)) / 2

Eps = input_Eps()
# N = passive_search_N(a, b, Eps)
# x, fx = passive_search_count(N, a, b)
# min_x, min = search_min_fun(x, fx)
# print(min_x, min)

i = golnden_search_count(Eps, a, b)
print(i)