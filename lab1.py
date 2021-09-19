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


# f = -2 * math.sqrt(x) * math.sin(0.5 * x)
a, b = 2, 6

Eps = input_Eps()
N = passive_search_N(a, b, Eps)
x, fx = passive_search_count(N, a, b)
min_x, min = search_min_fun(x, fx)
print(min_x, min)

