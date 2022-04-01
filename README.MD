# Flask REST API template

## Project setup
Tested on `Windows 10` with `Python 3.10.4`, if any error is encountered please [download](https://www.python.org/downloads/release/python-3104/) and run project using this version.

```bash
git clone https://github.com/yoggys/flask-rest-api
cd flask-rest-api
pip install -r requirements.txt
python run.py 
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

Example:
```bash 
python run.py --dev --host localhost --port 8080
```
