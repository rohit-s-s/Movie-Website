from sqlalchemy import create_engine, text
import os
my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
                       connect_args={
                        "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      })

def load_movie_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from movie_data"))
    movie = []
    for row in result.all():
      movie.append(row)
    return movie






def load_movies_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM movie_data WHERE id = :movie_id")
        result = conn.execute(query.bindparams(movie_id=id))
        row = result.fetchone()
        if row is not None:
            movie_dict = dict(row._asdict())
            return movie_dict
        else:
            return None





