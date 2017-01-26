# tutorial-sqlalchemy

```bash
$ pip install -r requirements.txt
```

```bash
$ python run.py
```

### configurar Alembic


```bash
$ alembic init alembic
```

```bash
$ alembic current
```

```bash
$ alembic history
```

```bash
$ alembic stamp head
```

```bash
$ alembic upgrade head
$ alembic upgrade +2
$ alembic upgrade ae10+2
$ alembic upgrade ae10+2 --sql > apply-later.sql
```

```bash
$ alembic downgrade base
$ alembic downgrade -1
```

```bash
$ alembic revision --autogenerate -m "Added account table"
```


### criar script de migração

