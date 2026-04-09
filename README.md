# Nerzilus

Aplicacao Flask para login, criacao de conta, upload de imagens e feed simples.

## Requisitos

- Python 3.11+
- `pip`

## Como rodar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python main.py
```

## Deploy

O projeto esta preparado para executar com Gunicorn usando:

```bash
gunicorn wsgi:application
```

Defina estas variaveis no ambiente de producao:

- `SECRET_KEY`
- `DATABASE_URL`
- `UPLOAD_FOLDER` se quiser sobrescrever o padrao

## GitHub

Arquivos locais como `.venv`, `.idea`, `instance/` e caches Python estao ignorados no Git.
