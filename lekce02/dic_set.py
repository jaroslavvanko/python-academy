films = {
    "name": "Shawshank redemtion",
    "rating": 87,
    "year": 1984,
    "director": "frank darabont"}
films["staring"] = ["Tim Robbinson","Morgan Freeman"]
films["budget"] = 200
print(films)
del films["budget"]
print(films)
film = { "DRAMA" : films}
print(film)
print("We can currently offer")
print(list(film.keys()))
choice = input("What genre are you interest in")
print("Here we go")
print(film[choice])
films.clear()
print("Database was erased")
print(films)
print(film)

