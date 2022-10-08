""" 
File name: file-ops.py
Show how to perform file operations.
""" 

def readfile(file_path):
    """
    Read a text file and display its content. 
    :param file_path: path of the file to read
    :type file_path: string
    """
    # Read the file.
    with (open(file_path)) as read_file:
        file_content = read_file.read()
    # Display file content.
    print("\n*****Executing readfile*****\n")
    print("*****Available fruits*****")
    print(file_content)
    # Display partial content.
    print("*****Some available fruits*****")
    print(file_content[:20])

def word_occurence(word, file_path):
    """
    Find the occurrence of a word in a file.
    :param word: word to search for occurrence
    :type word: str
    :param file_path: path of the file whose content to search
    :type file_path: str
    """
    file = open(file_path)
    file_content = file.read()
    occurrence = file_content.count(word)
    print("\n*****Executing word_occurence*****")
    print("The occurrence of the word: " + "\"" + word + "\"" + " is " + str(occurrence))


def writefile(r_file, w_file):
    """
    Create a text file and write into it the content of the passed file.
    Display the content of the created file. 
    :param r_file: path of the file to read
    :type r_file: string
    :param w_file: path of the file to write
    :type w_file: string
    """
    # Read the file.
    with (open(r_file, "r")) as read_file:
        r_file_content = read_file.read()
    
    # Create a new file and write into it
    # 97 characters read from the previous file.    
    with (open(w_file, "w")) as write_file:
        write_file.write(r_file_content[:97])
    
    # Open the newly created file and read its content.
    with (open(w_file, "r")) as read_file:
        r_file_content = read_file.read()
        
    # Display the file content.
    print("\n*****Executing writefile*****\n")
    print("*****File content*****")
    print(r_file_content)
    
def appendfile(word, w_file):
    """
    Append a word to an existing file.
    :param word: word to append
    :type word: string
    :param w_file: path of the file to append the word
    :type w_file: string
    """
    # Open the file and append the word.
    with (open(w_file, "a")) as write_file:
        write_file.write("\n" + word)
    
     # Open the updated file and read its content.
    with (open(w_file, "r")) as read_file:
        r_file_content = read_file.read()
        
    # Display the file content.
    print("\n*****Executing writefile*****\n")
    print("*****File content*****")
    print(r_file_content)
    
    
def main():
    readfile("files/fruits.txt")
    word_occurence("spider", "files/spider.txt")
    writefile("files/spider.txt", "files/mini-spider.txt")
    appendfile("plums", "files/fruits.txt")
    
if __name__ == "__main__":
    main()
