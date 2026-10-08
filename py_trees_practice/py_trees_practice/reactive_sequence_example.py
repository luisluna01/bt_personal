import os

from ament_index_python.packages import get_package_share_directory
import py_trees
from py_trees.parsers.behaviour_tree_xml import parse_behaviour_tree_xml
import py_trees_ros
import rclpy

# Importing the module registers the behaviour tag with the XML parser
from py_trees_practice.behaviours.print import Print  # noqa: F401
from py_trees_practice.behaviours.dummy_condition import DummyCondition
from py_trees_practice.behaviours.dummy_task import DummyTask


def main():
    rclpy.init()

    # Build the tree from XML
    share_path = get_package_share_directory('py_trees_practice')
    root = parse_behaviour_tree_xml(
        os.path.join(share_path, 'trees', 'reactive_sequence_example.xml'),
        main_tree_id='ReactiveSequenceExample',
    )

    # The parser prefixes each node name with its parents' names
    # ("Sequence.ConditionA"); keep only the last part for display ("ConditionA")
    for node in root.iterate():
        node.name = node.name.rsplit('.', 1)[-1]

    # Create Tree (ROS version publishes snapshots for py-trees-tree-viewer)
    tree = py_trees_ros.trees.BehaviourTree(root, unicode_tree_debug=True)
    tree.setup(node_name='reactive_sequence_example')

    def stop_when_done(tree):
        print(f'Tree Status: {tree.root.status.value}\n')

        # Stop ticking once the tree is no longer RUNNING, but keep the node
        # alive so the final state stays visible in the viewer
        if tree.root.status != py_trees.common.Status.RUNNING:
            tree.timer.cancel()
            print('Tree finished, ticking stopped (Ctrl+C to exit)')

    tree.tick_tock(period_ms=1000.0, post_tick_handler=stop_when_done)

    try:
        rclpy.spin(tree.node)
    except KeyboardInterrupt:
        pass
    finally:
        tree.shutdown()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
