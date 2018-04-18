from lib.frasa_preposisional import init
from lib.Tagger import trainModel
from lib.Tagger import wordTagger
from sys import argv

def remove_punc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    my_str = text
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

def get_prep(text):
    return init(remove_punc(text))

def main_prog():
    param = argv[1:]

    if len(param) == 2:
        if param[0] == '-fp':
            print('Frasa Preposional: ')
            print(get_prep(param[1]))
        elif param[0] == '-tag':
            print(wordTagger([param[1]]))
        else:
            print('Command not found, try --help')
        return

    try:
        if (param[0] == '--help'):
            print('-fp "<string>": Menampilkan list frasa preposional dalam kalimat')
            print('-tag "<word>": Menampilkan kelas suatu kata')
            print()
            print('--help: Menampilkan bantuan')
            print('--train: Melatih model corpus')
        elif param[0] == '-train':
            print('Training model...')
            trainModel()
        else:
            print('Command not found, try --help')
    except:
        print('Error: Invalid argument(s), try --help')

main_prog()