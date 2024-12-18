import time

print("Please Insert Your Card!")

time.sleep(5)

balance = 5000 

password = 1234 

pin = int(input("Please Enter your pin: "))


if pin == password:

        while True:

            print(""" 
            1 == balance 
            2 == withdraw_amount
            3 == Deposit_amount
            4 == Exit """)
            
            try:
                option = int(input("Please enter your choice: ")) 

            except:
                print("Please choose valid option: ")    


            if option == 1:
                print(f"Your current balance is {balance}")

            if option == 2:
                withdraw_amount  = int(input("Please Enter your withdraw amount: "))

                balance = balance - withdraw_amount 

                print(f"{withdraw_amount} is debited from your account")

                print(f"Your Current Balance is {balance}")

            if option == 3:

                deposit_amount = int(input("Please Enter Your Deposit amount: "))

                balance = balance + deposit_amount 

                print(f"{deposit_amount} is Credited to your account")

                print(f"Your Current Balnce is {balance}")

            if option == 4:

                print("Please visit again!")

                break

else:
    print("Incorrect Pin! Please try again.")    

