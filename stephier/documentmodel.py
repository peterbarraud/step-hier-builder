# build the step object hierarchy from a file handle

import re

from stephier.step_entities.edge_loop import EDGE_LOOP
from stephier.step_entities.vector import VECTOR
from stephier.step_entities.definitional_representation import DEFINITIONAL_REPRESENTATION
from stephier.step_entities.line import LINE
from stephier.step_entities.plane import PLANE
from stephier.step_entities.circle import CIRCLE
from stephier.step_entities.face_bound import FACE_BOUND
from stephier.step_entities.axis import AXIS
from stephier.step_entities.closed_shell import CLOSED_SHELL
from stephier.step_entities.direction import DIRECTION
from stephier.step_entities.face_outer_bound import FACE_OUTER_BOUND
from stephier.step_entities.cylindrical_surface import CYLINDRICAL_SURFACE
from stephier.step_entities.cartesian_point import CARTESIAN_POINT
from stephier.step_entities.oriented_edge import ORIENTED_EDGE
from stephier.step_entities.edge_curve import EDGE_CURVE
from stephier.step_entities.vertex_point import VERTEX_POINT
from stephier.step_entities.surface_curve import SURFACE_CURVE
from stephier.step_entities.geometric_representation_context import GEOMETRIC_REPRESENTATION_CONTEXT
from stephier.step_entities.pcurve import PCURVE
from stephier.step_entities.advanced_face import ADVANCED_FACE



# this is the main object that holds the entire hirarchy
# this is the gateway to the object hiearchy.
# It only makes sense to get to the objects and metadata in the hierarchy via this object
class Document:
    def __init__(self, step_file_handle):
        # pull the contents of the step file into a single variable
        step_data = step_file_handle.read().replace('\n', '')
        # lets create a dict (comprehension) that holds the id as key and entity data as value from the step file
        self._entity_data = {int(item[1]): item[0] for item in re.findall('(#(\d+).+?;)', step_data)}
        # we are going to start with CLOSED_SHELL so let's get that id from stepdata
        closed_shell_id = int(re.findall(r'#(\d+)\s*=\s*CLOSED_SHELL', step_data)[0])
        # dictionary of doc entities: key (entity id). value: Step Entity instance
        # we need this for the public methods:
        # get_element_by_id
        self.__entities_by_id = dict()
        # get_elements_by_name
        self.__entities_by_name = dict()

        self._create_object(closed_shell_id, None)

        # member vars

    def _create_object(self, entity_id, parent):
        # entity_data_item = self._entity_data[entity_id]
        entity_data_item = self._entity_data.get(entity_id, -1)
        # TODO: Replace following hack with a reflection solution
        # I'm going to use a dirty hack here but for now we don't know the different entities in a step file
        # so I'm going to have to use this hack to catch any that we haven't accounted for
        # later we'll use reflection to do instantiate classes dynamically
        entity_name = re.search('([_A-Z]+)', entity_data_item).groups()[0]
        step_entity = None
        if entity_name == "CLOSED_SHELL":
            step_entity = CLOSED_SHELL(entity_data_item, parent)
        elif entity_name == "EDGE_LOOP":
            step_entity = EDGE_LOOP(entity_data_item, parent)
        elif entity_name == "VECTOR":
            step_entity = VECTOR(entity_data_item, parent)
        elif entity_name == "DEFINITIONAL_REPRESENTATION":
            step_entity = DEFINITIONAL_REPRESENTATION(entity_data_item, parent)
        elif entity_name == "AXIS":
            step_entity = AXIS(entity_data_item, parent)
        elif entity_name == "SURFACE_CURVE":
            step_entity = SURFACE_CURVE(entity_data_item, parent)
        elif entity_name == "VERTEX_POINT":
            step_entity = VERTEX_POINT(entity_data_item, parent)
        elif entity_name == "GEOMETRIC_REPRESENTATION_CONTEXT":
            step_entity = GEOMETRIC_REPRESENTATION_CONTEXT(entity_data_item, parent)
        elif entity_name == "PCURVE":
            step_entity = PCURVE(entity_data_item, parent)
        elif entity_name == "FACE_BOUND":
            step_entity = FACE_BOUND(entity_data_item, parent)
        elif entity_name == "DIRECTION":
            step_entity = DIRECTION(entity_data_item, parent)
        elif entity_name == "CARTESIAN_POINT":
            step_entity = CARTESIAN_POINT(entity_data_item, parent)
        elif entity_name == "PLANE":
            step_entity = PLANE(entity_data_item, parent)
        elif entity_name == "EDGE_CURVE":
            step_entity = EDGE_CURVE(entity_data_item, parent)
        elif entity_name == "LINE":
            step_entity = LINE(entity_data_item, parent)
        elif entity_name == "ADVANCED_FACE":
            step_entity = ADVANCED_FACE(entity_data_item, parent)
        elif entity_name == "ORIENTED_EDGE":
            step_entity = ORIENTED_EDGE(entity_data_item, parent)
        elif entity_name == "FACE_OUTER_BOUND":
            step_entity = ORIENTED_EDGE(entity_data_item, parent)
        elif entity_name == "CIRCLE":
            step_entity = CIRCLE(entity_data_item, parent)
        elif entity_name == "CYLINDRICAL_SURFACE":
            step_entity = CYLINDRICAL_SURFACE(entity_data_item, parent)
        elif entity_name == "FACE_OUTER_BOUND":
            step_entity = FACE_OUTER_BOUND(entity_data_item, parent)
        else:
            print("heyyyyy!!!!: " + entity_name)
            # step_entity = StepEntity(entity_data_item, parent);

        # lets add the step_entity object to the id and name dicts
        self.__entities_by_id[step_entity.id] = step_entity
        entity_list = self.__entities_by_name.get(step_entity.name)
        if entity_list is None:
            entity_list = []
        entity_list.append(step_entity)
        self.__entities_by_name[step_entity.name] = entity_list
        if parent is not None:
            parent.children.append(step_entity);
        # to get the children, we need to get all #numerics besides the first (which is the current ID)
        children_ids = [int(item) for item in re.findall(r'#(\d+)', entity_data_item) if int(item) != entity_id]
        for child_id in children_ids:
            self._create_object(int(child_id), step_entity)
        return

    # public methods
    def getEntityById(self, id):
        return self.__entities_by_id[id]

    def getEntitiesByName(self, name):
        return self.__entities_by_name[name]

    # Helper method
    # Just used to find out the list of Entities.
    # We use this list to figure out the entity classes that we need
    def getEntitiesByNameDict(self):
        return self.__entities_by_name













def get_document_object(step_file_name: str):
    # Instead of the file handle let's take the file name (with full path).
    # TODO: Reject file if it is not a valid STEP file
    with open(step_file_name, 'r') as step_file_handle:
        document = Document(step_file_handle)
    return document
