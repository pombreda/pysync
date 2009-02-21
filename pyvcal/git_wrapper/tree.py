from pyvcal.resource import Resource

class Tree(Resource):
    """A versioned container of Files"""

    def __init__(self, tree_id, repo):
        # all we need is the hash and repo; we let gitpython do the rest
        super(Revision, self).__init__()
        self._tree_id = tree_id
        self._repo = repo

    def get_path(self):
        """Return the path to this tree in its container Repository"""
        raise NotImplementedError 
        
    def get_contents(self, recursive=True):
        """Return the contents of a tree as a list of Paths."""

        raise NotImplementedError 
        
    path = property(get_path)
    contents = property(get_contents)
