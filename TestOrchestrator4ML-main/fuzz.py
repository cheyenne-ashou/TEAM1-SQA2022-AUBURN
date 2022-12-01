# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:29:52 2022

@author: tkher
"""

import traceback
import pandas as pd


from dataclasses import dataclass
from detection import constants
from datetime import datetime
from generation import py_parser
from detection import py_parser
from generation import attack_model
from select_repos import dev_count
from label_perturbation_attack import knn


def fuzzGetFunctionAssignments(fuzz):

    func_list = fuzz.fValue1
    
    if not func_list:

        getFunctionAssignments()

    else:

        print("Error: Wrong value for algo_list.")




def fuzzCalculate_K(fuzz):

    kVals = fuzz.fValue2

    if kVals == (3, 10, 2):

        calculate_k()

    else:

        print("Error: kVals has the wrong value.")



def fuzzGetDevCount(fuzz):

    repo_emails = fuzz.fValue3

    if not repo_emails:

        getDevCount()

    else:

        print("Error: repo_emails list does not exist")



def fuzzPredict(fuzz):

    predictions = fuzz.fValue4

    if not predictions:

        predict()

    else:

        print("Error: prediction not a list")
        
        
def fuzzGetImport(fuzz):

    import_list = fuzz.fValue5

    if not import_list:

        getImport()

    else:

        print("Error: Import_list list does not exist") 


@dataclass
class fuzzValues:
    
    fValue1 = "Some random sentence to test the code"
    fValue2 = "-1649867315794871491/-1"
    fValue3 = "fdsdafjasd;flkjdsfa;fj;dfasddfdsfafdfsdfa>"
    fValue4 = "../../../../../../../......//.//./..../"
    fValue5 = "1789749649854974859484984659489494984984448541619451449851"






if __name__ == '__main__':
    fuzz = fuzzValues()
    fuzzGetFunctionAssignments(fuzz)
    fuzzCalculate_K(fuzz)
    fuzzGetDevCount(fuzz)
    fuzzPredict(fuzz)
    fuzzGetImport(fuzz)