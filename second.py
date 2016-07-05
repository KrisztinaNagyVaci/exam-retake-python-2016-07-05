# Create a function that takes a filename as parameter,
# it should count the words in the file and is should return it as a number
# if the file not exists or any other error occures return 0

def countWordsinFile(filename):
    try:
        f = open(filename)
        text = f.read()
        f.close()
        list_of_words = []
        list_of_words = text.split()
        return len(list_of_words)
    except:
        return 0

print(countWordsinFile('1.txt'))
