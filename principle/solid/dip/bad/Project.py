from BackendDeveloper import BackendDeveloper
from FrontendDeveloper import FrontendDeveloper

"""
@File      : Project.py   
@Author    : Rohit Agarwal on 30/11/21 11:06 pm
@Copyright : https://github.com/javamultiplex
"""


class Project:
    def __init__(self, front_end_developer: FrontendDeveloper,
                 back_end_developer: BackendDeveloper) -> None:
        self.front_end_developer = front_end_developer
        self.back_end_developer = back_end_developer

    def implement(self) -> None:
        self.front_end_developer.write_javascript()
        self.back_end_developer.write_java()
