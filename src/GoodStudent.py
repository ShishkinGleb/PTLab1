# -*- coding: utf-8 -*-
from Types import DataType


class GoodStudent:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.count: int = 0

    def calc(self) -> DataType:
        for key in self.data:
            sum = 0
            num_les = 0
            for subject in self.data[key]:
                sum = subject[1] + sum
                num_les = num_les + 1
            if ((sum/num_les) >= 76):
                self.count = self.count + 1
        return self.count
