from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return """
        <html>
            <head>
                <title>Simple Python App</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 50px;
                        background-color: #f0f0f0;
                    }
                    h1 {
                        color: #333;
                    }
                </style>
            </head>
            <body>
                <h1>Hello, world from a very simple Python app!</h1>
            </body>
        </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0")
