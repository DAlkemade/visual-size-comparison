import json
from typing import Dict, List


def index_objects(img_objects_info: Dict[int, dict]) -> Dict[str, set]:
    """Create a dictionary to look up the image ids containing that object."""
    objects_lookup: Dict[str, set] = dict()
    for img_dict in img_objects_info.values():
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


def load_images_index(objects_path: str) -> Dict[int, dict]:
    """Load VG images lookup."""
    with open(objects_path, 'r') as f:
        images_list: list = json.load(f)
    assert type(images_list) is list
    images_lookup = dict()
    for image in images_list:
        images_lookup[image['image_id']] = image
    return images_lookup


# TODO create a dict with the keys being synsets and the values lists of image ids in which the objects occur. Then coocurrences can be found taking the intersection of dict[A] and dict[B]
