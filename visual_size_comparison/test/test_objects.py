from typing import Dict

import pytest

from visual_size_comparison.compare import Comparer
from visual_size_comparison.objects import index_objects


@pytest.fixture
def objects() -> Dict[int, dict]:
    objects = {1: {"image_id": 1, "objects": [
        {"synsets": ["tree.n.01"], "h": 557, "object_id": 1058549, "merged_object_ids": [], "names": ["trees"],
         "w": 799, "y": 0, "x": 0},
        {"synsets": ["sidewalk.n.01"], "h": 290, "object_id": 1058534, "merged_object_ids": [5046],
         "names": ["sidewalk"], "w": 722, "y": 308, "x": 78},
        {"synsets": ["building.n.01"], "h": 538, "object_id": 1058508, "merged_object_ids": [], "names": ["building"],
         "w": 222, "y": 0, "x": 1},
        {"synsets": ["street.n.01"], "h": 258, "object_id": 1058539, "merged_object_ids": [3798578],
         "names": ["street"], "w": 359, "y": 283, "x": 439},
        {"synsets": ["wall.n.01"], "h": 535, "object_id": 1058543, "merged_object_ids": [], "names": ["wall"], "w": 135,
         "y": 1, "x": 0},
        {"synsets": ["tree.n.01"], "h": 360, "object_id": 1058545, "merged_object_ids": [], "names": ["tree"], "w": 476,
         "y": 0, "x": 178},
        {"synsets": ["shade.n.01"], "h": 189, "object_id": 5045, "merged_object_ids": [], "names": ["shade"], "w": 274,
         "y": 344, "x": 116},
        {"synsets": ["van.n.05"], "h": 176, "object_id": 1058542, "merged_object_ids": [1058536], "names": ["van"],
         "w": 241, "y": 278, "x": 533},
        {"synsets": ["trunk.n.01"], "h": 348, "object_id": 5055, "merged_object_ids": [], "names": ["tree trunk"],
         "w": 78, "y": 213, "x": 623},
        {"synsets": ["clock.n.01"], "h": 363, "object_id": 1058498, "merged_object_ids": [], "names": ["clock"],
         "w": 77, "y": 63, "x": 422},
        {"synsets": ["window.n.01"], "h": 147, "object_id": 3798579, "merged_object_ids": [], "names": ["windows"],
         "w": 198, "y": 1, "x": 602},
        {"synsets": ["man.n.01"], "h": 248, "object_id": 3798576, "merged_object_ids": [1058540], "names": ["man"],
         "w": 82, "y": 264, "x": 367},
        {"synsets": ["man.n.01"], "h": 259, "object_id": 3798577, "merged_object_ids": [], "names": ["man"], "w": 57,
         "y": 254, "x": 238},
        {"synsets": [], "h": 430, "object_id": 1058548, "merged_object_ids": [], "names": ["lamp post"], "w": 43,
         "y": 63, "x": 537},
        {"synsets": ["sign.n.02"], "h": 179, "object_id": 1058507, "merged_object_ids": [], "names": ["sign"], "w": 78,
         "y": 13, "x": 123},
        {"synsets": ["car.n.01"], "h": 164, "object_id": 1058515, "merged_object_ids": [], "names": ["car"], "w": 80,
         "y": 342, "x": 719},
        {"synsets": ["back.n.01"], "h": 164, "object_id": 5060, "merged_object_ids": [], "names": ["back"], "w": 70,
         "y": 345, "x": 716},
        {"synsets": ["jacket.n.01"], "h": 98, "object_id": 1058530, "merged_object_ids": [], "names": ["jacket"],
         "w": 82, "y": 296, "x": 367},
        {"synsets": ["car.n.01"], "h": 95, "object_id": 5049, "merged_object_ids": [], "names": ["car"], "w": 78,
         "y": 319, "x": 478},
        {"synsets": ["trouser.n.01"], "h": 128, "object_id": 1058531, "merged_object_ids": [], "names": ["pants"],
         "w": 48, "y": 369, "x": 388},
        {"synsets": ["shirt.n.01"], "h": 103, "object_id": 1058511, "merged_object_ids": [], "names": ["shirt"],
         "w": 54, "y": 287, "x": 241},
        {"synsets": ["parking_meter.n.01"], "h": 143, "object_id": 1058519, "merged_object_ids": [],
         "names": ["parking meter"], "w": 26, "y": 325, "x": 577},
        {"synsets": ["trouser.n.01"], "h": 118, "object_id": 1058528, "merged_object_ids": [], "names": ["pants"],
         "w": 44, "y": 384, "x": 245},
        {"synsets": ["shirt.n.01"], "h": 102, "object_id": 1058547, "merged_object_ids": [], "names": ["shirt"],
         "w": 82, "y": 295, "x": 368},
        {"synsets": ["shoe.n.01"], "h": 28, "object_id": 1058525, "merged_object_ids": [5048], "names": ["shoes"],
         "w": 48, "y": 485, "x": 388},
        {"synsets": ["arm.n.01"], "h": 41, "object_id": 1058546, "merged_object_ids": [], "names": ["arm"], "w": 30,
         "y": 285, "x": 370},
        {"synsets": ["bicycle.n.01"], "h": 36, "object_id": 1058535, "merged_object_ids": [], "names": ["bike"],
         "w": 27, "y": 319, "x": 337},
        {"synsets": ["bicycle.n.01"], "h": 41, "object_id": 5051, "merged_object_ids": [], "names": ["bike"], "w": 27,
         "y": 311, "x": 321},
        {"synsets": ["headlight.n.01"], "h": 9, "object_id": 5050, "merged_object_ids": [], "names": ["headlight"],
         "w": 18, "y": 370, "x": 517},
        {"synsets": ["spectacles.n.01"], "h": 23, "object_id": 1058518, "merged_object_ids": [], "names": ["glasses"],
         "w": 43, "y": 317, "x": 448},
        {"synsets": ["chin.n.01"], "h": 8, "object_id": 1058541, "merged_object_ids": [], "names": ["chin"], "w": 9,
         "y": 288, "x": 401}], "image_url": "https://cs.stanford.edu/people/rak248/VG_100K_2/1.jpg"},
               2: {"image_id": 2, "objects": [
                   {"synsets": ["road.n.01"], "h": 254, "object_id": 1023841, "merged_object_ids": [],
                    "names": ["road"], "w": 364, "y": 345, "x": 0},
                   {"synsets": ["sidewalk.n.01"], "h": 253, "object_id": 1023813, "merged_object_ids": [],
                    "names": ["sidewalk"], "w": 478, "y": 347, "x": 320},
                   {"synsets": ["building.n.01"], "h": 414, "object_id": 1023819, "merged_object_ids": [],
                    "names": ["building"], "w": 228, "y": 0, "x": 569},
                   {"synsets": ["building.n.01"], "h": 319, "object_id": 1023846, "merged_object_ids": [],
                    "names": ["building"], "w": 258, "y": 0, "x": 171},
                   {"synsets": [], "h": 412, "object_id": 1023845, "merged_object_ids": [], "names": ["street light"],
                    "w": 114, "y": 120, "x": 386},
                   {"synsets": ["crossing.n.05"], "h": 68, "object_id": 5077, "merged_object_ids": [],
                    "names": ["crosswalk"], "w": 366, "y": 531, "x": 0},
                   {"synsets": ["man.n.01"], "h": 246, "object_id": 1023838, "merged_object_ids": [], "names": ["man"],
                    "w": 142, "y": 325, "x": 321},
                   {"synsets": ["pole.n.01"], "h": 533, "object_id": 1023847, "merged_object_ids": [],
                    "names": ["pole"], "w": 49, "y": 0, "x": 423},
                   {"synsets": ["window.n.01"], "h": 165, "object_id": 5080, "merged_object_ids": [],
                    "names": ["window"], "w": 94, "y": 68, "x": 649},
                   {"synsets": ["car.n.01"], "h": 108, "object_id": 1023836, "merged_object_ids": [], "names": ["car"],
                    "w": 127, "y": 354, "x": 240},
                   {"synsets": ["tree.n.01"], "h": 220, "object_id": 5074, "merged_object_ids": [], "names": ["tree"],
                    "w": 89, "y": 146, "x": 0},
                   {"synsets": ["tree.n.01"], "h": 161, "object_id": 5076, "merged_object_ids": [], "names": ["tree"],
                    "w": 106, "y": 195, "x": 102},
                   {"synsets": ["tree.n.01"], "h": 205, "object_id": 5075, "merged_object_ids": [], "names": ["tree"],
                    "w": 62, "y": 155, "x": 58},
                   {"synsets": ["window.n.01"], "h": 110, "object_id": 5082, "merged_object_ids": [],
                    "names": ["window"], "w": 98, "y": 263, "x": 644},
                   {"synsets": ["window.n.01"], "h": 161, "object_id": 5081, "merged_object_ids": [],
                    "names": ["window"], "w": 53, "y": 71, "x": 746},
                   {"synsets": ["car.n.01"], "h": 61, "object_id": 5085, "merged_object_ids": [], "names": ["car"],
                    "w": 81, "y": 337, "x": 350},
                   {"synsets": ["backpack.n.01"], "h": 80, "object_id": 5071, "merged_object_ids": [],
                    "names": ["backpack"], "w": 70, "y": 362, "x": 361},
                   {"synsets": ["window.n.01"], "h": 107, "object_id": 5083, "merged_object_ids": [],
                    "names": ["window"], "w": 49, "y": 264, "x": 750},
                   {"synsets": ["gym_shoe.n.01"], "h": 24, "object_id": 5088, "merged_object_ids": [],
                    "names": ["sneakers"], "w": 40, "y": 541, "x": 338},
                   {"synsets": ["window.n.01"], "h": 170, "object_id": 5084, "merged_object_ids": [],
                    "names": ["window"], "w": 18, "y": 73, "x": 631},
                   {"synsets": [], "h": 12, "object_id": 5069, "merged_object_ids": [5090], "names": ["walk sign"],
                    "w": 27, "y": 195, "x": 473},
                   {"synsets": [], "h": 126, "object_id": 5086, "merged_object_ids": [], "names": ["street light"],
                    "w": 27, "y": 217, "x": 292},
                   {"synsets": ["bicycle.n.01"], "h": 63, "object_id": 5089, "merged_object_ids": [], "names": ["bike"],
                    "w": 47, "y": 405, "x": 418},
                   {"synsets": ["sign.n.02"], "h": 62, "object_id": 1023823, "merged_object_ids": [], "names": ["sign"],
                    "w": 14, "y": 288, "x": 233},
                   {"synsets": ["light.n.02"], "h": 16, "object_id": 1023848, "merged_object_ids": [],
                    "names": ["lights"], "w": 14, "y": 288, "x": 233}],
                   "image_url": "https://cs.stanford.edu/people/rak248/VG_100K_2/2.jpg"},
               }
    return objects


def test_object_lookup_creation(objects):
    # specify file that is always available
    lookup = index_objects(objects)
    assert 'tree.n.01' in lookup.keys()
    tree_ids = lookup['tree.n.01']
    assert type(tree_ids) is set
    assert 1 in tree_ids
    assert 2 in tree_ids


def test_comparison(objects):
    lookup = index_objects(objects)
    comparer = Comparer(lookup, objects)
    res = comparer.compare('tree.n.01', 'van.n.05')
    assert len(res) == 2
    for scale in res:
        assert pytest.approx(3.31, .1) == scale or pytest.approx(1.98, .1) == scale
