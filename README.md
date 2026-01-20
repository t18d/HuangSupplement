---
title: A Supplement to 近現代漢語辭源
description: Antedatings, errata and addenda to 近現代漢語辭源
permalink: /
seo:
  type: Dataset
  name: A Supplement to 近現代漢語辭源
last_modified_at: 2026-01-20T09:02:32+00:00
---
# A Supplement to 近現代漢語辭源 [![DOI](https://t18d.github.io/HuangSupplement/assets/svg/zenodo.15514850.svg)](https://doi.org/10.5281/zenodo.15514850)
<p align="right"><em>a project of <a href="https://t18d.github.io/">Open Source by Tonkünstler-on-the-Bund</a></em></p>
<br>
<br>
<br>
<p>This database is searchable as <a href="https://github.com/t18d/HuangSupplement/tree/main/dict">CSVs</a>. The quickest way to get an addition or correction merged is to fork the repo or <a href="https://github.com/t18d/HuangSupplement/wiki/Clone-the-repo">clone locally</a>, edit a CSV file and send in a pull request.</p>
  
<p>The focus is on antedating and amending entries where the lemma is still current in educated speech. Editorial history and argumentation can be accessed via git blame. Triage of items in <a href="https://github.com/t18d/HuangSupplement/tree/main/Yang">Yang's bibliography</a> (2026-01-14) is now completed.</p>

