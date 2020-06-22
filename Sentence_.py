from functions import *

class Sentence_:
    """
    A class which holds the attributes of the single sentence 
    """
    
    def __init__(self, params=None):
        
        self.text=None
        self.text_tokens=None
        self.text_entities=None
        self.text_emb=None
        self.text_actions=None
        self.text_imperative=None
        self.text_allen_result=None
        self.text_depparse=None
        
        if params is not None:
            for key in params:
                setattr(self, key, params[key])
                
    def preprocess_text(self, pipeline=None, tokenizer_func=None):
        
        if pipeline is None:
            pipeline = [to_lower_func, punctuation_removal_func, remove_spaces_func]
        
        for func in pipeline:
            self.text = func(self.text)
            
        if tokenizer_func is not None:
            self.tokenize_sentence(tokenizer_func)
            
        
    def tokenize_sentence(self, tokenize_func):
        if self.text_tokens is None:
            self.text_tokens = tokenize_func(self.text)

        
    def compute_embedding(self, compute_sentence_embedding_func, model):
        if self.text_tokens is None:
            raise ValueError("Error: Text Tokens have not been generated")
            
        self.text_emb = compute_sentence_embedding_func(self.text_tokens, model)

    
    def compute_entities(self, compute_entities_func):
        if self.text_entities is None:
            self.text_entities = compute_entities_func(self.text)

    def compute_text_actions(self, action_extractor_func):
        
        self.text_actions = list(itertools.chain(*(action_extractor_func(self.text))))

