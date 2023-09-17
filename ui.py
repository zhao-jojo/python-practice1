from stu import Student

# 用户交互
class UI():
    # 显示主界面
    def main_ui(self):
        print('=======================学生信息管理系统============================')
        print('--------------------------功能菜单--------------------------------')
        print('\t\t1.录入学生信息')
        print('\t\t2.查找学生信息')
        print('\t\t3.删除学生信息')
        print('\t\t4.修改学生信息')
        print('\t\t5.排序')
        print('\t\t6.统计学生总人数')
        print('\t\t7.显示所有学生信息')
        print('\t\t8.保存')
        print('\t\t0.退出系统')
        print('----------------------------------------------------------------')

        nval = -1
        while nval < 0:
            option = UI.__get_option(self)
            if option.__len__() != 2:
                break

            nval = option[0]

            if nval < 0:
                print(option[1])

        return nval
    
    
    # 获取学生信息
    def get_student_info(self):
        stu = Student()
        stu.name = UI.get_student_name(self)
        stu.math_score = UI.__get_student_score(self, '数学')
        stu.chinese_score = UI.__get_student_score(self,'语文')
        stu.english_score = UI.__get_student_score(self,'英语')
        return stu
    
    # 获取是否继续当前操作
    def is_continue(self, action_name):
        action_name = '是否继续%s?(y/n)' % action_name

        while True:
            val = input(action_name)

            if val == 'y':
                return True
            
            elif val == 'n':
                return False
            
            else:
                print('输入错误，请重新输入！')


    # 显示信息
    def show_message(self, msg):
        print(msg)

    
    # 显示学生信息
    def show_info(self, info, show_title = True):
        if show_title:
            print('姓名\t数学\t语文\t英语')

        print(info.name, end='\t')
        print(info.math_score, end='\t')
        print(info.chinese_score, end='\t')
        print(info.english_score)

    # 显示所有学生信息
    def show_infos(self, infos):
        show_title = True
        for info in infos:
            self.show_info(info, show_title)
            show_title = False


    # 获取学生名字
    def get_student_name(self):
        name = ''
        while name.__len__() == 0:
            name = input('请输入学生姓名：')
            if name.__len__() == 0:
                print('学生姓名不能为空，请重新输入！')
        
        return name

    # 获取排序选项
    def get_sort_option(self):
        # 需要排序的科目
        item = 1
        while True:
            print('排序列：')
            print('\t1.姓名')
            print('\t2.数学成绩')
            print('\t3.语文成绩')
            print('\t4.英语成绩')
            val = input('请选择：')

            if val.isdecimal():
                item = int(val)
                if item > 0 and item <= 4:
                    break

            print('输入错误请重新输入！')

        type = True
        while True:
            val = input('是否升序排列(y/n):')

            if val == 'y':
                type = True
                break

            if val == 'n':
                type = False
                break

            print('输入错误请重新输入！')
        
        return item, type


    # 获取用户主界面输入选项
    def __get_option(self):
        strinput = input('请选择：')

        errMsg = '输入内容必须为0-8范围内整数，请重新输入!'
        # 输入内容必须为0-7范围内整数
        if strinput.isdecimal():
            nval = int(strinput)
            if nval >= 0 and nval <= 8:
                return nval, errMsg

        return -1, errMsg
    

    # 获取学生成绩
    def __get_student_score(self, scorename):
        scorename = '请输入%s成绩：' % scorename
        strinput = ''
        score = 0.0
        finish = False
        while not finish:
            strinput = input(scorename)

            if not strinput.isnumeric():
                print('学生成绩必须为0-100间的数字，请重新输入！')
                continue

            score = float(strinput)
            if score < 0.0 or score > 100.0:
                print('学生成绩必须为0-100间的数字，请重新输入！')
                continue

            finish = True

        return score


        

