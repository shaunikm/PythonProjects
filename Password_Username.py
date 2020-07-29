import time

loopi = True

global k
k = 0

error_message = "\u001b[31mError: Invalid Response\u001b[0m"

loop_signup = False
loop_login = False
back_security = False

user_list = {
}


while loopi is True:
    global username
    global password
    global password_new
    global password_ask
    global pass_check_change
    loop_start = input("Hello! Do you want to sign up or log in? ")
    starter = True
    security_start = False
    loop_signup = False
    loop_login = False
    back_security = False
    loop_dec = False
    repeat_acc = False
    Task_settings = False
    user_pass = False
    weak = True
    x = 40*"\n"

    def change_password_l(juser):
        global password
        global password_new
        juser.pop(user_check_change)
        juser[user_check_change] = password_new

    def change_password(juser):
        global user_check_change
        global password_new
        juser.pop(user_check_change)
        juser[user_check_change] = password_new


    def user_create(juser):
        juser[username] = password
        return k


    def pass_encryption(kgf):
        re = str(kgf.replace("a", "!"))
        re = str(re.replace("b", "@"))
        re = str(re.replace("c", "#"))
        re = str(re.replace("d", "$"))
        re = str(re.replace("e", "("))
        re = str(re.replace("f", "_"))
        re = str(re.replace("g", "3"))
        re = str(re.replace("h", "/"))
        re = str(re.replace("i", "{"))
        re = str(re.replace("j", "B"))
        re = str(re.replace("k", "p"))
        re = str(re.replace("l", "&"))
        re = str(re.replace("m", "4"))
        re = str(re.replace("n", "q"))
        re = str(re.replace("o", "="))
        re = str(re.replace("p", "Z"))
        re = str(re.replace("q", "["))
        re = str(re.replace("r", "J"))
        re = str(re.replace("s", "2"))
        re = str(re.replace("t", "w"))
        re = str(re.replace("u", "v"))
        re = str(re.replace("v", "M"))
        re = str(re.replace("w", "L"))
        re = str(re.replace("x", "+"))
        re = str(re.replace("y", "\\"))
        re = str(re.replace("z", "\""))
        re = str(re.replace("1", "O"))
        re = str(re.replace("2", "."))
        re = str(re.replace("3", "j"))
        re = str(re.replace("4", "?"))
        re = str(re.replace("5", "S"))
        re = str(re.replace("6", "}"))
        re = str(re.replace("7", "Y"))
        re = str(re.replace("8", "W"))
        re = str(re.replace("9", "Q"))
        re = str(re.replace("0", "%"))
        re = str(re.replace("!", "1"))
        re = str(re.replace("@", "T"))
        re = str(re.replace("#", "U"))
        re = str(re.replace("$", "9"))
        re = str(re.replace("%", "G"))
        re = str(re.replace("^", "P"))
        re = str(re.replace("^", "N"))
        re = str(re.replace("&", "*"))
        re = str(re.replace("*", "&"))
        re = str(re.replace("(", "-"))
        re = str(re.replace(")", "H"))
        re = str(re.replace("_", "="))
        re = str(re.replace("-", "8"))
        re = str(re.replace("+", "{"))
        re = str(re.replace("=", "X"))
        re = str(re.replace("|", "R"))
        re = str(re.replace("\\", "H"))
        re = str(re.replace("{", ";"))
        re = str(re.replace("[", "]"))
        re = str(re.replace("]", "["))
        re = str(re.replace("}", "("))
        return re


    i = bool(loop_start)
    lowerloop_start = str(loop_start.lower())

    if starter is True and lowerloop_start == "sign up" or lowerloop_start == "signup":
        starter = False
        print("\n\u001b[37mDO NOT MAKE YOUR USERNAME AND PASSWORD THE SAME FOR SECURITY REASONS")
        username = input("Username: ")
        print("\n ")
        print("(Your password will be encrypted after you make an account and until you want it to be decrypted)")
        password = input("Password: \u001b[0m")
        if username in user_list and bool(user_list) is True:
            print("\u001b[31mUsername already taken\u001b[0m")
            repeat_acc = True
            time.sleep(2)
            print(x)
        if username == password:
            user_pass = True
            print("\u001b[31mYour username and password cannot be the same\u001b[0m")
            time.sleep(2)
            print(x)
        elif username != password:
            user_pass = False
        if password in user_list.values():
            print("\u001b[31mWeak password. Try a different one.\u001b[0m")
            time.sleep(2)
            print(x)
            weak = False
        elif password not in user_list:
            weak = True
        encrypted_password = pass_encryption(password)
        encrypted_username = pass_encryption(username)
        if repeat_acc is False and user_pass is False and weak is True:
            user_create(user_list)
            loop_signup = True
        elif repeat_acc is True:
            loop_signup = False
        if user_pass is True:
            loop_signup = False
        if weak is False:
            loop_signup = False
        while loop_signup is True:
            encrypted_username = pass_encryption(username)
            encrypted_password = pass_encryption(password)
            back_security = True
            print(x)
            print("Menu")
            print("---------------------------------------------------------")
            print("Settings\nSecurity\n\u001b[31mLOG OUT\u001b[0m")
            Taskl = input("What do you want to select? ")
            lowerTaskl = str(Taskl.lower())
            if lowerTaskl == "log out" or lowerTaskl == "logout":
                print(x)
                loop_signup = False
            elif lowerTaskl == "security":
                security_start = True
                while security_start is True:
                    back_security = True
                    loop_dec = False
                    print(x)
                    print("Security")
                    print("---------------------------------------------------------")
                    print("Encrypted Username: " + encrypted_username)
                    print("Encrypted Password: " + encrypted_password)
                    print("\u001b[37mDecrypt\u001b[0m")
                    print("\u001b[37mChange Password\u001b[0m")
                    print("\u001b[31mBACK\u001b[0m")

                    if back_security is True:
                        Task_security = input("What do you want to select? ")
                        Task_security_lower = Task_security.lower()

                        if Task_security_lower == "back" and back_security is True:
                            break
                        elif Task_security_lower == "change password" or Task_security_lower == "changepassword" and back_security is True:
                            print("To carry this function out, you will need to enter your account information")
                            user_check_change = input("\u001b[37mUsername: ")
                            pass_check_change = input("Password: \u001b[0m")
                            if user_check_change in user_list and user_list.get(user_check_change) == pass_check_change:
                                print(x)
                                password_new = input("\u001b[37mWhat would you like to change your password to? \u001b[0m")
                                if password_new in user_list.values():
                                    print("\u001b[31mWeak password. Try a different one.\u001b[0m")
                                    time.sleep(2)
                                    print(x)
                                elif password_new not in user_list.values():
                                    change_password(user_list)
                                encrypted_username = pass_encryption(username)
                                encrypted_password = pass_encryption(password_new)
                                password = password_new

                            else:
                                print("\u001b[31mWrong username or password\u001b[0m")
                                time.sleep(2)
                        elif Task_security_lower == "decrypt":
                            print("To carry this function out, you will need to enter your account information")
                            user_check = input("\u001b[37mUsername: ")
                            pass_check = input("Password: \u001b[0m")
                            if user_check in user_list and user_list.get(user_check) == pass_check:
                                loop_dec = True
                                break
                            else:
                                print("\u001b[31mWrong username or password\u001b[0m")
                                time.sleep(2)

                        else:
                            print(error_message)
                            time.sleep(2)

                while loop_dec is True:
                    encrypted_username = pass_encryption(username)
                    encrypted_password = pass_encryption(password)
                    print(x)
                    print("\u001b[0mSecurity")
                    print("---------------------------------------------------------")
                    print("Username: " + username)
                    print("Password: " + password)
                    print("\u001b[37mChange Password\u001b[0m")
                    print("\u001b[31mBACK\u001b[0m")
                    Task_security = input("What do you want to select? ")
                    Task_security_lower = Task_security.lower()

                    if Task_security_lower == "back" and back_security is True:
                        break
                    elif Task_security_lower == "change password" or Task_security_lower == "changepassword" and back_security is True:
                        print("To carry this function out, you will need to enter your account information")
                        user_check_change = input("\u001b[37mUsername: ")
                        pass_check_change = input("Password: \u001b[0m")
                        if user_check_change in user_list and user_list.get(user_check_change) == pass_check_change:
                            print(x)
                            password_new = input("\u001b[37mWhat would you like to change your password to? \u001b[0m")
                            if password_new not in user_list.values():
                                change_password(user_list)
                                password = password_new
                            elif password_new in user_list.values():
                                print("\u001b[31mWeak password. Try a different one.\u001b[0m")
                                time.sleep(2)
                                print(x)

                        else:
                            print("\u001b[31mWrong username or password\u001b[0m")
                            time.sleep(2)
                    else:
                        print(error_message)
                        time.sleep(2)
            elif lowerTaskl == "settings":
                Task_settings = True
                while Task_settings is True:
                    print(x)
                    print("\u001b[0mNothing here yet!\u001b[0m")
                    print("\u001b[31mBACK\u001b[0m")
                    Task_setting_task = input("\u001b[0mWhat do you want to select? \u001b[0m")
                    Task_setting_task_lower = Task_setting_task.lower()
                    if Task_setting_task_lower == "back":
                        break
                    else:
                        print(error_message)
                        time.sleep(2)
            else:
                print(error_message)
                time.sleep(2)

    elif starter is True and lowerloop_start == "login" or lowerloop_start == "log in" and bool(user_list) is False:
        print("\u001b[31mError: No user accounts have been made yet\u001b[0m")
        starter = False
        time.sleep(2)
        print(x)

    elif starter is True and lowerloop_start == "login" or lowerloop_start == "log in" and bool(user_list) is True:
        starter = False
        username_ask = input("\u001b[37mUsername: ")
        print("\n ")
        print("(Your password will be encrypted after you make an account and until you want it to be decrypted)")
        password_ask = input("Password: \u001b[0m")
        encrypted_username = pass_encryption(username_ask)
        encrypted_password = pass_encryption(password_ask)
        if user_list.get(username_ask) == password_ask:
            loop_login = True
        else:
            print("\u001b[31mWrong username or password\u001b[0m")
            time.sleep(2)
            print(x)
        while loop_login is True:
            print(x)
            print("Menu")
            print("---------------------------------------------------------")
            print("Settings\nSecurity\n\u001b[31mLOG OUT\u001b[0m")
            Task = input("What do you want to select? ")
            lowerTask = str(Task.lower())
            print(lowerTask)
            if lowerTask == "log out" or lowerTask == "logout":
                print(x)
                loop_login = False
            elif lowerTask == "settings":
                print("john likes pie:)))")
                Task_settings = True
                while Task_settings is True:
                    print(x)
                    print("\u001b[0mNothing here yet!\u001b[0m")
                    print("\u001b[31mBACK\u001b[0m")
                    Task_setting_task = input("\u001b[0mWhat do you want to select? \u001b[0m")
                    Task_setting_task_lower = Task_setting_task.lower()
                    if Task_setting_task_lower == "back":
                        break
                    else:
                        print(error_message)
                        time.sleep(2)
            elif lowerTask == "security":
                security_start = True
                while security_start is True:
                    back_security = True
                    loop_dec = False
                    print(x)
                    print("Security")
                    print("---------------------------------------------------------")
                    print("Encrypted Username: " + encrypted_username)
                    print("Encrypted Password: " + encrypted_password)
                    print("\u001b[37mDecrypt\u001b[0m")
                    print("\u001b[37mChange Password\u001b[0m")
                    print("\u001b[31mBACK\u001b[0m")

                    if back_security is True:
                        Task_security = input("What do you want to select? ")
                        Task_security_lower = Task_security.lower()

                        if Task_security_lower == "back" and back_security is True:
                            break
                        elif Task_security_lower == "change password" or Task_security_lower == "changepassword" and back_security is True:
                            print("To carry this function out, you will need to enter your account information")
                            user_check_change = input("\u001b[37mUsername: ")
                            pass_check_change = input("Password: \u001b[0m")
                            if user_check_change in user_list and user_list.get(user_check_change) == pass_check_change:
                                print(x)
                                password_new = input("\u001b[37mWhat would you like to change your password to? \u001b[0m")
                                if password_new not in user_list.values():
                                    change_password_l(user_list)
                                    password_ask = password_new
                                    encrypted_username = pass_encryption(username_ask)
                                    encrypted_password = pass_encryption(password_ask)
                                elif password in user_list.values():
                                    print("\u001b[31mWeak password. Try a different one.\u001b[0m")
                                    time.sleep(2)
                                    print(x)
                            else:
                                print("\u001b[31mWrong username or password\u001b[0m")
                                time.sleep(2)
                        elif Task_security_lower == "decrypt":
                            print("To carry this function out, you will need to enter your account information")
                            user_check = input("\u001b[37mUsername: ")
                            pass_check = input("Password: \u001b[0m")
                            if user_check in user_list and user_list.get(user_check) == pass_check:
                                loop_dec = True
                                break
                            else:
                                print("\u001b[31mWrong username or password\u001b[0m")
                                time.sleep(2)

                        else:
                            print(error_message)
                            time.sleep(2)

                while loop_dec is True:
                    encrypted_username = pass_encryption(username_ask)
                    encrypted_password = pass_encryption(password_ask)
                    print(x)
                    print("\u001b[0mSecurity")
                    print("---------------------------------------------------------")
                    print("Username: " + username)
                    print("Password: " + password_ask)
                    print("\u001b[37mChange Password\u001b[0m")
                    print("\u001b[31mBACK\u001b[0m")
                    Task_security = input("What do you want to select? ")
                    Task_security_lower = Task_security.lower()

                    if Task_security_lower == "back" and back_security is True:
                        break
                    elif Task_security_lower == "change password" or Task_security_lower == "changepassword" and back_security is True:
                        print("To carry this function out, you will need to enter your account information")
                        user_check_change = input("\u001b[37mUsername: ")
                        pass_check_change = input("Password: \u001b[0m")
                        if user_check_change in user_list and user_list.get(user_check_change) == pass_check_change:
                            print(x)
                            password_new = input("\u001b[37mWhat would you like to change your password to? \u001b[0m")
                            if password_new in user_list.values():
                                print("\u001b[31mWeak password. Try a different one.\u001b[0m")
                                time.sleep(2)
                                print(x)
                            elif password_new not in user_list.values():
                                change_password_l(user_list)
                                password_ask = password_new

                        else:
                            print("\u001b[31mWrong username or password\u001b[0m")
                            time.sleep(2)
                    else:
                        print(error_message)
                        time.sleep(2)
            else:
                print(error_message)
                time.sleep(2)

    elif starter is True or lowerloop_start != "sign up" or lowerloop_start != "signup" or lowerloop_start != "login" or lowerloop_start != "log in":
        error_message.strip()
        print(error_message)
        time.sleep(2)
        print(x)
        i = True
        starter = False