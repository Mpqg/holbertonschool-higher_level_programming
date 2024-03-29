# 0x03. Python - Data Structures: Lists, Tuples
## Details
      By Guillaume          Weight: 1                Ongoing project - started May 9, 2022 , must end by May 10, 2022           - you're done with 0% of tasks.              Checker was released at May 9, 2022 12:00 PM        An auto review will be launched at the deadline      ## Resources
Read or watch :
* [3.1.3. Lists](https://intranet.hbtn.io/rltoken/drYW-75JbHtmqdjshB4dzw) 

* [Data structures](https://intranet.hbtn.io/rltoken/gUEiytlF3ZgpQ8W9MXzQKw) 
 (until  ` 5.3. Tuples and Sequences `  included)
* [Learn to Program 6 : Lists](https://intranet.hbtn.io/rltoken/smot10KJXMP-a84UxJ7WrQ) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/5QCc7m2ddxSRnXo-kOO0Gg) 
 ,  without the help of Google :
### General
* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the  ` del `  statement and how to use it
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
### C
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* Your code should use the  ` Betty `  style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) 
 and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl) 

* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the  ` main.c `  files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own  ` main.c `  files at compilation. Our  ` main.c `  files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called  ` lists.h ` 
* Don’t forget to push your header file
* All your header files should be include guarded
## Trace
To help you with your journey, feel free to try your code inside Trace. The link is available on each task.
You will be able to see in real time your code and what is really happening.
You can find  [here](https://intranet.hbtn.io/rltoken/C8QnwPzrs4Lod0rAB7y7_Q) 
  a quick explanation about how to use it.
## Quiz questions
Great!          You've completed the quiz successfully! Keep going!          (Show quiz)#### 
        
        Question #0
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> a[0]
 `  Quiz question Answers * 1

* 2

* [1]

* [1, 2]

* [1, 2, 3, 4]

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> a[-1]
 `  Quiz question Answers * -1

* 2

* 4

* [4, 3, 2, 1]

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> a[-3]
 `  Quiz question Answers * -3

* [4, 3]

* 2

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> len(a)
 `  Quiz question Answers * 2

* 4

* 6

* 8

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)
 `  Quiz question Answers * 2

* 5

* 6

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> a[1:3]
 `  Quiz question Answers * [1, 2, 3]

* [1, 2]

* [2, 3]

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a
 `  Quiz question Answers * [1, 2, 3, 4]

* [1, 10, 3, 4]

* [1, 2, 10, 4]

* [1, 2, 10, 10]

 Quiz question Tips #### 
        
        Question #7
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> b = a
>>> b
 `  Quiz question Answers * [1, 2, 3, 4]

* [1]

* 1

* a

 Quiz question Tips #### 
        
        Question #8
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> a
 `  Quiz question Answers * [1]

* [1, 2, 10, 4]

* [1, 2, 3, 4]

* a

* b

 Quiz question Tips #### 
        
        Question #9
    
 Quiz question Body What do these lines print?
 ` >>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b
 `  Quiz question Answers * [1]

* [1, 2, 10, 4]

* [1, 2, 3, 4]

* a

* b

 Quiz question Tips ## Tasks
### 0. Print a list of integers
          mandatory         Progress vs Score  Task Body Write a function that prints all integers of a list.
* Prototype:  ` def print_list_integer(my_list=[]): ` 
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
You can test your code  [here](https://intranet.hbtn.io/rltoken/fdo4qZ9SvQEKXL4ayTGCIg) 

```bash
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 0-print_list_integer.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Secure access to an element in a list
          mandatory         Progress vs Score  Task Body Write a function that retrieves an element from a list like in C.
* Prototype:  ` def element_at(my_list, idx): ` 
* If  ` idx `  is negative, the function should return  ` None ` 
* If  ` idx `  is out of range (> of number of element in  ` my_list ` ), the function should return  ` None ` 
* You are not allowed to import any module
* You are not allowed to use  ` try/except ` 
You can test your code  [here](https://intranet.hbtn.io/rltoken/uQxOrv7Ucsy8QJsn-JHsuA) 

```bash
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 1-element_at.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Replace element
          mandatory         Progress vs Score  Task Body Write a function that replaces an element of a list at a specific position (like in C).
* Prototype:  ` def replace_in_list(my_list, idx, element): ` 
* If  ` idx `  is negative, the function should not modify anything, and returns the original list
* If  ` idx `  is out of range (> of number of element in  ` my_list ` ), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use  ` try/except ` 
You can test your code  [here](https://intranet.hbtn.io/rltoken/YaCYKeb5Vk-uzsgq-cHqQQ) 

```bash
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 2-replace_in_list.py ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Print a list of integers... in reverse!
          mandatory         Progress vs Score  Task Body Write a function that prints all integers of a list, in reverse order.
* Prototype:  ` def print_reversed_list_integer(my_list=[]): ` 
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
You can test your code  [here](https://intranet.hbtn.io/rltoken/OJKIDBxKEvYI5Z5kUWDKww) 

```bash
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 3-print_reversed_list_integer.py ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Replace in a copy
          mandatory         Progress vs Score  Task Body Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
* Prototype:  ` def new_in_list(my_list, idx, element): ` 
* If  ` idx `  is negative, the function should return a copy of the original  ` list ` 
* If  ` idx `  is out of range (> of number of element in  ` my_list ` ), the function should return a copy of the original  ` list ` 
* You are not allowed to import any module
* You are not allowed to use  ` try/except ` 
You can test your code  [here](https://intranet.hbtn.io/rltoken/GqXn9BlYSuYRRjehScuf0Q) 

```bash
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 4-new_in_list.py ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Can you C me now?
          mandatory         Progress vs Score  Task Body Write a function that removes all characters   ` c `   and   ` C `   from a string.
* Prototype:  ` def no_c(my_string): ` 
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use  ` str.replace() ` 
You can test your code  [here](https://intranet.hbtn.io/rltoken/a-ZBj12HLJG9L4IQMHCNLw) 

```bash
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 5-no_c.py ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Lists of lists = Matrix
          mandatory         Progress vs Score  Task Body Write a function that prints a matrix of integers.
* Prototype:  ` def print_matrix_integer(matrix=[[]]): ` 
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
You can test your code  [here](https://intranet.hbtn.io/rltoken/zpBpvX96FjPyFojJ2lOQcw) 

```bash
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 6-print_matrix_integer.py ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Tuples addition
          mandatory         Progress vs Score  Task Body Write a function that adds 2 tuples.
* Prototype:  ` def add_tuple(tuple_a=(), tuple_b=()): ` 
* Returns a tuple with 2 integers:* The first element should be the addition of the first element of each argument
* The second element should be the addition of the second element of each argument

* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value  ` 0 `  for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers
You can test your code  [here](https://intranet.hbtn.io/rltoken/Qa6jzV3OQojtSUde3S5pqA) 

```bash
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 7-add_tuple.py ` 
 Self-paced manual review  Panel footer - Controls 
### 8. More returns!
          mandatory         Progress vs Score  Task Body Write a function that returns a tuple with the length of a string and its first character.
* Prototype:  ` def multiple_returns(sentence): ` 
* If the sentence is empty, the first character should be equal to  ` None ` 
* You are not allowed to import any module
You can test your code  [here](https://intranet.hbtn.io/rltoken/xe6liq2ygxX1TxfdvVno_A) 

```bash
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 8-multiple_returns.py ` 
 Self-paced manual review  Panel footer - Controls 
### 9. Find the max
          mandatory         Progress vs Score  Task Body Write a function that finds the biggest integer of a list. 
* Prototype:  ` def max_integer(my_list=[]): ` 
* If the list is empty, return  ` None ` 
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin  ` max() ` 
You can test your code  [here](https://intranet.hbtn.io/rltoken/AnUzlVBaQ2YCCF-BWeYazA) 

```bash
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 9-max_integer.py ` 
 Self-paced manual review  Panel footer - Controls 
### 10. Only by 2
          mandatory         Progress vs Score  Task Body Write a function that finds all multiples of 2 in a list.
* Prototype:  ` def divisible_by_2(my_list=[]): ` 
* Return a new list with  ` True `  or  ` False ` , depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module
You can test your code  [here](https://intranet.hbtn.io/rltoken/dVRcvt-FsxLaEJ9GOXtjLA) 

```bash
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 10-divisible_by_2.py ` 
 Self-paced manual review  Panel footer - Controls 
### 11. Delete at
          mandatory         Progress vs Score  Task Body Write a function that deletes the item at a specific position in a list.
* Prototype:  ` def delete_at(my_list=[], idx=0): ` 
* If  ` idx `  is negative or out of range, nothing change (returns the same list)
* You are not allowed to use  ` pop() ` 
* You are not allowed to import any module
You can test your code  [here](https://intranet.hbtn.io/rltoken/BnV7Mx995hyiXItqU1oM-A) 

```bash
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 11-delete_at.py ` 
 Self-paced manual review  Panel footer - Controls 
### 12. Switch
          mandatory         Progress vs Score  Task Body Complete the source code in order to switch value of   ` a `   and   ` b ` 
* You can find the source code [here](https://intranet.hbtn.io/rltoken/RfHRsVZK5IVZ5e4-0WAOJQ) 

* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long
You can test your code  [here](https://intranet.hbtn.io/rltoken/SqPZCgnU0yDr1wnh3yIS0g) 

```bash
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 12-switch.py ` 
 Self-paced manual review  Panel footer - Controls 
### 13. Linked list palindrome
          mandatory         Progress vs Score  Task Body Technical interview preparation : 
* You are not allowed to google anything
* Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.
* Prototype:  ` int is_palindrome(listint_t **head); ` 
* Return:  ` 0 `  if it is not a palindrome,  ` 1 `  if it is a palindrome
* An empty list is considered a palindrome
```bash
carrie@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
carrie@ubuntu:0x03$

```
```bash
carrie@ubuntu:0x03$ cat linked_lists.c 
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:0x03$

```
```bash
carrie@ubuntu:0x03$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
carrie@ubuntu:0x03$

```
```bash
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x03-python-data_structures ` 
* File:  ` 13-is_palindrome.c, lists.h ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 1 advanced task now!](https://intranet.hbtn.io/projects/241/unlock_optionals) 

