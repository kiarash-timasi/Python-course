from math import fabs, cos

def cal_cos(n):
    accuracy = 0.0001

    n = n * (3.142 / 180.0)

    x1 = 1

    cosx = x1

    cosval = cos(n)
    i = 1

    denominator = 2 * i * (2 * i - 1)
    x1 = -x1 * n * n / denominator
    cosx = cosx + x1
    i = i + 1
    while accuracy <= fabs(cosval - cosx):
        denominator = 2 * i * (2 * i - 1)
        x1 = -x1 * n * n / denominator
        cosx = cosx + x1
        i = i + 1

    print('Cos (x) is:', round(cosx))

if __name__ == '__main__':
    n = int(input(' Enter x:'))
    cal_cos(n)


