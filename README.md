


# 1) Getting started

```bash
git clone https://github.com/vinthara/press-fastapi
```

```bash
cd press-fastapi
```

Create `venv/` :

```bash
python3 -m venv venv
```

Activate the virutal environment for dependencies `venv` :

```bash
source venv/bin/activate
```

Install all the dependencies :

```bash
pip3 install -r requirements.txt 
```

You need to add .env in `press-fastapi/`

```
SQLALCHEMY_DATABASE_URL="URI"
SQLALCHEMY_DATABASE_TEST_URL="URI_TEST"
SECRET_KEY="run this command openssl rand -hex 32"
ALGORITHM="An algorithm"
```

You can now start the `app` :

```bash
uvicorn app.main:app --reload
```

# 2) How to use alembic

Alembic is useful for doing schema migration, when you need to add columns, alter columns, you can even do small data migration, like adding some rows to a table.

There is an `alembic.ini` file :

Which contains the following : 

```ini
[test]
script_location = alembic
prepend_sys_path = .
version_path_separator = os
env = test

[prod]
script_location = alembic
prepend_sys_path = .
version_path_separator = os
env = prod
```

Inside `alembic/env.py` :

There is the following added : 

```python
sqlalchemy_url = settings.sqlalchemy_database_test_url

if config.get_main_option("env") == "prod":
    sqlalchemy_url = settings.sqlalchemy_database_url

config.set_main_option("sqlalchemy.url", sqlalchemy_url)
```

This allow us to run alembic schema migration on the wanted database :

```bash
alembic -n test downgrade -1
```

```bash
alembic -n prod upgrade +1
```

