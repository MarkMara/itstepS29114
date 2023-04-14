result = []
def divider(a, b):
    if a < b:
        raise ValueError("")
    if b > 100:
        raise IndexError("")
    return a/b

data = {(10, 2): 2, (2, 5): 5, ("123", 4): 4, (18, 0): 0, ((), 15): 15, (8, 4): 4}

for key in data:
    try:
        res = divider(key[0], key[1])
        result.append(res)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"Exception: {e}")

print(result)