"""
为前端提供后台服务
"""
import rclpy
from rclpy import node
from std_msgs import msg

import typing
from threading import Thread
from subprocess import Popen


class Listener:
    def __init__(self, msg_type, topic: str, callback: typing.Callable):
        self.node = node.Node("listener")
        self.sub = self.node.create_subscription(msg_type, topic, callback, 1)  # XXX: Qos ???

    def run(self):
        rclpy.spin(self.node)


class Command:
    """

    """
    SHELL_NAMES = {"shell", "bash"}
    default_callback: typing.Callable = print

    def __init__(self, cmd: list[str]):
        self.cmd = cmd
        self.thread: None | Thread | Popen = None

        self.cmd_type, self.args = self.get_cmd(cmd)

    def get_cmd(self, cmd):
        """

        :param cmd:
        :return:
        """
        string, *args = cmd
        if string == "listener":
            msg_type, topic, callback = args
            msg_type = getattr(msg, msg_type)
            callback = self.get_callback_function(callback)
            return Listener, (msg_type, topic, callback)
        else:
            return string, args

    def get_callback_function(self, callback_name: str) -> typing.Callable:
        """

        :param callback_name:
        :return:
        """
        return self.default_callback

    def is_running(self) -> bool:
        if isinstance(self.thread, Thread):
            return self.thread.is_alive()
        if isinstance(self.thread, Popen):
            return self.thread.poll() is None
        # self.thread is None
        return False

    def run(self):
        if self.is_running():
            return
        if callable(self.cmd_type):
            self.thread = Thread(target=self.cmd_type, args=self.args)
        elif isinstance(self.cmd_type, str):
            is_shell = self.cmd_type in self.SHELL_NAMES
            self.thread = Popen(self.args, shell=is_shell)
