import json
import os
from stu import Student

# 学生数据管理类
class StudentInfoManager():
    def __init__(self) -> None:
        self.m_infos = list()


    def load(self):
        self.m_infos.clear()
        
        if not os.path.exists('StudentInfo.json'):
             return
        
        dicls = []
        with open('StudentInfo.json', 'r') as file:
                dicls = json.load(file)

        for infodic in dicls:
             info = Student()
             info.name = infodic['Name']
             info.math_score = infodic['Math']
             info.chinese_score = infodic['Chinese']
             info.english_score = infodic['English']
             self.add(info)


    def save(self):
        dicls = []
        for info in self.m_infos:
                dic = {}
                dic['Name'] = info.name
                dic['Math'] = info.math_score
                dic['Chinese'] = info.chinese_score
                dic['English'] = info.english_score
                dicls.append(dic)

        with open('StudentInfo.json', '+w') as file:
                json.dump(dicls, file, indent = 4)


    def add(self, studentInfo):
        if self.find(studentInfo.name) != None:
            self.remove(self, studentInfo.name)

        self.m_infos.append(studentInfo)


    def find(self, name):
        for info in self.m_infos:
            if info.name == name:
                return info
            
        return None


    def remove(self, name):
        info = self.find(name)
        if info == None:
            return False
        else:
            self.m_infos.remove(info)
            return True
        
    
    def sort_by_name(self, rev):
        self.m_infos.sort(key = lambda item: item.name, reverse = rev)


    def sort_by_math(self, rev):
        self.m_infos.sort(key = lambda item: item.math_score, reverse = rev)


    def sort_by_chinese(self, rev):
        self.m_infos.sort(key = lambda item: item.chinese_score, reverse = rev)


    def sort_by_english(self, rev):
        self.m_infos.sort(key = lambda item: item.english_score, reverse = rev)