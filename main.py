from ui import UI
from stu import Student
from service import StudentInfoManager

def add(userinterface, info_manager):
    userinterface.show_message('--------------------录入学生信息------------------------')
    while True:
        student_info = userinterface.get_student_info()
        info_manager.add(student_info)

        userinterface.show_message('录入成功！')

        if not userinterface.is_continue('录入学生信息'):
            break


def find(userinterface, info_manager):
    userinterface.show_message('--------------------查找学生信息------------------------')
    while True:
        name = userinterface.get_student_name()

        info = info_manager.find(name)

        if info != None:
            userinterface.show_info(info)
        else:
            userinterface.show_message('没有找到%s的信息!' % name)

        if not userinterface.is_continue('查找学生信息'):
            break


def del_info(userinterface, info_manager):
    userinterface.show_message('--------------------删除学生信息------------------------')
    while True:
        name = userinterface.get_student_name()

        ret = info_manager.remove(name)

        if ret:
            userinterface.show_message('删除成功！')
        else:
            userinterface.show_message('没有找到%s的信息，删除失败!' % name)

        if not userinterface.is_continue('删除学生信息'):
            break


def modify(userinterface, info_manager):
    userinterface.show_message('--------------------修改学生信息------------------------')
    while True:
        name = userinterface.get_student_name()

        info = info_manager.find(name)

        if info == None:
            userinterface.show_message('没有找到%s的信息!' % name)
        else:
            new_info = userinterface.get_student_info()
            info_manager.remove(info.name)
            info_manager.add(new_info)
            userinterface.show_message('修改成功！')

        if not userinterface.is_continue('修改学生信息'):
            break


def sort_info(userinterface, info_manager):
    userinterface.show_message('--------------------学生信息排序------------------------')
    opt = userinterface.get_sort_option()

    if opt[0] == 1:
        info_manager.sort_by_name(opt[1] == False)
    elif opt[0] == 2:
        info_manager.sort_by_math(opt[1] == False)
    elif opt[0] == 3:
        info_manager.sort_by_chinese(opt[1] == False)
    elif opt[0] == 4:
        info_manager.sort_by_english(opt[1] == False)
    
    userinterface.show_message('排序成功！')


def count(userinterface, info_manager):
    userinterface.show_message('--------------------统计学生人数------------------------')
    userinterface.show_message('当前学生人数为：%d' % info_manager.m_infos.__len__())
    userinterface.show_message('------------------------------------------------------')


def show_list(userinterface, info_manager):
    userinterface.show_message('--------------------所有学生信息------------------------')
    userinterface.show_infos(info_manager.m_infos)
    userinterface.show_message('------------------------------------------------------')


def save(userinterface, info_manager):
    userinterface.show_message('--------------------保存------------------------')
    info_manager.save()
    userinterface.show_message('保存成功!')


if __name__ == '__main__':
    userinterface = UI()
    info_manager = StudentInfoManager();
    info_manager.load()

    while True:
        # 从UI获取用户选项
        option = userinterface.main_ui()

        # 退出
        if option == 0:
            break
        
        # 异常退出
        elif option == -1:
            userinterface.show_message('程序异常，已自动结束！')
            break

        # 录入学生信息
        elif option == 1:
            add(userinterface, info_manager)

        # 查找学生信息
        elif option == 2:
            find(userinterface, info_manager)

        # 删除学生信息
        elif option == 3:
            del_info(userinterface, info_manager)

        # 修改学生信息
        elif option == 4:
            modify(userinterface, info_manager)

        # 排序
        elif option == 5:
            sort_info(userinterface, info_manager)

        # 统计学生人数
        elif option == 6:
            count(userinterface, info_manager)

        # 显示所有学生信息
        elif option == 7:
            show_list(userinterface, info_manager)

        # 保存数据
        elif option == 8:
            save(userinterface, info_manager)

        userinterface.show_message('\n')
