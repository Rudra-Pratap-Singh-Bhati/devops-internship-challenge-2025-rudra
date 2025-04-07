from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Rudra!"

@app.route("/compute")
def compute():
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
    result = fib(10000)
    return f"Fibonacci computed: {result}"
