word = str(input())
new_word = word.replace("A", '').replace("O", '').replace("Y", '').replace("E", '').replace("U", '').replace("I", '')\
    .replace("a", '').replace("o", '').replace("y", '').replace("e", '').replace("u", '').replace("i", '').lower()

new_word = '.'.join(new_word)
new_word = '.' + new_word

print(new_word)

