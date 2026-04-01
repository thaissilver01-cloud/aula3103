def ex1_contar_pares_while(inicio: int, fim: int) -> int:
    """Exercício 1: contar quantos números pares existem entre início e fim."""
    quantidade_pares = 0
    atual = inicio

    while atual <= fim:
        if atual % 2 == 0:
            quantidade_pares += 1
        atual += 1

    return quantidade_pares

print(ex1_contar_pares_while(1, 10)) # Deve imprimir 5 (2, 4, 6, 8, 10)