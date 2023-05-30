#!/bin/bash

rm block_txs.txt

for i in `seq 1 1 13`; do
    #curl https://viewblock.io/arweave/block/0?page=$i -o temp
    python3 scrap.py $i > temp
    grep -Po '(?<=href=")[^"]*' temp | grep /tx/ >> block_txs.txt
    rm temp
done

