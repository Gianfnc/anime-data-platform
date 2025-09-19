# 🚀 Plataforma de Dados de Animes

![CI Pipeline](https://github.com/SEU_USUARIO/anime-data-platform/actions/workflows/ci.yml/badge.svg)
[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

**Status do Projeto: Concluído** ✅

Uma plataforma de dados end-to-end que automatiza a coleta, armazenamento e exposição de dados de animes através de uma API RESTful, construída com as melhores práticas de engenharia de software e DevOps.

---

### 📖 Visão Geral do Projeto

Este projeto consiste em duas partes principais:

1.  **Pipeline de ETL (Engenharia de Dados):** Um script Python que extrai dados da API pública [Jikan](https://jikan.moe/), realiza a transformação e limpeza dos dados, e os carrega em um banco de dados PostgreSQL.
2.  **API RESTful (Desenvolvimento Backend):** Uma API de alta performance construída com FastAPI que serve os dados armazenados, permitindo consultas e o uso por outras aplicações.

Todo o ambiente é orquestrado e containerizado com Docker, e a qualidade do código é garantida por testes automatizados com Pytest, executados em um pipeline de CI/CD com GitHub Actions.

---

### 🏛️ Diagrama da Arquitetura

*(Recomendação: Crie um diagrama simples usando ferramentas como [diagrams.net](https://app.diagrams.net/) ou [Excalidraw](https://excalidraw.com/) e adicione a imagem aqui. Isso impressiona muito!)*

```
[API Pública Jikan] -> [Script de ETL Python] -> [Banco de Dados PostgreSQL (Docker)] <- [API FastAPI (Docker)] -> [Usuário Final]
```

---

### 🛠️ Stack Tecnológica

| Área                 | Tecnologias                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Backend** | Python 3.13, FastAPI, Pydantic                                            |
| **Banco de Dados** | PostgreSQL, SQLAlchemy                                                    |
| **Testes** | Pytest                                                                    |
| **DevOps** | Docker, Docker Compose, GitHub Actions (CI/CD)                            |

---

### ✨ Funcionalidades

- **Pipeline de ETL:** Coleta automatizada dos animes mais populares.
- **API RESTful:**
  - `GET /animes`: Retorna a lista de todos os animes.
  - `GET /animes/{id}`: Retorna um anime específico por ID.
- **Testes Automatizados:** Testes unitários e de integração para garantir a confiabilidade da API.
- **Pipeline de CI/CD:** Automação dos testes a cada `push`, garantindo a qualidade contínua do código.
- **Containerização:** Aplicação e banco de dados totalmente containerizados, garantindo portabilidade e facilidade de execução.

---

### 🏁 Como Executar Localmente

**Pré-requisitos:**
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/products/docker-desktop/)

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/anime-data-platform.git](https://github.com/SEU_USUARIO/anime-data-platform.git)
    cd anime-data-platform
    ```

2.  **Inicie os containers com Docker Compose:**
    Este comando irá construir a imagem da API e iniciar o container do banco de dados.
    ```bash
    docker-compose up -d
    ```
    
3.  **Crie as tabelas e popule o banco de dados:**
    *(Nota: Estes passos precisarão ser executados dentro do container da aplicação)*
    ```bash
    # Crie as tabelas
    docker-compose exec app python create_db.py
    
    # Popule o banco com os dados da API Jikan
    docker-compose exec app python load_data.py
    ```

4.  **Acesse a API:**
    * A API estará disponível em `http://127.0.0.1:8000`.
    * A documentação interativa (Swagger UI) está em `http://127.0.0.1:8000/docs`.

---

### 👤 Autor

**Gian Cordeiro**

* **LinkedIn:** [https://www.linkedin.com/in/gianfn/](https://www.linkedin.com/in/gianfn/)
* **GitHub:** [https://github.com/raincloudz](https://github.com/raincloudz)
