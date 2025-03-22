---
title: A Supplement to 近現代漢語辭源
description: Antedatings, errata and addenda to Huang He-ch'ing's lexicon
permalink: /
seo:
  type: Dataset
  name: A Supplement to 近現代漢語辭源
last_modified_at: 2025-03-22T05:35:14+00:00
---
# A Supplement to 近現代漢語辭源
<p align="right"><em>a project of <a href="https://t18d.github.io/">Open Source by Tonkünstler-on-the-Bund</a></em></p>
<br>
<br>
<br>
<p>This database is searchable as a <a href="https://github.com/t18d/HuangSupplement/blob/main/supplement.csv">CSV file</a>. The quickest way to get an addition or correction merged is to fork the repo or <a href="https://github.com/t18d/HuangSupplement/wiki/Clone-the-repo">clone locally</a>, edit the CSV file and send in a pull request. The focus is on antedating and amending the entries in Huang where the lemma is still current in everyday usage.</p>

<div align="center">
<a href="https://github.com/t18d/HuangSupplement/wiki/Notes-to-Contributors">Notes to Contributors</a> ·
<a href="https://github.com/t18d/HuangSupplement/wiki/Checklist-of-Editions">Checklist of Editions</a><br>
<a href="https://t18d.github.io/HuangSupplement/pitfalls/">Pitfalls in Historical Lexicography</a>
</div>
<br>
<p>
  <details>
    <summary>Conventions</summary>
    <br>
    <ul>
      <li><strong>Abbreviations</strong>
        <ul>
          <li>Adv – adverb</li>
          <li>aYEAR – ante YEAR</li>
          <li>CHJ – 日本語歴史コーパス</li>
          <li>cYEAR – circa YEAR</li>
          <li>M1 – 官話<sub>1</sub> in Tai (2017)</li>
          <li>M2 – 官話<sub>2</sub> in Tai (2017)</li>
          <li>M3 – 官話<sub>3</sub> in Tai (2017)</li>
          <li>NP – noun phrase</li>
          <li>Nikkoku – 日本国語大辞典 (2nd edn)</li>
          <li>Prep – preposition</li>
          <li>V – verb</li>
          <li>VP – verb phrase</li>
        </ul>
      </li>
      <li><strong>Solidus</strong>
        <ul>
          <li>This database is designed to be consulted alongside Huang and <em>Han yü ta tz'u tien</em>. A <strong>solidus</strong> ('/') indicates that the infomation is the same as in (1) the previous entry, (2) Huang or (3) <em>Han yü ta tz'u tien</em>.</li>
        </ul>
      </li>
      <li><strong>Lemma</strong>
        <ul>
          <li>To facilitate cross-checking, the arrangement of lemmas is that of Mair et al. (2003) with the following exceptions:
            <ul>
              <li>words whose <strong>head characters</strong> share the same sequence of letters and tone are sorted by subsequent characters;</li>
              <li>in case that fails, they are sorted by the number of <strong>strokes</strong> of the characters concerned.</li>
            </ul>
          </li>
          <li>The <a href="https://t18d.github.io/HuangSupplement/dictionary/#ideograph"><strong>ideographs</strong></a> used are their common form as contained in the character set of the system font on modern computers that is coded as TC, which tends to be the only form attested throughout the period covered here.</li>
          <li><strong>Numerals</strong> following a lemma refer to the different senses of a homonymous word. They form a superset of the senses defined in Huang.</li>
          <li><a href="https://t18d.github.io/HuangSupplement/dictionary/#phonetic-loan">Phonetic</a> <strong>loanwords</strong> and anatomical terms are collected in separate appendices. For loanwords, see <a href="https://t18d.github.io/HuangSupplement/diglossia/">On Diglossia</a>.</li>
          <li>For <strong>obsolete words</strong>, see the <a href="https://t18d.github.io/HuangSupplement/style/">Stylistic Appendix</a>.</li>
        </ul>
      </li>
      <li><strong>Sense</strong>
        <ul>
          <li>Glosses serve to disambiguate and are set in <strong>roman type</strong>.</li>
          <li>Domain classification is set in <strong>italic type</strong>.</li>
        </ul>
      </li>
      <li>Assignment to <strong>Word Class</strong> follows the analysis of Huang–Shi (2016) as corrected in the <a href="https://t18d.github.io/HuangSupplement/grammar/#defining-word">Grammatical Appendix</a>.</li>
      <li><strong>Year</strong>
        <ul>
          <li>The first entry for a lemma represents the first known attestation. When a date is given, it is generally earlier than the earliest quotation in Huang except in the case of <strong>postdating</strong>.</li>
          <li>When the <strong>publication date</strong> and <strong>composition date</strong> of a source differ, the dating styles of the Middle English Dictionary and <a href="https://www.oed.com/discover/dating-middle-english-evidence-in-the-oed/">OED3</a> are adopted.</li>
          <li>When a source has been added from the documentation of <em>Han yü ta tz'u tien</em>, only the <strong>political period</strong> is available. Such fuzzy dating will gradually be replaced by more precise dates.</li>
        </ul>
      </li>
      <li><strong>Quotation</strong>
        <ul>
          <li>To make full-text search possible, the <a href="https://t18d.github.io/HuangSupplement/dictionary/#ideograph"><strong>ideographs</strong></a> used are those contained in the character set of the system font on modern computers that are closest to a diplomatic transcription of the source.</li>
          <li>The <strong>typography</strong> of the source is reproduced to the extent that the resources of HTML allow.</li>
          <li>A <strong>blank</strong> means the scholar who antedated the word didn't supply the evidence in their writings.</li>
          <li>A <strong>question mark</strong> ('?') means the word has not been found in the source cited by the scholar who antedated the word.</li>
          <li>For traditional <strong>critical symbols</strong>, see <a href="https://archive.org/details/textualcriticismandeditorialtechniquemartinwestl./">West (1973)</a>.</li>
        </ul>
      </li>
      <li><strong>Source</strong>
        <ul>
          <li><a href="https://t18d.github.io/HuangSupplement/dictionary/#evidence-dictionary"><strong>Dictionary evidence</strong></a> is treated as a primary rather than secondary source, and represents one single attestation instead of a statement about contemporary usage.</li>
          <li>When the earliest source for a lemma is written by a non-native speaker, a <strong>second quotation</strong> from the earliest native source is added if one does not exist in Huang.</li>
          <li>A <strong>plus sign</strong> ('+') following a source means the word is also attested in at least one other source dating from the same year.</li>
          <li>A <strong>question mark</strong> ('?') means the scholar who antedated the word didn't supply the source in their writings.</li>
          <li>A <strong>question mark</strong> ('?') following a source means the scholar who antedated the word didn't clearly specify the source in their writings and that the one given here was inferred from their bibliography.</li>
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
      <li><a href="https://t18d.github.io/HuangSupplement/style/">A Stylistic Appendix</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/grammar/">A Grammatical Appendix</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/orthography/">An Orthographic Appendix</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/diglossia/">On Diglossia</a></li>
      <li><a href="https://t18d.github.io/HuangSupplement/obsolete/">Obsolete Words</a></li>
      <li><a href="https://github.com/t18d/HuangSupplement/blob/main/anatomy.csv">Anatomical Terms</a></li>
      <li><a href="https://github.com/t18d/HuangSupplement/blob/main/loanwords.csv">Loanwords</a></li>
    </ul>
  </details>
