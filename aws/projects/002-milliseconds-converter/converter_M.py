def conv_mil(num):
    h,m,s = 3600000, 60000, 1000

    num2 = int(num)
    numh = num2 // h
    numm = (num2 % h) // m
    nums = (num2 % m) // s

    result = {numh : "hour/s", numm : "minute/s", nums : "second/s"}
    if num2 < 1000:
        return f"Just {num} milliseconds"
    else:
        rest=""
        for i, j in result.items():
            if i > 0:
                res= f"{i} {j} "
                rest += res
        return rest