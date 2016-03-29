#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# xcodeのmapfileを読み込みサイズをカウント
# "# Sections:"以下の行を抜粋していることが前提
#
import sys
import os.path

# 引数の取得
argv = sys.argv

# 引数の確認
if len(argv) <= 1:
    print 'no file path in argument'
    sys.exit()

# ファイルの存在チェック
path = argv[1]
if not os.path.exists(path):
    print 'not exists file' + path
    sys.exit()

# サイズを計測
size = 0
mapfile = open(path)
for line in mapfile:
    # 戦闘が0xから始まっているObjectfiles軍であることをチェック
    if line.find('0x') != 0:
        continue
    # 分解して、3つ以上のパーツが有ることを確認
    parts = line.split('\t')
    if len(parts) < 3:
        continue

    # サイズも16進数
    if parts[1].find('0x') != 0:
        continue

    # サイズを取得し一応出力
    sizeOne = int(parts[1][2:], 16)
    print parts[2][0:-1] + ' : ' + str(sizeOne)

    size += sizeOne

# 合計サイズを出力
print 'summary ' + str(size)
