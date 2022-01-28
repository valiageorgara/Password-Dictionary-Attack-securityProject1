import nacl.pwhash
import string
import random
from random import randrange
import csv
from colorama import Fore, Style
from nacl.exceptions import InvalidkeyError

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    """
    url: https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python
    :return: hash

    """

    length = randrange(8, 16)
    random.shuffle(characters)
    random_password = []
    for j in range(length):
        random_password.append(random.choice(characters))
    random.shuffle(random_password)
    return "".join(random_password)


def get_username(number):
    if len(str(number)) == 1:
        return 'user00' + str(number)
    elif len(str(number)) == 2:
        return 'user0' + str(number)
    elif len(str(number)) == 3:
        return 'user' + str(number)
    else:
        raise Exception('Invalid User Counter ' + str(number))


user_and_pass = {}
user_and_hash_pass = {}
all_hash_pass = []
common_pass = []
TOTAL_USERS = 10
leaked_data = {}
leaked_users = []

answer_1 = input(
    'Welcome to crack master by Valia Georgara.\n'
    'This program is about to check 9800 common passwords of 2021 from a kaggle dataset.\n'
    'This may take a while, so if you want to reduce the execution time type yes, otherwise press any button...\n'
)
num_to_check = 10000
if answer_1 == 'yes':
    answer_2 = input('Nice, now you can specify the number of common passwords to check in range [10, 9800], for example 10: ')
    try:
        num_to_check = int(answer_2)
        if num_to_check < 10 or num_to_check > 9800:
            raise Exception
    except ValueError:
        print("That's not a number! Now I'm gonna check all 9800 common passwords...Press ctrl+C if you want to try again.")
        num_to_check = 10000
    except Exception:
        print("Number not in range 10-9281! Now I'm gonna check all 9800 common passwords...Press ctrl+C if you want to try again.")
        num_to_check = 10000
else:
    print("Okay...let's check them all.")

# Get Common Password from kaggle
# https://www.kaggle.com/prasertk/`top-200-common-passwords-in-2021/data?select=top_200_password_2020_by_country.csv

c = 0
with open('./top_200_password_2020_by_country.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for row in reader:
        if row[3] == "Password":
            continue
        if c > (num_to_check - 1):
            break
        c = c + 1
        common_pass.append(row[3])

c1 = 0
c2 = 0
for i in range(TOTAL_USERS):
    if randrange(100) > 70:
        c1 = c1 + 1

        password = bytes(common_pass[randrange(len(common_pass))], 'utf-8')
        user_and_hash_pass[get_username(i)] = nacl.pwhash.str(password)
        user_and_pass[get_username(i)] = password
        # print(get_username(i))
        # print(password)
    else:
        c2 = c2 + 1
        password = bytes(generate_random_password(), 'utf-8')
        user_and_hash_pass[get_username(i)] = nacl.pwhash.str(password)
        user_and_pass[get_username(i)] = password

# print(c1, c2)
# print(user_and_hash_pass)
# print(user_and_pass)

with open('users_data.csv', 'w') as file1:
    writer = csv.writer(file1)
    for key, value in user_and_hash_pass.items():
        writer.writerow([key, value])

for k in user_and_hash_pass.keys():
    print('\n' + Style.BRIGHT + Fore.WHITE + '[INFO] Checking user: ' + k)
    for c_pass in common_pass:
        try:
            if nacl.pwhash.verify(user_and_hash_pass[k], bytes(c_pass, encoding='utf-8')):
                print(Style.BRIGHT + Fore.LIGHTRED_EX + '[WARNING] FOUND LEAK FOR: ' + k)
                leaked_data[k] = c_pass
                break
        except InvalidkeyError as e:
            pass

print()

with open('leaked_data.csv', 'w') as file:
    writer = csv.writer(file)
    for key, value in leaked_data.items():
        writer.writerow([key, value])
print('Data written in csv file.')
print(leaked_data)

