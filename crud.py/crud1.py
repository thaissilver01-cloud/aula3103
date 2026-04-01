from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from aula_repeticao import (
    executar_demos,
    exemplo_break_continue,
    exemplo_for_range_quadrados,
    exemplo_for_range_tabuada,
    exemplo_loops_aninhados_matriz_3x3,
    exemplo_while_contagem,
    exemplo_while_soma_ate_n,
    teoria_repeticao_resumo,
)

app = FastAPI(title="Tasks CRUD API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    done: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_id = 1


@app.get("/")
def health_check():
    return {"message": "API de tasks online Petros"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    global next_id

    task = Task(id=next_id, **payload.model_dump())
    tasks[next_id] = task
    next_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")

    data = task.model_dump()
    updates = payload.model_dump(exclude_unset=True)
    data.update(updates)

    updated_task = Task(**data)
    tasks[task_id] = updated_task
    return updated_task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task não encontrada")

    del tasks[task_id]


@app.get("/aula/repeticao/exemplos")
def exemplos_repeticao():
    return executar_demos()


@app.get("/aula/repeticao/teoria")
def teoria_repeticao():
    return teoria_repeticao_resumo()


@app.get("/aula/repeticao/while")
def exemplo_while(limite: int = 5, n_soma: int = 10):
    return {
        "contagem": exemplo_while_contagem(limite),
        "soma": exemplo_while_soma_ate_n(n_soma),
    }


@app.get("/aula/repeticao/for")
def exemplo_for(inicio: int = 1, fim: int = 5, numero_tabuada: int = 7):
    return {
        "quadrados": exemplo_for_range_quadrados(inicio, fim),
        "tabuada": exemplo_for_range_tabuada(numero_tabuada),
    }


@app.get("/aula/repeticao/controle-fluxo")
def exemplo_controle_fluxo():
    return {
        "matriz": exemplo_loops_aninhados_matriz_3x3(),
        "break_continue": exemplo_break_continue([5, -2, 9, 0, 12]),
    }


@app.get("/aula/repeticao/exercicios")
def listar_exercicios():
    return {
        "entrega": "Resolver funções TODO em aula_repeticao.py e abrir PR.",
        "itens": [
            "ex1_contar_pares_while",
            "ex2_somar_impares_for",
            "ex3_login_tentativas_while",
            "ex4_condicional_repeticao_fizzbuzz",
            "ex5_media_aprovacao",
        ],
    }