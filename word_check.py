import string

def load_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        return set(words)

    except FileNotFoundError:
        print("File not found.")
        return set()


def find_occurrence(input_string: str, word_set: set):
    for elem in word_set:
        if str(elem).lower() in str(input_string).lower():
            return True
    return False


if __name__ == '__main__':
    test = "hit123"
    print(find_occurrence(test, load_words_from_file("QuackGen\\bad-words-mini.txt")))
    