from setuptools import setup

package_name = 'gary_rqt'

setup(
    name=package_name,
    version='0.3.0-alpha',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juntong20XX',
    maintainer_email='juntong_2021@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #  NOTE: 节点登记在这个列表里, 格式为: "{节点名} = {python模块}.{python文件}:{入口函数}"

        ],
    },
)
