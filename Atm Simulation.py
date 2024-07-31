import getpass

# Load user data from files
def load_data():
    with open('pins.txt', 'r') as pin_file:
        pins = pin_file.read().splitlines()
    return pins

# Save updated PINs back to the file
def save_data(pins):
    with open('pins.txt', 'w') as pin_file:
        pin_file.write('\n'.join(pins))

users = ['sagheer', 'rohith', 'babu']
pins = load_data()
amounts = [10000, 20000, 30000]
count = 0

print("****************************************************************************")
print("*                                                                          *")
print("*                             WELCOME TO ICICI BANK                        *")
print("*                                                                          *")
print("****************************************************************************")

while True:
    user = input('\nENTER USER NAME: ').lower()
    if user in users:
        n = users.index(user)
        break
    else:
        print('INVALID USERNAME')

while count < 3:
    pin = getpass.getpass('PLEASE ENTER PIN: ')
    if pin.isdigit() and pin == pins[n]:
        break
    else:
        count += 1
        print('INVALID PIN\n')

if count == 3:
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    exit()

print('LOGIN SUCCESSFUL, CONTINUE\n')
print(str.capitalize(users[n]), 'welcome to ATM')

while True:
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposite__(D)  \nChange PIN_(P)  \nQuit_______(Q) \nType The Letter Of Your Choice: ').lower()
    
    if response == 's':
        print(f"{str.capitalize(users[n])}, YOU HAVE {amounts[n]} RUPEES IN YOUR ACCOUNT.")
        
    elif response == 'w':
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        if cash_out % 100 != 0:
            print('AMOUNT YOU WANT TO WITHDRAW MUST BE A MULTIPLE OF 100 RUPEES')
        elif cash_out > amounts[n]:
            print('YOU HAVE INSUFFICIENT BALANCE')
        else:
            amounts[n] -= cash_out
            print('YOUR NEW BALANCE IS:', amounts[n], 'RUPEES')
            
    elif response == 'd':
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT: '))
        if cash_in % 100 != 0:
            print('AMOUNT YOU WANT TO DEPOSIT MUST BE A MULTIPLE OF 100 RUPEES')
        else:
            amounts[n] += cash_in
            print('YOUR NEW BALANCE IS:', amounts[n], 'RUPEES')
            
    elif response == 'p':
        new_pin = getpass.getpass('ENTER A NEW PIN: ')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            new_ppin = getpass.getpass('CONFIRM NEW PIN: ')
            if new_ppin != new_pin:
                print('PIN MISMATCH')
            else:
                pins[n] = new_pin
                save_data(pins)
                print('NEW PIN SAVED')
        else:
            print('NEW PIN MUST CONSIST OF 4 DIGITS AND MUST BE DIFFERENT FROM THE PREVIOUS PIN')
        
    elif response == 'q':
        print('THANK YOU FOR USING ICICI BANK ATM. HAVE A NICE DAY!')
        break
        
    else:
        print('RESPONSE NOT VALID')
