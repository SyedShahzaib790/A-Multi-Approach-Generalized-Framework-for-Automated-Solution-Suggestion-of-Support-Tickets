class Token_:
    """ A class which holds the attribute details of a single token"""
    
    def __init__(self, params=None):
        
        self.token=None
        self.token_emb=None
        
        if params is not None:
            for key in params:
                setattr(self, key, params[key])
        
    def get_embedding(self, model):
        return model[self.token]

                                 

