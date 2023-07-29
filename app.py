from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            return "Please provide a valid URL."

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
                return render_template('results.html', headings=headings, url=url)
            else:
                return "Failed to fetch the webpage."
        except requests.exceptions.RequestException:
            return "Error occurred while fetching the webpage."

    return render_template('index.html')

if __name__ == '_main_':
    app.run(debug=True)