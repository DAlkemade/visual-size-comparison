import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class BoundingBox:
    def __init__(self):
        pass

class Comparer:
    def __init__(self, objects_lookup: Dict[str, set], imgs_lookup: Dict[int, dict]):
        self.imgs_lookup: Dict[int, dict] = imgs_lookup
        self.objects_lookup = objects_lookup
        logger.info("Created Comparer")

    def compare(self, synset_1: str, synset_2: str) -> List[float]:
        cooccurences = self.objects_lookup[synset_1].intersection(self.objects_lookup[synset_2])
        relative_sizes: List[float] = list()
        for img_id in cooccurences:
            relative_sizes_on_img = self.compare_on_image(img_id, synset_1, synset_2)
            relative_sizes += relative_sizes_on_img
        return relative_sizes

    def get_image(self, image_id: int):
        return self.imgs_lookup[image_id]

    def compare_on_image(self, image_id: int, synset_1: str, synset_2: str) -> List[float]:
        img = self.get_image(image_id)
        max_sizes_1: List[int] = list()
        max_sizes_2: List[int] = list()
        #TODO might be better to first index all synsets for each img to avoid this loop
        for object in img['objects']:
            # TODO think about area vs max(width, height). The second seems to be more consistent with the linguistic bootstrapping
            if synset_1 in object['synsets']:
                max_sizes_1.append(max(object['w'], object['h']))
            if synset_2 in object['synsets']:
                max_sizes_2.append(max(object['w'], object['h']))

        relative_sizes: List[float] = list()
        for size_1 in max_sizes_1:
            for size_2 in max_sizes_2:
                relative_sizes.append(size_1/size_2)
        return relative_sizes


