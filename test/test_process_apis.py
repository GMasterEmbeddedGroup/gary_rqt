"""
测试 gary_rqt.process_apis.py 文件. 不过因为不会用 pytest, 将手动编写测试
"""
from gary_rqt.process_apis import Listener
from std_msgs import msg
import rclpy

NODE_NAME: str = "~/name"


def test_listener():
    """
    测试启用一个接收者
    :return:
    """
    listener = Listener(msg.String, NODE_NAME, print)

    listener.run()

    rclpy.shutdown()
