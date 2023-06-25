# Arweave Puzzle #11 - "#Stegonagraphy ...format does not matter..."

Here i am going to publish ideas i consider about and dummy instruments related to Arweave puzzle #11.

This puzzle is one from the series of Arweave Puzzles made by @Tiamat (official Arweave project discord member, apps developer, miner, early investor). Originally, puzzle posted in official @Tiamat twitter [[1]](https://twitter.com/arweavep/status/1252961944807641090): with hints and link to the blockchain [[2]](https://bmzbghtrbcleimhve3nf7f7owqwmllfjgwu67toc6wtsagmp3h3a.arweave.net/CzITHnEIlkQw9SbaX5futCzFrKk1qe_NwvWnIBmP2fY)

***Meanwhile, THE ORIGINAL Tiamat TWEET was DELETED***, but comments (including his own comments as well as mine) are still there.

Puzzle consists of the single PNG file (picture) (sources also attached in this git - but could be found on Arweave "blockchain"). In contrast to most AR puzzles, this one has no encrypted message and so there is no page with decryption code. The author stated that Private Key (to the ***1 ETH (~1900$)*** wallet [[3]](https://etherscan.io/address/0xFF2142E98E09b5344994F9bEB9C56C95506B9F17) somehow "hidden" in this image and the way to claim the prize is to extract the private key from it.

![AR puzzle #11](https://github.com/HomelessPhD/AR_Puzzles/blob/1bd70c836a55b7b3a093e0cce7186e2daba416b1/PZL11/CzITHnEIlkQw9SbaX5futCzFrKk1qe_NwvWnIBmP2fY.png)

# The official hints given by the puzzle creator are listed below:

    
```
    From Twitter:
    
    1] "0xFF2142E98E09b5344994F9bEB9C56C95506B9F17 it is also included somewhere in the image 🧐"

    2] One guy asked: "What's the photo format. It'smnot JPG !?"
       And Tiamat answered: "format does not matter"

    3] Someone asked for more hints: "Can we get another hint?"
       But Tiamat replied: "Next set of hints when AR reaches $100 :)"

```    

Some ideas came to my mind, others were captured from Twitter or\and the telegram group [[4]](@arweavep) - you definitely should visit it for ideas sharing.
(at first few months i have forcefully avoided visiting any forums or groups when i saw the puzzle at first because i thought that ideas of others could freeze my own thinking process - it is when you start to think primarly in the way proposed by some other solver and, got stuck on it, but later trying my own ideas with my own dummy brute forcing method i skipped that rule. I am actively posting any ideas came to my mind in that group, hoping someone of us will be able to solve the puzzle sharing some part of revenue and GLORY)

## Picture METADATA
Given *.PNG file (picture) contain some interesting METADATA:
1] ```color_type: Grayscale with Alpha``` - The image has extra 8bit channel withing the Grayscale. The alpha channel, that code the "transaprecy", mostly zero over all picture but have non-zero values in some points around the Biggest Boat - it could be a hint that stresses us to pay bigger attention to the biggest boat, it could be coincidence showing that boat was copy-pasted from another canvas and so its just a noise in alpha channel, or it could be done in order to save the PNG image from twitter destortion (PNG images without alpha channel usually re-packed by twitter and so could loss some information, i faced that thing by myself and to avoid that staff the user could add some aplha channel data to the picture)

2] Some less valuable data - better view this in HEX format (discussed a bit lower in this article - PNG chunks data)
```
gamma 2.2
white_point_x 0.3127
white_point_y 0.329
red_x 0.64
red_y 0.33
green_x 0.3
green_y 0.6
blue_x 0.15
blue_y 0.06
background_color 0
pixels_per_unit_x 2835
pixels_per_unit_y 2835
pixel_units meters
```

3] And here is something really interesting:
```
warning [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
comment 0xFF2142E98E09b5344994F9bEB9C56C95506B9F17
datecreate 2020-03-30T11:38:07+03:00
datemodify 2020-03-30T11:34:44+03:00
image_size 1600x1105
```

The "comment" field appeared (that is ignored by typical Image Viewers) with the Prize address. I have not found this address anywhere else than in Tiamat comment and i guess Tiamat meant this place where we cand found the Prize Address.

The datecreate and datemodify fields are "strange", right? create 2020-03-30T11:38:07+03:00 modify 2020-03-30T11:34:44+03:00. This seemed strange to me at first, but later i've checked others Tiamat puzzle pictures and found out this occasion in them too. So, for now, i am not so happy and enthusiastic with this strange dates (modified earlier than created, and difference is 143 seconds?) 

Also, the one who solving this should consider the date of 1 ETH transfer: 04-14-2020 09:10:29 in accordance to etherscan. 


## PNG service fields - "PNG chunks"

A PNG file is composed of an 8-byte signature header, followed by any number of chunks that contain control data / metadata / image data. Each chunk contains three standard fields – 4-byte length, 4-byte type code, 4-byte CRC – and various internal fields that depend on the chunk type.

There are online tools for PNG "chunks" inspection, here is one of them [[5]](https://www.nayuki.io/page/png-file-chunk-inspector).

I've noticed cHRM PNG chunk - nice 32 bytes (just like the Private Key should be): 00007a26000080840000fa00000080e8000075300000ea6000003a9800001770. Tried reversed too. No success.

![PNG chunks](https://github.com/HomelessPhD/AR_Puzzles/blob/13acff7c922b35015a04556534219b6d8a20401e/PZL11/pics/Chunks.png)

Have also tried to list all PNG chunk names: 4948445267414d416348524d624b474470485973494441547445587449454e44. No success.

## LSB
....

## BUILDING HEIGHT-WIDTH
The first thing that could came to mind looking that picture - the "buildings" code something. There are exactly 12 buildings, right? And one of possible way to code the Private Key is 12 BEP39 words. Interesting coincidence.

I've tried to estimate the building sizes:

```
height: 100 190 90  165 240 55  180 160 90  160 100 190
width:  115 90  100 170 100 100 150 110 110 100 70  50
```

But have not succeed Private Key extraction, yet.
May be we should transform this sizes to 256 bit number (introduce some grid for height\width and transform this 12\12 numbers into 256 bits .... 
Maybe we should rank the BEP39 wordlist (2048 English words of different length from 4 to 8 letter - check here [[6]](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt)

Maybe we should name all objects on image, write out all their synonyms, filter through BIP39 English word-list and than list them in the order of lengths like buildings height? 

```
...
[boat]: boat, craft, canoe, sail, ship, bottom
[shadow]: shadow, gloom, obscure, cover,
...
```



## Information hidden in the plain sight - may be even in plain text. It could private key, seed phrase or some valuable hint etc.

Guessed that KEY is written as plain text:  some pixel values used for PK and others to form the picture, make the noise, distruct. 
Here Histogram, few "collored" picture + central (127 p. with 40 p. width) histo-slice. I feel like PK is on the biggest boat but cant get it.

![HISTOGRAM](https://github.com/HomelessPhD/AR_Puzzles/blob/b9781b93c256d7868a48e11ae0f6d87a27d03706/PZL11/pics/plain_HIST.png)

![filtered histogram 1](https://github.com/HomelessPhD/AR_Puzzles/blob/b9781b93c256d7868a48e11ae0f6d87a27d03706/PZL11/pics/plain_FILTERED_1.png)

![filtered histogram 2](https://github.com/HomelessPhD/AR_Puzzles/blob/b9781b93c256d7868a48e11ae0f6d87a27d03706/PZL11/pics/plain_FILTERED_2.png)

![filtered histogram 3](https://github.com/HomelessPhD/AR_Puzzles/blob/b9781b93c256d7868a48e11ae0f6d87a27d03706/PZL11/pics/plain_FILTERED_3.png)

Should add here - i've tried to cut different parts of histogram, played with that alog and yet no result. BUT i rellay feel like this is it, there could be a text typed and noised on on that boat image. Zooming out i mostly see it.

![boat hide wallet](https://github.com/HomelessPhD/AR_Puzzles/blob/f2d7820a5191dd3db05e3d6cdc6a6de3e5a27a7d/PZL11/pics/plain_boat.png)

And yet another thing - "https://twitter.com/ArweaveP". Thats 20 symbols written on the picture, on the plain sight. Tried to make sha256 form it and nothing. Tried its ASCII adding zero bytes - nothing again.


# "Exotic" ideas

1] What if the given picture represent some real world place? Some skyscrappers pictured or shotted above the reaver or smth?!

Like Canary Wharf or some else city with "scyscrapers" panorama (Sidney, Boston, New York ....). 
May be the author left the key or hint in Google Maps (for example on photo uploaded and bounded to the specific coordinates).

![scyscrapper #1](https://github.com/HomelessPhD/AR_Puzzles/blob/ca373d9e7e72805666c072250ed285096412db1c/PZL11/pics/skyscrap_1.jpg)
![scyscrapper #2](https://github.com/HomelessPhD/AR_Puzzles/blob/ca373d9e7e72805666c072250ed285096412db1c/PZL11/pics/skyscrap_2.jpg)


`to be continued`



## P.S.

Thank you for spending time on my notes, i hope it was not totally useless and you've found something interesting. 

Any ideas\questions or propositions you may send to generalizatorSUB@gmail.com - also look at my twitter [[*]](https://twitter.com/miningpredict) @MiningPredict.

-------------------------------------------------------------------------
### References:

[1] Original @ArweaveP (@Tiamat) tweet - 
https://twitter.com/arweavep/status/1252961944807641090

[2] Arweave Puzzle #11 stored in Arweave "blockchain" - https://bmzbghtrbcleimhve3nf7f7owqwmllfjgwu67toc6wtsagmp3h3a.arweave.net/CzITHnEIlkQw9SbaX5futCzFrKk1qe_NwvWnIBmP2fY

[3] THE PRIZE - https://etherscan.io/address/0xFF2142E98E09b5344994F9bEB9C56C95506B9F17

[4] Telegram group of Arweave puzzles solvers community - @arweavep

[5] PNG service fields (chunks) inspecting tool -  https://www.nayuki.io/page/png-file-chunk-inspector

[6] BEP39 English seed wordlist - https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

[*] MiningPredict (my twitter page) - https://twitter.com/miningpredict

-------------------------------------------------------------------------
### Support
I am poor Ukrainian student that will really appreciate any donations.
I have no home (flat\appartment), live in the dorm (refugee shelter).
 
P.S. Successfully evacuated from occupied regions of Ukraine.

**BTC**:  `1QKjnfVsTT1KXzHgAFUbTy3QbJ2Hgy96WU`

**LTC**:  `LNQopZ7ozXPQtWpCPrS4mGGYRaE8iaj3BE`

**DOGE**: `DQvfzvVyb4tnBpkd3DRUfbwJjgPSjadDTb`

 **BSV**: `1E56gGQ1rYG4kkRo5qPLMK7PHcpVYj15Pv`

**AR**: `0UM6uoLrrnxXuYpHMBDAv-6txNTMdaEkR2m_bP_1HyE`
(have never used Arweave wallet)
