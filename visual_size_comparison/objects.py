import json
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


def index_objects(img_objects_info: Dict[int, dict], object_synsets: Dict[str, str] = None) -> Dict[str, set]:
    """Create a dictionary to look up the image ids containing that object."""
    objects_lookup: Dict[str, set] = dict()
    object_ids = set()
    all_names: set = set()
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

            names: List[str] = object['names']
            if len(names) > 0:
                object_ids.add(object['object_id'])

            for name in names:
                all_names.add(name)
    if object_synsets is not None:
        no_synset: set = all_names - set(object_synsets.keys())
        synsets_from_names = set()
        for name in all_names:
            try:
                s = object_synsets[name]
                synsets_from_names.add(s)
            except KeyError:
                continue
        new_synset_not_in_synsets_list: set = synsets_from_names - set(objects_lookup.keys())
        logger.info(f'No synset: {len(no_synset)}')
        logger.info(f'Maps to synset: {len(all_names)-len(no_synset)}')
        logger.info(f'Not in synses list (likely data entry error): {len(new_synset_not_in_synsets_list)}')
    logger.info(f'Number of object names: {len(all_names)}')
    logger.info(f'Number of unique object ids: {len(object_ids)}')
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
