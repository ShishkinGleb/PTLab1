# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml_mess = "<root>\n<student>\n<name>Куликов Юрий Петрович</name>\n" + \
            "<math>100</math>\n<programming>100</programming>\n<litera" + \
            "ture>76</literature>\n</student>\n<student>\n<name>Кузнецов" + \
            " Петр Петрович</name>\n<math>91</math>\n<sociology>90</" + \
            "sociology>\n<chemistry>61</chemistry>\n</student>\n</root>\n"
        data = {
            "Куликов Юрий Петрович": [
                ("math", 100), ("programming", 100), ("literature", 76)
            ],
            "Кузнецов Петр Петрович": [
                ("math", 91), ("sociology", 90), ("chemistry", 61)
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
