# Arweave Puzzle #3 - "...You'd be surprised how easy #3 is..."

Here i am going to publish ideas i consider about and dummy instruments related to Arweave puzzle #3.

This puzzle is one from the series of Arweave Puzzles made by @Tiamat (official Arweave project discord member, apps developer, miner, early investor). Originally, puzzle posted in official @Tiamat twitter [[1]](https://twitter.com/ArweaveP/status/1132936723162378240): with hints and link to the blockchain [[2]](https://kszeqgxezf5quhzld4nhpasyilhxphclq2peqi5mrn7utxmqhwga.arweave.net/VLJIGuTJewofKx8ad4JYQs93nEuGnkgjrIt_Sd2QPYw
)

Puzzle consists of the HTML page (sources also attached in this git - but could be found on Arweave "blockchain") page with an AES encrypted message (the Arweave wallet with **1000 AR** coins on it, that is around of **10 k$** right now). The decryption mechanism is already built in page so the solver should only type the correct 4-symbols "words" (4-symbol combinations) to the 8 placeholders as show on picture below. The key to the puzzle solving is an image with 8 separated pictures:

![AR puzzle #3 keys](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/pzl_3.png )


![AR puzzle #3 solving](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/pzl_3_keys_screen.png )

# The official hints given by the puzzle creator are listed below:


    
```
    From Twitter:
    
1] Did anybody count the dots?

2] With N.1.7.0.0 release, third pic became obsolete 😉
```    

	
```
	From discord:
3] You'd be surprised how easy #3 is

4] It is not hard actually, someone which followed the project during last six months 
should solve 7 images easily and for 1 some luck needed 

5] When you reach a question/part and you have more answers for it, most likely none of them
is the right one 🙂

6] It's not my fault that people see a tree with - - - -  and they actually type TREE and
expect to unlock.

7] (Some dev about other dev guessing the answer for pic 4) Haha interesting, when we first 
looked at it, I think @arweave-india got number 4 😆 -> (PZL creator) I'm 99% she was thinking 
about the right answer, which  by the way, in the sketch was different, but this one was so 
obvious, I just adjusted to it:)  -> (that other dev that guessing) Hehe, I think I might be 
in the right area now for a few more of the clues for puzzle 3 🤔 Good job though, I am 
impressed at how tricky it is! -> (pzl creator) exactly, once you get on the right track, 
one by one they seem much easier
```

Some ideas came to my mind, others were captured from Twitter or\and the telegram group [[3]](@arweavep) - you definitely should visit it for ideas sharing.
(at first few months i have forcefully avoided visiting any forums or groups when i saw the puzzle at first because i thought that ideas of others could freeze my own thinking process - it is when you start to think primarly in the way proposed by some other solver and, got stuck on it, but later trying my own ideas with my own dummy brute forcing method i skipped that rule. I am actively posting any ideas came to my mind in that group, hoping someone of us will be able to solve the puzzle sharing some part of revenue and GLORY)

There are pretty "classic" ideas of what each image could code, but also there apretty exotic ideas. The last will be discussed at the end of this paper. Lets consider each picture one by one at first:

## 1-st key
![1-st key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/1.png )

Thats pretty hard one. One may assume that it images 4 letters: "A", "N", "N" or "H", "D" or "O". That forms 4-symbol "word" just as requested: ANNO, ANHO, ANWO,... BUT, i doubt one of theese letter combinations is the answer. 
ANNO could be interpreted as "since" meaning the year (like the "ANNO 1901" that could be found on top of some European buildings that means that it was constructed in year 1901, and that was the first i thought it should be - the year of Arweave birthday or ICO or any other related date - may be even DD/MM combination).
ANHO could be assumed to denote the investor who supported the Arweave project by a descent investment - "ANdreessen HOrowitz" or "a16z" that is a logo of his company and so it could be the key.
More trivial answers here would be 4-letter words somehow related to Arweave or the image.

Finally, i consider the next keys: `2014, 2015, 2016, 2017, 2018, 2019, a16z, ANHO, hack, logo, tags, apps, dapp, hack, text, icon, name, page, anon, html, link, http, main, mail, type, json, file, luck,....`

## 2-nd key
![2-nd key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/2.png )

This a tricky piece. 

The first thing the solvers usually do here is googling this number "21863" that results in coordinates: 21863 is ZIP code (index) of Snow Hill, MD in USA [[4]](https://www.unitedstateszipcodes.org/21863/). That instantly gives: "snow", "hill", "city", "town", "code", "mail" keys. Recalling the fact that the picture contains this number in romb with arrows - someone could go further and see that roads around the city forms the romb AND the road MD12 goes through the city (through the romb) exactly or very likely as drawn on the picture by two arrows. So another option here is "md12", "road", "path". Going even further with thi idea - i have found that there is a mine not far by the md12 road [[5]](https://thediggings.com/places/md0472391417/map) - somewhere close to the bolder arrow on the picture.

![Snow HIll MD12 - ZIP 21863](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/MD12.png)

Another interesting idea about this picture - "21863" missing the "0". In other words - it is a date: 2018\06\03 that could be interpreted as Arweave ICO date for example, that also give "date", "fund" keys.

Finally, i'd consider the next keys here: `md12, mine, mail, path, road, main, link, text, code, hash, fund, date, towm city, hill, snow, data, mark, luck, ...`

Someone could also look for the block number 21863 - but there is nothing interesting about it. (sure, many complex manipulations could be done with block data - but that is a dead end).

## 3-rd key
![3-rd key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/3.png )

This picture was directly hinted by the @Tiamat. "With N.1.7.0.0 release, third pic became obsolete". It is very likely related to Arweave sources [[6']](https://github.com/ArweaveTeam/arweave/releases), especially N.1.7.0.0 release [[6]](https://github.com/ArweaveTeam/arweave/releases/tag/N.1.7.0.0). The most interesting part of this release comments (readme) are the following:

```
We're very happy to announce the N.1.7.0.0 release of the Arweave node!
...
New features
   1. RandomX proof-of-work algorithm
   
      RandomX is a PoW algorithm that is optimized for general-purpose
      CPUs. RandomX uses random code execution together with several
      memory-hard techniques to maximize the efficiency of
      general-purpose CPUs and therefore make GPU accelerated miners
      and ASIC based miners less likely to be advantageous.
      ....
      The mining benchmark is updated with a new argument for choosing
      RandomX hashing or the previous SHA-384 hashing. E.g.
      `./arweave-server benchmark randomx max_miners 4`. A bug was
      also fixed which halved all the performance numbers.
      ...

   2. Two-way integration with IPFS
   
      Arweave is launching an IPFS incentivisation layer, providing
      permanent storage for the IPFS network. Read more about it here:
      ...

   5. Config file
      All startup arguments can be put in a JSON based config file and
      be loaded with the new startup argument `config_file`.
      ...

Reliability and operations improvements
   1. Cowboy
      The HTTP server Elli is replaced with Cowboy.
...
```

Recalling that picture likely to image the mining process and contains two letters "SH", the next ideas instantly come to mind:
"ASIC" (the mining algorithm has been changed from sha384 to RandomX that should have helped ordinary miners in their battle with ASICS), "a384" or "-384"  that stands form SHA 384 that is an old mining algorithm the was replaced by RandomX in this release. Also, HTTP server Ellis were replaced with Cowboy. And some IPFS arrangements as well.
 
Finally, i'd consider the next keys here: `ASIC, a384, -384, a256, -256, hash, mine, farm, earn, gpus, Elli, IPFS, luck, ...`

## 4-th key
![4-th key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/4.png )

This pic was mentioned in a small talk in discord between @Tiamat and one of the developers. That talk is not very helpful (given above).
Anyway, the first thing came to mind is AR transaction or AR coin transaction or swap procedure or selling or just pointing to the price or cost. Also, should be noted that transaction in AR bring\store the data.

Some could propose LOKI or SILO here (arweave product) [[7]](https://arweave.medium.com/building-silo-a-truly-private-internet-556c860222ca) - just look at picture in article

![LOKI - SILO](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/LOKI_SILO.png)

Finally, i'd consider the next keys here: `artx, LOKI, SILO, coin, cash, data, cost, rate, swap, sell, list, view, arql, luck, ...`

## 5-th key
![5-th key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/5.png )

One may notice here the map of SCANdinavia or more like Denmark, Norway, Sweden (DNS). And first things could be reasoned here: it is SCAN or PORT that is used in Arweave node that is 1984. Some others propose here LOKI from Scandinavian mythology that is also a name of " a decentralised network" that collaborated with Arweave in "the creation of SILO" (one of arweave product) [[7]](https://arweave.medium.com/building-silo-a-truly-private-internet-556c860222ca).

Finally, i'd consider the next keys here: `scan, port, 1984, silo, loki, " dns", luck, ...`

## 6-th key
![6-th key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/6.png )

Thats the tree. Interesting fact - it seems to have 4 roots, 4 branches, 32 leafs. @Tiamat mentioned this: " It's not my fault that people see a tree with - - - -  and they actually type TREE and expect to unlock.".

Well, not gonna judge his statement, but he said #3 should be very easy, so the option TREE was on my list before i've found that discord statement made by him. Tree could symbolize the graph or tree-like data structure. So it could be data, root, node or their alliases like "beam" (the is the name of the node program or daemon - correct me if i wrong). Also it could be Arweave-Sparse Merkle Tree (ASMT). Look this page stored in arweave for example [[8]](https://5ykygzjsftdm7ri7dutxuj45jiabjs7mvidaw5gaqbvcwkwm7wlq.arweave.net/7hWDZTIsxs_FHx0neiedSgAUy-yqBgt0wIBqKyrM_Zc
).

Finally, i'd consider the next keys here: `tree, root, ASMT, node, byte, data, beam, luck, ...`

## 7-th key
![7-th key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/7.png )

Many solvers got stuck on this picture, but i clearly see the easy answer here: it are letters U, p, L, L, that could form PULL (that can also be represented by its sound like pool).

Some think that it could be a point to UpVest that invested in arweave some funds [[9]](https://support.upvest.co/support/solutions/folders/47000738293)

Finally, i'd consider the next keys here: `pull,  pool, vest, node, fork, luck,...`

## 8-th key
![8-th key](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/8.png )

The last one is tricky, but seems to be mentioned by @Tiamat in his official twitter hints: " Did anybody count the dots?". Considering he pointed the picture 8 only and all black object on it, it results in 58 "dots". The base58 encoding is a typical in cryptosphere, so BASE could be mean here.

Finally, i'd consider the next keys here: `base, data, apps, dapp, star, cost, code, luck,...`


# "Exotic" ideas

1) I suppose, all the puzzle could be related to Arweave project [[10]](https://arweave.news/what-is-arweave-ar/),[[10']](https://arwiki.wiki/#/en/main) or even more convrete - the mining. Fresh article about Arweave mining could be found here [[10'']](https://arwiki.wiki/#/en/arweave-mining)

2) I have posted in twitter [[11]](https://twitter.com/miningpredict) an exotic idea - all 8 "keys" should form one sentence. Moreover, some words or symbols typed in __ __ __ __ placeholders could decay to pieces forming several words with its neighbors. Just look at an example below:

![idea?](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/idea.png)

3) Some telegram member assumed, that each picture could somehow be related to symbols on the PC keyboard: `1 - "!", 2 - "@", 3 - "#", 4 - "$", 5 - "%", 6 - "^", 7 - "&", 8 - "*"`
Should say, that this idea seems very funny and same time interesting. "!" - could be related to company anouncement (may be year or date),  @ could be related to emails or just mail, # is for hashing, $ - even presented on the picture itself and could be related to cash or cost or sell and swap or rate ..., % - rate (no great ideas here, maybe its from controlling symbols), ^ - top of the tree or fork or root etc., & - could be related to pools where miner & miner & miner ... do the work (lol), * - points even drawn on that picture but could be related to star or "luck" (anything). 


`to be continued`

# Brute-Force - "that's impossible (?!)" [12](https://www.youtube.com/watch?v=6ixvpLCdqkA)
![Its necessary](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/Cooper_necessary.gif)
![brute it TARS!!!](https://raw.githubusercontent.com/HomelessPhD/AR_Puzzles/main/PZL3/pics/interstellar-cooper.gif)

`TO BE WRITTEN VERY SOON (day or two i will fill this section)`


## P.S.

Thank you for spending time on my notes, i hope it was not totally useless and you've found something interesting. 

Any ideas\questions or propositions you may send to generalizatorSUB@gmail.com - also look at my twitter @MiningPredict.

I have read all Tiamat posts in discord. ENGLISH is not my native, i am tired af, its so boring\sleepy to read all those. I mean, it would be "hard" to read in Russian\Ukraine but in english magnified x2,x3. Now i have mostly the same ideas as before actually. Constructing new "brute" list. Will re-read all posts for those 6 months Tiamat talking about. Have already viewed all twitter posts\youtube videos\articles for that period of time. Discord and telegram on the way cause previously i have not viewed those.

-------------------------------------------------------------------------
### References:

[1] Original @ArweaveP (@Tiamat) tweet - https://twitter.com/ArweaveP/status/1132936723162378240

[2] Arweave Puzzle #3 stored in Arweave "blockchain" - https://kszeqgxezf5quhzld4nhpasyilhxphclq2peqi5mrn7utxmqhwga.arweave.net/VLJIGuTJewofKx8ad4JYQs93nEuGnkgjrIt_Sd2QPYw

[3] Telegram group of Arweave puzzles solvers community - @arweavep

[4] ZIP Code 21863 Snow Hill, MD, USA - https://www.unitedstateszipcodes.org/21863/

[5] Snow Hill Mine - https://thediggings.com/places/md0472391417/map

[6] Arweave Github, N.1.7.0.0 release of Arweave sources - https://github.com/ArweaveTeam/arweave/releases/tag/N.1.7.0.0

[6'] Arweave Github, arweave sources - https://github.com/ArweaveTeam/arweave/releases

[7] LOKI\SILO - https://arweave.medium.com/building-silo-a-truly-private-internet-556c860222ca

[8] ASMT - Arweave Sparse Merkle Tree -  https://5ykygzjsftdm7ri7dutxuj45jiabjs7mvidaw5gaqbvcwkwm7wlq.arweave.net/7hWDZTIsxs_FHx0neiedSgAUy-yqBgt0wIBqKyrM_Zc

[9] UpVest invested in Arweave - https://support.upvest.co/support/solutions/folders/47000738293

[10] AR - https://arweave.news/what-is-arweave-ar/
[10'] AR - https://arwiki.wiki/#/en/main
[10''] AR mining - https://arwiki.wiki/#/en/arweave-mining

[11] MiningPredict (my twitter page) - https://twitter.com/miningpredict

[12] "that's impossible (?!) no it's necessary"  - https://www.youtube.com/watch?v=6ixvpLCdqkA


-------------------------------------------------------------------------
### Support
I am poor Ukrainian student that will really appreciate any donations.
I have no home (flat\appartment), live in the dorm (refugee shelter).
 
P.S. Successfully evacuated from occupied regions of Ukraine.

**BTC**:  `1QKjnfVsTT1KXzHgAFUbTy3QbJ2Hgy96WU`

**LTC**:  `LNQopZ7ozXPQtWpCPrS4mGGYRaE8iaj3BE`

**DOGE**: `DQvfzvVyb4tnBpkd3DRUfbwJjgPSjadDTb`

**AR**: `0UM6uoLrrnxXuYpHMBDAv-6txNTMdaEkR2m_bP_1HyE`
(have never used Arweave wallet)
