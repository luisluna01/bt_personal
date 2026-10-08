import py_trees
from py_trees.ports import BehaviourWithPorts, PortInformation


class Print(BehaviourWithPorts):
    """Log the `message` input port at ROS info level and succeed."""

    @classmethod
    def input_ports(cls):
        return {'message': PortInformation(data_type=str, required=True)}

    @classmethod
    def output_ports(cls):
        return {}

    def setup(self, **kwargs) -> None:
        # py_trees_ros passes the tree's ROS node to every behaviour's setup()
        self.ros_logger = kwargs['node'].get_logger()

    def update(self) -> py_trees.common.Status:
        self.ros_logger.info(f'[{self.name}]: {self.get_input("message")}')
        return py_trees.common.Status.SUCCESS
