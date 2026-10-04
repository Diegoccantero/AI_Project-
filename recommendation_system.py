import numpy as np

# Datos de prueba: Películas y características
movies = {
    "Pelicula A": [1, 0, 1, 0],
    "Pelicula B": [0, 1, 1, 0],
    "Pelicula C": [0, 0, 1, 1],
    "Pelicula D": [1, 1, 0, 0]
}

user_profile = [1, 0, 1, 0]

def recommend(user_profile, movies):
    scores = {}
    for movie, features in movies.items():
        scores[movie] = np.dot(user_profile, features)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print("--- Recomendaciones del Sistema ---")
    for movie, score in recommend(user_profile, movies):
        print(f"Película: {movie} | Afinidad: {score}")