# BRUTE FORCE helper in solving Arweave Puzzle #3

## JavaScript solver (very slow but very easy to use)

Based on the idea to simply automotize the input of expected solutions on the puzzle page. It could be run simply from the puzzle page in browser:
```
1) Open the puzzle #3 page in browser [[1]](https://kszeqgxezf5quhzld4nhpasyilhxphclq2peqi5mrn7utxmqhwga.arweave.net/VLJIGuTJewofKx8ad4JYQs93nEuGnkgjrIt_Sd2QPYw)

2) Turn on the developer tools (ctr+shift+I im most browsers or simply find that feature in the options menu) that will look similar to this [[2]](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)

3) Go to the console in developer tools, and type or copy-paste the whole bruteforce JavaScript (found it attached in this git around this README file) code in there

4) Wait till the script finish its work
```

Do not forget to adjust the script for YOUr needs replacing default "keys" (inputs):

```
var k_1 = ["icon","logo","text","name",'page',"html","link","tags","apps","http","main","hack","mail","type","luck"];  
var k_2 = ["md12","mine","mail","hash","path","road","main","link","text","code","luck"];
var k_3 = ["a384","-384","asic","hash","luck"];
var k_4 = ["cash","cost","swap","cost","rate","artx" ,"sell","list","arql","view","data","luck"];
var k_5 = [" dns","port","1984","scan","luck"];
var k_6 = ["root","ASMT","node","byte","data","beam","luck"];
var k_7 = ["pool","pull","vest","node","luck"];
var k_8 = ["base","data","apps","star","cost","code","luck"];
```

The script work could be easily paralelized - just open few instances of the page and make the same procedure in both, BUT adjust the parameters in script: look at variables **thr_ind** and **thr_num**.
**thr_num** define the total number of threads you want to run (number of instances) and **thr_ind** define the current index of the thread. So, for example, if you want to run 2 threads of this script (2 instances): you need to open the puzzle #3 page 2 times and run the script in each with different variables values as following:
```
page #1 script:
    ...
        var thr_ind = 1;
        var thr_num = 2;   
    ...
page #2 script:
    ...
        var thr_ind = 2;
        var thr_num = 2;   
    ...
```
