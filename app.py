from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def is_it_friday():
    today = datetime.datetime.now().strftime('%A')
    if today == 'Friday':
        return "It is friday !\n"
    else:
        return "It is not friday yet :(\n"

if __name__ == '__main__':
    app.run(port=5000)


#comment to test ruff
