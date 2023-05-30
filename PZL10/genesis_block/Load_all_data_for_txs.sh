#!/bin/bash

rm all_block_data.txt
rm all_block_data_numbered.txt

i=1
for tx_tag in `cat block_txs.txt`; do
    tx_add=`echo $tx_tag | cut -d'/' -f4`
    wget https://arweave.net/$tx_add --output-document temp_data
    tx_data=`cat temp_data`
    echo "$i $tx_data">> all_block_data_numbered.txt
    echo "$tx_data">> all_block_data.txt
    rm temp_data
    i=$(( i+1 ))
    sleep 2
done
