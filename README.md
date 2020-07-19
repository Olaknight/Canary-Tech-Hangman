# Hangman Game - Web application

##### Simple web application for playing Hangman, created with HTML, CSS and Flask framework

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a simple web application that allows its users to play the popular word-guessing game, Hangman. The
puzzles consists over 40, 000 words of the english language. A very simple user interface is also available, so
as to make user interaction intuitive.

Please note: In order to make the testing of this application logic deterministic, the result of each puzzle is displayed on the last
paragraph of the hint.


## Technologies
Project is created with:
* Python 3
* Flask version: 1.1.1
* HTML/CSS

## Setup
To run this project, make sure you have python 3 installed, then:

*Activate the virtual environment and install the dependencies from the requirements.txt file

```
$ cd ../hangman_game/venv/Scripts
$ activate
$(venv) ../../
$ (venv) pip install -r requirements.txt
```

*Spin up a development server
```
$ (venv) python app.py
```

*This spins up a development server running on http://127.0.0.1:5000/
Enter http://127.0.0.1:5000/ on your preferred web browser and enjoy!
