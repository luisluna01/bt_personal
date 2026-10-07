import os

from ament_index_python.packages import get_package_share_directory
import py_trees
from py_trees.parsers.behaviour_tree_xml import parse_behaviour_tree_xml

# Importing the module registers the Print tag with the XML parser
from py_trees_practice.behaviours.print import Print  # noqa: F401


def main():
    # Build the tree from XML
    share_path = get_package_share_directory('py_trees_practice')
    root = parse_behaviour_tree_xml(
        os.path.join(share_path, 'trees', 'simple_sequence_example.xml'),
        main_tree_id='SimpleSequenceExample',
    )
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup()

    # Tick tree once
    print('Sending one tick signal...')
    tree.tick()
    print('Finished executing Behavior Tree...')


if __name__ == '__main__':
    main()
