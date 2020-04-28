import logging
import os
from datetime import datetime

from logging_setup_dla.logging import set_up_root_logger

from visual_size_comparison.objects import create_object_lookup

set_up_root_logger(f'VG_objects_{datetime.now().strftime("%d%m%Y%H%M%S")}', os.path.join(os.getcwd(), 'logs'))

logger = logging.getLogger(__name__)


def main():
    objects_lookup = create_object_lookup('data/objects.json')
    logger.info(objects_lookup['tree.n.01'])


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logger.exception("Unhandled exception")
        raise
