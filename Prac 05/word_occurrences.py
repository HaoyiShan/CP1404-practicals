def main():
    Get_Text = input("Please enter the Text:")
    List_Text = Get_Text.split()
    words = {}
    max_len = 0
    for word in List_Text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        if len(word) > max_len:
            max_len = len(word)
    for i in words:
        print(i.ljust(max_len), ":", words[i])


main()
