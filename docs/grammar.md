---
title: A Grammatical Appendix @ HuangSupplement
description: Contributions to a real grammar of Mandarin Chinese
permalink: grammar/
seo:
  type: Guide
  name: A Grammatical Appendix
last_modified_at: 2025-01-17T08:44:16+00:00
layout: anchor
---
# A Grammatical Appendix
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
## 2 Syntax

### Gaps in terminology

|          |        | [Oxford](https://t18d.github.io/HuangSupplement/tally/#the-oxford-chinese-dictionary) | Huang–Shi | Chang |
|----------|:-----:|:------:|:-----:|:-----:|
| phoneme  |  音素  |   音位  |  音位  | 音位  |
| phone    |  単音  |   音素  |   /   |   /   |
| morpheme | 形態素 |   詞素   |   /   |  語素 |
| morph    |    /  |    /    |   /   |   /  |
| lexeme   | 語彙素 |     /   |  詞位  |   /  |

See further [On Diglossia](https://t18d.github.io/HuangSupplement/diglossia/) and [**consistency of sets**](https://t18d.github.io/HuangSupplement/dictionary/#sets-consistency-of).

### Emic

The consequences of a failure to distinguish between **morphs** and **morphemes** are of two kinds:

1. By using the term _morpheme_ when they really mean a _morph_, one can like Huang–Shi miss a whole phenomenon like [**orthographic alternation**](#orthographic-alternation).
2. By not grasping the difference between **abstract units** and their physical **realisation**, one can fall prey to irrelevant concepts such as _êrh tzŭ tz'ŭ_ (e.g. Shên 2019) and _spondee_ which describe **orthography** and **prosody** respectively.

## 15 Coordination

### Asyndetic coordination

[Dictionaries](https://t18d.github.io/HuangSupplement/tally/) and Chang §4.4.4.3 give the impression that as a marker of **asyndetic coordination** -等 must be followed by a **numeral classifier**. This is _not_ true; other clues, e.g. 都, can also serve to show that it is an exhaustive enumeration.

**Example:** 比如時間、地點、工具<ins>等</ins>短語都有語序變化問題 (2010)

## 19 Lexical word-formation

### False tests

**Expansion**-based tests are _not_ a reliable tool for distinguishing between syntactic constructions and **compounds**. Their operation ultimately depends on knowledge of semantic content and orthographic conventions. Under the delusion that syntactic rules are **innate**, however, faulty lexical analysis is often used to explain away conflicting evidence.

**Examples:** A matchbox is _not_ a box for matches (CGEL §14.4), but one in which matches are sold, with a striking surface on one side; 羊肉 is _not_ equivalent to 羊的肉 (Chang §5.2.2.3), but flesh of sheep used as food.

### Two-character morphs

-主義 (1883) was borrowed from Japanese as a bound root. It constitutes a single morph which cannot be analysed into 主 and 義. Similarly, -製品 (1880).

### Defining 'word'

In _Mandarin_ Chinese, a native **word** is a **lexeme** realised by

1. a free **morph** _or_
2. a compound of two or more **morphs** _or_
3. a compound of a **bound root** as head and a **word** as dependent _or_
4. a fossilised NP.

### Words _vs_ phrases

Huang–Shi §8.5.1 gives up trying to distinguish between compounds and NPs; Chang §5.2.1.2 meekly accepts Lü's arbitrary rule. The following analysis implements the [defition](#defining-word) above on Chang's examples:

||人造|絲|
|:-:|:-:|:-:|
|Rule 1||free morph|
||adjective|noun|
|NP|modifier|head|

||人造|纖維|
|:-:|:-:|:-:|
|Rule 1||free [morph](https://t18d.github.io/HuangSupplement/grammar/#two-character-morphs) (Japanese, 1897)|
||adjective|noun|
|NP|modifier|head|

||豆|製品|
|:-:|:-:|:-:|
|Rule 3|word|bound [morph](https://t18d.github.io/HuangSupplement/grammar/#two-character-morphs) (Japanese, 1880)|
||noun|nominal bound root|
|noun|dependent|head|

||生物|製品|
|:-:|:-:|:-:|
|Rule 3|word|bound [morph](https://t18d.github.io/HuangSupplement/grammar/#two-character-morphs) (Japanese, 1880)|
||noun|nominal bound root|
|noun|dependent|head|

||耐火|磚|
|:-:|:-:|:-:|
|Rule 1||free morph|
||adjective|noun|
|NP|modifier|head|

||耐火|材料|
|:-:|:-:|:-:|
|||word (s.xi)|
||adjective|noun|
|NP|modifier|head|

||自由|泳|
|:-:|:-:|:-:|
|Rule 3|word|bound morph|
||adjective|nominal bound root|
|noun|dependent|head|

||自由|體操|
|:-:|:-:|:-:|
|Rule 1||free [morph](https://t18d.github.io/HuangSupplement/grammar/#two-character-morphs) (Japanese, 1889)|
||adjective|noun|
|fossilised NP|complement|head|
|Rule 4|||

Implementation for examples in Huang–Shi §3.4.2:

||光|線|
|:-:|:-:|:-:|
|fossilised NP|complement|head|
|Rule 4|||

||水|土|
|:-:|:-:|:-:|
|Rule 2|morph|morph|
|noun|||

### Orthographic alternation

A **lexeme** is often realised by multiple **orthographic variants**, which can be either **stylistic** variants or **free** variants. The **alternation** takes the form of **allomorphy** in one or more of the **morphs**.

**Example:** 通假 (s.xii) _vs_ 通叚 (s.xix)

### -等國

Huang–Shi §3.5.1.1:

> 英法等國 … 'countries like England and France.' … a case of conventionalized contextual ellipsis.

Both the gloss and the analysis are wrong. They illustrate some of the commonest pitfalls in **synchronic** analysis:

1. The **elided** part must be unambiguously specified.
2. No attention is paid to **paradigmatic alternants** like -等地, where a **semantically equivalent** full form is not in use. Cf. 英法等國 _vs_ 英法等國家 with 台北上海等地 _vs_ <sup>#</sup>台北上海等地區 _vs_ <sup>#</sup>台北上海等地方 _vs_ 台北上海等城市.
3. No attention is paid to more established alternants such as 各國 (1602) and 各地 (1822), from which -等國 and -等地 are created **by analogy**.

英法等國 should be glossed as 'Britain and France' (等 as marker of [**asyndetic coordination**](#asyndetic-coordination)) or 'Britain, France and other countries' (等 as **abbreviatory device**).

## 20 Punctuation

By abandoning any pretence of being **descriptive** of real-world usage, the appendix on punctuation is probably the weakest chapter in Huang–Shi.

An adequate treatment of Mandarin punctuation must take account of the following facts:

1. Punctuation marks are _not_ an integral part of written Mandarin. It is very common in written communications to use **space** as the only punctuation **indicator**.
2. The actual **set** of punctuation marks being used varies considerably depending on the particular Mandarin-speaking **region** and personal preferences as influenced by **contact with other languages**, especially Japanese and English.
3. **Unicode** glyphs and descriptions must be used if punctuation marks are to specified unambigously.
