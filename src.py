from __future__ import print_function, division

__author__ = 'amrit'

from gensim.models import Doc2Vec
from LabeledLineSentence import LabeledLineSentence
from Preprocess import *

sys.dont_write_bytecode = False

def most_similar(sentences=None, model=None,input=None):
    max = -float('inf')
    number = None
    for i, x in enumerate(sentences.to_array()):
        sim_score = model.n_similarity(input.split(), x.words)
        if sim_score >= max:
            max = sim_score
            number = i
    return number

def train_doc2vec(sentences=None):
    model = Doc2Vec(min_count=1, window=10, size=100, sample=1e-4, negative=5, workers=8)
    model.build_vocab(sentences.to_array())
    for epoch in range(10):
        model.train(sentences.sentences_perm())

    return model

def print_output(sentences=None,number=None,input=None):
    print("Input string: " + input)
    # a) It belongs to document number:
    print("a) Document No: %s" % (number + 1))
    # b) The author for this incomplete part:
    print("b) Author Name: " + " ".join(sentences.to_array()[number].tags))
    print()
    # c) The further part of this document:
    print("c) Document it belongs to:\n" + " ".join(sentences.to_array()[number].words))
    print()

if __name__ == '__main__':

    inputs=['chippewa escobar','trondheim trondheim bergen','notabl sign ninth argentina fire rock']


    sentences = LabeledLineSentence('dataset/file')

    ## Doc2vec Model training
    model=train_doc2vec(sentences)

    for input in inputs:
        input = process(input, string_lower, punctuate_preproc,
                        numeric_isolation, stopwords, stemming, word_len_less, str_len_less)
        try:
            ## Input prediction with model, cosine similarity
            number=most_similar(sentences,model,input)

            ## Print Output
            print_output(sentences,number,input)
        except:
            print("Wrong String Input: "+input+'\n')

