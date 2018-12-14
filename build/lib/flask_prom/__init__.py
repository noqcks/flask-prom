import time
from flask import request
from prometheus_client import Counter, Histogram
from prometheus_client import start_http_server, make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware

FLASK_REQUEST_ENDPOINT_SENTINEL = "-"

def monitor(app, path="/metrics", http_server=False, port=9090, addr=""):
  FLASK_REQUEST_COUNT = Counter(
    "{}_flask_request_count".format(app.name),
    "{} - Flask Request Count".format(app.name),
    ["method", "endpoint", "http_status"],
  )
  FLASK_REQUEST_LATENCY = Histogram(
    "{}_flask_request_latency_seconds".format(app.name),
    "{} - Flask Request Latency".format(app.name),
    ["method", "endpoint"],
  )

  def before_request():
    request.start_time = time.time()

  def after_request(response):
    request_latency = time.time() - request.start_time
    FLASK_REQUEST_LATENCY.labels(request.method, request.path).observe(
      request_latency
    )
    FLASK_REQUEST_COUNT.labels(
      request.method, request.path, response.status_code
    ).inc()

    return response

  app.before_request(before_request)
  app.after_request(after_request)

  if http_server:
    start_http_server(port, addr)
  else:
    prometheus_app = make_wsgi_app()
    return DispatcherMiddleware(app.wsgi_app, {path: prometheus_app})
