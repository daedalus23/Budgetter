from collections.abc import Iterable

import os


__all__ = ["BaseConfiguration"]


"""
BaseConfiguration module/class is base level attributes of both
shared types of configuration usage Single/Multiple. Adding
file extensions to BaseConfiguration attribute 'configFileTypes'
more file extensions can be loaded & read.
"""


class BaseConfiguration:

    workingDir = None
    sections = []
    content = {}
    configFileTypes = [
        "ini", "cnf", "conf"
    ]

    def _check_config_path(self, path) -> bool:
        """Check for config file in path"""
        for fileType in self.configFileTypes:
            if fileType in path:
                return True
            else:
                return False

    @staticmethod
    def check_iterator(item) -> bool:
        """Check if object is iterable"""
        excluded_types = str
        if isinstance(item, Iterable) and not isinstance(item, excluded_types):
            return True
        else:
            return False

    def get_working_dir(self) -> None:
        """Get current working directory"""
        self.workingDir = os.path.abspath(os.curdir)

    def parse_path(self, fullPath) -> tuple:
        """Separate file name & path"""
        tempPath = list(fullPath.split("\\"))
        for fileType in self.configFileTypes:
            if fileType in tempPath[-1].lower():
                fileNameLen = len(tempPath[-1])
                pathDiff = len(fullPath) - fileNameLen
                return fullPath[0:pathDiff], tempPath[-1]

    @staticmethod
    def parse_list_content(newContent) -> list:
        """Parse loaded content into list starting with '**'"""
        tempList = []
        for item in newContent.strip("**").split(","):
            if item[0] == " ":
                tempList.append(item.strip(" "))
            else:
                tempList.append(item)
        return tempList

    @staticmethod
    def prepare_content(newContent) -> tuple:
        """Parse Key from Dict to set Section name of config.ini"""
        sectionName = list(newContent.keys())[0]
        sectionContent = newContent[sectionName]
        return sectionName, sectionContent
