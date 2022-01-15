secret_number= int(777)
guess= int(input("""
+===========================+
|    Welcome to my game, muggle !     |
|    Enter an integer number                |
|    and guess what number I' ve         |
|    picked for you.                                 |
|    So, what is the secret number ?    |
+===========================+
"""))
counter=1
while guess != secret_number:
    if guess<secret_number:
        print('Ha ha, You\'re stuck in my loop ! The Secret Number is more than your guess:')
    elif guess>secret_number:
        print('Ha ha, You\'re stuck in my loop! The Secret Number is less than your guess')
    guess= int(input('Try Again!, Enter the number again now: '))
    counter=counter+1
print('Well done, muggle ! You are free now.',guess,' is the correct answer. You succeeded in',counter,'attempts.') 
    
