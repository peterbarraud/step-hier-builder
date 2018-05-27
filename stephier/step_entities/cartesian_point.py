# https://www.steptools.com/stds/stp_aim/html/t_cartesian_point.html
import re
from stephier.step_entities.cartesian_coordinates import CARTESIAN_COORDINATES


class CARTESIAN_POINT(CARTESIAN_COORDINATES):
    def __init__(self, entity_data_item, parent):
        CARTESIAN_COORDINATES.__init__(self, entity_data_item, parent)
