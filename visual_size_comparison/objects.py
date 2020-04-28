import json
from typing import Dict, List


def index_objects(img_objects_info: list) -> Dict[str, set]:
    """Create a dictionary to look up the image ids containing that object."""
    objects_lookup: Dict[str, set] = dict()
    for img_dict in img_objects_info:
        img_id: int = img_dict['image_id']
        objects = img_dict['objects']
        for object in objects:
            synsets: List[str] = object['synsets']
            for synset in synsets:
                try:
                    objects_lookup[synset].add(img_id)
                except KeyError:
                    objects_lookup[synset] = {img_id}

    return objects_lookup



def load_objects(objects_path: str) -> List[dict]:
    """Load VG objects."""
    with open(objects_path, 'r') as f:
        objects = json.load(f)
    return objects


def create_object_lookup(objects_path: str) -> Dict[str, list]:
    objects = load_objects(objects_path)
    return index_objects(objects)


#TODO create a dict with the keys being synsets and the values lists of image ids in which the objects occur. Then coocurrences can be found taking the intersection of dict[A] and dict[B]