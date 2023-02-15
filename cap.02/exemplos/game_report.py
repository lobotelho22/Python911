import json

# file = open("video_games.json", "r")


# video_games = json.load(file)
# file.close()

def main():
    try:
        with open("video_games.json", "r") as file:
            video_games = json.load(file)

    except FileNotFoundError as exc:
        print("arquivo não existente")
        print(exc)

    except json.JSONDecodeError as exc:
        print("arquivo não existente")
        print(exc)

    all_consoles = set()
    all_genres = set()

    for game in video_games:
        all_consoles.add(game["Release"]["Console"])
        genres = (game["Metadata"]["Genres"]).split(',')
        for genre in genres:
            all_genres.add(genre)

    print(f"All Consoles: {all_consoles}")
    print(f"All Genres: {all_genres}")


if __name__ == "__main__":
    main()
