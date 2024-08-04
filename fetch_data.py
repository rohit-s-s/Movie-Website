def fetch_data(movie_name: str,results:dict) -> str:
    for objects in results:
        if movie_name.lower().replace(" ", "") == objects["title"].lower().replace(
            " ", ""
        ):
            return objects
    return {}
