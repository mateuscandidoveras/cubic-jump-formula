# Cubic Jump Formula / Fórmula de Salto Entre Cubos

Este projeto apresenta uma fórmula matemática que permite calcular o próximo cubo perfeito a partir de um cubo perfeito conhecido e sua raiz cúbica, sem recalcular do zero.

This project introduces a mathematical formula to calculate the next perfect cube based on a known cube and its root, using only arithmetic operations.

## 📐 A Fórmula / The Formula

Dado um valor `n`:

- Cubo atual / Current cube: `n³`
- Próximo cubo perfeito / Next perfect cube:  
  (n + 1)^3 = n^3 + (3 * n) * (n + 1) + 1

## 💻 Código / Code

```python
def raiz_cubica():
    n = int(input("Digite a raiz cúbica (n): "))
    y = n**3
    z = y + (n * 3) * (n + 1) + 1
    py = (n * 2) ** 3

    print(f"{n}³ = {y}")
    print(f"Próximo cubo perfeito: {z}")
    print(f"Cálculo: {y} + (3*{n})*({n}+1) + 1 = {z}")
    print(f"{y} * 8 = {py}, que é (2*{n})³")
```

## ✨ Inovação / Innovation

- Reutiliza o cubo anterior com crescimento estruturado.
- Pode ser expandida para saltos maiores como (n + k)^3.
- Útil para ensino, algoritmos e computação simbólica.

## 📊 Visualização / Visualization

![Gráfico de comparação entre cubos](cubos_formula_grafico.png)

## 📂 Licença / License

MIT
