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

    def update(self) -> py_trees.common.Status:
        if self.get_input('condition_bool'):
            print(f'[{self.name}]: condition is true')
            return py_trees.common.Status.SUCCESS

        print(f'[{self.name}]: condition is false')
        return py_trees.common.Status.FAILURE
