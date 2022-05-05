# 0x02. Python - import & modules
## Details
      By Guillaume          Weight: 1                Ongoing project - started May 5, 2022 , must end by May 6, 2022           - you're done with 0% of tasks.              Checker was released at May 5, 2022 12:00 PM        An auto review will be launched at the deadline      ## Resources
Read or watch :
* [Modules](https://intranet.hbtn.io/rltoken/4SOY6RYv_fYUM-4NNB3Abg) 

* [Command line arguments](https://intranet.hbtn.io/rltoken/pIjNhhRLMFfHoqcTM7u3_A) 

* [Pycodestyle – Style Guide for Python Code](https://intranet.hbtn.io/rltoken/ngVTmU2SAH3NW1Z2IGqmLA) 

man or help :
*  ` python3 ` 
## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/GzK0HyXjvp5fcKQiiTyLRQ) 
 ,  without the help of Google :
### General
* Why Python programming is awesome
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function  ` dir() ` 
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version  ` 2.8.* ` )
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
## Quiz questions
Great!          You've completed the quiz successfully! Keep going!          (Show quiz)#### 
        
        Question #0
    
 Quiz question Body What do these lines print?
 ` >>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function()
 `  Quiz question Answers * “In my function”

* In my function

* function my_function at …

* Nothing

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What do these lines print?
 ` >>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function
 `  Quiz question Answers * “In my function”

* In my function

* function my_function at …

* Nothing

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What do these lines print?
 ` >>> def my_function(counter):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
 `  Quiz question Answers * Counter: counter

* Counter: c

* Counter: 12

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body What do these lines print?
```bash
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)

```
 Quiz question Answers * Counter: 12

* Counter: 89

* Counter: 101

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body What do these lines print?
```bash
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function()

```
 Quiz question Answers * Counter: 12

* Counter: 89

* Counter: 101

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body What do these lines print?
 ` >>> def my_function(counter=89):
>>>     return counter + 1
>>> 
>>> print(my_function())
 `  Quiz question Answers * 1

* 89

* 90

* 891

 Quiz question Tips ## Tasks
### 0. Import a simple function from a simple file
          mandatory         Progress vs Score  Task Body Write a program that imports the function   ` def add(a, b): `   from the file   ` add_0.py `   and prints the result of the addition   ` 1 + 2 = 3 ` 
* You have to use  ` print `  function
* You have to assign:* the value  ` 1 `  to a variable called  ` a ` 
* the value  ` 2 `  to a variable called  ` b ` 
* and use those two variables as arguments when calling the functions  ` add `  and  ` print ` 

*  ` a `  and  ` b `  must be defined in 2 different lines:  ` a = 1 `  and another  ` b = 2 ` 
* Your program should print:  ` <a value> + <b value> = <add(a, b) value> `  followed with a new line
* You can only use the word  ` add_0 `  once in your code
* You are not allowed to use  ` * `  for importing or  ` __import__ ` 
* Your code should not be executed when imported - by using  ` __import__ ` , like the example below
```bash
guillaume@ubuntu:~/0x02$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x02-python-import_modules ` 
* File:  ` 0-add.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. My first toolbox!
          mandatory         Progress vs Score  Task Body Write a program that imports functions from the file   ` calculator_1.py `  , does some Maths, and prints the result.
* Do not use the function  ` print `  more than 4 times 
* You have to define:* the value  ` 10 `  to a variable  ` a ` 
* the value  ` 5 `  to a variable  ` b ` 
* and use those two variables only, as arguments when calling functions (including  ` print ` )

*  ` a `  and  ` b `  must be defined in 2 different lines:  ` a = 10 `  and another  ` b = 5 ` 
* Your program should call each of the imported functions. See example below for format
* the word  ` calculator_1 `  should be used only once in your file
* You are not allowed to use  ` * `  for importing or  ` __import__ ` 
* Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
guillaume@ubuntu:~/0x02$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x02-python-import_modules ` 
* File:  ` 1-calculation.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. How to make a script dynamic!
          mandatory         Progress vs Score  Task Body Write a program that prints the number of and the list of its arguments.
* The output should be:* Number of argument(s) followed by  ` argument `  (if number is one) or  ` arguments `  (otherwise), followed by
*  ` : `  (or  ` . `  if no arguments were passed) followed by
* a new line, followed by (if at least one argument),
* one line per argument:* the position of the argument (starting at  ` 1 ` ) followed by  ` : ` , followed by the argument value and a new line


* Your code should not be executed when imported
* The number of elements of  ` argv `  can be retrieved by using:  ` len(argv) ` 
* You do not have to fully understand lists yet, but imagine that  ` argv `  can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
```bash
guillaume@ubuntu:~/0x02$ ./2-args.py 
0 arguments.
guillaume@ubuntu:~/0x02$ ./2-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/0x02$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
guillaume@ubuntu:~/0x02$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x02-python-import_modules ` 
* File:  ` 2-args.py ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Infinite addition
          mandatory         Progress vs Score  Task Body Write a program that prints the result of the addition of all arguments
* The output should be the result of the addition of all arguments, followed by a new line
* You can cast arguments into integers by using  ` int() `  (you can assume that all arguments can be casted into integers)
* Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py
0
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10
89
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
guillaume@ubuntu:~/0x02$ 

```
Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:
```bash
guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
guillaume@ubuntu:~/0x02$

```
Remember how you did (or did not) do it in C?   ` #pythoniscool ` 
 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220505T203515Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=63e00d5e91410bf849bacb63e22f878effae3b6721de446dd37e569bc068b896) 

 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x02-python-import_modules ` 
* File:  ` 3-infinite_add.py ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Who are you?
          mandatory         Progress vs Score  Task Body Write a program that prints all the names defined by the compiled module  [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) 
  (please download it locally).
* You should print one name per line, in alpha order
* You should print only names that do not start with  ` __ ` 
* Your code should not be executed when imported
* Make sure you are running your code in Python3.8.x ( ` hidden_4.pyc `  has been compiled with this version)
```bash
guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x02-python-import_modules ` 
* File:  ` 4-hidden_discovery.py ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Everything can be imported
          mandatory         Progress vs Score  Task Body Write a program that imports the variable   ` a `   from the file   ` variable_load_5.py `   and prints its value.
* You are not allowed to use  ` * `  for importing or  ` __import__ ` 
* Your code should not be executed when imported
```bash
guillaume@ubuntu:~/0x02$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/0x02$ ./5-variable_load.py
98
guillaume@ubuntu:~/0x02$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x02-python-import_modules ` 
* File:  ` 5-variable_load.py ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 4 advanced tasks now!](https://intranet.hbtn.io/projects/239/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(1/5 Sandboxes spawned)
### Ubuntu 20.04
Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/20113/webterm) 
[Restart]() 
[Destroy]() 
#### Credentials
Hostce7c3a1aab61.324f89ee.hbtn-cod.ioUsernamece7c3a1aab61Password5ab9d58153e0bb3e1d8c#### Web access
[HTTPS](https://ce7c3a1aab61.324f89ee.hbtn-cod.io/) 
[HTTP](http://ce7c3a1aab61.324f89ee.hbtn-cod.io/) 
[3000](http://ce7c3a1aab61.324f89ee.hbtn-cod.io:3000/) 
[4000](http://ce7c3a1aab61.324f89ee.hbtn-cod.io:4000/) 
[5000](http://ce7c3a1aab61.324f89ee.hbtn-cod.io:5000/) 
[5001](http://ce7c3a1aab61.324f89ee.hbtn-cod.io:5001/) 
[8000](http://ce7c3a1aab61.324f89ee.hbtn-cod.io:8000/) 
[8080](http://ce7c3a1aab61.324f89ee.hbtn-cod.io:8080/) 
#### Port mapping
SSH49202HTTP49201HTTPS49200300049199MySQL49198400049197500049196500149195800049194808049193