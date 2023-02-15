"""

"""
from __future__ import annotations

try:
    from . import window_ui
except ImportError:
    import window_ui
try:
    from . import process_apis
except ImportError:
    import process_apis

import yaml
import typing
import pathlib
from PyQt6 import QtWidgets


class Worker:
    """

    """

    def __init__(self):
        self.commands_dict: dict[str, process_apis.Command] = {}

    def add_command(self, name: str, cmd: str | list[str]):
        """

        :param name:
        :param cmd:
        :return:
        """
        cmd = process_apis.Command(cmd)
        self.registered(name, cmd)
        self.commands_dict[name] = cmd

    def registered(self, name, cmd):
        """

        :param name:
        :param cmd:
        :return:
        """
        pass

    def get_state(self, name: str) -> bool:
        """

        :param name:
        :return: bool
        """
        return self.commands_dict[name].is_running()

    def get_command(self, key: str, default=None):
        return self.commands_dict.get(key, default)


class Main(window_ui.Ui_Form):
    """
    The Main Window
    """

    def __init__(self, cmds_cfg: str | None = None, widget: QtWidgets.QWidget | None = None):
        """

        """
        self.parent = widget if widget else QtWidgets.QWidget()
        self.worker = Worker()

        self.setupUi(self.parent)

        if cmds_cfg:
            self.load_commands_config(cmds_cfg)

    def enter(self):
        """

        :return:
        """
        cmd = self.worker.get_command("enter")
        if cmd:
            cmd.run()

    def exit(self):
        """

        :return:
        """
        cmd = self.worker.get_command("exit")
        if cmd:
            cmd.run()

    def load_commands_config(self, path):
        """

        :param path:
        :return:
        """
        with open(path, "r", encoding="utf-8") as fp:
            data = yaml.safe_load(fp)
        assert isinstance(data, dict)

        for name, cmd in data.items():
            self.worker.add_command(name, cmd)
