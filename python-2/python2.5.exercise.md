# python 2.5 excercises

## 1. typehints
1. Let `mypy` (use strict checking) to check types in file [python2.5.exercise.mypy.py](python2.5.exercise.mypy.py):
1. Add proper type typehints according to report from previous step

## 2. test driven development (TDD)

> Don't implement functionality as first step. Write tests and after that implement them.
> See https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle

Implement class `PasswordVerificator` that you can find at plenty forms to 
create new registration on internet. It took two inputs from user and has following capabilities:
1. Given passphrase has to be min 5 chars long.
1. Took two inputs from user to decide if they are same or not.
1. Calculate *strenght* by simple metric that will sum points by these rules:
   1. If passphrase contains a number, (**+1** point)
   1. If passphrase contains a `@` char, (**+1** point)
   1. If length of passphrase is bigger than 7 chars, (**+1** points)
   1. If passphrase contains a sequence `abc`, (**-2** points)

Scenario:
User will provide two input passphrases. Purpose of second passphrase is 
to notify user, that there is a typo in his input, and it will not be further
accepted.

After these two inputs will be given, the class provides a way to check rules 
(defined above) and tell user what is the strength of given passphrase as sum of points.


#### Wider context for consideration
Don't implement anything from following paragraph!
> We want to calculate statistics from user's behaviour to be able to tell 
how mamy people do typos, how strong/weak passwords they are using...