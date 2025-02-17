# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AQaITi0YMwP5TavD8n5t_OpAgALKw8Yu
"""

import random

# List of words to choose from
word_list = ['python', 'hangman', 'programming', 'challenge', 'ateeq']

def select_random_word(word_list):
    """Select a random word from the word list."""
    return random.choice(word_list)

def display_current_progress(word, guessed_letters):
    """Display the current progress of the word being guessed."""
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print('Current word: ' + ' '.join(display_word))

def play_hangman():
    """Play a game of Hangman."""
    word = select_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        display_current_progress(word, guessed_letters)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You have guessed the word '{word}' correctly.")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()

pip install yfinance

import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Ticker', 'Shares', 'Average Cost'])

    def add_stock(self, ticker, shares, average_cost):
        if ticker in self.portfolio['Ticker'].values:
            print(f"{ticker} is already in the portfolio.")
            return
        new_stock = pd.DataFrame([[ticker, shares, average_cost]], columns=['Ticker', 'Shares', 'Average Cost'])
        self.portfolio = pd.concat([self.portfolio, new_stock], ignore_index=True)
        print(f"Added {shares} shares of {ticker} at an average cost of {average_cost}.")

    def remove_stock(self, ticker):
        if ticker not in self.portfolio['Ticker'].values:
            print(f"{ticker} is not in the portfolio.")
            return
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
        print(f"Removed {ticker} from the portfolio.")

    def get_portfolio_value(self):
        total_value = 0
        for index, row in self.portfolio.iterrows():
            ticker = row['Ticker'];
            shares = row['Shares']
            current_price = yf.Ticker(ticker).history(period='1d')['Close'].iloc[-1]
            total_value += shares * current_price
        return total_value

    def show_portfolio(self):
        portfolio_value = self.get_portfolio_value()
        data = []
        for index, row in self.portfolio.iterrows():
            ticker = row['Ticker']
            shares = row['Shares']
            average_cost = row['Average Cost']
            current_price = yf.Ticker(ticker).history(period='1d')['Close'].iloc[-1]
            current_value = shares * current_price
            data.append([ticker, shares, average_cost, current_price, current_value])

        portfolio_df = pd.DataFrame(data, columns=['Ticker', 'Shares', 'Average Cost', 'Current Price', 'Current Value'])
        print(portfolio_df)
        print(f"\nTotal Portfolio Value: ${portfolio_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            average_cost = float(input("Enter average cost per share: "))
            portfolio.add_stock(ticker, shares, average_cost)
        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ").upper()
            portfolio.remove_stock(ticker)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")