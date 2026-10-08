import os
import time

from ament_index_python.packages import get_package_share_directory
import py_trees
from py_trees.parsers.behaviour_tree_xml import parse_behaviour_tree_xml

# Importing the module registers the behaviour tag with the XML parser
from py_trees_practice.behaviours.print import Print  # noqa: F401
from py_trees_practice.behaviours.dummy_condition import DummyCondition
from py_trees_practice.behaviours.dummy_task import DummyTask


def main():
    # Build the tree from XML
    share_path = get_package_share_directory('py_trees_practice')
    root = parse_behaviour_tree_xml(
        os.path.join(share_path, 'trees', 'reactive_sequence_example.xml'),
        main_tree_id='ReactiveSequenceExample',
    )

    # Create Tree
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup()

    # Tick until the tree is no longer RUNNING
    tree_running = True
    while tree_running:
    # while tree.root.status == py_trees.common.Status.RUNNING:
        time.sleep(1.0)

        print('\n---tick---')
        tree.tick() 
        print('---end of tick---')
        print(f'Tree Status:{tree.root.status.value}')

        tree_running = tree.root.status == py_trees.common.Status.RUNNING


if __name__ == '__main__':
    main()
