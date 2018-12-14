# Flask-Prom

This will allow you to easily add Prometheus metrics to your Flask applications.

This extension instruments every flask route and exports the following metrics:

Histogram: <myapp_flask_request_latency_seconds> {'endpoint', 'method'}
Summary: <myapp_flask_request_count> {'endpoint','method','http_status'}

# Install

```
pip install flask_prom
```

# Usage


## 1. WSGI Add-On (Same Port)

For serving Prometheus metrics on the same port as your Flask application.

```
from flask import Flask
from flask_prom import monitor

app = Flask("myapp")

@app.route('/')
def hello():
    return 'Hello'

app.wsgi_app = monitor(app, path="/metrics")
app.run()
```

Then visit `localhost:8000/metrics` to see your metrics. They are served from the
same port as your application!

## 2. HTTP Server (Different Port)

For creating a separate HTTP server to serve prometheus metrics.

```
from flask import Flask
from flask_prom import monitor

app = Flask("myapp")

@app.route('/')
def hello():
    return 'Hello'

monitor(app, path="/metrics", http_server=True, port=9090, addr="127.0.0.1")
app.run()
```

Then visit `localhost:9090/metrics` to see your metrics.

# Credits

This python library was forked from https://github.com/sbarratt/flask-prometheus,
since it was no longer being maintained.

# License

[BSD-3](LICENSE)
