from brain_games.engine import engine
from brain_games.games import progression


def main():
    engine(progression.progress, progression.DESC)


if __name__ == "__main__":
    main()
