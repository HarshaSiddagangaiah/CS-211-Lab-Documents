# Aliasing 

In this lab, we will write a program to help `ASUO` (The Associated Students of the University of Oregon) to form and schedule clubs for students.

For this program, we will create 3 classes (`Student`, `Club`, `ASUO`)

There is also a section called supplemental material attached at the bottom.

## Coding step 1
1. Create a class called Student with the following constructor.

```python
from typing import List, Set, Dict, Optional
class Student:

    def __init__(self, name: str,
                 interests: List[str]):
        self.name = name
        self.interests = interests
        self.freetimes = set([8, 9, 10, 11, 12, 13, 14, 15])
        self.meetings: List[int] = []
```

- `freetimes`: a list of available time slots for a student, simplified to be just integers representing hours. Each student starts out with free times 8,9,...,15.

Note: Here are some of the characteristics of Python's built-in set type:

Sets are unordered.
Set elements are unique. Duplicate elements are not allowed.
A set itself may be modified, but the elements contained in the set must be of an immutable type.
- meetings: a list of time slots for all the meetings that a student has scheduled. Note that a time slot in meetings should not be included in freetimes. 

2. Create a method called schedule_meeting() to schedule a meeting for a student given a time slot.

```python
    def schedule_meeting(self, time: int):
```

This function takes in one parameter time, it checks if the student is free at the time, if so, it will add time to meetings and remove time from freetimes.

## Coding step 2
1. Create a class called Club with the following constructor:

```python
class Club:

    def __init__(self, name: str):
        self.name = name
        self.members: List[Student] = []
        self.meeting_time: Optional[int] = None
```

- `name`: the name of the club.

- `members`: a list of members (students).

- `meeting_time`: a meeting time so that all members can attend.

Notice that we used Optional[int]=None here, this is called type checking or type hints. This line of code simply says that a variable (meeting_time) either has the type specified (int) or is None.

2. Create the following function to add a student to the member list.

```python
    def join(self, student: Student):
```

3. Create the following function to find the common time slot for all members from their freetimes to attend. If it cannot find a common time, return 0.

```python
    def find_common_time(self) -> int:
```

4. Create the following function to schedule the club meeting for all of its members.

```python
    def schedule(self, time: int):
```

5. Add __str__ magical method:

```python
    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f"{self.name} ({', '.join(member_names)})"
```

## Coding step 3
1. Create a class called ASUO with the following constructor:

```python
class ASUO:

    def __init__(self):
        self.students: List[Student] = []
        self.clubs: List[Club] = []
```

2. Create the following function to add a student to the list of students.

```python
    def enroll(self, s: Student):
```

3. Create the following function to form clubs:

```python
    def form_clubs(self):
        clubs_to_form: Dict[str, Club] = {}
 ```

For each student, checks if student interested club has already been formed. If not, creates a new Club object with the interest and add it to the clubs_to_form dictionary. If a club for that interest already exists, then add the student to the existing club.

Notice that clubs_to_form is a dictionary. A dictionary contains key-value pairs. We can look up the dictionary by providing the key. For example, clubs_to_form[key] will give you the value.

4. Create the following function to schedule clubs:

```python
    def schedule_clubs(self):
```

For each club, check for the common time and schedule the club meeting time.

5. Add a function to print out club schedule:

```python
    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f"{club} meets at {club.meeting_time}")
```            

## Coding step 4
Add the following code to test your program:

```python
asuo = ASUO()
asuo.enroll(Student("Marty", ["badminton", "robotics"]))
asuo.enroll(Student("Kim", ["backgammon"]))
asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
asuo.enroll(Student("George", ["chess", "badminton"]))

asuo.form_clubs()
asuo.schedule_clubs()
asuo.print_club_schedule()
```

### What to submit?
If everything works correctly, you should have the following output:

```python
badminton (Marty, George) meets at 8
robotics (Marty, Tara) meets at 9
backgammon (Kim) meets at 8
horticulture (Tara) meets at 8
chess (Tara, George) meets at 10
```

Submit a file named Aliasing.py with your code to Canvas.

 

## Supplemental Material
Please go over these concepts and make sure you understand them.

