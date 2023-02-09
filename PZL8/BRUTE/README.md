# BRUTE FORCE helper in solving Arweave Puzzle #8

## JavaScript solver (very slow but very easy to use)

Based on the idea to simply automotize the input of expected solutions on the puzzle page. It could be run simply from the puzzle page in browser:
```
1) Open the puzzle #8 page in browser [1]

2) Turn on the developer tools (ctr+shift+I im most browsers or simply find that feature in the options menu) 
that will look similar to this [2]

3) Go to the console in developer tools, and type or copy-paste the whole bruteforce JavaScript (found it attached
in this git around this README file) code in there

4) Wait till the script finish its work
```

Do not forget to adjust the script for YOUr needs replacing default "keys" (inputs):

```
var k_1 = ["rasputin", "Rasputin"];
var k_2 = ["Wilhelm", "wilhelm"];
var k_3 = ["alekhine", "Alekhine"];
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

# References
[1] Arweave Puzzle #8 page - https://mwgauw2twixdxh3fm6mywx7tvuxo442xtckttdbhpbctxz3em5fq.arweave.net/ZYwKW1OyLjufZWeZi1_zrS7uc1eYlTmMJ3hFO-dkZ0s

[2] Open developers tools \ using Java Script console in Firefox - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools
