i=0
while i < 3:
    user_name = input("name: ")
    password = input("password: ")
    if user_name == "lzy" and password =="lizeyu":
        print("登录成功")
        i=8
    elif i <2:
        print("密码不正确！你还有",2-i,"次机会！")
        i+=1
    else:
        print("登录失败！")
        break