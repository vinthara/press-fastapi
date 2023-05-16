# 0) Tree overview

```bash
tree -L 2 -I __pycache__ -I venv/
```

```bash
.
├── alembic
│   ├── env.py
│   ├── migration
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 210bb53de308_add_is_active.py
│       ├── 83ad6d6f77c4_create_user_table.py
│       ├── 87acc7a1e86f_create_employee_week_calendar_table.py
│       ├── 93e3cb2b3fcf_add_press_details_data.py
│       └── ea6b75090bef_add_employee_press_employee_role.py
├── alembic.ini
├── app
│   ├── config.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── routers
│   │   ├── auth.py
│   │   └── employee.py
│   ├── schemas.py
│   ├── tests
│   │   ├── conftest.py
│   │   ├── create_employee_test.py
│   │   └── __init__.py
│   └── utils.py
├── press.db
├── press.service
├── press-test.db
├── README.md
└── requirements.txt
```


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

