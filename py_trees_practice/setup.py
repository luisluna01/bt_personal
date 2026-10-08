from glob import glob

from setuptools import find_packages, setup

package_name = 'py_trees_practice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/trees', glob('trees/*.xml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Luis Luna',
    maintainer_email='luisluna12@utexas.edu',
    description='ROS2 Python Humble pkg for practicing PyTrees concepts',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'reactive_sequence_example = py_trees_practice.reactive_sequence_example:main',
        ],
    },
)
