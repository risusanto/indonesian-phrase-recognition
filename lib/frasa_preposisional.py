from lib.Tagger import wordTagger
all_prep = []

def check(data):
    exception_words = [
        'dalam','antara','ke','akan','terhadap','dengan',
        'berkat','tentang','hingga','sampai','untuk','buat',
        'guna'
    ]
    if data[1] == 'IN':
        return True
    for word in exception_words:
        if data[0] == word:
            return True
    return False

def wordParser(data):
     for i in range(len(data)):
         if check(data[i]):
             all_prep.append(i)

def gath_phrase(prep,data):
    all_phrase = []
    for i in range(len(prep)):
        word = []
        idx = prep[i]

        try:
            if(data[idx + 2][1] == 'VB'):
                word.append(data[idx][0])
                word.append(data[idx+1][0])
            elif data[idx+1][1] == 'PR':
                word.append(data[idx][0])
                word.append(data[idx+1][0])
            else:
                word.append(data[idx][0])
                word.append(data[idx+1][0])
                word.append(data[idx + 2][0])
        except:
            pass
        word_join = ' '.join(word)
        all_phrase.append(word_join)
    return all_phrase

def init(text):
    text_casefolded = text.lower()
    token = text_casefolded.split()
    word_tagged = wordTagger(token)
    wordParser(word_tagged)
    frasa = gath_phrase(all_prep,word_tagged)
    return frasa

