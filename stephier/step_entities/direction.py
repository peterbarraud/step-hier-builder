import re
from stephier.step_entities.cartesian_coordinates import  CARTESIAN_COORDINATES


class DIRECTION(CARTESIAN_COORDINATES):
    def __init__(self, entity_data_item, parent):
        CARTESIAN_COORDINATES.__init__(self, entity_data_item, parent)

    @property
    def dir_type(self):
        return re.search("'(.+?)'", self.params).groups()[0]
