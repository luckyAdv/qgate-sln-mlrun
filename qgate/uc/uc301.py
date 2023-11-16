"""
  UC301: Ingest data to feature set(s)
"""

from qgate.uc.ucbase import UCBase
from qgate.solution import Solution
from qgate.uc.ucoutput import UCOutput


class UC301(UCBase):

    def __init__(self, sln: Solution, output: UCOutput):
        super().__init__(sln, output, self.__class__.__name__)

    @property
    def desc(self) -> str:
        return "Ingest data to feature set(s)"

    def exec(self):
        self.sln.ingest_data(self)

