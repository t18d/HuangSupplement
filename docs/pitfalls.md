---
title: Pitfalls in Historical Lexicography @ HuangSupplement
permalink: pitfalls/
seo:
  type: Collection
last_modified_at: 2024-12-21T02:39:41+00:00
layout: anchor
---
# Pitfalls in Historical Lexicography

<p class="text-right">Gleanings from HuangSupplement</p>

&nbsp;  
&nbsp;  
&nbsp;  
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

[f4e8297](https://github.com/t18d/HuangSupplement/commit/f4e8297a1459d10285015b5d3b30ff885771578d)

```diff
- 本土,local,adjective,1857,有本土邏卒四人、為華民所殺,"『六合叢談』1/4, 15+",
```

This sense of 本土 dates back to 11th century

[10200d6](https://github.com/t18d/HuangSupplement/commit/10200d667f8782e6f418bd58cd5d2e449b073a36)

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

[pull/2#issuecomment-2544494345](https://github.com/t18d/HuangSupplement/pull/2#issuecomment-2544494345)
