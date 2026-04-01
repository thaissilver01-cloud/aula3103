def ex5_media_aprovacao(notas: list[float]) -> dict[str, float | str]:
    if not notas:
        return {"media": 0.0, "staus": "Sem notas"}
    
    soma_notas = 0.0
    for nota in notas: 
        soma_notas += nota

    media = soma_notas / len(notas)

    # Motor de regras 
    if media >= 7:
        status = "Aprovado"
    elif media >= 5:
        status = "Recuperação"
    else: 
        status = "Reprovado"

    # Retorna uma estrutura de dados organizada
    return {
        "media": round(media, 2),
        "status": status
    }

#1. Lista de otas simulando as avaliacações de um aluno
notas_semestre = [8.5, 7.0, 6.0, 9.0]

#2. Executando a função e imprimindo o retorno diretamnte
resultado = ex5_media_aprovacao(notas_semestre)
print(resultado)