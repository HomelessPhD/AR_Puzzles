# Advanced Solutions Research for Arweave Puzzles

## Executive Summary

This document contains advanced research and proposed solutions for the 4 unsolved Arweave puzzles: PZL3, PZL10, PZL11, and PZL12. After comprehensive analysis of solved puzzles (PZL5, PZL7, PZL8), clear patterns emerge that guide solution strategies.

---

## Patterns from Solved Puzzles

### Key Insights from PZL5 (SOLVED)
- **Answer**: `*48GCEErisUmberCastlePicasso`
- Solutions combined literal symbols (`*`), counting (`48` blades of grass), music theory (`GCE` piano keys), mythology (`Eris`), pop culture (`Umber` from GoT), chess notation (`Castle` = O-O), and art history (`Picasso`)
- **Critical Pattern**: Tiamat uses diverse knowledge domains - music, literature, chess, cultural references

### Key Insights from PZL7 (SOLVED - 57 chars)
- **Answer**: `Vivaldi227PermanentArnheimBulgakov1157Ulysses143176176209`
- Solutions required: classical music (Vivaldi), movie references (227 days in Life of Pi), anagrams (PET + manner = Permanent), literature (Edgar Allan Poe's Arnheim), Russian literature (Bulgakov), eclipse years (1157), children's literature (Flora and Ulysses - 2014 Newbery winner), geometry (perimeters 143, 176, 176, 209)
- **Critical Pattern**: HTML hints indicate answer length; anagrams are common; obscure cultural references required

### Key Insights from PZL8 (SOLVED)
- **Answer**: `RasputinWilhelmAlekhine`
- All three parts referenced famous historical deaths
- **Critical Pattern**: Historical knowledge; each image tells a story about HOW someone died

---

## PUZZLE #3 - Deep Analysis (1000 AR - ~$6k)

### Puzzle Structure
- 8 images, each requires a 4-character answer
- Total: 32 characters concatenated
- AES-256 encryption with 11,512 SHA-512 iterations

### Advanced Solution Proposals

#### Key 1 (Crooked Letters Image)
**Analysis**: The letters appear to spell "ANNO" or "AHNO" with curved/wavy lines.

**Most Likely Solutions**:
1. `2018` - Arweave ICO year (ANNO = "since" in Latin, pointing to founding year)
2. `a16z` - Andreessen Horowitz investor logo
3. `NOAH` - Letters rearranged (AHNO → NOAH), connects to "Ark" theme
4. `1984` - Port number for Arweave nodes; also "Big Brother" reference (curved lines = surveillance distortion)

**NEW HYPOTHESIS**: The curved lines might represent "ARC" (curved = arc). Before rebranding, Arweave was called **ARC**. Answer could be `ar->` or `ARC!` or `arCH` (arChain original name).

#### Key 2 (21863 in Diamond)
**Analysis**: ZIP code for Snow Hill, MD or missing-zero date (2018/06/03)

**Most Likely Solutions**:
1. `0603` - ICO date June 3rd (the missing zero theory)
2. `md12` - Route 12 through Snow Hill
3. `zero` - The missing "0" from 2018/06/03
4. `null` - Programming reference for the missing zero
5. `fund` - Token sale/funding event reference

**NEW HYPOTHESIS**: Given Snow Hill's location near Arweave HQ in London, and the diamond shape, this could be `head` or `home` (headquarters reference).

#### Key 3 (Mining/SH Letters)
**Analysis**: Mining imagery with "SH" letters, hinted as obsolete after N.1.7.0.0

**Most Likely Solutions**:
1. `a384` - SHA-384 (replaced by RandomX in N.1.7.0.0)
2. `ASIC` - Mining hardware made obsolete
3. `hash` - Generic mining reference
4. `IPFS` - IPFS integration announced in that release

**HIGH CONFIDENCE**: `a384` or `-384` (SHA-384 → "SH" visible, remaining is "A384")

#### Key 4 (AR Transaction Symbol)
**Analysis**: AR logo with transaction arrows, mentioned by developers as "obvious"

**Most Likely Solutions**:
1. `SILO` - Arweave privacy product
2. `LOKI` - Partner network for SILO
3. `cash` - AR.CASH was original token name
4. `coin` - Generic token reference
5. `fees` - Transaction fees

**NEW HYPOTHESIS**: Given the dev comment about @arweave-india "getting it right", this might be a Hindi/Sanskrit reference. Consider `DATA` (Arweave's core mission).

#### Key 5 (Scandinavia Map)
**Analysis**: Map of Denmark, Norway, Sweden with annotations

**Most Likely Solutions**:
1. `e4d5` - Chess notation for Scandinavian Defense opening
2. `1984` - Port number (also Orwell reference)
3. `.erl` - Erlang language (from Sweden)
4. `nord` - Nordic reference
5. `scan` - Obvious visual reference

**HIGH CONFIDENCE**: `e4d5` - Tiamat loves chess references (proven in PZL5 with "Castle")

#### Key 6 (Tree with 32 Leaves)
**Analysis**: Tree with 4 roots, 4 branches, 32 leaves - Tiamat said "don't type TREE"

**Most Likely Solutions**:
1. `ASMT` - Arweave Sparse Merkle Tree
2. `root` - Tree data structure
3. `hash` - Merkle tree = hash tree
4. `node` - Network node reference
5. `32AR` - 32 coins (block reward at that time)

**NEW HYPOTHESIS**: The hint "don't type TREE" with 32 leaves suggests binary tree. 32 = 2^5, so answer might be `fork` (blockchain fork) or `leaf` or `byte` (8 bits per byte, 4 bytes = 32 bits).

#### Key 7 (U, P, L, L Letters)
**Analysis**: Clear letters forming "PULL" or "UPLL"

**Most Likely Solutions**:
1. `pull` - Git pull / data pull
2. `pool` - Mining pool (sounds like PULL)
3. `vest` - UpVest investor reference
4. `UP##` - Some UP-related word

**HIGH CONFIDENCE**: `pull` (Git reference - developer-oriented puzzle)

#### Key 8 (58 Dots)
**Analysis**: 58 circular objects, Tiamat hinted "Did anybody count the dots?"

**Most Likely Solutions**:
1. `base` - Base58 encoding (common in crypto)
2. `dots` - D(4)+O(15)+T(20)+S(19) = 58!
3. `btc!` - Bitcoin uses Base58

**HIGH CONFIDENCE**: `base` (Base58 encoding reference)

### FINAL PROPOSED ANSWER FOR PZL3
Primary hypothesis: `2018a384SILOe4d5ASMTpullbase`
Alternative: `arc!zero-384cashe4d5hashpullbase`
Alternative: `NOAHfunda384datae4d5rootpullbase`

---

## PUZZLE #10 - Deep Analysis (500 AR - ~$3k)

### Puzzle Structure
- Shredded/assembled image with 5 key elements
- Key 4 specifies `[0-19]` = 20 character answer
- References: Dice (1,4), Numbers (6,3,18), Palpatine/Order 66, Genesis block #28

### Advanced Solution Proposals

**Key 1 - Dice**: Numbers shown are 1, 4 (winning positions) and 2, 1, 4, 2, 4 visible
- Could mean: `14` or `2142` or position reference

**Key 2 - Numbers 6, 3, 18**: ICO date 2018/06/03
- Could mean: `20180603` or `june` or `63`

**Key 3 - Palpatine with Arweave "a"**: Order 66 + 66M max supply
- Could mean: `66000000` or `order66` or `execute`

**Key 4 - [0-19]**: 20 characters constraint
- This LIMITS the total answer to 20 characters

**Key 5 - "...nesis #28"**: Genesis block transaction #28 = "We'll see what happens"
- Trump's famous phrase; also investor's message

### Critical Insight
The puzzle title references "Order 66" which in Star Wars means executing a command. Combined with:
- Genesis (#28) = "We'll see what happens" (20 chars including spaces!)
- [0-19] = exactly 20 characters
- Dice winning = 1 and 4

**NEW HYPOTHESIS**:
The answer might be the Genesis block message #28 itself, but modified:
- `We'llseewhat happens` (20 chars, no space in middle)
- `we'llseewhatHappens` (case-sensitive variation)

Alternative approach - combine all numeric clues:
- `14` (dice) + `20180603` (date) + `66` (order) = `1420180603066` (13 chars) + need 7 more

**STRONGEST HYPOTHESIS**:
The [0-19] constraint + Genesis #28 suggests: Take first 20 characters of the concatenated answer.
If keys 1-3 form parts that total >20 chars, slice to [0-19].

Proposed answer combining elements:
- `14june20186666000000` (20 chars) - dice, month, year, order 66, max supply
- `14060318order6628tx` (19 chars)
- `We'llseewhat happens` (exact 20 with space = 21, so maybe `Wellseewhat happens` = 19)

---

## PUZZLE #11 - Deep Analysis (1 ETH - ~$3.6k)

### Puzzle Structure
- Single PNG image with hidden Ethereum private key (steganography)
- Wallet: `0xFF2142E98E09b5344994F9bEB9C56C95506B9F17`
- Hint: "format does not matter" and "alternative forms of storing a private key"

### Image Analysis
The image shows:
- City skyline with ~12 buildings of varying heights
- Water/river in foreground
- Small sailboat (left)
- 5 sailboats in a row (right) - looks like a rowing crew/kayak formation
- Twitter watermark: `twitter.com/ArweaveP`

### Advanced Steganography Approaches

**Building Heights as BIP39 Words**:
- 12 buildings = 12-word seed phrase!
- Building heights observed: ~100, 190, 90, 165, 240, 55, 180, 160, 90, 160, 100, 190 pixels
- Map heights to BIP39 word indices (2048 words, need to normalize heights)

**NEW HYPOTHESIS - Height-to-Index Mapping**:
```
BIP39 has 2048 words. If max building height ≈ 240 pixels:
Index = height * (2048/256) = height * 8
Building 1 (100px) → Index 800 → BIP39 word #800
Building 2 (190px) → Index 1520 → BIP39 word #1520
... etc.
```

**LSB Steganography - Advanced**:
- Focus on the ALPHA CHANNEL (image has grayscale with alpha)
- Non-zero alpha values cluster around the biggest boat
- Extract pixels where alpha > 0, read their grayscale values as private key bytes

**Coordinate-based**:
- Image mentions real-world location (Canary Wharf, London, Boston, Sydney)
- If Boston/Canary Wharf, specific building coordinates could encode data

**Private Key Structure**:
- Ethereum private key = 64 hex characters (32 bytes)
- Need to find 32 bytes hidden in the image

**STRONGEST HYPOTHESIS**:
The "biggest boat" emphasis + alpha channel non-zero values around it suggests:
1. Extract all pixels with non-zero alpha channel
2. Use their grayscale values (or coordinates) as the private key
3. Or: the 5 boats on right = 5 parts of data, sailboat = final piece

Alternative: The image dimensions (1600x1105) could encode something:
- 1600 * 1105 = 1,768,000 pixels
- Total bytes in grayscale = 1,768,000
- Look for specific byte pattern

---

## PUZZLE #12 - Deep Analysis (400 AR - ~$3k)

### Puzzle Structure
- 4 puzzle pieces forming 58-character answer (case-sensitive)
- Pieces can be in different order (4! = 24 permutations)

### Advanced Solution Proposals

#### Piece 1 - Flag IQ Test
**Analysis**: 6 flags with endpoint styles, positions, and colors

Pattern observed:
- Flags come in pairs (ball endpoint / no ball)
- Colors: Red, Purple, Gray, Green, Purple, White (unknown)

**Color Pattern Analysis**:
```
RGB values suggest a progression:
Red:    (192,   0,   0)
Purple: ( 65,   0, 128)
Gray:   (128, 128, 128)
Green:  ( 63, 128,   0)
Purple: (127,   0, 255)
White:  (255, 255, 255) → The answer!
```

**NEW HYPOTHESIS**:
The white flag's color should follow the pattern. Looking at the RGB values:
- R channel: 192 → 65 → 128 → 63 → 127 → ?
- G channel: 0 → 0 → 128 → 128 → 0 → ?
- B channel: 0 → 128 → 128 → 0 → 255 → ?

The answer might be the COLOR NAME or the RGB values of what white "should" be in the pattern.
Possible: `Yellow` (255, 255, 0) or `Cyan` (0, 255, 255) based on complementary patterns.

Or answer is simply: `White` or `Milk` or the pattern number sequence

#### Piece 2 - Whale + Date 16-03-2020
**Analysis**: Points to Andreessen Horowitz $8.3M investment announcement

**Most Likely Solutions**:
- `AndreessenHorowitz` (18 chars)
- `a16z` (4 chars)
- `8300000` (7 chars - funding amount)
- `Horowitz` (8 chars)
- `whale` (5 chars)

**HIGH CONFIDENCE**: `a16z` or `AndreessenHorowitz` or combination with date

#### Piece 3 - Shape Cipher
**Analysis**: SQUARE=101111, DIAMOND=2111112, RECTANGLE=111211021, HEXAGON=?

Pattern: Each digit represents a letter's position relative to baseline:
- 0 = letter extends below (like g, p, y)
- 1 = letter stays on line (like a, e, s)
- 2 = letter extends above (like b, d, h) OR below

For HEXAGON (H-E-X-A-G-O-N):
- H = extends above = 2
- E = on line = 1
- X = crosses both = 1 (or special)
- A = on line = 1
- G = below = 0
- O = on line = 1
- N = on line = 1

**HIGH CONFIDENCE**: `2111011` for HEXAGON

#### Piece 4 - 5-Letter Word from A, L, I, E, N
**Analysis**: Squares with different dashing patterns around letters

**Most Likely Solutions**:
- `ALIEN` (most common arrangement)
- `ALINE` (a line - programming reference)
- `LIANE` (a climbing plant)
- `ANILE` (relating to old women)
- `ELAIN` (chemistry compound)

**NEW HYPOTHESIS**: The dashing patterns might indicate ORDER:
- Analyze dash patterns to determine correct letter sequence
- Or: the answer is longer, using repeated letters

### FINAL PROPOSED ANSWER FOR PZL12
Assuming 58 characters, case-sensitive, 4 pieces:

**Permutation possibilities (piece order matters)**:
1. Piece1 + Piece2 + Piece3 + Piece4
2. Piece2 + Piece1 + Piece3 + Piece4
... (24 total permutations)

**Most likely 58-char combinations**:
- `White16-03-2020AndreessenHorowitz2111011ALIEN` (46 chars) - needs more
- `WhiteandreessenHorowitz8300000USDMarch2111011ALIEN` (51 chars)
- Possibility: pieces have longer answers than expected

**Strongest complete hypothesis**:
`255255255a16z8300000March2020211101ALIEN` + variations with proper capitalization

---

## Recommended Testing Priority

### PZL3 (Highest Reward)
1. Test: `2018a384SILOe4d5ASMTpullbase`
2. Test: `2018-384datae4d5hashpullbase`
3. Test: `a16za384LOKIe4d5roothashbase`
4. Test: `anno0603ASICcashe4d5leafpullbase`

### PZL10
1. Test: `We'llseewhat happens` (exact genesis message variants)
2. Test: `14063186600000028` + variants
3. Test: `execute66201863014`

### PZL11
1. Run LSB steganography on alpha channel around biggest boat
2. Map 12 building heights to BIP39 indices
3. Extract all non-white pixels and analyze patterns

### PZL12
1. Test: `Whitea16z8300000March20202111011ALIEN` + permutations
2. Test: `255255255AndreessenHorowitz2111011LIANE`

---

## Technical Notes

### Encryption Details
All puzzles use:
- AES-256 encryption
- 11,512 SHA-512 iterations for key derivation
- CryptoJS library (has unique behavior different from standard implementations)
- Validation: Look for `"kty":"RSA"` in decrypted content

### Brute Force Considerations
- ~0.5 sec per attempt in browser JavaScript
- Pre-computing SHA-512 hashes improves speed
- Go/Python hybrid: 40-60 combos/sec/thread
- CUDA acceleration available in repository

---

## Conclusion

Based on pattern analysis from solved puzzles, the most promising approaches are:
1. **PZL3**: Focus on Arweave-specific terminology and chess references
2. **PZL10**: Genesis block message #28 is likely central to the solution
3. **PZL11**: BIP39 seed phrase from building heights or alpha channel steganography
4. **PZL12**: Shape cipher is nearly solved (2111011); flag IQ test and whale reference need color/investor analysis

The puzzles reward deep knowledge of:
- Arweave project history and terminology
- Chess notation and moves
- Classical music and literature
- Cryptocurrency fundamentals (BIP39, Base58)
- Visual pattern recognition and steganography

---

## Additional Web Research Findings (December 2024)

### Current Puzzle Value
According to recent discussions, **PZL3 alone is worth over $21,000** at current AR prices. The total unclaimed rewards across all puzzles represent a significant treasure.

### Confirmed Community Consensus on PZL3

1. **Key 8 (58 Dots)**: The community strongly agrees this refers to **Base58** encoding. Tiamat's hint "Did anybody count the dots?" directly points to the 58 dots = Base58.

2. **Key 3 (Mining/SH)**: After N.1.7.0.0 release, Arweave moved from SHA-384, making the mining reference "obsolete." The "SH" visible likely leaves "A384" as the answer.

3. **Key 6 (Tree)**: Tiamat explicitly said "don't type TREE" - this confirms the answer is NOT tree but something tree-related (ASMT, root, hash, etc.)

4. **Key 4 (AR Transaction)**: Community speculation suggests "Rate" (exchange rate AR/USD) might be the answer.

### Puzzle Creator Philosophy
From Tiamat's interview: *"I also see it as a good way to raise awareness about the Arweave project."* This confirms puzzles are heavily Arweave-themed and require knowledge of the project's history, technology, and community.

### Steganography Techniques in Crypto Puzzles
Research on similar puzzles (like "Wealth in Poetry" with 0.03 BTC) reveals common techniques:
- **Trithemian seeds**: BIP39 words hidden in plain text
- **Building/visual element encoding**: Heights or positions mapping to seed phrase indices
- **Alpha channel hiding**: Data embedded in transparency layer

---

## External Resources

- [GitHub: AR_Puzzles Repository](https://github.com/HomelessPhD/AR_Puzzles)
- [Medium: Can you solve the 1000 AR puzzle?](https://dionguillaume.medium.com/can-you-solve-this-1000-ar-puzzle-worth-over-21-000-30e9f7f1d5ea)
- [Medium: Community Spotlight - Meeting Tiamat](https://arweave.medium.com/community-spotlight-meeting-tiamat-e484655b25e0)
- [X/Twitter: Forward Research on Tiamat's Puzzles](https://x.com/fwdresearch/status/1991816223454314555)
- [Telegram: @arweavep puzzle solver community](https://t.me/arweavep)

---

*Research compiled: December 2024*
*Total unsolved rewards: ~1000 AR + 500 AR + 1 ETH + 400 AR ≈ $21,000+ (AR value fluctuates)*
