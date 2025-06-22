def raiz_cubica():
    n = int(input("Digite a raiz cúbica (n): "))
    y = n**3
    z = y + (n * 3) * (n + 1) + 1
    py = (n * 2) ** 3

    print(f"{n}³ = {y}")
    print(f"Próximo cubo perfeito: {z}")
    print(f"Cálculo: {y} + (3*{n})*({n}+1) + 1 = {z}")
    print(f"{y} * 8 = {py}, que é (2*{n})³")

# Chamada do programa
raiz_cubica()
