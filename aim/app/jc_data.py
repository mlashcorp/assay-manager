# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="cortereal"
__date__ ="$Apr 17, 2014 10:13:12 AM$"
from datetime import datetime

class JCResults():
    """ Class defining JC results """
    def __init__(self,jc_id,assay_number1,assay_number2,date,results1,results2):
        self.jc_id = jc_id
        self.date = date
        print "object initialized with date: "+str(self.date)
        self.results1 = results1
        self.results2 = results2
        self.assay_number1 = assay_number1
        self.assay_number2 = assay_number2

