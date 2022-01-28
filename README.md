# Store Password Hashes and find common passwords

A python script that simulates a scenario where an attacker 
has a list of usernames and their hashes. The attacker has to hash 
a list of common hashes to see if they match any user of the list.

## Requirements

`pip install -r requirements.txt`

## Usage

`python ./password_hashing.py`

A message is prompted to the screen stating that it is about to check many common passwords, so you need to specify how many.

## Example

```
Welcome to crack master by Valia Georgara.
This program is about to check 9800 common passwords of 2021 from a kaggle dataset.
This may take a while, so if you want to reduce the execution time type yes, otherwise press any button...
```
At this point you should type "yes".

```
Nice, now you can specify the number of common passwords to check in range [10, 9800], for example 10:
```
At this point, you should type the number of common passwords you wish to check.
I recommend typing 10, to reduce even more the execution time, but you are welcome to type whatever.

## Quick Summary

After selecting the number of common passwords to check, the script creates 10 usernames/passwords randomly generated to be hard to crack and always makes sure to replace 30% of those passwords with common ones.
The leaked data is written to a file after the execution, named "leaked_data.csv".

## Contributing
Pull requests are welcome.

## Acknowledgements
[Kaggle's Common Passwords Dataset](https://www.kaggle.com/prasertk/`top-200-common-passwords-in-2021/data?select=top_200_password_2020_by_country.csv)
[Generate Random Passwords](https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python)



