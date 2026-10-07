import py_trees
from py_trees.ports import BehaviourWithPorts, PortInformation


class Print(BehaviourWithPorts):
    """Print the `message` input port to stdout and succeed."""

    @classmethod
    def input_ports(cls):
        return {'message': PortInformation(data_type=str, required=True)}

    @classmethod
    def output_ports(cls):
        return {}

    def update(self) -> py_trees.common.Status:
        print(f'[{self.name}]: {self.get_input("message")}')
        return py_trees.common.Status.SUCCESS
