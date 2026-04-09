# 📌 Nerzilus — FakePinterest

Uma aplicação web inspirada no Pinterest, construída com Flask. Permite que usuários criem contas, façam login, publiquem fotos e naveguem por um feed de imagens.

---

## 🚀 Funcionalidades

- ✅ Cadastro e autenticação de usuários (login/logout)
- ✅ Upload de fotos no perfil
- ✅ Feed com todas as fotos publicadas
- ✅ Senhas criptografadas com Bcrypt
- ✅ Proteção de rotas com Flask-Login
- ✅ Banco de dados SQLite com SQLAlchemy

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3.14 | Linguagem principal |
| Flask | Framework web |
| Flask-SQLAlchemy | ORM para banco de dados |
| Flask-Login | Gerenciamento de sessões |
| Flask-Bcrypt | Criptografia de senhas |
| Flask-WTF / WTForms | Formulários com validação |
| SQLite | Banco de dados local |

---

## 📁 Estrutura do Projeto

```
FlaskProject/
│
├── main.py                  # Ponto de entrada da aplicação
├── criar_banco.py           # Script para criar o banco de dados
│
├── Nerzilus/
│   ├── __init__.py          # Configuração e inicialização do app
│   ├── models.py            # Modelos do banco (Usuario, Foto)
│   ├── routes.py            # Rotas da aplicação
│   ├── forms.py             # Formulários (login, cadastro, foto)
│   │
│   ├── static/
│   │   ├── css/             # Estilos
│   │   └── fotos_posts/     # Fotos enviadas pelos usuários
│   │
│   └── templates/
│       ├── homepage.html    # Página de login
│       ├── criarconta.html  # Página de cadastro
│       ├── perfil.html      # Página de perfil do usuário
│       └── feed.html        # Feed de fotos
```

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/nerzilus.git
cd nerzilus
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install flask flask-sqlalchemy flask-login flask-bcrypt flask-wtf email-validator
```

### 4. Crie o banco de dados
```bash
python criar_banco.py
```

### 5. Rode a aplicação
```bash
python main.py
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 🗄️ Modelos do Banco de Dados

### Usuario
| Campo | Tipo | Descrição |
|---|---|---|
| id | Integer | Chave primária |
| username | String(80) | Nome de usuário único |
| email | String(80) | E-mail único |
| senha | String(80) | Senha criptografada |

### Foto
| Campo | Tipo | Descrição |
|---|---|---|
| id | Integer | Chave primária |
| imagem | String(80) | Nome do arquivo |
| data_criacao | DateTime | Data de upload |
| id_usuario | Integer | FK para Usuario |

---

## 🔐 Rotas Disponíveis

| Método | Rota | Descrição |
|---|---|---|
| GET/POST | `/` | Página de login |
| GET/POST | `/criarconta` | Cadastro de novo usuário |
| GET/POST | `/perfil/<id>` | Perfil do usuário (protegida) |
| GET | `/feed` | Feed de fotos (protegida) |
| GET | `/logout` | Encerrar sessão |

---

## 📌 Observações

- As fotos enviadas são salvas em `Nerzilus/static/fotos_posts/`
- O banco de dados SQLite é gerado localmente em `comunidade.db`
- A `SECRET_KEY` deve ser substituída por uma variável de ambiente em produção

---

## 👤 Autor

Desenvolvido por **Kelle** — projeto de aprendizado com Flask.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais.
