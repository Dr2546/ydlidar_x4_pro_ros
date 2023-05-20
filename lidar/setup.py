from setuptools import setup

package_name = 'lidar'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Daniel Riyavong',
    maintainer_email='danjan36@gmail.com',
    description='ydlidar x4 pro package',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'lidar = lidar.lidar:main',
        'lidarcli = lidar.lidarcli:main'
        ],
    },
)
