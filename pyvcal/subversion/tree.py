from resource import Resource
from cStringIO import StringIO
import mimetypes
import os

class Tree(Resource):
    """ A versioned container of Files - that is, it represents a 
    directory or tree in the Repository """

    def get_path(self):
        """ Return the path to this tree in its container Repository """
        raise NotImplementedError 



    def get_contents(self, recursive=True):
        return get_data(recursive)

    def get_data(self, recursive=True):
        """ Return the contents of a tree as a list of Paths """
        ##  raise NotImplementedError 
        self.dir_paths = []

        if self._path == '':
            abs_path = self._branch_path
        else:
            abs_path = os.path.join(self._branch_path, self._path)

        file_names = _file_list(abs_path, self._ra_api, self._revnum)

        for item in file_names:
            full_file_path = os.path.join(self._branch_path,
                                          self._path,
                                          item)

            branch_node_path = os.path.join(self._path, item)
            # Actually appending the path to the list 
            # TODO: add a Path object not a single path
            self.dir_paths.append(branch_node_path)

        return self.dir_paths



    def _file_list(path, ra_api, revnum=None):
        """ Return a list of strings representing the contents of a given path """
        if revnum is None:
            revnum = ra_api.get_latest_revnum()

        path_level_info = ra_api.get_dir(path, revnum)

        return path_level_info[0].keys

    def _is_tree(self):
        """ Overrides the method from parent (Resource) """
        return True

    def type(self):
        return 'directory'
        
    path = property(get_path)
    contents = property(get_contents)




