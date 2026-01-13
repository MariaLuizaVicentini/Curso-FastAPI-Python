# CURSO

AULA: https://www.youtube.com/watch?v=GmigfELFbn4

----

# CRIAR AMBIENTE

```
python -m venv venv
```

---

# ATIVANDO O AMBIENTE CRIADO

```
venv\Scripts\activate
```

---

# INSTALANDO AS DEPENDENCIAS DO PROJETO

```
pip install -r requirements.txt
```
----

# RODANDO O SCRIPT 

```
uvicorn main:app --reload
```
----

# SQL ALCHEMY + SQLITE



----

# Alembic

```
pip instal alembic
```

```
alembic init alembic
```

Editar no alembic.ini:

sqlalchemy.url = sqlite:///banco.db

Conforme definido no models.py
--> cria conexao com banco de dados
db = create_engine("sqlite:///banco.db")


---

# PROCESSO DE MIGRAÇÃO DE BANCO DE DADOS 

```
alembic revision --autogenerate - "mensagem_da_alteracao"
```


```
alembic upgrade head
```