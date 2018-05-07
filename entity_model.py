#
"""
entity_model.py

main description for how a data entity should behave.
will define the base types for the data structures.
"""

# reserve this for the implementation.
#import kwargv; # Might remove this. as it should be independent.
import pickle;
import sys;

class model_base:
    """
    main definition for the data containment mechanism.
    (primary goal is to define some storage mechanisms);
    """
    pass;

    __slots__=[
        "name",
        "source",
        "fields" # I might suggest using this as a dict - but who knows.
    ]

    def _expand_(string):
        """
        take an instance string and load it as an instance of model_base
        (or a derivative of model base)
        """
        pass;
        return pickle.loads(string);

    def _reduce_(self):
        """
        return a pickleable representation of an instance of model_base.
        this will help with data persistance.
        """
        return pickle.dumps(self);    

    def _store_(self, path=None):
        """
        store self as a pickled object in
        the file at the end of path.
        """
        # reduce and store a copy of self.
        pass;
        if path is not None:
            with open(path,'wb') as pickle_jar:
                pickle.dump(self,pickle_jar);

    def _loads_(path = None):
        """
        instantiate an object at the end of path.
        """
        # load and expand an instance.
        n = None;
        if path is not None:
            with open(path,'rb') as pickle_jar:
                n = pickle.load(pickle_jar)
        return n;

    def __init__(self):
        pass;
