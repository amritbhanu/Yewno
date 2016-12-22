from __future__ import print_function, division

__author__ = 'amrit'

from gensim import utils
from Preprocess import *
import unicodedata
from random import shuffle
from gensim.models.doc2vec import TaggedDocument
sys.dont_write_bytecode = True

## Preprocessing and Tagging
class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename

    def to_array(self):
        self.sentences = []
        with utils.smart_open(self.filename) as fin:
            for line in fin:
                data=line.split('>>>')[0].strip()
                data=process(data, string_lower, punctuate_preproc,
                        numeric_isolation, stopwords, stemming, word_len_less, str_len_less)
                data= unicodedata.normalize('NFKD', data).encode('ascii', 'ignore')
                self.sentences.append(TaggedDocument(data.split(), ['%s' % line.split('>>>')[1].strip()]))
        return self.sentences

    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences