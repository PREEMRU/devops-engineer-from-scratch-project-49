from brain_games.engine import engine
from brain_games.games import even


def main():
    engine(even.is_even, even.DESC)


if __name__ == "__main__":
    main()
