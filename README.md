# World of Games

Welcome to the World of Games! In this application, you can find many cool games to play. 

## How to play

To start playing, you will need to run the `main.py`. This will greet you and prompt you to enter your name. Then, you will be able to select a game to play from the following options:

1. Guess Game - In this game, you will guess a number and see if you chose like the computer.
2. Memory Game - In this game, a sequence of numbers will appear for 1 second, and you have to guess it back.
3. Currency Roulette - In this game, you will try and guess the value of a random amount of USD in ILS.

You will also be able to choose the difficulty level for the game, from 1 to 5.

After playing the game, you will be asked if you want to play again. If you choose to play again, you will be able to select a new game and difficulty level.

## Other features

The `Live` class also keeps track of the user's score, using the `add_score` method from the `Score` class. This method updates the score based on whether the user won the game and the difficulty level of the game.

## Endpoints

The following endpoints are available in this application:

### `GET /scores/<user_id>`

Retrieves the users score with the specified ID.