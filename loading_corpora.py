from corus import load_corpora
import tqdm
import wget


url = 'http://opencorpora.org/files/export/annot/annot.opcorpora.xml.byfile.zip'
wget.download(url)
path = 'annot.opcorpora.xml.byfile.zip'
records = load_corpora(path)

with open('pos_data.txt', 'w', encoding='utf8') as f:
    for rec in tqdm.tqdm(records):
        for par in rec.pars:
            for sent in par.sents:
                for token in sent.tokens:
                    f.write(f'{token.text} {token.forms[0].grams[0]}\n')