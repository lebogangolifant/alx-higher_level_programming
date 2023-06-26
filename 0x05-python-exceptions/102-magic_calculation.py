def magic_calculation(a, b):
    result = 0

    for index in range(1, 4):
        try:
            if index > a:
                raise Exception("Too far")
            result += (a ** b) / index
        except:
            result = b + a
            break

    return result
