# 🚀 Primeiro Projeto de REST API em Python

Este repositório marca **meu primeiro projeto de REST API**, desenvolvido durante meus estudos de **Python** e **FastAPI**. O objetivo é consolidar conceitos fundamentais como:

* Estruturação de uma API REST
* Criação e ativação de ambiente virtual (venv)
* Gerenciamento de dependências
* Integração com banco de dados usando **SQLAlchemy + SQLite**
* Controle de versões do banco de dados com **Alembic**
* Autenticação utilizando **JWT (JSON Web Tokens)**

> 📌 Projeto com foco **educacional**, acompanhando uma aula introdutória e servindo como base para projetos futuros.

---

## 🐍 Criando o Ambiente Virtual

```bash
python -m venv venv
```


## ▶️ Ativando o Ambiente Virtual (VS Code)

- Ativando o ambiente no POWERSHELL
```bash
.\venv\Scripts\Activate.ps1
```

- Ativando o ambiente no CMD
```bash
venv\Scripts\activate
```

> ⚠️ Sempre confirme se o ambiente virtual está ativo antes de instalar bibliotecas.



## 📦 Gerenciamento de Dependências

### Sempre que instalar uma nova biblioteca

Atualize o arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### Instalando dependências do projeto

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando a API

```bash
uvicorn main:app --reload
```

Após iniciar, a API ficará disponível em:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Documentação automática (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🗄️ Banco de Dados

O projeto utiliza:

* **SQLAlchemy** como ORM
* **SQLite** como banco de dados

Ideal para projetos iniciais e aprendizado.

---

## 🔄 Alembic (Migrations)

### Instalação

```bash
pip install alembic
```

### Inicialização

```bash
alembic init alembic
```

### Configuração

No arquivo `alembic.ini`, ajuste a URL do banco:

```text
sqlalchemy.url = sqlite:///banco.db
```

Essa configuração deve ser a mesma definida no `models.py`:

```python
db = create_engine("sqlite:///banco.db")
```

---

## 🧱 Processo de Migração de Banco de Dados

### Criar uma nova migration

```bash
alembic revision --autogenerate -m "mensagem_da_alteracao"
```

### Aplicar as migrations

```bash
alembic upgrade head
```

---

## 🔐 JWT – JSON Web Tokens

Para **decodificar ou inspecionar tokens JWT**, utilize:

👉 [https://www.jwt.io/](https://www.jwt.io/)

---

## 🛠️ Correção de Conflito de Bibliotecas (bcrypt / passlib)

Com o ambiente virtual **ativado**:

```bash
pip uninstall bcrypt passlib
```

Em seguida:

```bash
pip install "passlib[bcrypt]" bcrypt==4.0.1
```

---

## 🎯 Considerações Finais

Este projeto representa um **marco inicial** na minha jornada com desenvolvimento backend e APIs REST. Ele servirá como base para evoluções futuras, incluindo:

* Novos endpoints
* Autenticação mais robusta
* Testes automatizados
* Integração com outros bancos de dados

🚀 Em constante evolução!
