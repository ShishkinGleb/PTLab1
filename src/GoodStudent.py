# -*- coding: utf-8 -*-
from Types import DataType


class GoodStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.count: int = 0

    def calc(self) -> DataType:
        self.count = len(self.data)
        for key in self.data:
            bad_mark = 0
            for subject in self.data[key]:
                if (subject[1] < 76):
                    bad_mark = bad_mark + 1
            if (bad_mark > 0):
                self.count = self.count - 1
        return self.count
