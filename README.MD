# Flask REST API template

## Project setup

Tested on `Windows 10` with `Python 3.10.4`. If any error occurs, [download](https://www.python.org/downloads/release/python-3104/) and run the project in this version.

```bash
git clone https://github.com/yoggys/flask-rest-api
cd flask-rest-api
pip install -r requirements.txt
python3 run.py
```

### Optional arguments

By default server run as `127.0.0.1:5000` in `production mode`.

```bash
usage: run.py [-h] [--host HOST] [--port PORT] [--dev]

options:
  -h, --help   show this help message and exit
  --host HOST  Host name
  --port PORT  Port number
  --dev        Run server in development mode
```

### Example

```bash
python3 run.py --dev --host localhost --port 8080
```

## Tests

```bash
python3 -m pytest ./tests/tests.py
```

### Output

```bash
================================================== test session starts ===================================================
platform win32 -- Python 3.10.11, pytest-7.3.1, pluggy-1.0.0
rootdir: ...\flask-rest-api\tests
plugins: asyncio-0.21.0
asyncio: mode=strict
collected 7 items

tests.py .......                                                                                                    [100%]

=================================================== 7 passed in 2.19s ====================================================
```

## Project structure

```bash
├── flask-rest-api
│   ├── core
│   │   ├── __init__.py
│   │   ├── setup.py
│   │   └── utils.py
│   ├── models
│   │   └── UserModel.py
│   ├── routes
│   │   └── UserRoute.py
│   ├── tests
│   │   └── tests.py
│   └── run.py
```

## API

### Users

Methods: `GET`, `POST`, `DELETE`

```bash
api/v1/users/ - Users list
```

Methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`

```bash
api/v1/users/\<int:user_id\> - User by id
```
