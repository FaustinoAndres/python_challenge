import requests


def main():
    """
    Level 2:
        Recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
        Hint:
            - Use the hints. They are helpful, most of the times.
            - Investigate the data given to you.
            - Avoid looking for spoilers.

    """
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"

    with open('files/file_level_2.txt', 'r') as file:
        content = file.read()

    message = [char for char in content if char.isalpha()]
    message = ''.join(message)

    url = url.replace('ocr', message)
    print(url)



if __name__ == '__main__':

    main()