### Mutability
As you probably know by now, everything in Python is an Object. Even the native types such as integers, floats, and strings are Objects. That is why we've been able to do things such as:

```python
>>> "oregon".upper()
OREGON
```

That is, calling a method from the 'string' class of objects.

Now, some objects can be changed after they've been created. For example, lists CAN be modified after they are initially instantiated:

```python
>>> lst = ['a', 'b']
>>> lst.append('c')
>>> print(lst)
['a', 'b', 'c']
```

These types of objects that can be changed after they're created are called MUTABLE. Most, if not all, of the classes you've created so far during the course, have been mutable.

There is, however, another kind of object. Objects that cannot be changed after they've been created. Those objects are called IMMUTABLE. Examples of immutable objects in Python include integers and strings.

Now, at this point you might be thinking that you actually CAN modify strings, for example:

```python
>>> st1 = "oregon"
>>> st1 += " ducks"
>>> print(st1)
"oregon ducks"
```

However, in reality, every time you "modify" a string, a NEW string object is created.

### Aliasing
Going back to aliasing, if you assign 2 variable names to the same objects, then you've created an alias.

```python
>>> lst1 = ['a', 'b', 'c']
>>> lst2 = lst1
```

At this point, lst2 is an alias of lst1. This means that both names point to the same location in memory. You can verify this using the 'is' operator:

```python
>>> lst1 is lst2
True
```

Now, here comes the interesting part, if you modify lst2, the changes will be reflected when you use the lst1 name, given that they refer to the same object:

```python
>>> lst2.append('d')
>>> print(lst1)
['a', 'b', 'c', 'd']
```

This behavior isn't necessarily bad, as it has its uses (the Sudoku project, for example), but it can certainly be unexpected if you're not aware of it.

As you can probably guess by now, this is only an issue when dealing with mutable objects:

```python
>>> st1 = "oregon"
>>> st2 = st1
>>> st1 is st2
True
>>> st2 += " ducks"
>>> print(st1)
"oregon"
>>> st1 is st2
False
```

Since strings are immutable, they can't be modified. So, when we concatenate a second string to st2 a NEW object is created and st2 no longer points to the same location as st1.

### Dealing with aliasing
So, when dealing with mutable objects we need to be aware of the way their methods work.

In lists, for examples, some methods work "in place", i.e. they modify the object that called them. Examples of in place methods for lists are append and sort.

```python
>>> lst = [5,2,4]
>>> lst.sort()
>>> print(lst)
[2, 4, 5]
```

As you can see, these methods usually do not return anything.

Methods that do not work in place return a new object instead. An example of this type of methods for lists is slicing:

```python
>>> lst = [4, 3, 5, 1, 2]
>>> lst[2:]
[5, 1, 2]
```

So, if you have an alias for a mutable object and call an in place method, you can expect the effects of the call to affect all other names too. If the method returns a new object instead, then you do not have to worry about aliasing.

Avoiding aliasing
As stated before, aliasing can be useful. However, if you're intention is not to create an alias then what you can do is create a copy of the original object.

For lists, for example:

```python
>>> lst1 = [1,2,3]
>>> lst2 = lst1.copy()
>>> lst2.append(4)
>>> print(lst1)
[1, 2, 3]
```

However, if the mutable object you must be aware that there are 2 distinct types of copies: shallow and deep.

Shallow copies create a new object but elements inside are references to the elements inside the original.
Deep copies create a new object and recursively create new objects for all elements of the original.
This distinction is important because, if the object you're copying contains mutable objects, then you've inadvertently created an alias for them if you use a shallow copy:

```python
>>> lst1 = [1, 2, [3, 4]]
>>> lst2 = lst1.copy()
>>> lst2[2].append('a')
>>> print(lst1)
[1, 2, [3, 4, 'a']]
>>> lst1[2] is lst2[2]
True
```

To avoid the behavior above you must create a deep copy instead.

The copy module provides both a copy and a deepcopy function that works for all objects:

```python
>>> from copy import copy, deepcopy
>>> lst1 = [1,2,[3,4]]
>>> lst2 = deepcopy(lst1)
>>> lst2[2].append('a')
>>> lst2
[1, 2, [3, 4, 'a']]
>>> lst1
[1, 2, [3, 4]]
```
