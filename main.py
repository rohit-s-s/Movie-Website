from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
from data import movie_data
from fetch_data import fetch_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("view", name=name))
    else:
        message = request.args.get("message",None)
        return render_template("home.html",message=message)

@app.route('/view')
def view():
    name = request.args.get("name", None)
    # url = f'https://api.themoviedb.org/3/movie/popular?api_key=3d1cb94d909aab088231f5af899dffdc'
        # response = requests.get(url, timeout=30)
        # response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        # movie_data = response.json()
    results = movie_data['results']
    result = fetch_data(movie_name=name,results=results)
    if result:
        # Print the movie data for debugging
        return render_template("view.html", message=result)
    else:
        return redirect(url_for("home", message="Movie not found"))
   

if __name__ == '__main__':
    app.run(debug=True)

