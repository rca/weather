"""
JSON Weather Parsing
"""
import requests

URL = "https://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=b1b15e88fa797225412429c1c50c122a1"


def main():
    # 1. Write a function which gets the contents of the URL above & print the "main" and "description" values of the first 20 weather objects in the response list.


    # 2. Extend the function above to only list out the weather items where "main" = "Snow"

    # 3. Write another function that to output a list of objects with key being
    #    the "main" field and the value being the number of times that field
    #    exists in the first 20 items

   print(f"hello world, URL={URL}!")


if __name__ == "__main__":
    main()
