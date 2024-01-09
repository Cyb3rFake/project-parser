from app import app
from flask import render_template, request
import requests
from bs4 import BeautifulSoup


@app.route('/')
def index():

    return app.render_template('index.html')


@app.route('/parse', methods=['POST'])
def parse():
    # Заготовка для парсера контента сайта
    url = app.request.form['url']

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = []
    # здесь типа должен быть код самого парсера, результат которого сохраняется в список headlines
    # который выводиться в шаблон results.html
        
    return app.render_template('results.html', headlines=headlines)