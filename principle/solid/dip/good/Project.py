from typing import List

from Developer import Developer

"""
@File      : Project.py   
@Author    : Rohit Agarwal on 30/11/21 11:18 pm
@Copyright : https://github.com/javamultiplex
"""


class Project:
    def __init__(self, developers: List[Developer]) -> None:
        self.developers = developers

    def implement(self) -> None:
        for developer in self.developers:
            developer.develop()
