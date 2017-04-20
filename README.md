# tutorial-sqlalchemy

[![Coverage Status](https://coveralls.io/repos/github/arthuralvim/tutorial-sqlalchemy/badge.svg?branch=master)](https://coveralls.io/github/arthuralvim/tutorial-sqlalchemy?branch=master)

[![Build Status](https://travis-ci.org/arthuralvim/tutorial-sqlalchemy.svg?branch=master)](https://travis-ci.org/arthuralvim/tutorial-sqlalchemy)

### DEPENDÊNCIAS

```bash
$ make requirements
```

### ALEMBIC


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


### PEP8

```bash
$ make pep8
```

### TESTES

```bash
$ make test
```

```bash
$ make testx
```

```bash
$ make test.collect
```

```bash
$ make coverage
```

```bash
$ make coverage.html
```