<div align="center">
<a href="https://github.com/t18d/HuangSupplement/wiki/Notes-to-Contributors">Notes to Contributors</a> ·
<a href="https://github.com/t18d/HuangSupplement/wiki/Checklist-of-Editions">Checklist of Editions</a> (414)<br>
<a href="https://t18d.github.io/HuangSupplement/pitfalls/">Pitfalls in Historical Lexicography</a><br>
<a href="https://t18d.github.io/HuangSupplement/bibliography/">Bibliography</a> ·
<a href="https://t18d.github.io/HuangSupplement/papers/">Working Papers</a>
</div>
<br>
<p>
  <details>
    <summary>Conventions</summary>
    <br>
    <ul>
      <li><strong>Abbreviations</strong>
        <ul>
          <li>AdjP – adjective phrase</li>
          <li>Adv – adverb</li>
          <li>Asahi – Asahi Shimbun Cross-Search</li>
          <li>aYEAR – ante YEAR</li>
          <li>CC – copula complement</li>
          <li>CHJ – 日本語歴史コーパス</li>
          <li>CS – copula subject</li>
          <li>cYEAR – circa YEAR</li>
          <li>Han-ta – 漢語大詞典 (1st edn)</li>
          <li>Hathi – HathiTrust</li>
          <li>Hsien-han – 現代漢語詞典 (7th edn)</li>
          <li>Huang – 近現代漢語辭源</li>
          <li>Koten – 古典ライブラリー</li>
          <li>M1 – 官話<sub>1</sub> in Tai (2017)</li>
          <li>M2 – 官話<sub>2</sub> in Tai (2017)</li>
          <li>M3 – 官話<sub>3</sub> in Tai (2017)</li>
          <li>NDL – 国立国会図書館デジタルコレクション</li>
          <li>NP – noun phrase</li>
          <li>Nikkoku – 日本国語大辞典 (2nd edn)</li>
          <li>Prep – preposition</li>
          <li>V – verb</li>
          <li>VCC – verbless clause complement</li>
          <li>VCS – verbless clause subject</li>
          <li>VP – verb phrase</li>
          <li>Yomidasu – Yomiuri Database Service</li>
        </ul>
      </li>
      <li><strong>Solidus</strong>
        <ul>
          <li>This Supplement is designed to be consulted alongside Huang. A <strong>solidus</strong> ('/') in a cell indicates that the infomation is the same as in Huang or the previous entry.</li>
        </ul>
      </li>
      <li><strong>Lemma</strong>
        <ul>
          <li>To facilitate cross-checking, the arrangement of lemmas is that of Mair et al. (2003) with the following modifications:
            <ul>
              <li>words whose <strong>head characters</strong> share the same sequence of letters and tone are sorted by subsequent characters;</li>
              <li>in case of a tie, they are sorted by the <strong>complexity</strong> of the characters concerned in terms of (1) the number of strokes in the radical and (2) the number of residual strokes.</li>
            </ul>
          </li>
          <li>The <a href="https://t18d.github.io/HuangSupplement/dictionary/#ideograph"><strong>ideographs</strong></a> used are those suggested by the Traditional Chinese character set of iOS at the time of the commit, which tend to be the only form attested throughout the period covered here.</li>
          <li><strong>Numerals</strong> following a lemma refer to the different senses of a homonymous word, which form a superset of the senses defined in Huang. If a word is absent from Huang, the numbering of Hsien-han (for neologisms) or Han-ta (for traditional words which underwent semantic change) is used.</li>
          <li><strong>Obsolete words</strong>, <a href="https://t18d.github.io/HuangSupplement/dictionary/#phonetic-loan">phonetic</a> <strong>loanwords</strong> and anatomical terms are collected in separate appendices. For loanwords, see also <a href="https://t18d.github.io/HuangSupplement/diglossia/">On Diglossia</a>; for obsolete words, see also the <a href="https://t18d.github.io/HuangSupplement/style/">Stylistic Appendix</a>.</li>
        </ul>
      </li>
      <li><strong>Sense</strong>
        <ul>
          <li>Glosses serve to disambiguate and are set in <strong>roman type</strong>.</li>
          <li>Domain classification is set in <strong>italic type</strong>.</li>
        </ul>
      </li>
      <li>Assignment to <strong>Word Class</strong> follows the analysis of Huang–Shih (2016) as corrected in the <a href="https://t18d.github.io/HuangSupplement-grammar/word-formation/defining-word">Grammatical Appendix</a>.</li>
      <li><strong>Year</strong>
        <ul>
          <li>The first entry for a lemma represents the first known attestation. When a date is given, it is generally earlier than the earliest quotation in Huang except in the case of <strong>postdating</strong>.</li>
          <li>When the <strong>publication date</strong> and <strong>composition date</strong> of a source differ, the dating style of the Middle English Dictionary and <a href="https://www.oed.com/discover/dating-middle-english-evidence-in-the-oed/">OED3</a> is used.</li>
        </ul>
      </li>
      <li><strong>Quotation</strong>
        <ul>
          <li>The exact <strong>variant ideographs</strong> as used in the source are reproduced when they are available in <a href="http://fgwang.blogspot.com">the latest version of FSung</a>. Failing that, the closest variant is substituted.</li>
          <li>The <strong>typography</strong> of the source is reproduced to the extent that the baseline features of modern browsers allow.</li>
          <li>A <strong>blank</strong> means we had no access to the source.</li>
          <li>For traditional <strong>critical symbols</strong>, see <a href="https://archive.org/details/textualcriticismandeditorialtechniquemartinwestl./">West (1973)</a>.</li>
        </ul>
      </li>
      <li><strong>Source</strong>
        <ul>
          <li><a href="https://t18d.github.io/HuangSupplement/dictionary/#evidence-dictionary"><strong>Dictionary evidence</strong></a> is treated as a primary rather than secondary source, and represents one single attestation instead of a statement about contemporary usage.</li>
          <li>When a word is attested in an item carried in multiple <strong>newspapers</strong> on the same day, the least well-known paper is cited as a way to diversify scholarly sources away from <em>Shen-pao</em> and <em>L'Impartial</em>. Other attestations may be located in 全國報刊索引.</li>
          <li>An <strong>exclamation mark</strong> ('!') preceding a source means the quotation is taken from a modern edition with normalised orthography and we had no access to an early version.</li>
          <li>A <strong>plus sign</strong> ('+') following a source means the word is attested more than once in that source.</li>
          <li>When a <strong>shelfmark</strong> is added in parentheses, it can be used to identify the relevant digital copy linked to in the <a href="https://github.com/t18d/HuangSupplement/wiki/Checklist-of-Editions">Checklist of Editions</a>.</li>
        </ul>
      </li>
    </ul>
  </details>
</p>

