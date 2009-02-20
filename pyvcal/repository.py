class Repository(object):
    """A container for codelines"""
    def __init__(self, **kwargs):
        super(Repository, self).__init__()
    
    def get_uri(self):
        """Return the URI of the repository"""
        raise NotImplementedError
        
    def get_branches(self):
        """Return the branches available in the repository"""
        raise NotImplementedError 
        
    def get_revisions(self):
        """Return the Revision objects available in this repository"""
        raise NotImplementedError 
    
    uri = property(get_uri)
    branches = property(get_branches)
    revisions = property(get_revisions)
    
    @classmethod
    def create(cls,**kwargs):
        """Create a new Repository and return it."""
        raise NotImplementedError
