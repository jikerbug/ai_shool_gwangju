#import sqlite3
import json
import sqlite3
import sys

default_json_dictionary = {
          "students": [
                  {
                           "이름" : "임지백",
                                "나이" : "23",
                                     "직업" : "학생",
                                          "id" : "wlqor98",
                                               "비밀번호" : "dlagus123"
                                                   },
                      {
                               "이름" : "임백지",
                                    "나이" : "22",
                                         "직업" : "프로그래머",
                                              "id" : "paper123",
                                                   "비밀번호" : "t11355422"
                                                       } 
                        ]
          }

JSON_PATH = 'data.json'


def save_data(students_data, student):
      if(student.get('id') == None or student.get('id') == '' ):
                  print("id가 없습니다")
                    else:
                            students_data['students'].append(student)
                                set_data(students_data)
                                  


                                  def set_data(dictionary):
                                        with open(JSON_PATH, "w", encoding="UTF-8") as json_file:
                                                  json.dump(dictionary, json_file,ensure_ascii=False)


                                                  def load_data(data_path):
                                                          with open(JSON_PATH, "r", encoding="UTF-8") as fp:
                                                                      data = json.load(fp)
                                                                          return data


                                                                      set_data(default_json_dictionary)


                                                                      students_data = load_data(JSON_PATH)


                                                                      for student in students_data["students"]:
                                                                                print(student['이름'])

                                                                                student_young = {
                                                                                             "이름" : "백지임",
                                                                                                  "나이" : "18",
                                                                                                       "직업" : "고등학생",
                                                                                                            "id" : "hello",
                                                                                                                 "비밀번호" : "1234"
                                                                                                                     } 
                                                                                #sys.exit()

                                                                                save_data(students_data, student_young)
                                                                                students_data = load_data(JSON_PATH)

                                                                                print("-----------------")

                                                                                def print_student(students_data):
                                                                                            
                                                                                      for student in students_data["students"]:
                                                                                                  print(student['이름'])
                                                                                                  print_student(students_data)


                                                                                                  print("-----------------")
                                                                                                  def print_under_20(students_data):      
                                                                                                        for student in students_data["students"]:
                                                                                                                    if(int(student['나이']) < 20):    
                                                                                                                                  print(student['이름'] + "는(은) 20살 미만입니다")
                                                                                                                                  print_under_20(students_data)

                                                                                                                                  student_error = {
                                                                                                                                               "이름" : "백지임",
                                                                                                                                                    "나이" : "18",
                                                                                                                                                         "직업" : "고등학생",
                                                                                                                                                              "비밀번호" : "1234"
                                                                                                                                                                  } 

                                                                                                                                  save_data(students_data,student_error)


                                                                                                                                  student_default = {
                                                                                                                                               "이름" : "",
                                                                                                                                                    "나이" : "",
                                                                                                                                                         "직업" : "",
                                                                                                                                                              "id" : "",
                                                                                                                                                                   "비밀번호" : ""
                                                                                                                                                                       } 

                                                                                                                                  def add_data(students_data):
                                                                                                                                          student_default = {
                                                                                                                                                       "이름" : "",
                                                                                                                                                            "나이" : "",
                                                                                                                                                                 "직업" : "",
                                                                                                                                                                      "id" : "",
                                                                                                                                                                           "비밀번호" : ""
                                                                                                                                                                               } 
                                                                                                                                              student_default["이름"] = input("이름을 입력해주세요: \n")
                                                                                                                                                  student_default["나이"] = input("나이를 입력해주세요: \n")
                                                                                                                                                      student_default["직업"] = input("직업을 입력해주세요: \n")
                                                                                                                                                          student_default["id"] = input("id를 입력해주세요: \n")
                                                                                                                                                              student_default["비밀번호"] = input("비밀번호를 입력해주세요: \n")
                                                                                                                                                                  save_data(students_data, student_default)

                                                                                                                                                                  add_data(students_data)
                                                                                                                                                                  print_under_20(students_data)
                                                                                                                                                                        







                                                                                                                                                                        #conn = sqlite3.connect('aischool.db')
                                                                                                                                                                        #cur = conn.cursor()

                                                                                                                                                                        #insert_student = "INSERT INTO students VALUES (?,?,?);"

                                                                                                                                                                        #data = ['홍길동', 20, 'Seoul']



                                                                                                                                                                        #sql = """CREATE TABLE students (
                                                                                                                                                                                  #studentName Text NOT NULL,
                                                                                                                                                                                            #studentAge INT,
                                                                                                                                                                                                      #studentHome Text);
                                                                                                                                                                                                      #"""
                                                                                                                                                                                                      #cur.execute(sql)
                                                                                                                                                                                                      #conn.commit()

                                                                                                                                                                                                      #cur.execute(insert_student,data)
                                                                                                                                                                                                      #conn.commit()



