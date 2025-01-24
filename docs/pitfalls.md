---
title: Pitfalls in Historical Lexicography @ HuangSupplement
permalink: pitfalls/
seo:
  type: Collection
  name: Pitfalls in Historical Lexicography
last_modified_at: 2025-01-24T03:58:12+00:00
layout: anchor
description: Gleanings from HuangSupplement
---
# Pitfalls in Historical Lexicography

<p align="right">Gleanings from HuangSupplement</p>

&nbsp;  
&nbsp;  
&nbsp;  
## diachronic semantics

```diff
- 汽車,2,noun,1855,,B. Hobson『博物新編』,
+ 汽車,2,noun,1903,近有法人与英人及他国人合擬賭賽。汽車由法京巴黎斯至日斯巴尼亜京城馬得利脱。,『申報』5月27日「賽車肇事」,
```

汽車 always meant train in the 19th century. All exx. in Chao (2016), p. 232, actually refer to trains.

That's Chu Chün-sheng's 望文生訓.

[184802e](https://github.com/t18d/HuangSupplement/commit/184802ea9877186b40b7e33c3b3a4d7926029dfb), [f7352a1](https://github.com/t18d/HuangSupplement/commit/f7352a1d426877852ee4ceca7a91740278a6612e)

## dictionary evidence

**Dictionary evidence** is used liberally in HuangSupplement and treated as _first class_.

A **nonce word** attested in a dictionary is just that, a **hapax legomenon**. A word first found in a dictionary is no less a word – to be adopted, ignored or reinvented, as the case may be. It doesn't matter how it got there.

**Usage statements** made by lexicographers, on the other hand, are subject to the same caveats that apply to reports of **fieldwork**.

<p><details>
    <summary>Bibliography</summary>
    <h3>Pace …</h3>
    <ul>
      <li>Hawke, Andrew, '11.11.2 Dictionary Evidence', in Philip Durkin (ed.), <em>The Oxford Handbook of Lexicography</em> (Oxford, 2016), 192–3.</li>
      <li>Osselton, N.&VeryThinSpace;E., 'Secondary Documentation in Historical Lexicography', in <em>Chosen Words: Past and Present Problems for Dictionary Makers</em> (Exeter, 1995), 137–47.</li>
    </ul>
</details></p>

<p><details>
    <summary>Exception</summary>
    <br>
    <ul>
      <li>Gilliver, Peter, 'Dictionary words', in John Considine (ed.), <em>Adventuring in Dictionaries: New Studies in the History of Lexicography</em> (Newcastle upon Tyne, 2010), 216–8.</li>
    </ul>
</details></p>

## IC analysis

> 忠厚老成者擯之為無能，俠少儇辨者取之為可用，守道愛國者謂之為流俗，敗常害民者謂之為通變。

I do not think 愛國者 here is a constituent. I'm leaning towards `[[守道][愛國]者]謂之為流俗` where 者 is not attached to 愛國 as a suffix.

[pull/2#issuecomment-2539182438](https://github.com/t18d/HuangSupplement/pull/2#issuecomment-2539182438)

## new edition, new name

Schmidt mistakenly dated _Hand Book of New Terms and Newspaper Chinese_ to 1913, when it was first published in 1917 (see [preface](https://babel.hathitrust.org/cgi/pt?id=mdp.39015021731313&seq=9) in the book dated 1917, where Mateer stated that the 1917 _Hand Book of New Terms and Newspaper Chinese_ was an improvement to the _New Terms for New Ideas_ published in 1913.

[pull/2#issuecomment-2541665188](https://github.com/t18d/HuangSupplement/pull/2#issuecomment-2541665188)

## original punctuations

> It was a 。 in the 1934 edition of [飲冰室全集](https://commons.wikimedia.org/wiki/File:SSID-13347803_%E9%A3%B2%E5%86%B0%E5%AE%A4%E5%85%A8%E9%9B%86_%E4%B8%8A.pdf). 自由書 was originally written in 1899.

This is actually non-trivial: even when an author personally oversaw the production of their own collected edition, there’s no guarantee that what they print there reflects what they printed the first time.

What gets changed may be a punctuation mark, but it could just as likely be a word.

[pull/2#discussion_r1883680686](https://github.com/t18d/HuangSupplement/pull/2#discussion_r1883680686)

## reinventing the wheel

```diff
- 本文,the original (text),noun,1857,合衆領事、及日本官、於兩國方言文字、均不能互相明曉、故於合約中准用荷蘭字為本文,"『六合叢談』1/12, 11",
```

本文 in this sense dates back to 3rd century

```diff
- 本土,local,adjective,1857,有本土邏卒四人、為華民所殺,"『六合叢談』1/4, 15+",
```

This sense of 本土 dates back to 11th century

[f4e8297](https://github.com/t18d/HuangSupplement/commit/f4e8297a1459d10285015b5d3b30ff885771578d), [10200d6](https://github.com/t18d/HuangSupplement/commit/10200d667f8782e6f418bd58cd5d2e449b073a36)

## reverse translation

```diff
- 內容,/,noun,1839,,林則徐『嚴禁本地民人與外人非法往來交易告示』,
```

Even the very title of this proclamation came from a translation by the editors of Lin. See https://books.google.com/books?id=ngMMAAAAYAAJ&pg=PA212.

> 為迄今中外資料中未見原文者，現按英文譯回來。

[1574258](https://github.com/t18d/HuangSupplement/commit/157425807f2b66ec69fc56cbe6804d77362298cc)

## same set, same period

```diff
- 槍彈,/,noun,1874,大日斯巴尼亞國 定造鎗並鎗彈,"『萬國公報』306, 21?",
- 槍械,/,noun,1872,…,志剛『初使泰西記』,
+ 槍彈,/,noun,s.xvii,受數百槍彈從脅穿透,『行在陽秋·下』,
+ 槍械,/,noun,1600,疏火器鳥銃長短槍械法,『譚襄敏奏議·序』,
```

槍彈 & 槍械 are in a set with 槍砲 (1643) and should date from the same period.

Cf. [**consistency of sets**](https://t18d.github.io/HuangSupplement/dictionary/#sets-consistency-of).

[cd7b712](https://github.com/t18d/HuangSupplement/commit/cd7b712d8378c9eb0b41a2770c824320036b336a)

## same word, different orthography

```diff
+ 偶像,/,noun,1927,我好像也已經成了偶象了,魯迅『兩地書·一〇五』,metaphorical
```

A word is a word whatever its surface orthography. The phenomenon, of course, is a very old one in Chinese.

See further [**Orthographic alternation**](https://t18d.github.io/HuangSupplement/grammar/#orthographic-alternation).

[2247d61](https://github.com/t18d/HuangSupplement/commit/2247d61a7a29015fe309c1d910501e839677ada1)

## same year, whose priority?

```diff
- 兵工廠,/,noun,1917,"Arsenal 軍械局, 兵工廠","A. H. Mateer, _Hand Book of New Terms and Newspaper Chinese_",
```

> Antedating fails. Huang cites 朱執信 1917 中國存亡問題 as a source.

Mateer’s cut-off date was mid-1916 according to herself, and Chu is known to be penning his in 1917. We do want to establish the exact priority here.

[pull/2#discussion_r1886144398](https://github.com/t18d/HuangSupplement/pull/2#discussion_r1886144398)

## searching OCR layer

> 安樂椅子 not found in New Terms for New Ideas (1913) or Hand Book of New Terms and Newspaper Chinese (1917)

<img src="https://t18d.github.io/HuangSupplement/assets/椅子.webp" width="50%">

Characters can easily get dropped so you just have to search for all the substrings as well before you can say for sure that it’s not there.

That’s the lexicology counterpart to the phonetician Chao’s 言無難.

<p><details>
    <summary>Cf.</summary>
… Edward K. Conklin's antedating of 'Justice delayed is justice denied.' from 1868 to 1646 in <a href="https://t18d.github.io/HuangSupplement/sourcebook/#:~:text=Confessions%20of%20the%20Antedater">Shapiro (2018)</a>.
</details></p>

[pull/2#issuecomment-2544494345](https://github.com/t18d/HuangSupplement/pull/2#issuecomment-2544494345)
