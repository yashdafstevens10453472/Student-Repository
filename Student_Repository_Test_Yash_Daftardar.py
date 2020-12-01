"""unittest file to test HW10"""
import unittest
from Student_Repository_Yash_Daftardar import Repository,Student,Instructor
import os, sys
from prettytable import PrettyTable

class test_class_instructor(unittest.TestCase):
    """ Class  to perform error checking ad handelling """
    def test_class_instructor(self):
        
        stevens: Repository = Repository(r"E:/SSW-810-Special Topics/SSW-810-Yash/Assignment/10")
        list1 = list()
        list2 = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]
        for instructor in stevens._instruct.values():
            for row in instructor.details():
                list1.append(list(row))
        self.assertEqual(list1, list2)

class test_class_student(unittest.TestCase):
    def test_class_student(self):
        
        stevens: Repository = Repository(r"E:/SSW-810-Special Topics/SSW-810-Yash/Assignment/10")
        list1 = list()
        list2 = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], '3.44'],['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], '3.81'],['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], '3.88'],['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], '3.58'],['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], '4.00'],['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], '3.00'],['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], '3.92'],['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], '3.00'],['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], '4.00']]
        for student in stevens._stud.values():
            list1.append(list(student.details()))
        self.assertEqual(list1, list2)
    
class test_file_not_found_error(unittest.TestCase): 
    def test_file_not_found_error(self) -> None:
       
        with self.assertRaises(FileNotFoundError):
            Repository(r"E:/SSW-810-Special Topics/SSW-810-Yash/Assignment/10/Nofile")

   
class test_class_major(unittest.TestCase):
    def test_class_major(self):
       
        stevens: Repository = Repository(r"E:/SSW-810-Special Topics/SSW-810-Yash/Assignment/10")
        list1 = list()
        list2 = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]
        for major in stevens._maj.values():
            list1.append(major.details())
       
        self.assertEqual(list1, list2)

        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
