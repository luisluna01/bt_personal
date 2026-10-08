import py_trees
from py_trees.ports import BehaviourWithPorts, PortInformation


class DummyTask(BehaviourWithPorts):
    """Pretend to perform a task by running for `completion_time` seconds."""

    print_period = 1.0  # Seconds between "performing task" prints

    @classmethod
    def input_ports(cls):
        return {
            'completion_time': PortInformation(
                data_type=float, required=False,
                description='Time in seconds for the task to run'),
        }

    @classmethod
    def output_ports(cls):
        return {}

    def setup(self, **kwargs) -> None:
        # py_trees_ros passes the tree's ROS node to every behaviour's setup()
        self.ros_logger = kwargs['node'].get_logger()
        self.clock = kwargs['node'].get_clock()

    def now_sec(self) -> float:
        return self.clock.now().nanoseconds * 1e-9

    def initialise(self) -> None:
        self.completion_time = self.get_input('completion_time', default=10.0)
        self.start_time = self.now_sec()
        self.last_print_time = self.start_time
        self.ros_logger.info(f'[{self.name}]: performing task...')

    def update(self) -> py_trees.common.Status:
        now = self.now_sec()
        elapsed = now - self.start_time

        # Return SUCCESS if completion time reached
        if elapsed >= self.completion_time:
            self.ros_logger.info(f'[{self.name}]: task complete!')
            return py_trees.common.Status.SUCCESS

        # Print every print_period
        if now - self.last_print_time >= self.print_period:
            self.last_print_time = now
            self.ros_logger.info(f'[{self.name}]: performing task...')

        return py_trees.common.Status.RUNNING

    def terminate(self, new_status: py_trees.common.Status) -> None:
        # INVALID while RUNNING means the task was interrupted rather than finished
        if (new_status == py_trees.common.Status.INVALID
                and self.status == py_trees.common.Status.RUNNING):
            self.ros_logger.info(f'[{self.name}]: halted')
