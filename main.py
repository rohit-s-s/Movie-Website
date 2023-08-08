from flask import Flask, render_template,jsonify
from database import load_movie_from_db,load_movies_from_db
app = Flask(__name__)

@app.route("/")
def hello_jovian():
  movie = load_movie_from_db()
  return render_template('index.html',movie=movie)
@app.route("/movie/<id>")
def show_movie(id):
    movie = load_movies_from_db(id)
    if movie is None:
        return jsonify({})
    else:
        return render_template('movie.html',movie=movie)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

