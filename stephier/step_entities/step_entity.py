import re

class Step_Entity:
    def __init__(self, entity_data_item, parent):
        # member vars
        self.__entity_data_item = entity_data_item
        # id of the entity as defined in the STEP document
        self.__id = int(re.search('#(\d+)', entity_data_item).groups()[0])
        # name of the entity as defined in the STEP document
        self.__entity_name = re.search('([_A-Z]+)', entity_data_item).groups()[0]
        # parent object
        self.__parent = parent
        # list of children objects
        self.__children = []
        self.__param_str = re.search('\((.+?)\);$', entity_data_item).groups()[0]

    # entity name as defined in the STEP file (eg; CLOSED_SHELL, ADVANCED_FACE, CARTESIAN_POINT
    @property
    def entity_name(self):
        return self.__entity_name

    @property
    def id(self):
        return self.__id

    # name is defined in the entity defintion
    # usually the first param in the param str
    @property
    def name(self):
        return re.match("\\'(.*?)\'",self.__param_str).groups()[0]

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    # I seem not to be able to access member variables of the parent hence I created a public params property
    @property
    def param_str(self):
        return self.__param_str

    def add_child(self, child):
        self.__children.append(child)
