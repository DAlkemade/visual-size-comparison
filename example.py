import logging
import os
from datetime import datetime

import numpy as np

from logging_setup_dla.logging import set_up_root_logger

from visual_size_comparison.compare import Comparer
from visual_size_comparison.objects import load_images_index, index_objects

set_up_root_logger(f'VG_objects_{datetime.now().strftime("%d%m%Y%H%M%S")}', os.path.join(os.getcwd(), 'logs'))

logger = logging.getLogger(__name__)


def main():
    objects = load_images_index('data/objects.json')
    objects_lookup = index_objects(objects)
    logger.info(f'Number of imgs with a tree: {len(objects_lookup["tree.n.01"])}')

    comparer = Comparer(objects_lookup, objects)
    tree_van_scales = comparer.compare('tree.n.01', 'van.n.05')
    logger.info(f'Number of tree_van_comparisons: {len(tree_van_scales)}')
    logger.info(f'Average scale of tree/van : {np.mean(tree_van_scales)}')


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Unhandled exception")
        raise
