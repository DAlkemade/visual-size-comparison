import logging
import os
from datetime import datetime

from logging_setup_dla.logging import set_up_root_logger

from visual_size_comparison.objects import load_images_index

set_up_root_logger(f'VG_objects_{datetime.now().strftime("%d%m%Y%H%M%S")}', os.path.join(os.getcwd(), 'logs'))

logger = logging.getLogger(__name__)


def main():
    images = load_images_index('data/objects.json')
    count_person = 0
    count_region = 0
    for image in images.values():
        synsets_all = list()
        for object in image['objects']:

            synsets = object['synsets']
            synsets_all += synsets
        if 'people.n.01' in synsets_all:
            count_person += 1
        if 'region.n.01' in synsets_all:
            count_region += 1

    logger.info(f'person: {count_person} region: {count_region}')



if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Unhandled exception")
        raise
