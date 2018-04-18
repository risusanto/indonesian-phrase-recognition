from lib.CrfTagger import CRFTagger

def trainModel():
    jumSample = 500000
    namaFile = "data/Indonesian_Manually_Tagged_Corpus.tsv"

    with open(namaFile, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    pasangan = []
    allPasangan = []

    for line in lines[: min(jumSample, len(lines) - 1)]:
        if line == '':
            allPasangan.append(pasangan)
            pasangan = []
        else:
            kata, tag = line.split('\t')
            p = (kata, tag)
            pasangan.append(p)

    ct = CRFTagger()
    ct.train(allPasangan, 'models/all_indo_man_tag_corpus_model.crf.tagger')

def wordTagger(data):
    ct = CRFTagger()
    ct.set_model_file('models/all_indo_man_tag_corpus_model.crf.tagger')
    return ct.tag(data)


