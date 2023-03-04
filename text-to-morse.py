

morse_dict = {
    "a" : "._",
    "b" : "_...",
    "c" : "_._.",
    "d" : "_..",
    "e" : ".",
    "f" : ".._.",
    "g" : "_ _.",
    "h" : "....",
    "i" : "..",
    "j" : "._ _ _",
    "k" : "_._",
    "l" : "._..",
    "m" : "_ _",
    "n" : "_.",
    "o" : "_ _ _",
    "p" : "._ _.",
    "q" : "_ _._",
    "r" : "._.",
    "s" : "...",
    "t" : "_",
    "u" : ".._",
    "v" : "..._",
    "w" : "._ _",
    "x" : "_.._",
    "y" : "_._ _",
    "z" : "_ _..",
    " " : " "
}

def main():
    text = input("Enter text to convert to morse code: ")
    for letter in text:
        if letter in morse_dict:
            print(morse_dict[letter.lower()], end="/")
    print()

if __name__ == '__main__':
    main()