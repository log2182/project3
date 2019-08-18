#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 19:56
# @Author  : zx-long  
# @File    : src.py


from tool import user, manager

user_obj = None
user_type = None

# 登陆与注册
def login():
    global user_obj,user_type
    if user_obj:
        print('您已经登陆了')
        return
    while True:
        print('''
            =========登陆=========
            1.学生登陆
            2.教师登陆
            3.管理员登陆
            ------按q退出------
            ''')
        option = input('请选择身份登陆:')
        if option in ['1', '2', '3']:
            id = input('请输入ID：').strip()
            password = input('请输入密码：').strip()
            flg, msg = user.User.login_interface(option, id, password)    # 调用登陆接口函数，输入为用户输入的两个参数
            if flg:
                user_obj = flg
                user_type = option
                print(msg)
                break
            else:
                print(msg)
        elif option == 'q':break
        else:
            print('输入错误')


def register():
    if user_obj:
        print('您已经登陆了')
        return
    while True:
        print('''
        =======注册=======
        1.学生注册
        2.管理注册
        ---按q退出---
        ''')
        option = input('请选择:').strip()
        if option == 'q': break
        if option in ['1','2']:
            name = input('请输入姓名：').strip()
            id = input('请输入账号id:').strip()
            password = input('请输入密码').strip()
            conf_password = input('请确认密码').strip()
            if password == conf_password:
               flg, msg = user.User.register_interface(option, name, id, password)    # 调用类初始化
               if flg:
                   print(msg)
               else:
                   print(msg)
            else:
                print('两次密码不一致')

def login_out():
    global user_obj,user_type
    user_obj = None
    user_type = None
    print('Bye')


# 管理员操作
def create_teacher():
    user_obj.show_school()
    school_id = input('选择学校，输入学校id：')
    name = input('输入姓名：')
    id = input('创建ID:')
    psd = input('设置密码：')
    flg,msg = user_obj.create_teacher(school_id, name, id, psd)
    if flg:
        print(msg)
    else:
        print(msg)


def create_school():
    name = input('输入学校名称：')
    school_id = input('输入学校id：')
    flg,msg = user_obj.create_school(name,school_id)
    if flg:
        print(msg)
    else:
        print(msg)


def create_course():
    user_obj.show_school()
    school_id = input('选择学校，请输入id:')
    name = input('输入课程名称:')
    period = input('请输入课程周期:')
    price = input('请输入课程价格:')
    flg, msg = user_obj.create_course(school_id,name,period,price)
    if flg:
        print(msg)
    else:
        print(msg)

def del_course():
    user_obj.show_school()
    school_id = input('选择学校，请输入id:')
    flg,msg = user_obj.del_course(school_id)
    if flg:
        print(msg)
    else:
        print(msg)

# 学生操作
def choose_school():
    if user_obj.school_id:
        print('已经选择了学校')
    else:
        manager.Manager.show_school()
        school_id = input('请选择学校,输入学校ID:')
        flg,msg = user_obj.choose_school(school_id)
        if flg:
            print(msg)
        else:
            print(msg)

def choose_course():
    if not user_obj.school_id:
        print('还未选择学校,先选择学校吧')
        choose_school()
    else:
        user_obj.show_courses_inschool()
        option = input('请输入课程名称:')
        flg,msg = user_obj.add_course(option)
        if flg:
            print(msg)
        else:
            print(msg)

def show_score():
    user_obj.show_score()

# 教师操作
def teach_course():
    user_obj.show_courses_inschool()
    option = input('请输入课程名称:')
    flg, msg = user_obj.add_course(option)
    if flg:
        print(msg)
    else:
        print(msg)

def show_courses():
    user_obj.show_courses()

def show_students():
    user_obj.show_students()

def set_score():
    show_students()
    course = input('请选择课程:')
    id = input('请输入学生ID')
    score = input('设置分数为：')
    flg,msg = user_obj.set_score(course,id,score)
    if flg:
        print(msg)
    else:
        print(msg)

func_dic_mng = {
    '1':create_school,
    '2':create_teacher,
    '3':create_course,
    '4':del_course,
    '5':login_out,
}

func_dic_tea = {
    '1':teach_course,
    '2':show_courses,
    '3':show_students,
    '4':set_score,
    '5':login_out
}

func_dic_stu = {
    '1': choose_school,
    '2':choose_course,
    '3':show_score,
    '4':login_out,
}

menu_dic_stu = '''
1.选学校
2.选课程
3.查看分数
4.退出
'''

menu_dic_teac = '''
1.选课
2.查看课程
3.查看学生
4.设置分数
5.退出登陆
'''

menu_dic_mng = '''
1.创建学校
2.创建教师
3.创建课程
4.删除课程
5.退出登录
'''
menu_dic = {'1': menu_dic_stu, '2': menu_dic_teac, '3': menu_dic_mng}
func_dic = {'1': func_dic_stu, '2': func_dic_tea, '3': func_dic_mng}
def run():
    while True:
        print('''
        1、登录
        2、注册
        -----q退出------
        ''')
        choice = input('请选择:').strip()
        if choice == '1':
            login()
            while user_obj:
                print(menu_dic[user_type])
                func = func_dic[user_type]
                option = input('选择:')
                if option.isdigit() and 0 < int(option) <= len(func):
                    func[option]()
        elif choice == '2':
            register()
        elif choice == 'q':
            break
        else:
            print('输入有误')
