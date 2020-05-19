from typing import List, Dict

from visual_size_comparison.compare import Comparer
from visual_size_comparison.objects import load_images_index, index_objects

import pandas as pd

class VisualConfig:
    def __init__(self, vg_objects, vg_objects_anchors):
        images = load_images_index(vg_objects)
        self.objects_lookup = index_objects(images)

        self.comparer: Comparer = Comparer(self.objects_lookup, images)

        test_objects_df = pd.read_csv(vg_objects_anchors)
        self.test_objects = list(test_objects_df.itertuples(index=False))
        self.entity_to_synsets: Dict[str, List[str]] = dict()
        self.fill_synset_mapping(list(self.objects_lookup.keys()))

    def fill_synset_mapping(self, synsets: List[str]):
        for synset in synsets:
            name_raw = synset.split('.')[0]
            try:
                self.entity_to_synsets[name_raw].append(synset)
            except KeyError:
                self.entity_to_synsets[name_raw] = [synset]