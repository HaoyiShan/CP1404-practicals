import wikipedia


def search():
    title = input("Please input the title or search phrase:")
    if title == "":
        return False
    try:
        i = wikipedia.page(title, auto_suggest=False)
        print(i.title)
        print(i.summary)
        print(i.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(title, "does not match any pages. Try another query!")


print("Welcome！(enter blank input to finish)")
while search():
    print()

