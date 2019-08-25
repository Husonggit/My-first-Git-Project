_author_ = 'husong'


passwd = 'test'
exit_flag = False
for i in range(3):
    user_input = input("please input you passwd: ").strip()
    if len(user_input) == 0:continue
    if user_input == passwd:
        print ("welcome login!")
        while True:
            user_choice = input('''
                1.run a cmd
                2. send a file
                3. exit this level
                4. exit the whole system
                ''').strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print ("going to run cmd")
            if user_choice == 2:
                print ("going to send a file")
            if user_choice == 3:
                print ("going to exit this level")
                break
            if user_choice == 4:
                print ("going to logout ")
                exit_flag = True
                break
        print ("-----going to do something else... ") 
        if exit_flag == True:
            break           
    if i == 2:
        print ("you have no chance")
        break
    print ("please try again")
    
