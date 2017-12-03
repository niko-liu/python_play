# encoding: utf-8
'''
Created on 2017年11月15日

@author: niko
'''

class Parent():
    '''
    parent
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
    
    def show_name(self):
        print self.name

class Child(Parent):
    def __init__(self, name, toys_num):
        Parent.__init__(self, name);
        self.toys_num = toys_num
    def show_name(self):
        print self.name + "," + str(self.toys_num)
        
parent = Parent("cat")
child = Child("dog", 2)

child.show_name()