# Kevin Chen
# 10/13/17
# This program can figure out a file's lines, words, and characters


def open_file():
    """
    This function will open the sample text file
    :return: this file's lines
    """

    myfile = open("sample.txt", "r")

    print(myfile)

    list_of_file_contents = myFile.readlines()

    print(list_of_file_contents)

    return list_of_file_contents


def main():

    numline = 0
    numword = 0
    numchar = 0
    list_of_file_contents = open_file()
    for line in list_of_file_contents:
        # create a list for words of file
        wordlist = line.split()
        numline += 1
        numword += len(wordlist)  # get length of wordslist list
        numchar += len(line)  # get length of line on each iteration will be number of characters

    print("lines:", numline)
    print("words:", numword)
    print("characters:", numchar)

main()
