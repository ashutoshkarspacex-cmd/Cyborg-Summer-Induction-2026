from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'bot_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'scripts'), glob('scripts/*'))
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cyborg',
    maintainer_email='soumitranayak71@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                            'trace_path_odom = bot_control.trace_path_odom:main',
                            'move_spiral = bot_control.move_spiral:main',
                            'odom_broadcaster = bot_control.odom_broadcaster:main',
                            'trace_ground_truth = bot_control.trace_ground_truth:main',
                            'move_ellipse = bot_control.move_ellipse:main',
                            'visualization = bot_control.visualization:main',
                            'feedback = bot_control.feedback:main',
                            'go_to_goal= bot_control.go_to_goal:main',],
    },
)
