# Algorithms (アルゴリズム)
# アルゴリズムは、問題を解決するためにコンピューターに実行させる手順を
# プログラミング言語を使用して表現するコンピューターサイエンスの概念
# データを読み取り、浮動小数点に変換....
# またはファイルを開いてすべてを読み取り、最初の行が何の文字で始まっているか判断し....



# Data Structures
# データが意図したとおりに動作することを確認する賢い方法

# List (もっとも単純なデータ構造)

# What is not a "Collextion"

# *********************
# 変数とは、ラベルが付けられた "小さなメモリの一部" である
# *********************
x = 2 # xに代入ステートメント「=」で「2」が代入
x = 4 # xにある「2」が消去され、「4」が代入
print(x)



# A List is a kind of Collection
friends = ['Joseph', 'Glenn', 'Sally'] # リストは基本的にリスト定数である
carryon = ['socks', 'shirt', 'perfumr'] # Listが変数に代入されている


# List Constants
print([1, 24, 76])               # 整数のリスト
print(['red', 'yellow', 'blue']) # 文字列のリスト
print(['red', 24, 98.6])         # 文字列、整数、浮動小数点のリスト　※すべてが同じデータ型である必要がない
print([1, [5, 6], 7])            # ☆☆☆　構造的　リストが他のリストを含むことができる　☆☆☆
print([])                        # ❐　空のリスト  ❐


# For loops
for i in [5, 4, 3, 2, 1] :
  print(i)
print('Blastoff!')


# Lists and definite loops - best pals
friends = ['Joseph', 'Glenn', 'Sally']

# for statementはリストで使用するもの
# リストを反復処理してすべての項目を順番に確認する必要がある場合、forはそれを行うために優れた方法である
for friend in friends : # 単数形、複数形の命名は恣意的なもの
  print('Happy New Year:', friend)
print('Done!')

# Pythonは単数形か複数形かを判断しないし、気にしない
z = ['Joseph', 'Glenn', 'Sally']
for x in z :
  print('Happy New Year:', x)
print('Done!')



# Looking Inside Lists

# 文字列と同じように、リスト内を調べることができる
friends = ['Joseph', 'Glenn', 'Sally']
# \Joseph \ Glenn \ Sally \
# \   0   \   1   \   2   \

print(friends[1])


# ::::::::::::::::::::::::
#
# リストには位置があり、順序が維持される
#
# ::::::::::::::::::::::::




# Lists are Mutable (changeable)
fruit = 'Banana'
# fruit[0] = 'b' >>> トレースバックが発生する
#「文字列」は一度作ると変更不可能ということ

x = fruit.lower()
print(x)

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)
# 整数は変更 "可能"