# BRUTE FORCE helper in solving Arweave Puzzle #3

## GO solver + Python (much much faster than JavaScript or browser solution - up to 50-60 keys per sec PER THREAD resulting in 400-500 keys per sec on my 8 core laptop CPU)

This way of the Brute-Force will require Python and GO to be installed on your system to run the script. 
Here [[1]](https://docs.python-guide.org/starting/install3/linux/), [[2]](https://www.cyberciti.biz/faq/how-to-install-gol-ang-on-ubuntu-linux/) or [[2']](https://go.dev/doc/install) you can see some guide for Pytohn and GO (or simply google it)

Its work is pretty close to what i've done with NODEjs version - wrapped the raw solver (GO script) into python for better management. 

The GO script were mainly proposed by the core member of the puzzle solver group (@arweavep) and he found out that GO library with a slight modificaiton works same as CryptoJS library (that caused me problems).
The modifications that should be done looks as following (just leave me a message in Issues if you have problems and we will workaround it):
```
To use this program you should remove two "condition" lines in a file $GOROOT/src/crypto/aes/cipher_asm.go:
	--- if !supportsAES {
          return newCipherGeneric(key)
	--- }

and change "case" line in a file $GOROOT/src/crypto/aes/cipher.go:

	func NewCipher(key []byte) (cipher.Block, error) {
	...
	--- case 16, 24, 32:
	+++ case 16, 24, 32, 128:
	...
	}

```

The script run the task in parralel invoking several threads. 
Each thread goes over its part of the search among the resulting solutional space ( combinations of given keys). Each 2000 combos (its adjustable in script -
parameter BATCH_SIZE) each thread print the status information to the LOG file ***main.log*** (in folder ***LOG***) 
***AND DUMP ALL TRIED COMBINATIONS OF KEYS INTO  file "pzl3_bruttedAnswers.txt"*** - this file will be used on each next program run to identify wich combinations
have been already tried and such would be ignored (this could be even shared among solvers).
If solution was found - the thread that have found the solution will print it to the ***main.log*** as well as in its own LOG file ***{t_id}_main.log*** 
(where t_id is the id of the thread) and the program would be terminated (printing FINISH to the console). 

***SIMPLIFYING ALL THIS, HERE WHAT YOU SHOULD DO TO RUN THE BRUTEFORCE***
```
1) Create some folder on your PC and download three files there: "brute_pzl3_GO.py", "pzl3_GOscript.go" and "pzl3_KEYS.txt"

2) Adjust the "pzl3_KEYS.txt" to your brute list

3) Install GO and Python (to be accessible from this folder - GO could require some extra manipulation for that.
  i simply proceed through the installation path for Ubuntu described in [2] and thats it)

4) Run the python script:
    python3 brute_pzl3_GO.py
   Or
    python brute_pzl3_GO.py


5) Wait till the script finish its work - monitor the LOG files in the folder LOG

P.S. To stop the program - write 1 (instead of 0) into the "failsafe_AR_3.txt"

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

# P.S: I have bruted pretty much of options so far and shared the list of brutted answers in telegram group - msg me there (or by mail) if you want to get that list as well

# References
[1] Python installation for Linux - https://docs.python-guide.org/starting/install3/linux/

[2] GO lang on UBUNTU installation - https://www.cyberciti.biz/faq/how-to-install-gol-ang-on-ubuntu-linux/

[2'] GO lang on UBUNTU installation - https://go.dev/doc/install

[*] Telegram group of Arweave puzzles solvers community - @arweavep