</p>

<p>
  <details>
    <summary>Bibliography</summary>
    <h3>Theory</h3>
    <ul>
      <li>Aikhenvald, Alexandra A., <em>Classifiers: A Typology of Noun Categorization Devices</em> (Oxford, 2000).</li>
      <li>Chang, Pin (ed.), <em>Hsien tai Han yü miao hsieh yü fa</em> (Peking, 2010).</li>
      <li>Huang, Chu-Ren, and Dingxu Shi (eds), <em>A Reference Grammar of Chinese</em> (Cambridge, 2016).</li>
      <li>Huddleston, Rodney, and Geoffrey K. Pullum (eds), <em>The Cambridge Grammar of the English Language</em> (Cambridge, 2002).</li>
      <li>Kretschmer, Paul, <em>Sprachregeln für die Bildung und Betonung zoologischer und botanischer Namen</em> (Berlin, 1899).</li>
      <li>Kühner, Raphael, and Friedrich Blass, <em>Ausfürliche Grammatik der Griechischen Sprache: I. Elementar- und Formenlehre</em>, ii (Hanover, 1892).</li>
      <li>Liu, Ch'uan-hung, and Hsiung Jun-chu, '試論古籍整理中他校的操作原則',『古籍整理研究學刊』, 3 (2018), 37–46.</li>
      <li>Mair, Victor H. et al. (eds), Han yü ta tz'u tien<em> tz'u mu yin hsü so yin</em> (Shanghai, 2003).</li>
      <li>Tai, Li-kang, '晚清的官話音系及其性質',『古漢語研究』, 117 (2017), 28–41.</li>
      <li>Yeh, Pao-k'uei, '民初國音的回顧與反思',『廈門大學學報』, 183 (2007), 44–50.</li>
    </ul>
    <h3>Sources</h3>
    <ul>
      <li>陳戈, '《東西洋考每月統記傳》新詞研究', master's thesis, 浙江財經大學, 2013.</li>
      <li>陳華, '有關《四洲志》的若干问题',『暨南學報』, 15/3 (1993), 80. [英吉利]</li>
      <li>崔蕭寒, '「摩擦」の語史：日中両語の相互影響', master's thesis, Osaka University, 2021.</li>
      <li>馮天瑜–聶長順,『三十個關鍵詞的文化史』(Peking, 2021), 68–9. [中國]</li>
      <li>馮玥, '「反応」の語誌', master's thesis, Osaka University, 2022.</li>
      <li>黃河清, '<a href="http://www.huayuqiao.org/DOCC/DOC129/NO_076.php">"界說""定義"考</a>',『語文建設』, 129 (2024), 76. [定義]</li>
      <li>李志良, '"電子"一詞的譯定歷程及其意義引申',『或問』, 45 (2024), 45–55.</li>
      <li>繆蓬, '晚清民國“病毒”知識的翻譯與引介：知識翻譯學視角',『當代外語研究』, 4 (2022), 22–32.</li>
      <li>牛振, '近代日語譯詞對漢語地理學譯詞的影響探析',『漢字漢語研究』, 24 (2023), 109–24.</li>
      <li>Schmidt, Christian et al. (eds), <a href="https://mhdb.mh.sinica.edu.tw/vocabulary/search.php">漢語新詞資料庫</a>, accessed 23 Dec. 2024.</li> 
      <li>沙廣聰, '接尾辞「性」の歴史：日中両語間の相互影響', master's thesis, Osaka University, 2020.</li>
      <li>沈國威, '近代關鍵詞考源：傳統、近代、現代',『東亞觀念史集刊』, 4 (2013), 433. [現代]</li>
      <li>Tanomura, Tadaharu, 'カレーを表す中国語名称の変遷',『或問』, 38 (2020), 15–25. [咖哩]</li>
      <li>Tanomura, Tadaharu, '「接種」の語史: 種痘関連用語の生成と消長',『阪大日本語研究』, 34 (2022), 27–45.</li>
      <li>Tanomura, Tadaharu, '「卡車」の語史──その起源と展開',『或問』, 46 (2024), 31–45.</li>
      <li>Tanomura, Tadaharu, '学問名「考古学」の成立',『阪大日本語研究』, 37 (2025), forthcoming.</li>
      <li>Todani, Masayoshi, '中国語における日本語の借用と意味変化：“赤字”を例として',『日中語彙研究』, 10 (2020), 149–70.</li>
      <li>Todani, Masayoshi, '中国語における日本語「手続」の借用過程',『日中語彙研究』, 11 (2021), 143–163.</li>
      <li>Tola, Gabriele, <em>John Fryer and </em>The Translator’s Vade-mecum (Leiden, 2021), 237–79.</li>
      <li>佟藝辰, '"分詞"考源',『或問』, 46 (2024), 117–28.</li>
      <li>王銘宇, '明末天主教文獻所見漢語基督教詞彙考述',『漢語學報』, 44 (2013), 60.</li>
      <li>王銘宇, '羅明堅、利瑪竇《葡漢辭典》詞彙問題舉隅',『勵耘語言學刊』, 19 (2014), 148.</li>
      <li>袁書予, '「分析」の成立と変化', master's thesis, Osaka University, 2022.</li>
      <li>章可, '清末民初"傳統"的出現：概念史視角的考察',『史學月刊』, 4 (2020), 127. [傳統(2)]</li>
      <li>章可, '近現代「慈善」新詞考源',『東亞觀念史集刊』, 19 (2021), 456.</li>
      <li>張涌泉, '"別字"正名',『語文建設』, 4 (1989), 56–7.</li>
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
<br>
<!-- Anything not in the table must be before this comment. -->

