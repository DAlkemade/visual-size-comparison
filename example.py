import json
import logging
import os
import sys
from datetime import datetime

import numpy as np
from logging_setup_dla.logging import set_up_root_logger

from visual_size_comparison.compare import Comparer
from visual_size_comparison.objects import load_images_index, index_objects

import matplotlib.pyplot as plt
import pandas as pd

set_up_root_logger(f'VG_objects_{datetime.now().strftime("%d%m%Y%H%M%S")}', os.path.join(os.getcwd(), 'logs'))

logger = logging.getLogger(__name__)

METHOD = 'mean'

N = 20

def main():
    images = load_images_index('data/objects.json')
    with open('data/object_synsets.json') as f:
        name_to_synset = json.load(f)

    objects_lookup = index_objects(images, object_synsets=name_to_synset)

    all_synsets = set(name_to_synset.values())
    logger.info(f'objects_lookups.keys() - all_synsets {len(set(objects_lookup.keys()) - all_synsets)}')

    all_synsets = all_synsets.union(set(objects_lookup.keys()))


    logger.info(f'Number of imgs with a tree: {len(objects_lookup["tree.n.01"])}')

    comparer = Comparer(objects_lookup, images)
    tree_van_scales = comparer.compare('tree.n.01', 'van.n.05')
    logger.info(f'Number of tree_van_comparisons: {len(tree_van_scales)}')
    logger.info(f'Average scale of tree/van : {np.mean(tree_van_scales)}')

    #todo MIsmatch in sizes!!!!
    logger.info(f'Number of object synsets in images: {len(set(objects_lookup.keys()))} out of total {len(all_synsets)}')
    logger.info(f'Number of images: {len(images)}')
    counts = []
    never_occurs = set()
    for synset_name in all_synsets:
        try:
            v = len(objects_lookup[synset_name])
        except KeyError:
            never_occurs.add(synset_name)
            v = 0
        counts.append((synset_name, v))
    logger.info(f'Objects that never occur: {never_occurs}')

    counts = list(sorted(counts, key=lambda x: x[1], reverse=True))
    most_occurring = counts[:N]
    logger.info(f"{N} most occurring objects: {most_occurring}")

    # Histogram of counts
    _, values = zip(*counts)
    bins = np.linspace(0, 200, 201)
    logger.info(f"Bins: {bins}")
    bin_counts, _, _ = plt.hist(np.clip(values, bins[0], bins[-1]), bins=bins)
    plt.xlabel('# images an object occurs in')
    plt.show()
    logger.info(f'Number of objects that never occur {bin_counts[0]}')

    # Histogram of co-occurrence with most_occurring
    # most_occurring_img_sets = [objects_lookup[synset] for synset, _ in most_occurring]
    logger.info("Find co-occurrences")
    cooccurence_counts = []
    for k in objects_lookup.keys():
        count = 0
        img_set = objects_lookup[k]
        for synset_most, _ in most_occurring:
            if synset_most == k:
                continue # don't check cooccurrence with itself
            img_set_most = objects_lookup[synset_most]
            intersection = img_set.intersection(img_set_most)
            count += len(intersection)
        cooccurence_counts.append(count)

    bins = np.linspace(0, 200, 201)
    plt.hist(np.clip(cooccurence_counts, bins[0], bins[-1]), bins=bins)
    plt.xlabel(f'# co-occurrences with {N} most occurring objects')
    plt.show()

    test_objects = pd.read_csv('data/test_objects.csv')
    test_objects = list(test_objects.itertuples(index=False))
    results = []
    for object1 in test_objects:
        for object2 in test_objects:
            synset1 = object1.object
            synset2 = object2.object
            if synset1 == synset2:
                continue
            comp = comparer.compare(synset1, synset2)
            if METHOD == 'mean':
                res = np.mean(comp)
            else:
                raise ValueError('Unknown method')
            correct = (object1.size > object2.size) == (res > 1.)
            results.append(correct)

    logger.info(f'Fraction correct based on test suite: {np.mean(results)}')

    k = 10
    count = 0
    for v in cooccurence_counts:
        if v >= k:
            count += 1
    logger.info(f'fraction {count/len(values)} at least {k} co-occurrences')






if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Unhandled exception")
        raise
