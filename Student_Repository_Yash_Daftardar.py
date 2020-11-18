""" Creating a Data Repository for University """

import os
from collections import defaultdict
from prettytable import PrettyTable
from typing import Dict, DefaultDict, Tuple, List, Iterator


class Repository:
    "Repository for list of student and Instructor"
    def file_reading(self,path:str,fields:int,sep:str=',',header:bool=False)->Iterator[List[str]]:
        if not isinstance(path,str):
            raise ValueError("Path is Not a string")
        if not isinstance(fields,int):
            raise ValueError("Fields is Not a Integer")
        try:
            fp:IO = open(path, 'r')
            base=os.path.basename(path)
        except FileNotFoundError:
            print("No file in such directory")
        else:
            with fp:
                if header:
                    next(fp)
                for n, line in enumerate(fp, 1):
                    line = line.strip()
                    if line.count(sep)==fields-1:
                        yield tuple(line.split(sep))
                    else:
                        raise ValueError(f"{base} has {line.count(sep) + 1} fields on line {n} but expected {fields} ")
    def __init__(self, dir_path: str) -> None:
        self._dir_path: str = dir_path
        self._stud= dict()
        self._instruct=dict()
        os.chdir(self._dir_path)
        self.file_list = os.listdir()
        cwd: str=os.getcwd()
        try:
            self.new_stud(os.path.join(cwd, 'students.txt'))
            self.new_instruct(os.path.join(cwd, 'instructors.txt'))
            self.new_grades(os.path.join(cwd, 'grades.txt'))
        except (FileNotFoundError, ValueError) as e:
            print(e)
    def new_instruct(self, path) -> None:
        """ Instructor detail """
        for cwid, name, deptarment in self.file_reading(path, 3, sep='\t', header=False):
            self._instruct[cwid] = Instructor(cwid, name, deptarment)       
    def new_stud(self, path) -> None:
        """ Student detail """
        for cwid, name, major in self.file_reading(path, 3, sep='\t', header=False):
            self._stud[cwid] = Student(cwid, name, major)
    def new_grades(self, path) -> None:
        """Grades details to map with student and instructor"""
        for std_cwid, course, grade, instructor_cwid in self.file_reading(path, 4, sep='\t', header=False):
            if instructor_cwid in self._instruct:
                self._instruct[instructor_cwid].add_student_to_course(course)
            else:
                print(f'The Grade file Contains a instructor {instructor_cwid} who is not in instructor file')            
            if std_cwid in self._stud:
                self._stud[std_cwid].add_coursework(course, grade)
            else:
                print(f'The Grade file contains a student {std_cwid} who is not in student file')
    def stud_table(self) -> None:
        """to display Student table """
        student_tab = PrettyTable()
        student_tab.field_names = ['CWID', 'Name', 'Completed Courses']
        for student in self._stud.values():
            student_tab.add_row(student.details())
        print(student_tab)
    def instruct_table(self) -> None:
        """ to display Instructor table """
        instructor_tab = PrettyTable()
        instructor_tab.field_names = ['CWID', 'Name', 'Deptarment', 'Course', 'Students']
        for instructor in self._instruct.values():
            for row in instructor.details():
                instructor_tab.add_row(row)
        print(instructor_tab)
class Student:
    """store student data"""
    def __init__(self, cwid: str, name: str, major: str) -> None:
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()
    def add_coursework(self, course: str, grade: str) -> None:
        """ grads and course are added """
        self._courses[course] = grade
    def details(self) -> Tuple[str, str, List[str]]:
        """ return vale to display in table """
        return [self._cwid, self._name, sorted(self._courses.keys())]
class Instructor:
    """ store Instructor data """
    def __init__(self, cwid: str, name: str, deptarment: str) -> None:
        self._cwid: str = cwid
        self._name: str = name
        self._deptarment: str = deptarment
        self._courses: DefaultDict[str, int] = defaultdict(int)
    def add_student_to_course(self, course: str) -> None:
        """ map the course with student """
        self._courses[course] += 1
    def details(self) -> Iterator[Tuple[str, str, str, str, int]]:
        """ Yield  to display in table """
        for course, count in self._courses.items():
            yield [self._cwid, self._name, self._deptarment, course, count]
def main():
    studuni=Repository('E:/SSW-810-Special Topics/SSW-810-Yash/Assignment/09')
    studuni.stud_table()
    studuni.instruct_table()
if __name__ == '__main__':
    main()