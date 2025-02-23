from extract import get_weather
from load import load_data


def main():
    get_weather()

    load_data()

if __name__ == "__main__":
    main()