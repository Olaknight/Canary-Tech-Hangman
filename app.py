from flask import Flask, jsonify, render_template, redirect, url_for, make_response, session, request, flash
from resources.game import Game, GameHandler
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bees2geesRock'

@app.route('/')
def enter_game():
    return render_template('index.html')

@app.route('/new_game.html', methods=['GET'])
def start_new_game():
    if session.get('game'):
        del session['game']
    return redirect(url_for('play_game'))

@app.route('/hangman.html', methods=['POST', 'GET'])
def play_game():
    game = session.get('game')
    if not game or GameHandler().is_game_over(game):
        game = GameHandler().new_game()
        session['game'] = game
    if request.method == 'GET':
        return render_template('hangman.html', game=game)

    ch = request.form.get('character')
    if not GameHandler().enter_char(ch.lower(), game):
        flash('Wrong!')
    if GameHandler().level_passed(game):
        flash('You have passed this round')
        GameHandler().next_level(game)
    if GameHandler().is_game_over(game):
        return redirect(url_for('game_over'))
    session['game'] = game
    return render_template('hangman.html', game=game)

@app.route('/game_over.html', methods=['GET'])
def game_over():
    game = session.get('game')
    if not game:
        return redirect(url_for('play_game'))
    return render_template('game_over.html', game=game)



if __name__ == '__main__':
    app.run(port=5000, debug=True)