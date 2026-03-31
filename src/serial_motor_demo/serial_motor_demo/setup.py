from setuptools import setup
import os
from glob import glob

# Имя должно совпадать с названием папки, в которой лежит этот setup.py
package_name = 'serial_motor_demo'

setup(
    name=package_name,
    version='0.0.0',
    # ВАЖНО: это имя папки, где лежат driver.py и __init__.py
    packages=[package_name], 
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, 'description'), glob('description/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='Robot package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Слева - имя команды, справа - путь: папка.файл:функция
            'driver = serial_motor_demo.driver:main',
        ],
    },
)