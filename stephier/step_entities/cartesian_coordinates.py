# base class for any co-ordinate based class (e.g. cartesian point)
import re
from stephier.step_entities.step_entity import Step_Entity

# We've created a separate coordinates class for any object that might require them (POINT, DIRECTION)
class CARTESIAN_COORDINATES(Step_Entity):
    def __init__(self, entity_data_item, parent):
        Step_Entity.__init__(self, entity_data_item, parent)
        co_or_params = re.search("\((.+?)\)", self.param_str).groups()[0].split(',')
        self.__x = co_or_params[0]
        self.__y = co_or_params[1]
        self.__z = co_or_params[2]

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z
