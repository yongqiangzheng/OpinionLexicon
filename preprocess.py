#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   preprocess.py
@Time    :   2022/03/15 14:53:47
@Author  :   ZYQ
'''

import os

from nltk.corpus import sentiwordnet as swn
from senticnet.senticnet import SenticNet
from torch import le

root = './Lexicon/'
lexicon = ['Hu&Liu', 'SenticNet', 'SentiWordNet', 'VADER']
pos_txt = 'positive.txt'
neg_txt = 'negative.txt'
if not os.path.exists(root):
    os.mkdir(root)
for l in lexicon:
    if not os.path.exists(root+l):
        os.mkdir(root+l)


def prepocess(lexicon):
    pos_path = root+lexicon+'/'+pos_txt
    neg_path = root+lexicon+'/'+neg_txt
    fpos = open(pos_path, 'w')
    fneg = open(neg_path, 'w')

    if lexicon == 'Hu&Liu':
        with open('./Source/Hu&Liu/positive-words.txt', 'r') as f1:
            lines = f1.readlines()
            for i in lines[35:]:
                fpos.write(i)
        with open('./Source/Hu&Liu/negative-words.txt', 'r') as f2:
            lines = f2.readlines()
            for i in lines[35:]:
                fneg.write(i)
    elif lexicon == 'SenticNet':
        sn = SenticNet()
        for k, v in sn.data.items():
            if v[6] == 'positive':
                fpos.write(k+'\t'+v[7]+'\n')
            else:
                fneg.write(k+'\t'+v[7]+'\n')
    elif lexicon == 'SentiWordNet':
        path = root+lexicon+'/{}.txt'.format(lexicon.lower())
        fout = open(path, 'w')
        for i in swn.all_senti_synsets():
            if i.pos_score()+i.neg_score() > i.obj_score():
                fout.write(str(i.synset)[8:-2]+'\t' +
                           str(i.pos_score())+'\t'+str(i.neg_score())+'\t'+str(i.obj_score())+'\n')
                if i.neg_score() == 0.:
                    fpos.write(str(i.synset)[8:-2] +
                               '\t'+str(i.pos_score())+'\n')
                elif i.pos_score() == 0.:
                    fneg.write(str(i.synset)[8:-2] +
                               '\t'+str(i.neg_score())+'\n')
        fout.close
    elif lexicon == 'VADER':
        with open('./Source/VADER/vader_lexicon.txt', 'r') as f1:
            lines = f1.readlines()
            for i in lines:
                word, score, _, _ = i.strip().split('\t')
                if float(score) > 0.0:
                    fpos.write(word+'\t'+score+'\n')
                elif float(score) < 0.0:
                    fneg.write(word+'\t'+score+'\n')

    print('done!')
    fpos.close()
    fneg.close()


if __name__ == '__main__':
    # prepocess('Hu&Liu')
    # prepocess('SentiWordNet')
    # prepocess('SenticNet')
    # prepocess('VADER')
