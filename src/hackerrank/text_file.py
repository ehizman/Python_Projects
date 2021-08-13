if __name__ == "__main__":
    with open("second_text.txt", 'a+', encoding='utf-8') as f:
        f.write("This is my third linen e ekhehj ejline of text\n")
        f.write("This is the next line of text\n")
        f.write("This is the final ine of text\n")
        f.seek(0)
        for line in f:
            print(line, end=" ")