from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def generate_random_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    
    # Render the HTML template with the random number directly
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random Number Generator</title>
        </head>
        <body>
            <h1>Random Number Generator</h1>
            <p>Generated Random Number: {{ random_number }}</p>
        </body>
        </html>
    """, random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True)
