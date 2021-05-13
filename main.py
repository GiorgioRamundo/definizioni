from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def read_file():
    file = open("definizioni.tsv","r")
    defn = {}
    for line in file:
        data = line.split("\t")
        defn[data[0]] = data[1].replace('\n','')
    file.close()
    return defn


def preprocessing(_defn):
    res = {}
    for d in _defn:
        tokens = word_tokenize(_defn[d])
        res[d] = set(lemmatizer.lemmatize(w) for w in tokens if not w in stop_words)
    print(res)
    return res


def similarity(d, _d):
    min_seq = min(len(d),len(_d))
    return (len(d & _d)/min_seq)

_defn = read_file()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
defn = preprocessing(_defn)
sim = {}
for d in defn:
    for _d in defn:
        if d != _d:
            sim[(d,_d)]=similarity(defn[d],defn[_d])

print(sim)

elementi = {}
elementi['concreti'] = ['building','molecule']
elementi['astratti'] = ['freedom','compassion']
elementi['specifici'] = ['molecule','compassion']
elementi['generici'] = ['building','freedom']
categorie = ['concreti','astratti','specifici','generici']
somma = 0
for c in categorie:
    for _c in categorie:
        if c != _c:
            for e in elementi[c]:
                for _e in elementi[_c]:
                    if e != _e:
                        somma = somma + sim[(e,_e)]
            print('similarity between {} and {}: {}'.format(c,_c,somma / 4))
            somma = 0






