class film:
    def __init__(self, name_original="", name_russian="", rating_imdb="", time=0, age_restriction=0, description="", type_="", genres=[], poster_url=""):
        self.name_original = name_original,
        self.name_russian = name_russian,
        self.rating_imdb = rating_imdb,
        self.time = time,
        self.age_restriction = age_restriction,
        self.description = description,
        self.type = type_,
        self.genres = genres
        self.poster_url = poster_url

    def print_film(self):
        film_output = ""
        film_output += f"Название: {self.name_original[0]} ({self.name_russian[0]})\n"
        film_output += f"Рейтинг на IMDb: {self.rating_imdb[0]}\n"
        film_output += f"Время: {self.time[0]} мин.\n"
        film_output += f"Возраст: {self.age_restriction[0]}+.\n"
        film_output += f"Тип: {self.type[0]}\n"
        film_output += "Жанр: "

        for i in range(len(self.genres)):
            if i != len(self.genres)-1:
                film_output += f"{self.genres[i]}, "
            else:
                film_output += f"{self.genres[i]}\n"

        film_output += f"Описание: {self.description[0]}"

        print(film_output)