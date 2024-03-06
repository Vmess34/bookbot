def wcount(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict[1]

def lcount(text):
    letters = {}
    lower = text.lower()
    for letter in lower:
        if letter < 'a' or letter > 'z':
            continue
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    letterlist = sorted(letters.items(), key=sort_on, reverse=True)
    print("Letterlist")
    print(letterlist)
    return letterlist

def report(name, words, letters):
    print("--- Begin report of " + name + " ---")
    print(str(words) + " words found in the document\n")
    for i in letters:
        print("Letter " + i[0]+ " was found " + str(i[1]) + " times")
    print("--- End Report ---")
        

def get_book(path):
     with open(path) as f:
        return f.read()
     
def main():
    bookPath = "./books/frankenstein.txt"
    data = get_book(bookPath)
    num_words = wcount(data)
    num_letters = lcount(data)
    
    #print Stuff
    # print("Word Count: ")
    # print(num_words)
    # print("Letter Count: ")
    # print(num_letters)

    report(bookPath, num_words, num_letters)

main()