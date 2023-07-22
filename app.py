# app.py

from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

# A list of quotes. You can add more quotes here.
# quotes = [
#     "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
#     "The only way to do great work is to love what you do. - Steve Jobs",
#     "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
#     "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
#     "In three words I can sum up everything I've learned about life: It goes on. - Robert Frost",
# ]

def get_random_quote():
    response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")
    if response.status_code == 200:
        quote_data = response.json()
        return f"{quote_data['quoteText']} - {quote_data['quoteAuthor']}"
    return "Unable to fetch a quote at the moment."

@app.route('/')
def index():
    # random_quote = random.choice(quotes)
    random_quote = get_random_quote()
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
