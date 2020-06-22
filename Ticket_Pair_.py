class Ticket_Pair_:
    """
    This class holds a pair of ticket and their relating information
    """

    def __init__(self, params=None):
        
        self.ticket_1=None
        self.ticket_2=None
        self.content_similarity_score=None
        self.resolution_similarity_score=None
        
        if params is not None:
            for key in params:
                setattr(self, key, params[key])