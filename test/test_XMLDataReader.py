# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml_mess = """<?xml version="1.0" encoding="UTF-8"?>
        <students>
            <student name="Клюев Роман Фёдорович">
                <subject name="математика" score="91" />
                <subject name="химия" score="100" />
            </student>
            <student name="Кузнецов Руслан Тимофеевич">
                <subject name="русский язык" score="87" />
                <subject name="литература" score="78" />
            </student>
        </students>
        """

        data = {
            "Клюев Роман Фёдорович": [
                ("математика", 91), ("химия", 100)
            ],
            "Кузнецов Руслан Тимофеевич": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return xml_mess, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
