# BRUTE FORCE helper in solving Arweave Puzzle #7

## JavaScript solver (very slow but very easy to use)

Based on the idea to simply automotize the input of expected solutions on the puzzle page. It could be run simply from the puzzle page in browser:
```
1) Open the puzzle #7 page in browser [1]

2) Turn on the developer tools (ctr+shift+I im most browsers or simply find that feature in the options menu) 
that will look similar to this [2]

3) Go to the console in developer tools, and type or copy-paste the whole bruteforce JavaScript (found it attached
in this git around this README file) code in there

4) Wait till the script finish its work
```

Do not forget to adjust the script for YOUr needs replacing default "keys" (inputs):

```
var k_1 = ["Vivaldi", "vivaldi", "AntonioLucioVivaldi", "AntonioVivaldi", "Antonio", "music", "violin", "Valid", "valid", ....];
var k_2 = ["LifeOfPi", "lifeofpi", "RichardParker", "richardparker", "YannMartel", "yannmartel", "Martel", "martel", "Yann", "yann", "Thirsty", "thirsty", "film", "book", "story"];
var k_3 = ["Permanent", "permanent", "Etiquette", "etiquette", "etiquette", "Nathaniel", "nathaniel"];
var k_4 = ["Arnheim", "arnheim", "Ellison", "ellison"];
var k_5 = ["Behemoth", "behemoth", "Bulgakov", "bulgakov", "Azazello", "azazello", "Koroviev", "koroviev"];
var k_6 = ["Solar", "Lunar", "solar", "lunar", "Solareclipse", "SolarEclipse", "solareclipse", "Lunareclipse", "LunarEclipse", "lunareclipse", "1157", "eclipses", "Eclipses"];
for(var i=0;i<200;i++)
  k_6.push(1900+i)
  
var k_7 = ["Buterin", "buterin",Vitalik,vitalik,Network,network, "ANABP01", "anabp01", "Achacha", "achacha"];
var k_8 = ["462", "11", "143176176209", "14399176154110187176132209"];
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
[1] Arweave Puzzle #7 page - https://eplpvctnryuimypdq6gbfk4rx3bbfepzoxz5pldkqdjczy5udpla.arweave.net/I9b6im2OKIZh44eMEquRvsISkfl189esaoDSLOO0G9Y

[2] Open developers tools \ using Java Script console in Firefox - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools
