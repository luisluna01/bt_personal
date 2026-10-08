import py_trees
from py_trees.ports import BehaviourWithPorts, PortInformation


class DummyCondition(BehaviourWithPorts):
    """Succeed or fail based on the `condition_bool` input, printing the instance name."""

    @classmethod
    def input_ports(cls):
        return {
            'condition_bool': PortInformation(
                data_type=bool, required=True,
                description='Boolean determines if condition is true'),
        }

    @classmethod
    def output_ports(cls):
        return {}

    def setup(self, **kwargs) -> None:
        # py_trees_ros passes the tree's ROS node to every behaviour's setup()
        self.ros_logger = kwargs['node'].get_logger()

    def update(self) -> py_trees.common.Status:
        if self.get_input('condition_bool'):
            self.ros_logger.info(f'[{self.name}]: condition is true')
            return py_trees.common.Status.SUCCESS

        self.ros_logger.info(f'[{self.name}]: condition is false')
        return py_trees.common.Status.FAILURE
