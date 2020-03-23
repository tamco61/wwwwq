from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    return render_template('train.html', prof=prof)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/list_prof/<lst>')
def list_prof(lst):
    return render_template('index.html', lst=lst)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на марсе!'
    param['ready'] = 'True'
    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')