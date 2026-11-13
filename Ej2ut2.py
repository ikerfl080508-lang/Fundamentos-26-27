def a(x: int) -> None:
    print(x * 2)


def b(x: int) -> int:
    return x * 2

resultado_a = a(5)   # -> 10   (lo imprime la propia funcion)
resultado_b = b(5)

print(resultado_a)   # -> None   a() no devuelve nada
print(resultado_b)   # -> 10     b() SI devuelve, y por eso se puede reutilizar
print(b(5) + b(3))   # -> 16     esto con a() seria imposible