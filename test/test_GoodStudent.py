# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.GoodStudent import GoodStudent


class TestGoodStudent:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("Math", 85),
                ("Programming", 91),
                ("Literature", 100),
                ("Biology", 76),
                ("Technology", 0)
            ],
            "Петров Игорь Владимирович": [
                ("Math", 100),
                ("Sociology", 90),
                ("Chemistry", 80),
                ("Physics", 97)
            ],
            "Сидоров Иван Николаевич": [
                ("Math", 61),
                ("Sociology", 78),
                ("Chemistry", 52)
            ]
        }
        expected_good_students_count = 1
        return data, expected_good_students_count

    def test_init_good_students(self,
                                input_data: tuple[DataType, int]) -> None:
        good_students = GoodStudent(input_data[0])
        assert input_data[0] == good_students.data

    def test_calc_good_students(self,
                                input_data: tuple[DataType, int]) -> None:
        good_students = GoodStudent(input_data[0])
        good_students_count = good_students.calc()
        assert good_students_count == input_data[1]