<p>
  <details>
    <summary>Appendices</summary>
    <br>
    <ul>
      <li><a href="https://t18d.github.io/HuangSupplement-grammar/">HuangSupplement Grammar</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/style/">A Stylistic Appendix</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/orthography/">An Orthographic Appendix</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/diglossia/">On Diglossia</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/obsolete/">Obsolete Words</a></li>
      <li><a href="https://github.com/t18d/HuangSupplement/blob/main/scratch/anatomy.csv">Anatomical Terms</a></li>
      <li><a href="https://github.com/t18d/HuangSupplement/blob/main/scratch/loanwords.csv">Loanwords</a></li>
    </ul>
  </details>
</p>

<p>
  <details>
    <summary>Credits</summary>
    <br>
    <p>In addition to the studies referenced in the <a href="https://t18d.github.io/HuangSupplement/bibliography/#sources">bibliography</a>, the following scholars have contributed directly to the success of this Supplement:</p>
    <ul>
      <li>Design: 黃河清, Theodore Nze (etymology), 田野村忠温 (kana).</li>
      <li>Entries: Yan Cui, Lok Ching Roxanne Fung, Ruohan Ma (etymology), Theodore Nze (etymology), Jane Xuzhen Tang.</li>
      <li>Research: Edward Huang (synonyms), Xiaoyu Jin (orthography), Xingni Li (orthography), Ethan Liu (orthography).</li>
      <li>Tooling: Ansel X. Zhang (font).</li>
      <li>Corrigenda: 操瑞青, 田野村忠温.</li>
      <li>Supervision: Gabriele Tola (MT24).</li>
      <li>Bibliography: 菊地恵太 (ryakuji), Federico Masini, 繆蓬, 沈國威, 楊馳.</li>
    </ul>
  </details>
</p>

<p>
  <details>
    <summary>Can't edit?</summary>
    <br>
    <ul>
      <li>If you are in a place with internet restrictions, contact your local authorities and ask them to unblock the site for you. In the meantime, you can send the contributions to <span class="email">67616464787179717a6054607b7a7f617a6760787166397b7a39607c713976617a703a777b79</span>.</li>
    </ul>
  </details>
</p>
<br>
<p align="center">
<a href="https://t18d.github.io/HuangSupplement/a/">A (29)</a> ·
<a href="https://t18d.github.io/HuangSupplement/b/">B (129)</a> ·
<a href="https://t18d.github.io/HuangSupplement/c/">C (28)</a> ·
<a href="https://t18d.github.io/HuangSupplement/d/">D (33)</a> ·
<a href="https://t18d.github.io/HuangSupplement/e/">E (1)</a> ·
<a href="https://t18d.github.io/HuangSupplement/f/">F (32)</a> ·
<a href="https://t18d.github.io/HuangSupplement/g/">G (34)</a> ·
<a href="https://t18d.github.io/HuangSupplement/h/">H (20)</a> ·
<a href="https://t18d.github.io/HuangSupplement/j/">J (49)</a> ·
<a href="https://t18d.github.io/HuangSupplement/k/">K (17)</a> ·
<a href="https://t18d.github.io/HuangSupplement/l/">L (23)</a>
<br>
<a href="https://t18d.github.io/HuangSupplement/m/">M (14)</a> ·
<a href="https://t18d.github.io/HuangSupplement/n/">N (35)</a> ·
<a href="https://t18d.github.io/HuangSupplement/o/">O (1)</a> ·
<a href="https://t18d.github.io/HuangSupplement/p/">P (15)</a> ·
<a href="https://t18d.github.io/HuangSupplement/q/">Q (37)</a> ·
<a href="https://t18d.github.io/HuangSupplement/r/">R (3)</a> ·
<a href="https://t18d.github.io/HuangSupplement/s/">S (45)</a>
<br>
<a href="https://t18d.github.io/HuangSupplement/t/">T (17)</a> ·
<a href="https://t18d.github.io/HuangSupplement/w/">W (9)</a> ·
<a href="https://t18d.github.io/HuangSupplement/x/">X (27)</a> ·
<a href="https://t18d.github.io/HuangSupplement/y/">Y (24)</a> ·
<a href="https://t18d.github.io/HuangSupplement/z/">Z (42)</a>
<br>
<a href="https://t18d.github.io/HuangSupplement/letter/">Lettered (1)</a>
</p>
<br>
<p align="center">
  v2025.12.2 (FSung: v1.70.1)
</p>
