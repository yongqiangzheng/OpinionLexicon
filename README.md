# OpinionLexicon

情感词典及其简单处理

test

| 词典 | 年份 |
| ---- | ---- |
| [Hu&Liu](#hu--lius-opinion-lexicon) | 2004 |
| [SentiWordNet](#sentiwordnet) | 2010 |
| [General Inquirer] | 2011 |
| [VADER](#vader) | 2014 |
| [MPQA] | 2015 |
| [SenticNet](#senticnet) | 2020 |
## Hu & Liu's Opinion Lexicon
[[Source]](http://www.cs.uic.edu/~liub/FBS/opinion-lexicon-English.rar)

单词分成positive/negative两类，可直接使用

```
Lexicon/Hu&Liu/positive.txt
a+
abound
abounds
abundance
abundant
...

Lexicon/Hu&Liu/negative.txt
2-faced
2-faces
abnormal
abolish
abominable
```
## SentiWordNet
[[Source]](https://raw.githubusercontent.com/aesuli/SentiWordNet/master/data/SentiWordNet_3.0.0.txt)

由synset, pos_score, neg_score 和 obj_score组成

pos_score + neg_score + obj_score = 1
```
# POS	ID	PosScore	NegScore	SynsetTerms	Gloss
a	00001740	0.125	0	able#1	(usually followed by `to') having the necessary means or skill or know-how or authority to do something; "able to swim"; "she was able to program her computer"; "we were at last able to buy a car"; "able to get a grant for the project"
```
预处理仅保留pos_score + neg_score > obj_score的单词，根据两种pos和neg分数大小分类
```
Lexicon/SentiWordNet/sentiwordnet.txt
#Synset PosScore    NegScore    Objscore        
unable.a.01	0.0	0.75	0.25
direct.s.10	0.75	0.0	0.25
implicit.s.02	0.5	0.5	0.0
living.s.03	0.5	0.125	0.375
relative.a.01	0.25	0.5	0.25
...

Lexicon/SentiWordNet/positive.txt
direct.s.10	0.75
acceptable.a.01	0.625
accessible.a.01	0.625
come-at-able.s.02	0.625
complaisant.s.01	0.75
...

Lexicon/SentiWordNet/negative.txt
unable.a.01	0.75
assimilating.s.01	0.75
abstinent.s.01	0.625
rare.s.03	0.875
tight.s.06	0.625
...
```
## SenticNet
SenticNet的属性较多，详细解释请以[官网](http://www.sentic.net)为准，这里不再介绍
```
#senticnet['concept_name'] = ['introspection_value', 'temper_value', 'attitude_value', 'sensitivity_value', 'primary_mood', 'secondary_mood', 'polarity_label', 'polarity_value', 'semantics1', 'semantics2', 'semantics3', 'semantics4', 'semantics5']
senticnet['1st_class'] = ['0.9', '0', '0', '0.9', '#joy', '#eagerness', 'positive', '0.9', 'five_star', 'first_class', 'four-star', 'first-class', 'four_star']
```
预处理仅保留concept_name 和 polarity_value，并以polarity_label分类
```
Lexicon/SenticNet/positive.txt
1st_class	0.9
a1	0.827
aapl	0.9
abalone	0.934
abandon_flora	0.843
...

Lexicon/SenticNet/negative.txt
abandon	-0.83
abandon_camouflage	-0.62
abandon_eagle	-0.01
abandon_landscape	-0.06
abandon_pavement	-0.32
```

## VADER
[[Source]](https://github.com/cjhutto/vaderSentiment)



