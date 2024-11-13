import xml.etree.ElementTree as ET
from DataReader import DataReader
from Types import DataType

class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = dict()
    
    def read(self, path: str) -> DataType:
        tree = ET.parse('data.xml')
        root = tree.getroot()

        for student in root.findall('student'):
            student_name = student.get('name')
            self.students[student_name] = []

            for subject in student.findall('subject'):
                subj_name = subject.get('name')
                score = int(subject.get('score'))
                self.students[student_name].append((subj_name, score))

        #print(self.students)
        return self.students
        
#new_class = XMLDataReader()
#students = new_class.read("C:/VolgGTU/mag_1_1/tp/Lab_1_Shishkin/PTLab1/data/data.xml")
#print(students)
    