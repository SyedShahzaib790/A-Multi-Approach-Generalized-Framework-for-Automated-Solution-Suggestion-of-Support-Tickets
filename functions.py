""" ============= Preprocessing Functions ================ """

from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
stemmer = PorterStemmer()

""" Lemmatize the given Input String """
lemmatize_func = lambda x: lem.lemmatize(x,'v')
lemmatize_string_func = lambda x: ' '.join([lemmatize_func(a) for a in x.split()])

""" Stem the given Input String """
stemmer_func = lambda x: stemmer.stem(x)


""" Other Preprocessing Functions """
import string
import re
import numpy as np
import spacy
import pandas as pd


nlp = spacy.load('en_core_web_lg')



""" Punctution Removal """
punc_reg_exp = "["+('|').join([ "\\"+p for p in list(string.punctuation.replace(',','')) ])+"]"
punctuation_removal_func = lambda x: re.sub(punc_reg_exp, ' ', x)

""" Remove Extra Spaces """
remove_spaces_func = lambda x: re.sub('\s\s+',' ', x).strip()

""" Remove Empty from list """
remove_empty_from_list_func = lambda x: np.delete(np.asarray(x), np.where(np.asarray(x)=='')).tolist() if type(x)==list else x

""" Convert into LowerCase"""
to_lower_func = lambda x: x.lower()

""" Remove Tags """
remove_tags_func= lambda x: re.sub("&lt;/?.*?&gt;","",text)

""" Tokenization """
tokenize_on_space_func = lambda x: x.split()
tokenize_via_spacy_func = lambda x: [token.text for token in nlp(str(x))]

""" Split Sentences """

""" -- Via SpaCy --"""
sent_reg_exp = re.compile(r'\x1b[^m]*m')
split_sent_via_spacy_func = lambda x: [sent_reg_exp.sub('', sent.text).strip() for sent in nlp(re.sub('\\n','. ', x)).sents]


""" Flatten the list of lists """
import itertools
flatten_list_func=lambda x: list(itertools.chain(*x))


""" Compute Embeddings from Tokens """
import numpy as np
compute_token_emb_mean_func = lambda tokens, model: np.mean(model[tokens], axis=0) if len(tokens)>0 else []

""" ============= Calculating Similarity from Embeddings ================ """

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

get_CosineSim_func = lambda test, train: [] if (len(test) < 1) or (len(train) < 1) else cosine_similarity(np.matrix(test), np.matrix(train)) 

def jaccard_similarity(query, document, tokenize=True):
    
    if tokenize:
        query = tokenize_via_spacy_func(query)
        document = tokenize_via_spacy_func(document)
    
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)


def get_spacy_tokens(sent):
    if sent.strip() == '':
        return pd.DataFrame(columns=['text','tag','pos','dep','parent', 'parent_pos'])
    
    struct = []
    for token in nlp(sent):
        struct.append([token.text, token.tag_ , token.pos_, token.dep_, token.head.text, token.head.pos_])
    df = pd.DataFrame(struct, columns=['text','tag','pos','dep','parent', 'parent_pos'])
    df.index = df.text.values
    return df

""" Set Any Obj Attribute Value """
def setattr_obj_list(obj_list, attr_name, attr_value=None):
    for i in range(len(obj_list)):
        setattr(obj_list[i], attr_name, attr_value)
