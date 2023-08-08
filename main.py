from flask import Flask, render_template
import requests
import os
my_secret = os.environ['api_key']
app = Flask(__name__)

@app.route("/")
def hello_jovian():
    return render_template('index.html')

@app.route('/movie/<id>')
def movie_details(id):
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={my_secret}'

    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return render_template('movie_details.html', movie_data=movie_data)
    else:
        return 'Error fetching data from TMDb API.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

  
