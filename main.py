from flask import Flask, render_template,jsonify
from database import load_movie_from_db,load_movies_from_db
# add_application_to_db
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

# @app.route("/movie/<id>/apply", methods=['post'])
# def apply_movie(id):
#   data = request.form
#   movie = load_movie_from_db(id)
#   # add_application_to_db(id, data)
#   return render_template('application_submitted.html', 
#                          application=data,
#                          jobs=job)
@app.route("/about")
def about():
  return render_template("about.html")
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)