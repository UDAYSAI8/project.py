# project.py
from marks_mod import *
while True:
    print('''1.show all student marks
         2.search student marks
         3.edit student data
         4.delete student data
         5.add student data
         6.exit''')
    acti_select = int(input('enter the desired option:'))
    print('''---------------------------------------------------------------------------------------------------------------------------''')
    if acti_select == 1:
        show_all_marks()
    elif acti_select == 2:
        show_stu_marks()
    elif acti_select == 3:
        edit_marks()
    elif acti_select == 4:
        delete_marks()
    elif acti_select == 5:
        add_marks()
    else:
        break
