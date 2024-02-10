from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    return render_template('training.html', title="Тренировки в полете", prof=prof.lower())


@app.route('/list_prof/<list>')
def lis(list):
    return render_template('list_prof.html', title="Список профессий", ol_ul=list.lower())


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
