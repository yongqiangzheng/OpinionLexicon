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

root = './Lexicon/'
lexicon = ['SentiWordNet', 'SenticNet', 'Liu Bing']
pos_txt = 'positive.txt'
neg_txt = 'negative.txt'
if not os.path.exists(root):
    os.mkdir(root)
for l in lexicon:
    if not os.path.exists(root+l):
        os.mkdir(root+l)


def prepocess(lexicon):
    path = root+lexicon+'/{}.txt'.format(lexicon.lower())
    pos_path = root+lexicon+'/'+pos_txt
    neg_path = root+lexicon+'/'+neg_txt
    fout = open(path, 'w')
    fpos = open(pos_path, 'w')
    fneg = open(neg_path, 'w')

    if lexicon == 'SentiWordNet':
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
    elif lexicon == 'SenticNet':
        sn = SenticNet()
        for k, v in sn.data.items():
            fout.write(k+'\t'+v[6]+'\t' + v[7]+'\n')
            if v[6] == 'positive':
                fpos.write(k+'\t'+v[7]+'\n')
            else:
                fneg.write(k+'\t'+v[7]+'\n')

    print('done!')
    fout.close
    fpos.close()
    fneg.close()


if __name__ == '__main__':
    # prepocess('SentiWordNet')
    # prepocess('SenticNet')
