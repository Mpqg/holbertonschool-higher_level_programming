# 0x01. Python - if/else, loops, functions


## Resources
Read or watch :
* [More Control Flow Tools](https://intranet.hbtn.io/rltoken/YLjvfmHv_JJ-J-cyn8bS2Q) 
 (Read until “4.6. Defining Functions” included)
* [Myths about Indentation](https://intranet.hbtn.io/rltoken/Y-HaMMJBKPseiVDo_v9PVg) 

* [IndentationError](https://intranet.hbtn.io/rltoken/AorC2VSZ4yCOx-AbatvKLA) 

* [How To Use String Formatters in Python 3](https://intranet.hbtn.io/rltoken/BQD7VNGK4cYVjXhNx1hfAQ) 

* [Learn to Program](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw) 

* [Learn to Program 2 : Looping](https://intranet.hbtn.io/rltoken/mlo-dauC8pSM_NrO5VYobw) 

* [Pycodestyle – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/5uFnbDmoyPNoxwXUNxEypw) 

man or help :
*  ` python3 ` 
## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/zTORGnHYbsyIZDwVtF_aZw) 
 ,  without the help of Google :
### General
* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the  ` if ` ,  ` if ... else `  statements
* How to use comments
* How to affect values to variables
* How to use the  ` while `  and  ` for `  loops
* How is Python’s  ` for `  different from  ` C ` ‘s?
* How to use the  ` break `  and  ` continues `  statements
* How to use  ` else `  clauses on loops
* What does the  ` pass `  statement do, and when to use it
* How to use  ` range ` 
* What is a function and how do you use functions
* What does return a function that does not use any  ` return `  statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them
## Requirements
### Python Scripts
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version  ` 2.8.* ` )
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
### C Scripts
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
* All your files should end with a new line
* Your code should use the  ` Betty `  style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) 
 and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl) 

* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the  ` main.c `  files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own  ` main.c `  files at compilation. Our  ` main.c `  files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called  ` lists.h ` 
* Don’t forget to push your header file
* All your header files should be include guarded
## More Info
Note : you do not need to understand lists yet.
## Quiz questions
#### Question #0
 Quiz question Body What do these lines print?
 ` if True:
    print("Holberton")
else:
    print("School")
 `  Quiz question Answers * Holberton

* School

 Quiz question Tips #### Question #1
 Quiz question Body What do these lines print?
 ` if 12 == 48/4:
    print("Holberton")
else:
    print("School")
 `  Quiz question Answers * Holberton

* School

 Quiz question Tips #### Question #2
 Quiz question Body What do these lines print?
 ` if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")
 `  Quiz question Answers * Holberton

* School

 Quiz question Tips #### Question #3
 Quiz question Body What do these lines print?
 ` if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")
 `  Quiz question Answers * Holberton

* School

 Quiz question Tips #### Question #4
 Quiz question Body What do these lines print?
```bash
a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")

```
 Quiz question Answers * Holberton

* C is fun

* School

 Quiz question Tips #### Question #5
 Quiz question Body What do these lines print?
```bash
a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")

```
 Quiz question Answers * Holberton

* C is fun

* School

 Quiz question Tips #### Question #6
 Quiz question Body What do these lines print?
 ` for i in range(4):
    print(i, end=" ")
 `  Quiz question Answers * 1 2 3 4

* 1 2 3

* 0 1 2 3

* 0 1 2 3 4

 Quiz question Tips #### Question #7
 Quiz question Body What do these lines print?
 ` for i in range(2, 4):
    print(i, end=" ")
 `  Quiz question Answers * 2 4

* 2 3

* 2 3 4

* 3 4

 Quiz question Tips #### Question #8
 Quiz question Body What do these lines print?
 ` for i in range(2, 10, 2):
    print(i, end=" ")
 `  Quiz question Answers * 2 3 4 5 6 7 8 9 10

* 2 3 4 5 6 7 8 9

* 4 6 8 10 12 14 16 18

* 2 4 6 8

 Quiz question Tips Submit answers## Please make sure to validate all quiz questions before moving on to project tasks
