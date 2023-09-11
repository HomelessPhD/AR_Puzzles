# BRUTE FORCE helper in solving Arweave Puzzle #3

## JavaScript solver THAT USES NODEjs + Python (more comfortable and a bit faster than browser version)

This way of the Brute-Force will require Python and NODEjs to be installed on your system to run the script. 
Here [[1]](https://docs.python-guide.org/starting/install3/linux/), [[2]](https://nodejs.org/en/download/package-manager) you can see some guide for Pytohn and NODEjs (or simply google it)

Its work is pretty simple and close to what is done in "Browser version". BUT, here are few changes were made to make it more efficient and user-friend. 
The sha512 hashing of the inputs is made in python while the AES job is still done in JavaScript. The script run the task in parralel invoking several threads. 
Each thread goes over its part of the search among the resulting solutional space ( combinations of given keys). Each 500 combos (its adjustable in script -
parameter BATCH_SIZE) each thread print the status information to the LOG file ***main.log*** (in folder ***LOG***) 
***AND DUMP ALL TRIED COMBINATIONS OF KEYS INTO  file "pzl3_bruttedAnswers.txt"*** - this file will be used on each next program run to identify wich combinations
have been already tried and such would be ignored (this could be even shared among solvers).
If solution was found - the thread that have found the solution will print it to the ***main.log*** as well as in its own LOG file ***{t_id}_main.log*** 
(where t_id is the id of the thread) and the program would be terminated (printing FINISH to the console). 

***SIMPLIFYING ALL THIS, HERE WHAT YOU SHOULD DO TO RUN THE BRUTEFORCE***
```
1) Create some folder on your PC and download three files there: "brute_pzl3.py", "pzl3_pageCODE.js" and "pzl3_KEYS.txt"

2) Adjust the "pzl3_KEYS.txt" to your brute list

3) Install NODEjs and Python (to be accessible from this folder - NODEjs could require some extra manipulation for that.
  i simply proceed through the installation described in [3] and thats it)

4) Run the python script:
    python3 brute_pzl3.py
   Or
    python brute_pzl3.py


5) Wait till the script finish its work - monitor the LOG files in the folder LOG
```

Do not forget to adjust the KEYs list for YOUr needs replacing default "keys" (inputs) in file ***"pzl3_KEYS.txt"*** (keys are comma-separated):

```
node,data,lang,curl,site,tags,name,anon,meta,arql
sale,sell,date,code,sign,view,head,main,romb,bash
mine,asic,a384
when,coin,swap,sell,cash
port,1984,scan,maps,LOKI,view,.erl,lang
SILO,ASMT,beam,root,node,data,list,9788,4432,size,tree,peer
vest,pool,pull
base,dots,sell,swap,10000,list,desk

```

The script works "in parrallel" by defaul - its invoke several threads managing them through semaphore (in order to make the brutted keys dumping safe). 
To adjust amount of threads, adjust the ***t_num*** variable in file ***brute_pzl3.py***:

```
1 Thread
    ...
        t_num = 1 
    ...

4 Threads
    ...
        t_num = 4 
    ...
```

# References
[1] Python installation for Linux - https://docs.python-guide.org/starting/install3/linux/

[2] NODEjs installation for Linux - https://nodejs.org/en/download/package-manager

[3] NODEjs installation for Ubuntu - https://github.com/nodesource/distributions
