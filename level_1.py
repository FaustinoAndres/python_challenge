def main():
    """
    Resolver http://www.pythonchallenge.com/pc/def/0.html
    Hint: try to change the URL address.
    """
    url = "http://www.pythonchallenge.com/pc/def/0.html"
    number = 2**38

    url = url.replace('0', str(number))

    print(url)

if __name__ == "__main__":
    main()
