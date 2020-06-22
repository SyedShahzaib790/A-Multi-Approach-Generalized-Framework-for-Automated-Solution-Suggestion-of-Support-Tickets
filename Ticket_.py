from Sentence_ import *

class Ticket_:
    """
    A class which holds the attribute of a Neighboring Ticket
    """
    
    def __init__(self, params=None):
        
        self.number = None
        self.sysid = None
        self.date=None
        self.content = None
        self.resolution = None
        self.content_sents = None
        self.resolution_sents = None
        self.content_entities=None
        self.resolution_entities=None
        self.common_content_res_entities=None
        
        self.content_common_entities_sentences=None
        self.resolution_common_entities_sentences=None
        
        self.common_entities_sentences_sim_matrix=None
        
        
        if params is not None:
            for key in params:
                setattr(self, key, params[key])
                
    def set_params(self, params=None):
        
        if params is not None:
            for key in params:
                setattr(self, key, params[key])
                
    def split_sentences_all(self, split_sent_func, do_preprocessing=True, tokenizer_func=None, split_content=True, split_res=True):
        
        if split_content:
            self.content_sents = split_sent_func(self.content.text)
            for index, sent in enumerate(self.content_sents):
                sent_obj = Sentence_({'text':sent})
                if do_preprocessing:
                    sent_obj.preprocess_text(tokenizer_func=tokenizer_func)
                self.content_sents[index] = sent_obj
        
        if split_res:
            self.resolution_sents = split_sent_func(self.resolution.text)
            for index, sent in enumerate(self.resolution_sents):
                sent_obj = Sentence_({'text':sent})
                if do_preprocessing:
                    sent_obj.preprocess_text(tokenizer_func=tokenizer_func)
                self.resolution_sents[index] = sent_obj
            
    def set_entities(self, content_entities, resolution_entities):
        
        self.content_entities = content_entities
        self.resolution_entities = resolution_entities
        
        
    def compute_common_entities(self):
        
        if (self.content_entities is None) or (self.resolution_entities is None):
            raise ValueError("Error: Content/Resolution Entities have not been Generated Yet!")
        
        self.common_content_res_entities = set([ce[0] for ce in self.content_entities]).intersection(set([re[0] for re in self.resolution_entities]))
    
    def generate_common_sents_on_entities_all(self):
        
        if self.common_content_res_entities is None:
            raise ValueError("Error: Common Entities have not been Generated Yet!")
        
        self.content_common_entities_sentences=[sent for sent in self.content_sents if any(entity in sent.text for entity in self.common_content_res_entities)]
        self.resolution_common_entities_sentences=[sent for sent in self.resolution_sents if any(entity in sent.text for entity in self.common_content_res_entities)]
        
        
    def compute_common_entities_sentences_sim_matrix(self, similarity_func):
        
        
        content_sent_emb = np.asarray([sent.text_emb for sent in self.content_common_entities_sentences])
        resolution_sent_emb = np.asarray([sent.text_emb for sent in self.resolution_common_entities_sentences])
        
        if (None in content_sent_emb) or (None in resolution_sent_emb):
            raise ValueError("Error: Sentence Embeddings have not been Generated Yet!")
        
        self.common_entities_sentences_sim_matrix = similarity_func(content_sent_emb, resolution_sent_emb)
        

