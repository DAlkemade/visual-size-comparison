import logging
from typing import Set, List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import tqdm

from visual_size_comparison.config import VisualConfig

logger = logging.getLogger(__name__)


def build_cooccurrence_graph(objects: list, visual_config: VisualConfig) -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(objects)
    logger.info(f'Number of nodes: {G.number_of_nodes()}')
    for object1 in tqdm.tqdm(objects):
        synsets1 = visual_config.entity_to_synsets[object1]
        s1 = synsets1[0]  # TODO this is bad, do for all synsets
        for object2 in objects:

            synsets2 = visual_config.entity_to_synsets[object2]
            s2 = synsets2[0]  # TODO this is bad, do for all synsets
            cooccurrences = len(visual_config.comparer.find_cooccurrences(s1, s2))
            if cooccurrences > 0:
                G.add_edge(object1, object2, weight=cooccurrences)
    nr_edges = G.number_of_edges()
    max_edges = G.number_of_nodes() ** 2
    logger.info(f'Number of edges: {nr_edges} (sparsity: {nr_edges / max_edges})')
    return G

class Pair:
    def __init__(self, e1, e2):
        self.e2 = e2
        self.e1 = e1
        self.larger = None
        self.larger_gold = None

    def both_in_list(self, objects: list):
        return self.e1 in objects and self.e2 in objects


class VisualPropagation:
    def __init__(self, cooccurrence_graph: nx.Graph, visual_config: VisualConfig, max_path_length: int = 2):
        self.visual_config: VisualConfig = visual_config
        self.max_path_length: int = max_path_length
        self.cooccurrence_graph: nx.Graph = cooccurrence_graph
        self.useful_path_counts = []

    def find_paths(self, pair: Pair, draw=False) -> List[List[str]]:
        good_paths = list(nx.all_simple_paths(self.cooccurrence_graph, pair.e1, pair.e2, cutoff=self.max_path_length))

        logger.debug(f'Found paths: {good_paths}')
        if draw:
            subgraph_nodes = set()
            for path in good_paths:
                for node in path:
                    subgraph_nodes.add(node)
            SG = self.cooccurrence_graph.subgraph(subgraph_nodes)
            nx.draw(SG)
            plt.show()

        return good_paths

    def compare_pairs(self, pairs: Set[Pair]) -> None:
        for pair in pairs:
            self.compare_pair(pair)

    def compare_pair(self, pair: Pair) -> float:
        """Use propagation to compare two objects visually.

        Finds all paths of lenght <= self.max_path_length between the two objects and computes
        the size comparisons on all edges on the paths. Then uses the fraction of paths indicating one object being
        larger as the confidence of that being true.
        Results are saved in-place in the Pair object.
        :param pair: pair to be predicted
        """
        assert pair.both_in_list(list(self.visual_config.entity_to_synsets.keys()))  # TODO maybe quite expensive
        paths = self.find_paths(pair)
        logger.debug(f'Using {len(paths)} paths')
        larger_count = 0
        smaller_count = 0
        unknown_count = 0
        for path in paths:
            transitions = list()
            for i in range(0, len(path) - 1):
                j = i + 1
                e1 = path[i]
                e2 = path[j]
                synsets1 = self.visual_config.entity_to_synsets[e1]
                s1 = synsets1[0]  # TODO this is bad, do for all synsets
                synsets2 = self.visual_config.entity_to_synsets[e2]
                s2 = synsets2[0]  # TODO this is bad, do for all synsets
                comp = self.visual_config.comparer.compare(s1, s2)
                larger_array = [c > 1. for c in comp if c != 1.]
                if len(larger_array) == 0:
                    logger.debug(f'Encountered a larger array of length 0, because all relative sizes were 1.')
                    continue

                res = np.mean(larger_array)

                logger.debug(f'For comp {comp} larger array {larger_array} res {res}')
                if res != .5:  # TODO think about this. Rationale: if they are equal, the edge doesn't matter
                    transitions.append(res > .5)
            if len(transitions) > 0:
                larger = all(transitions)
                smaller = not any(transitions)
                if larger:
                    larger_count += 1
                elif smaller:
                    smaller_count += 1
                else:
                    unknown_count += 1
        logger.debug(f'Larger: {larger_count}')
        logger.debug(f'Smaller: {smaller_count}')
        logger.debug(f'Unknown: {unknown_count}')
        logger.debug(
            f'Total: {larger_count + smaller_count + unknown_count}. excluding unknown: {larger_count + smaller_count}')

        useful_count = larger_count + smaller_count
        self.useful_path_counts.append(useful_count)
        try:
            fraction_larger = larger_count / (larger_count + smaller_count)
        except ZeroDivisionError:
            fraction_larger = None

        # TODO somehow the reverse examples have slightly different counts
        return fraction_larger

        # edges =