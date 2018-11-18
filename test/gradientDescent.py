def calculate(d, start, epsilon, minStep):
    x = start
    step = 2*minStep

    while(abs(step) > minStep):
        y = d(x)
        step = epsilon * y
        x = x - step

    return x
