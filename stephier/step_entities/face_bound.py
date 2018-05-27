import re

from stephier.step_entities.step_entity import Step_Entity


class FACE_BOUND(Step_Entity):
    def __init__(self, entity_data_item, parent):
        Step_Entity.__init__(self, entity_data_item, parent)

    @property
    def orientation(self):
        print((self).params)
        pass
