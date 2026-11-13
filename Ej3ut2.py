def mayor(a: float, b: float) -> float:
    if a > b:
        return a
    return b

print(mayor(3, 9))     # -> 9
print(mayor(-2, -7))   # -> -2
print(mayor(4, 4))     # -> 4