Lemma|Sense|Word Class|Year|Quotation|Source|Note
---|---|---|---|---|---|---
癌症|/|/|1932|/|/|from Japanese: 1875 (NDL)
矮林|/|/|1909|/|/|from Japanese: 1877 (Nikkoku)
矮星|/|/|1934|/|/|from Japanese: 1919 (Hathi)
愛稱|/|/|1957|/|/|from Japanese: 1876 (Yomidasu)
愛國主義|/|/|1903|/|/|from Japanese: 1880 (NDL)
愛國者|/|/|1902|/|/|from Japanese: 1873 (NDL)
愛好者|/|/|1950|/|/|from Japanese: 1877 (Yomidasu)
X光線|/|/|1903|/|/|from Japanese: 1896 (Nikkoku); X光 is a [Chinese development](https://github.com/t18d/HuangSupplement/pull/36/commits/818c96432900119c5ea6ce03b389e5cefa84a5b1)
愛妻|/|noun|1165 (a233)|吳起之出愛妻文公之斬顚頡皆違其情者也|『韓非子·卷第十三外儲說右上』(17857)|
愛情|/|noun|a1641|司愛欲者。愛一物。必生一愛情而内含存之。|Ruggieri『天主聖教實錄』(Jap. Sin. I-54)|
愛人(2)|/|noun|1908|One in love, 愛人, 相好, 情人|顏惠慶『英華大辭典』s.v. Lover|from Japanese: 1862 (Nikkoku); cf. 雙解英和大辭典 s.v.
|/|/|1909|原來我方纔腦中的幻象。却變了眼前的眞境。我那愛人來了。我那愛人來了。|『民吁日報』十月念三號「古井波 (續)」|
安全島|/|/|1930|/|/|from Japanese: 1918 (Yomidasu); Nikkoku gives as primary reading あんぜんじま
安全燈|/|/|1903|/|/|from Japanese: 1872 (NDL)
安全地帶|/|/|1930|/|/|from Japanese: 1890 (NDL)
安全第一|/|/|1930|/|/|from Japanese: 1911 (Asahi)
愛犬|/|/|1914|/|/|from Japanese: a1842 (Nikkoku)
安樂椅|/|noun|1905|安樂椅鐵床。安置得齊整。|『閨秀救國小說 女媧石』乙卷, 8|
安樂椅子|/|noun|1912 (1910)|at the foot of your easy chair … 於安樂椅子之下|『英文書翰鑰』208|preface signed in Tokyo
安全剃刀|/|/|1930|/|/|from Japanese: 1886 (Nikkoku)
安全係數|/|/|1958|/|/|from Japanese: 1895 (NDL)
暗流|/|/|1894|/|/|from Japanese: 1894 (Asahi)
暗生植物|/|NP|1887|Cryptogam{e}æ 暗生植物|Fryer『西藥大成藥品中西名目表』18|dog-Latin: Kretschmer §31
暗示|/|/|1903|/|/|from Japanese: 1879 (Yomidasu)
暗箱|/|/|1901|/|/|from Japanese: c1868 (Nikkoku)
暗室|/|noun|1664|故山市海市暗室一隙皆得轉吸而見之|方以智『物理小識』|
暗轉|/|/|1948|/|/|from Japanese: 1908 (Yomidasu)
凹版|/|/|1913|/|/|from Japanese: 1890 (NDL)
凹面鏡|/|noun|1902|/|/|from Japanese: 1872 (CHJ)
凹透鏡|/|noun|1930|/|/|from Japanese 複凹透鏡: c1876 (NDL)
八重唱|/|noun|1930|/|/|from Japanese: 1906 (NDL)
八重奏|/|noun|1930|/|/|from Japanese: 1918 (NDL)
八分音符|/|/|1920|/|/|from Japanese: 1883 (NDL)
罷工(2)|/|verb|1819|罷 … 工 … in the ordinary sense, to strike work for a rise of wages, as is often done by the Canton weavers|Morrison, _A Dictionary of the Chinese Language_, ii/i, s.v. 罷|
罷免|/|verb|T'ang|/|/|What changes is the political process (monarchy > dictatorship > democracy), not the semantics
罷免權|/|/|1929|/|/|from Japanese: c1886 (NDL)
霸權|/|/|1896|/|/|from Japanese: 1870 (NDL)
白亞紀|/|/|1892|/|/|from Japanese: 1892 (NDL)
白癡(1)|unintelligent|adjective|c1200 (c282)|不慧蓋丗所謂白癡|杜預 in『春秋正義·卷第十九成公』64 (7283)|
|/|/|1909|觀此而猶不覺悟者。必白痴之也。|『神州日報』3月23日「美洲通信」|
白癡(2)|idiot|noun|1904|汝之家產不久將復歸於白痴之手。汝尚不悟耶。|冷血『偵探談二』90|also in Japanese 白痴: 1886 (NDL)
|(as term of abuse)|/|1917|(白痴投稿)|『日知報』4月12日「白牡丹之打櫻桃」|
|(with -式)|/|1923|那些白痴式的忠臣以爲敷衍學生，總得㩀學生爲己有。|『民國日報』11月21日「教育部老早該撤廢」|
白粉(2)|/|noun|1857|此時草木暢茂、成煤層、其上為新紅沙石、黃灰石、石膏、石鹽、蛋粉石、白粉、火石|W. Muirhead in『六合叢談』1/2, 2|
白鯨|/|/|1931|/|/|from Japanese: 1877
白金|/|noun|1848|Platina, 白金|Medhurst, _English and Chinese Dictionary_, s.v. Platina|
白開水|/|noun|c1813 (a1811)|右二味⋯每服一二錢。白開水送下。|吳瑭『溫病條辨·卷三下焦篇』55|
白内障|/|noun|1906|白內障(白翳)者。因于水晶體之溷濁。|『中學生理衛生教科書』100|from Japanese: 1867 (NDL); but cf. 白色內障 attested by 1644
白熱(1)|/|adjective|1867|white heat, 白熱|Lobscheid『英華字典』s.v. Heat|
白色恐怖|/|/|1928|/|/|from Japanese: 1923 (NDL)
白血病|/|/|1907|/|/|from Japanese: 1875 (NDL)
白夜|/|/|1954|/|/|from Japanese: 1913 (Nikkoku)
白雲岩|/|/|1954|/|/|from Japanese: 1891 (NDL)
白質|/|/|1880|/|/|from Japanese: 1870 (NDL)
百分率|/|/|1902|/|/|from Japanese: 1875 (NDL)
百合花|/|noun|a1487 (a863)|元和末海陵夏侯乙庭前生百合花大於常數倍異之|段成式『酉陽雜俎·卷六·器奇』3 (03915)|
百合科|/|/|1903|/|/|from Japanese: 1884 (Nikkoku)
百日咳|/|/|1902|/|/|from Japanese: 1797 (Nikkoku)
敗訴|/|/|1907|/|/|from Japanese: a1889 (NDL)
敗血症|/|/|1909|/|/|from Japanese: 1876 (NDL)
擺(1)|/|nominal bound root|1868|of o'clock, 擺|Lobscheid『英華字典』s.v. Pendulum|
拜金主義|/|noun|1907|實不外拜金主義也|『申報』4月8日「不允唐侍郞辭職辦路」|
斑馬|/|noun|1868|Zebra 斑馬|鄺其照『字典集成』s.v. Zebra|from Japanese: 斑驢 1876 (Nikkoku); Japanese reading is incorrect -- correct reading is しまうま
扳手(2)|/|noun|1893|其彈子均由後膛旁孔納入，膛下設木把手，用右手把住扳手 …|鄭觀應『盛世危言‧火器』|
班長(1)|/|noun|1902|續錄京師大學堂仕學院師範館學生班長副班長職務條規七條|『大公報』12月18日「時事要聞」|
班長(2)|/|noun|1929|/|/|from Japanese: 1869 (NDL)
板書(1)|/|/|1908|/|/|from Japanese: 1889 (NLD); Nikkoku gives alternate readings first いたがき and はんしょ; NLD source gives no reading
版畫|/|noun|1908|An impression from an engraved plate, block of wood, or other material, 刻版印刷物, 版畫, 印畫|顏惠慶『英華大辭典』s.v. Engraving|from Japanese: 1879 (Yomidasu)
版權|/|noun|1895 (1887)|/|黃遵憲『日本國志·食貨志二』|
版式|/|noun|1932|/|/|from Japanese: 1813 (Nikkoku)
半島|/|noun|1868|/|/|also in Japanese: 1801 (Nikkoku)
半導体|/|noun|1931|/|/|from Japanese: c1877 (NDL)
半島戦争|/|noun|1903|/|/|from Japanese: 1873 (NDL)
半封建|/|noun|1936|/|/|from Japanese: 1889 (NDL)
半旗|/|adverb|1876|「大日本國事 半旗弔慰」|『萬國公報』396, 23|[stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=半旗)
半數|/|/|1889|/|/|from Japanese: 1868 (NDL)
半自動|/|/|1936|/|/|from Japanese: 1893 (NDL)
伴生|/|/|1903|/|/|from Japanese: 1886 (NDL)
伴随|/|/|1930|/|/|from Japanese: 1886 (NDL)
伴星|/|noun|1936|/|/|from Japanese: 1885 (NDL)
伴奏|/|noun|1928|/|/|from Japanese: 1887 (NDL)
幫|/|nominal bound root|1872|Party _or company,_ 羣黨 … 朋黨 … 班 … 幫|Doolittle『英華萃林韻府』s.v. Party|
包圍|/|noun|1907|/|/|from Japanese: 1879 (NDL); with the sense of siege or entrapment
包物|/|noun|1907|/|/|from Japanese: 1871 (NDL)
胞子|/|noun|1903|/|/|from Japanese: 1872 (NDL)
飽和(1)|/|noun|1905|/|/|from Japanese: a1847 (Nikkoku)
飽和(2)|/|noun|1959|/|/|from Japanese: 1905 (Nikkoku)
飽和點|/|noun|1950|/|/|from Japanese: 1875 (NDL)
寶島|/|noun|1954|/|/|from Japanese: 1875 (NDL)
寶庫|/|noun|1916|/|/|from Japanese 宝庫: 1808 (Koten)
綁票|/|verb|1899|名爲綁票又名請財神|『申報』9月15日|
保留(1)|/|verb|1903|締結撤兵條約。其始或以保留權利許還清國為名。|『國民同盟會始末』55|
保險公司|/|NP|1868|insurance company, 保險會 … 保險公司|Lobscheid『英華字典』s.v. Insurance|
保持|/|/|1889|/|/|from Japanese: 1253 (Nikkoku)
保管|/|/|1899|/|/|from Japanese: 1870 (NDL); given the adjacent defintion/reading アヅケル
保證書|/|noun|1895 (1887)|又住在裁判所管內饒有貲產者亦可代納應充金額之保證書|黃遵憲『日本國志·刑法志二』|
報告(1)|/|verb|1895 (1887)|若更命留禁要將其事由報告裁判長|黃遵憲『日本國志·刑法志一』|
暴風|/|noun|1822|TEMPEST of wind, 暴風 … or reversed|Morrison, _A Dictionary of the Chinese Language_, iii, s.v. TEMPEST|
暴力|/|noun|1902|決非以暴力為尚而以自由為尚。人人以自由為尚此平等所由出也。|梁啟超輯譯『近世歐洲四大家政治學說』13|
暴雨|/|noun|1857|有燥土而時有暴雨、成大水不能潤土者|W. Muirhead in『六合叢談』1/13, 10|
北極星(2)|/|noun|Liang|十月乙丑有流星⋯出紫宮內北極星東南行三丈没空中|蕭子顯『南齊書·卷十三天文下』|
備考|/|verb|Ming|/|/|
背景(1)|/|noun|1916|雖成為歷史上主要之背景|『神州日報』3月19日「大亞細亞主義之運命」|
背景(2)|/|noun|1910|滬上所謂佈景有四大缺點⋯僅用背景一幅|『時報』3月14日「劇談」|cf. s.v. 佈景
背面|/|noun|1822|inside or back surface, 背面|Morrison, _A Dictionary of the Chinese Language_, iii, s.v. OUTSIDE|
被告|/|noun|a1368 (c1301)|被告 謂爲人所謡者|徐元瑞『吏學指南·卷六』|
被面|/|noun|1847|Coverlet, 被窩 … 被面|Medhurst, _English and Chinese Dictionary_, s.v. Coverlet|
被殺|/|preposition + verb|1857|又辨金色之吏、曰穵林敦、亦被殺|『六合叢談』1/4, 15|
本體|/|noun|1844|Essence, 精 … 本體 … 精氣|Williams『英華韵府歷階』s.v. Essence|
本義|/|noun|1868|the proper sense of a word, 本意 … 本義|Lobscheid『英華字典』s.v. Proper|
本質|/|noun|1672|夫風之本質乃地所発乾熱之気有多端可証一試|Verbiest『坤輿圖説』|
鼻音|/|noun|1869|Twang, a, … or nasal sound, 鼻音 … 鼻聲|Lobscheid『英華字典』s.v. Twang|
比重(1)|/|noun|1867|specific gravity, 比重|Lobscheid『英華字典』s.v. Gravity|
筆名|/|noun|1908|A false name, 偽名, 冒名, 假名, 別名, 筆名.|顏惠慶『英華大辭典』s.v. Pseudonym|名 is free only when the sense is 'given name'
必然|/|adverb|1703|Forçosam<sup>te</sup> piĕ̇ tińg. piĕ̇ kińg. piĕ̇ jên.|Varo, _Arte de la lengua mandarina_, 65|
標本|/|noun|1900|「製介類標本法」|『農學報』九十八|
標記|/|noun|1858|朔望上下弦表、歷年測量寒熱表、行進江海標記、潮汐表、中外寄書表|『六合叢談』2/1, 15|earliest use as noun
表達|/|verb|1907|坎拿大首相勞利安已向駐亞托華日本領事表逹歉仄之意|『申報』9月12日「美洲排斥黃人暴動事彙誌」|泣紅亭 cited by Han-ta (2nd edn) is a 1981 translation
表面張力|/|noun|1905|凡液體之表面因分子力不平均而生之收縮力為表面張力|湖北學務處『物理學』|
表情|/|noun|1908|Expression of the passions, 表情, 情徵|顏惠慶『英華大辭典』s.v. Pathognomy|
別字(1)|variant ideograph|noun|Northern Ch'i|/|『顏氏家訓』|
|/|/|1930|中國的俗字或別字，在十年之內，總可以研究完備了。|劉復『宋元以來俗字譜·序』5|
|/|/|2016|『碑別字新編 (修訂本)』|/|
別字(2)|misused ideograph|noun|Ch'ing|/|『日知錄』|postdating
冰箱(1)|/|noun|1869|Refrigerator 涼箱 … 冰箱|Lobscheid『英華字典』s.v. Refrigerator|
兵工廠|/|noun|1882|赴大坂兵工廠督造山野砲數十門|『申報』10月6日「彚譯東報」|
兵營|/|noun|1822|CAMP, 營 … 兵營 … 營寨|Morrison, _A Dictionary of the Chinese Language_, iii, s.v. CAMP|
並列|/|verb|1847|Collateral, running parallel, 並列|Medhurst, _English and Chinese Dictionary_, s.v. Collateral+|
並行(2)|/|verb|1869|Concurrent, acting in conjunction … 同行 … 並行|Lobscheid『英華字典』s.v. Concurrent|
病毒|/|noun|1908|疮疹之毒水、传染病毒、病毒、脓浆毒 (痘毒、痘浆)|顏惠慶『英華大辭典』s.v. Virus|postdating
病變|/|noun|1908|The transformation of a disease into another, (醫) 病症, 病變| 顏惠慶『英華大辭典』s.v. Diadexis|
摒絕|/|verb|1835|是以摒絕塑像、真心崇拜萬物之主宰|『東西洋考每月統記傳』乙未年六月「俠膽」|from 屏絕
摒棄|/|verb|c1715 (c1683)|丹砂白雉總摒棄檳榔萬斛無所須|『百尺梧桐閣集·遺稿詩十卷·送孫編修同周儀部奉使安南』(T5463/3140)|from 屏棄
波動(2)|/|verb|1902|譬如音響光溫之波動|廣智書局『心理教育學』72|
波形|/|noun|1906 (1904)|音色之差異依波形之差異而生|陳文哲『普通應用物理教科書』151|
伯爵|/|noun|1844|Earl, 伯爵|Williams『英華韵府歷階』s.v. Earl|
補助金|/|noun|1887|只允别賜補助金六萬元|『申報』2月1日「譯東洋朝日報」|
不法行爲|/|noun|1883|似此種種不法行爲實足爲地方大害|『申報』12月19日「憲示録登」|
不合理|/|adjective|1822|It does not comport with right reason, 不合理 … 與理不相符|Morrison, _A Dictionary of the Chinese Language_, iii, s.v. COMPORT|
不全|/|adjective|Chou|/|/|
不許|/|verb|1815|書上有講不明白的義旨就來細問不許含混|Morrison, _A Dictionary of the Chinese Language_, i/i, 750|
布告|/|noun|1862|「佈告」|『上海新報』8月23日|
裁員|/|verb|1882|「裁員節費」|『益聞錄』第百三十八號|
採掘|mine|verb|1882|又云生野鑛山局自採掘以來日見起色|『申報』9月24日「照譯東洋新聞」|
菜單|/|noun|1844|bill of fare, 菜單|Williams『英華韵府歷階』s.v. Tavern|
草書|/|noun|Han|睦善草書臨病明帝驛馬令作草書尺牘十首焉|劉珍『東觀漢記·卷七列傳二·北海敬王睦』|
草原|/|noun|1902|地多草原。故牧<畜>之業最盛。|作新譯書局『世界地理』292|
塵拂|/|noun|1912|尾端生有長毛。如塵拂。|杜亞泉–杜就田『新理科教授法二』12|likely from 塵払 (ちり‐はらい); [stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=塵拂,-noun)
秤桿|/|noun|1875|不料中有李秤杆范肉架者竊以爲必係鄕裏來者可以欺侮以顯跋扈之能|『申報』1月9日「記李秤杆等攔毆馮君事」|in nickname
赤字|/|noun|1931|日本歳入預定過大 赤字問題引起各方非難|『大公報』天津版1931年4月4日4版|cf. '「赤字」二字，是我抄的一個日本新應用的名詞' (『新社會』1931)
出版社|/|noun|1919|二十八號同紳商各界代表謁見總理詢問外交情形⋯並組織外交雜誌出版社|『益世報』5月1日「山東旅京各校代表之大聚會」|from Japanese 慶應義塾出版社: 1876 (NDL)
傳統(1)|/|adjective|1913|㩀暗殺者理由。謂羅氏破美國傳統慣例。故死之以爲預防。|『神州日報』1月14日「美總統選舉問題」|
傳統(2)|/|noun|1910|若夫美之於南美諸國.則既有傳統的約束…又以…劃出一新紀元.|『外交報』277「論遠東與南美」14|from Japanese: 1895 (CHJ)
|/|/|1911|利用列強之利害關係使之互相牽制 此種手段爲清國政治家傳統的政策|『神州日報』5月4日「日紙之四國借欵談」|
慈善|philanthropic|adjective|1896|披打古伯氏.爲慈善之事.銷費家貲一半.|『時務報』第十二冊「美國富家好善」26|also in Japanese: 1871 (Nikkoku)
詞源|/|noun|1916|聘請土頭土腦之土老先生編輯新詞源一種。補原有詞源所未備。|『新聞報』9月2日「諧著·贈送新詞源樣本廣告」|cf. 辭源
|/|/|1918|而况卽以小學之詞源而論。其字之用尚不爲完全正確耶。|(張)東蓀「論譯書」in『時事新報』5月23日|
辭源|/|noun|1912|聞該館尚編辭源一書亦已脫稿⋯兼望『辭源』之早日惠我也|『民立報』10月24日「惠書誌謝」|cf. 詞源
打胎|/|verb|1872|不然何卒以破血打胎終久而不知變計耶|『申報』5月23日「四醫斃一婦」|[stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=打胎)
擔保|/|verb|c1601|姑饒不殺各苗承認擔保將牛壹拾贰隻以求退兵|『平播全書·卷三』6 (NCL-02251)|here converted to noun
地基|/|noun|1583||_Dicionário Português-Chinês_ (Jap. Sin. I-198)|
地球儀|/|noun|1878|并製有小地球儀|『申報』6月21日「命題甚新」|
地下水|/|noun|1903|地下水 雨水之一部。|『中學地文教科書』74|
電鍍|/|noun|1885|Electro-planting 電鍍銀|Fryer『化學材料中西名目表』13|
電子|/|noun|1905|傳點亦名行點，或稱電子|纪立生–赵齐巽『最新化學詳要』+|
電子-|electronic|adjective|1935|電子告警器 Electronic Alarm|『通俗文化』1/4, 26|
定義(1)|/|verb|1914|例如⋯(Definition)日人譯爲定義⋯定義有兼攝⋯(Define) 動字之功。|胡以魯「論譯名」in『庸言』2月15日|
|/|/|1917|商業學爲最近採用之新名詞定義最爲困難|『大公報』12月17日「商業教育論 (十續)」|postdating; previously 下定義 & 正名定義
墊圈|/|noun|1889|Washer 墊圈|Fryer『汽機中西名目表』56|
二十四史|/|noun|c1796 (c1791)|余在長沙養疾讀史記以下諸史日有恆課摘二十四史同姓名錄|汪輝祖『病榻夢痕錄·卷下』49 (XD104)|與歐陽脩書並列共爲二十有四 (四庫總目卷四十五 c1795)
發動|/|verb|1872|電機發動卽將其人拋起躍至丈餘|『申報』6月29日「電氣抛人」|
發售|/|verb|a1792 (a1086)|農翁之善蓄稻也層藏累納有淹二十年不發售者|吕南公『灌園集·與楊次公書』(文淵閣)|
反應(1)|/|noun|1902|呈酸性之反應|『理化教科書』17|
反應(2)|/|noun|1902|吾入之意識、不外対於內部之剌戟之反應。|『新民叢報』「訳述三·人格論」|
方言|dialect|noun|1906|「統一方言說畧」|沈敦和 in『寰球中國學生報』1/1, 26|cf. [#22](https://github.com/t18d/HuangSupplement/issues/22)
方言學|dialectology|noun|1920|(表) 訓詁 {縱方面、—古訓學 橫方面、—現代方言學|沈兼士 in『時事新報』8月31日第七版|
-費|(in two-morpheme words)|nominal bound root|1853|q.v. 船費|/|
-費|(in three-morpheme words)|nominal bound root|1886|q.v. 保險費|/|
廢水|/|noun|1889|Waste tank 廢水箱|Fryer『汽機中西名目表』56|
分詞|/|noun|1904 (1903)|與“︁Be”︁合作Progressive時所附有ing之形曰現在分詞 (Present Pär'ti çi ple)|『正則英文教科書』ii, 85+|
分析|/|noun|1899|q.v. 定量分析, 定性分析|/|
分析|analyse|verb|1884|然律文雖簡下字極有權衡逐條分析皆以⋯|『申報』2月29日「論捉賭」|as one verb instead of two
咖喱|/|noun|1874|整啲咖喱魚|Dennys『初学階』|
干貝|/|/|/|/|/|likely a native word; see [#19](https://github.com/t18d/HuangSupplement/issues/19#issuecomment-2606537981)
功率|/|noun|1889|Duty of engine 汽機功率|Fryer『汽機中西名目表』17|
構想|/|verb|c1616 (c1596)|此臣早夜之所拮据夙昔之所搆想者也|馮夢禎『快雪堂集·卷二十五·隆儒優士疏』(CADAL)|
古文運動|/|noun|1927|我族之古文運動，非狹義之好古也。|『藝術界週刊』第十五期「雜記 (十四)」|
果汁|/|noun|1887|Colocynth pulp 𠹭囉噺果汁|Fryer『西藥大成藥品中西名目表』17|
海拔|/|noun|1901|此次爆發噴煙高出海拔一萬二千米|『清議報』八十六冊「支那現勢論」|
海洋性氣候|/|NP|1902|歐羅巴⋯大抵有海洋性氣候|作新譯書局『世界地理』240|
焊錫|/|noun|1889|Solder 銲錫|Fryer『汽機中西名目表』47|
花邊|/|noun|1866|an embroidered border, 花邊|Lobscheid『英華字典』s.v. Border|
花梗|/|noun|1887|Myrospermum pedicellatum 小花梗米羅司卑麻|Fryer『西藥大成藥品中西名目表』41|
环礁|/|noun|1903|自其形狀言之。則曰⋯環礁 (Atoll)|『中學地文教科書』96|
減速|/|verb|1889|Ease 減速|Fryer『汽機中西名目表』17|
教育者|/|noun|1866|Educator, 教養者 … 教育者|Lobscheid『英華字典』s.v. Educator|
接辦|/|verb|c1833|而其管理印度等處地方之事、仍容公司接辦|『東西洋考每月統記傳』癸巳十一月「英國之東地公司」|
接種|/|verb|1898|傳至日本互相接種其効昭然|『申報』7月11日「豫防痘症篇」|
精品|/|noun|Sung|/|/|[stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=精品)
卡車|/|noun|1923|曾宣言阻止外来卡車入路線之事、致有引起一般人之誤解、以卡車作乗客之車輛⋯此項卡車係専指運貨笨重之車而言|『申報』7月14日「滬太公司近況」|
考古|practise archaeology|verb|1902|瑞國得了這個古迹 考古的人 個個爭先再尋|『大公報』8月2日「新石代」|
考古學|/|noun|1896|Археологія, Као-гу-сі*о* 考古學|Попов『俄漢合璧増補字彙』|from Japanese 考古学: 1877/79 (Tanomura)
考古學家|/|noun|1907|義國夙以文明之淵藪見稱而入其境問十二銅標所在國人概答不知問之考古學家亦答不知|『順天時報』11月9日「客談歐美各國情形」|
科學|/|adjective|1914|聚百十不科學無條理之人日發生不痛不癢不達時勢之議論|『時事新報』12月4日「清朝復辟案之反響」|[stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=科學)
刻本|/|noun|Sung|近歲均州刻本輒改為仇香|陸遊『老學庵筆記』卷四|
|/|/|2001|「再说黄正甫刊本{乃}《三国志传》<乃>今见《三国演义》最早刻本」|『明清小說研究』1, 125|刻本 & 刋本 are stylistic variants
烙鐵|/|noun|1889|Soldering iron 嵌錫烙鐵|Fryer『汽機中西名目表』47|
禮拜|/|verb|c1584 (1583)|三當禮拜之日禁止工夫謁寺誦經禮拜天主|Ruggieri『祖傳天主十誡』(Jap. Sin. I-189)|
硫酸|/|noun|1883|Sulphuric acid 硫酸|Fryer『金石中西名目表』32|
漏斗|/|noun|1857|譬如水洩於漏斗|A. Williamson in『六合叢談』1/3, 7|
麵包|/|noun|1583||_Dicionário Português-Chinês_ (Jap. Sin. I-198)|
麵粉|/|noun|1583||_Dicionário Português-Chinês_ (Jap. Sin. I-198)|
描述|describe|verb|1909|其惶急尤難描述|『申報』8月2日「奇情小說 美人虹」+|not in 王雲五大辭典 & 國語辭典; very slowly took over the sense of 'describe' from [描寫(2)](https://t18d.github.io/HuangSupplement/obsolete/#:~:text=描寫(2))
|/|/|1958|現代語言學先分兩個大的方面 … 「描述的語言學」(descriptive linguistics) … 「歷史 (或比較的) 語言學」|董同龢「語言的研究」in『現代學術季刊』2/2|
描述語言學|/|NP|1958|個人覺得能代表近來美國描述語言學家的長處的倒是 Charles Fries 的兩本實用性的書|董同龢「語言的研究」in『現代學術季刊』2/2|the accurate translation of 'descriptive linguistics'
描寫(1)|depict|verb|Ming|/|/|the word's only current sense
描寫語言學|/|NP|1950|咱們現在應該嚴格使用描寫語言學的方法來分析現代中國語的結構|羅常培『語言與文化』103|fossilised use of the obsolete [描寫(2)](https://t18d.github.io/HuangSupplement/obsolete/#:~:text=描寫(2)) & no longer an accurate translation of 'descriptive linguistics'; cf. s.v. 描述語言學
摩擦(1)|/|verb|1851|琥珀用燥羊毛摩擦一辺、此摩擦処便能拾芥、就是電気発出、似磁石噏鉄一般。|Macgowan『博物通書』第一章|
納税人|/|/|1959|/|/|from Japanese: 1897 (Nikkoku)
奶糖|/|noun|1889|竊取主人奶糖|『申報』5月24日「英界公堂瑣案」|
耐火|/|/|1873/|/|/|from Japanese: 1867 (NDL)
耐熱|/|/|1892/|/|/|from Japanese: 1877 (Yomidasu)
耐酸|/|/|1965/|/|/|from Japanese: 1867 (NDL)
耐用|/|/|1873/|/|/|from Japanese: 1873 (NDL)
男女平等|/|/|1903/|/|/|from Japanese: 1880 (NDL)
男生|/|/|1903/|/|/|from Japanese: 1873 (NDL)
男聲|/|/|1920/|/|/|from Japanese 男声: 1873 (NDL)
男性|/|/|1902/|/|/|from Japanese: 1870 (NDL)
南北戦争|/|/|1900/|/|/|from Japanese: 1869 (NDL)
南回帰線|/|/|1903/|/|/|from Japanese: 1874 (NDL)
南歐|/|/|1899/|/|/|from Japanese 南欧: 1872 (NDL)
南温帶|/|/|1903/|/|/|from Japanese 南温帯: 1873 (NDL)
難產(1)|(literally)|verb|c1620 (a589)|芣苢⋯作茹大滑其子治婦人難產|『毛詩草木鳥獸蟲魚疏·卷之上·采采芣苢』1|
難產(2)|(metaphorically)|verb|1911|「難產之新內閣」|『盛京時報』3月15日|
嚢腫|/|/|1919/|/|/|from Japanese: 1871 (NDL)
蟯蟲|/|/|1909/|/|/|from Japanese 蟯虫: 1566頃 (Nikkoku)
腦充血|/|/|1909/|/|/|from Japanese 脳充血: 1873 (NDL)
腦海|/|noun|1904|把一切事情在腦海掃除乾淨|『美人妝』29|'An up-to-date man would no longer aspire to have it said of him, 滿肚子裡有學問.' (Mateer)
|/|/|1905|開設國會之思想。咸深印入國民腦海之中。|『津報』12月31日「論國民不可無政治思想 (續前稿)」|
腦力|/|/|1899/|/|/|from Japanese 脳力: 1872 (NDL)
腦膜炎|/|/|1906/|/|/|from Japanese 脳膜炎: 1868 (NDL)
腦貧血|/|/|1915/|/|/|from Japanese 脳貧血: 1873 (NDL)
腦橋|/|/|1898/|/|/|from Japanese 脳橋: 1873 (NDL)
腦神經|/|/|1903/|/|/|from Japanese 脳神経: 1822 (Hathi)
內在|/|adjective|1916|Immanent … 內在|Hemeling『官話』s.v. Immanent|
泥土|/|noun|1858|衝激泥土成新地|W. Muirhead in『六合叢談』1/13, 8|one word instead of two
凝固|/|verb|1847|to harden, 凝固|Medhurst, _English and Chinese Dictionary_, s.v. To condense|
濃度|/|noun|1905|蒸至適宜濃度再置冷處。|『中等化學教科書』294|
暖氣|/|noun|1866|Caliduct … 熱氣筒 … 暖氣筒|Lobscheid『英華字典』s.v. Caliduct|
偶像|/|noun|1927|我好像也已經成了偶象了|魯迅『兩地書·一〇五』|metaphorical
排外主義|/|noun|1902|舊日之排外主義|『壬寅新民叢報彙編』1053|
|/|/|1906|防止排外主義之傳播|『時報』12月26日|
砲灰|/|noun|1894|非砲灰卽刀頭之鬼耳|『申報』9月6日「論倭人窘况」|
|/|/|1934|殺人者在毁壞世界，救人者在修補它，而炮灰資格的諸公，卻總在恭維殺人者。|魯迅『且介亭雜文‧拿破侖與隋那』|
披露|/|verb|1889|本社著作無論社內社外⋯當逐期披露|『新社』第三期|
批判|/|verb|1902|故合印是編期我國民批判此二大問|『新廣東』100|
|/|/|1905|徒大聲疾呼慷慨悲憤以批判當局之失策者|『津報』11月7日「論戰後經營之第一著手」|
皮包|/|noun|1866|a leather bag, 皮包|Lobscheid『英華字典』s.v. Bag|
評論家|/|noun|1903|此評論家當然之天職|『國民日日報』9月20日「論辜鴻銘之無恥」|
破碎|/|verb|1844|Shatter, 破碎|Williams『英華韵府歷階』s.v. Shatter|
七色板|/|noun|1906 (1904)|牛頓七色板|陳文哲『普通應用物理教科書·本書應用試驗器械定價表』10|
|/|/|1926|現在的小學生就能玩七色板⋯收羅許多著名學者的大著作的大報，自然是光怪陸離，但也是轉不得|魯迅「雜論管閑事，做學問，灰色等」in『語絲』62, 3|
齊唱|/|VP|1844|Chorus, join 齊唱|Williams『英華韵府歷階』s.v. Chorus|
騎士|/|noun|1903|田奴騎士及君主之階級|進化譯社『史學通論』105|
歧義|/|noun|1921 (1877)|是以魏晉以還⋯獨於詩未聞歧義|孫詒讓『温州經籍志』卷二 s.v. 夏氏詩經漁樵野說|
起訴|/|verb|1895 (1887)|/|黃遵憲『日本國志·刑法志一』|
起義(2)|/|verb|1833|亦有人起義以應其隆奈者也。|『東西洋考每月統記傳』癸巳十二月, 79|
契據|/|noun|1872|(document) 契 … 契據|Doolittle『英華萃林韻府』s.v. Deed|
棄權|/|verb|1895 (1887)|/|黃遵憲『日本國志·刑法志一』|
汽車(2)|/|noun|1903|近有法人与英人及他国人合擬賭賽。汽車由法京巴黎斯至日斯巴尼亜京城馬得利脱。|『申報』5月27日「賽車肇事」|
汽油|/|noun|1904|有汽油六百八十罐又煤三百噸以供俄軍之用|『大公報』1月28日「時事要聞」|
鉛筆|/|noun|1822|Blacklead pencil, 鉛筆|Morrison, _A Dictionary of the Chinese Language_, iii, s.v. BLACKLEAD|
牽引力|/|noun|1908|其牽引力甚大且較牛皮橡皮各帶更為耐久堅韌|『申報』2月23日「專製布質引擎帶」|
前部|/|noun|1902|鞏膜之前部曰角膜|教科書譯輯社『中學生理教科書』166|This is where Huang corrects _Han yü ta tz'u tien_: 前部 was always military before 1900s.
前述|/|adjective|1880|如前述江西某委員信役濫刑|『申報』4月27日「論惡役殃民」|also in Japanese: 1877 (Nikkoku); [stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=前述)
潛伏期(1)|/|noun|1905|其初為病之潛伏期|湖北學務處『倫理學·課外餘談』34|
前景|/|noun|1867|Foreground 前地 … 前景|Lobscheid『英華字典』s.v. Foreground|
鉗子|/|noun|1848|鉗子⋯小鉗子|Medhurst, _English and Chinese Dictionary_, s.v. Pliers|
槍刺|/|noun|1903|「趕造槍刺」|『北洋官報』第一百四十八冊|
槍彈|/|noun|s.xvii|受數百槍彈從脅穿透|『行在陽秋·下』|
槍械|/|noun|1600|疏火器鳥銃長短槍械法|『譚襄敏奏議·序』|
強加|/|verb|1857|能強加力於他物者、謂重學之力|『六合叢談』1/11, 12|
牆腳|/|noun|1844|Foundation, 基址 … 墻腳|Williams『英華韵府歷階』s.v. Foundation|
侵入|/|verb|1868|to invade … as a disease a system, 侵入 … 侵害|Lobscheid『英華字典』s.v. Invade|metaphorical
侵襲|/|verb|1847|to come upon, to attack, 侵襲|Medhurst, _English and Chinese Dictionary_, s.v. To come|
群島|/|noun|1833|五島⋯共稱呂宋羣島|『東西洋考每月統計傳』癸巳年六月「東南州島嶼等形勢綱目」|
日全食|/|noun|c1632|舊法於日全食時。測定月之視徑。隨時不等。|Rho『崇禎曆書·月離曆指·月離三』9+|
三位一體(1)|/|idiom|c1636|吾主既降生後。有天主三位一體之像|Dias『聖經直解·雜事目錄』8 (Jap. Sin. I-70)|
山脈|/|noun|1858|山脈之方向|W. Muirhead in『六合叢談』1/13, 9|
上帝|/|noun|a1590|惟天主上帝其事未觧明否|Ricci, _Lettre de Sixte V au Maître de l'Empire des Ming_ (Chinois 1320)|
上述|/|adjective|1903|以上述之新兵爲自衛軍⋯宜協力迫俄國交還奉天之事|『俄事警聞』12月20日「清國之對俄政策」|from Japanese: 1895 (CHJ); [stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=上述)
哨子|/|noun|1889|Steam whistle 汽哨子|Fryer『汽機中西名目表』49|
生態學|/|noun|1903|論其習性與其相交之關係者。曰生態學。|作新社『新編動物學』3|
聖誕|(in Christianity)|verb|c1636|「吾主聖誕前第四主日」|Dias『聖經直解·卷之一』9 (Jap. Sin. I-70)|
聖母|/|noun|a1588|中間聖母無交配 誕聖原前室女躬|Ruggieri, _Chinese Poems_, 6 (Jap. Sin. II-159)|
石灰水|/|noun|1882|將膿泡一一挑破用石灰水洗淨|『申報』5月5日「火焚續述」|
石墨|/|noun|1883|Plumbago, or Graphite 石墨|Fryer『金石中西名目表』26|
石蕊|/|noun|1885|Litmus 石蕋|Fryer『化學材料中西名目表』21|
手動|/|adjective|1889|Hand gear 手動器具, 或手動齒輪|Fryer『汽機中西名目表』26|
手續|/|noun|1901|行政訴訟之手續|『譯書彙編』７, 54+|
水表|/|noun|1883|如是則該公司只須每日稽查水表|『申報』8月6日「自來水價宜變通說」|
所有者|/|noun|1903|猶未定議所有者只集股本十萬兩而已|『國民日日報』8月26日「天津經濟問題」+|
提神|/|verb|1837|雖鴉片惡毒、然其性能提神|『東西洋考每月統計傳』丁酉年四月「奏爲鴉片」|
體操|/|noun|1887|至櫻馬塲體操塲閱看師範學校生徒演習兵法|『申報』1月14日「日報譯略」|
天主|/|noun|c1584 (1583)|『祖傳天主十誡』|Ruggieri (Jap. Sin. I-189)|
天主教|/|noun|a1588|君尊天主教 予學舉人文|Ruggieri, _Chinese Poems_, 17.1 (Jap. Sin. II-159)|
外徑|/|noun|1874|外徑三寸|『申報』11月28日「怪疾二則」|
偉大(1)|/|adjective|1899|阿君爲此一段演說。神氣甚壯。抱負偉大。|『清議報』二十四「非律賓獨立一周年」|also in Japanese: 1872 (NDL)
西學東漸|/|idiom|1903|歐亞大通西學東漸|「泰西學案序」|signed in Tokyo; from Japanese: 1888 (CHJ)
峽谷|/|noun|1902|峽谷如壁地勢隆起|『申報』7月15日「詳紀張家口鐵路里程」+|
現代|/|noun|1875|recent ages 昭代, 現代.|鄺其照『字典集成』s.v. Recent|also in Japanese: 1894 (CHJ)
-性(2)|/|nominal bound root|1664|中通曰、水流下而趨中、有剛火性也、火炎上而旋昇、有柔水性也。|方以智『物理小識』|first occurrence in three-morpheme words
學理|/|noun|1903|解釋之意義由學者一己之私見者。謂之無權的解釋亦謂之學理解釋|汪–葉『新爾雅·釋法』27|
堰塞湖|/|noun|1903|大別之則分凹地湖堰塞湖二種|『中學地文教科書』86|
硬傷|(metaphorical)|noun|1928|袁世凱等，不過是個硬傷，忍痛用一次手術，還割得下來；若引用了那些下作小官僚，像微菌進血管，眞成不治之症了。|『民國日報』10月10日「祝政治建設的開始」|The literal sense dates back at least to s.xix med.
|glaring error|noun|1948|單就我們所說的「硬傷」而論，在這號稱「修訂本」、「標準本」當中就還多得難以計數。|鄧恭三「揭發『國定錯誤』廢除『國定課本』」in『大公報』10月3日|Note the quotes; [stylistics](https://t18d.github.io/HuangSupplement/style/#:~:text=硬傷)
原罪|/|noun|c1636|特吾主。及聖母。無染原罪。|Dias『聖經直解·雜事目錄』51 (Jap. Sin. I-70)|
-運動(1)|/|nominal bound root|1900|這運動兩字。不是講身體的運動。是講去運動別人。要他相信。|『紹興白話報』第九十六號「說運動」|here converted to verb; 運動(1) as a noun is obsolete
蔗糖|/|noun|1874|說畢卽將瓶中葡萄酒倒入玻璃盞又加蔗糖少許|『瀛寰瑣記』20, 7|
政體|/|noun|1834|南亞墨利加列國已良久驅逐西班呀國官員、自操其權、惟政體未尚定着。|『東西洋考每月統記傳』甲午年二月「新聞之撮要」|
致哀|/|verb|c1531 (488)|公事畢即往致哀|沈約『宋書·何尚之傳』(07347)|
誌哀|/|verb|1878|舉國臣民遵制縞素成服以誌哀也|『申報』7月20日|
-製品|/|nominal bound root|1880|牛角製品|『申報』12月22日「戲咏煙具十首錄呈諸大吟壇指政」|
中國|(in treaties)|noun|1731 (1690)|河之南岸、属于中国。河之北岸、属于鄂罗斯。|『聖祖仁皇帝實錄·卷一四三』|
中文|/|noun|1873|「英京設教習中文書院」|『申報』3月24日|
中文系|(of a high school)|noun|1923|中文系添古學哲學史學理論心理等類、英文系添有心理學高等幾何化學等課、|『時事新報』7月17日「蘇州桃塢改辦高級中學」|
|(of a university)|/|1925|「上大中文系戊辰級會大會」|『民國日報』3月23日|中文系 has the same referent as, but is _not_ semantically equivalent to, 中國語言文學系
钟乳石|/|noun|1903|鐘乳石 (Sta\<l>actite)|『中學地文教科書』75|Doolittle (1872): 石鐘乳
種樹|plant trees|verb|a1034 (c296)|/|『文選·閒居賦』(8575)|
-主義(1)|/|nominal bound root|1883|因係官權主義聞主筆者必將更迭|『申報』3月4日「會黨類誌」|
祝福|(intransitive)|verb|1538 (1370)|抑此乃祝福之詩非祭祀之詩|『五經蠡測·卷之四』13 (善000735)|
|(transitive)|/|1837|故皇上帝祝福是日、以爲聖日也。|『東西洋考每月統記傳』丁酉年六月「以色列遊野」|
資金(2)|money for a particular purpose|noun|1901|此時.乙不有滙資金.或不爲負擔債務.而拒絕清償.則買受者.對前者請求償還|『湖北商務報』90, 18|from Japanese: 1874 (Nikkoku); 資金(1) should probably be subsumed


