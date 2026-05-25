from flask import Blueprint, render_template, request, redirect, url_for
from app.models.game import Game 

tarefa_controller = Blueprint('games', __name__)

@tarefa_controller.route('/')
def index():
    all_games = Game.list_all()
    return render_template('index.html', games=all_games)

@tarefa_controller.route('/add', methods=['POST'])
def add_game():
    title = request.form.get('title')
    genre = request.form.get('genre')
    platform = request.form.get('platform')
    
    if title: 
        Game.add(title, genre, platform)
    return redirect(url_for('games.index'))