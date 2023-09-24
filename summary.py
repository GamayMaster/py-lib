
def pow(n):
    return n**2

def sqrt(n):
    return n**(1/2)

def sum(data):
    if len(data) == 0:
        return None
    sum = 0
    for l in data:
        sum += l
    return sum

def average(data):
    if len(data) == 0:
        return None
    return (sum(data) / len(data))

# Two cases:
# 1) even
# 2) odd
def median(data):
    if len(data) == 0:
        return None
    data.sort()
    l = len(data)
    n = (l % 2)
    med = 0
    if n == 0: # even number
        i = (l // 2)
        med += data[i]
        i -= 1
        med += data[i]
        med = med / 2
    elif n == 1: # odd number
        i = (l // 2)
        med += data[i]
        med += 1
        med = med / 2
    return med

def mode(data):
    if len(data) == 0:
        return None

    element_count = {}

    for item in data:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    
    # return element_count

    max_count = max(element_count.values())
    mode = [key for key, value in element_count.items() if value == max_count]
    return mode

def variance(data):
    if len(data) == 0:
        return None
    data.sort()
    ss = []

    x = average(data)
    n = len(data) - 1

    for d in data:
        ss.append(pow((d-x)))

    return (sum(ss) / n)

def standard_deviation(data):
    return sqrt(variance(data))
