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

x = fruit.lower() # 変数「fruit」を小文字にした「コピー」を、変数「x」に代入している
print(x)
# ❐❐　ポイントは、元の「fruit」は変わらないってこと　❐❐
print(fruit)

lotto = [2, 14, 26, 41, 63]
print(lotto)

# 変数に単に入力するのではなく、変数内のこの位置に入力するように左側に括弧構文を置くことで、リストに項目を割り当てることができる。
lotto[2] = 28
print(lotto)





# How Long is a List
greet = 'Hello Bob'
print(len(greet))
# |H|e|l|l|o| |B|o|b|
# |0|1|2|3|4|5|6|7|8|
# >>> 9文字の文字列

x = [1, 2, 'joe', 99]
print(len(x))
# \1\2\'joe'\99\
# \0\1\  2  \ 3\
# >>> List中の要素数




# Using the range function
print(range(4)) # rangeは、返したい数値の数をパラメータとして受け取る
# [0, 1, 2, 3]　>>>  [0 : 4]

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
# |'Joseph'|'Glenn'|'Sally'|
# |   0    |   1   |   2   |
# >>> 要素数は「3」

print(range(len(friends)))
# [0, 1, 2] >>> [0 : 3]



# A tale of two loops
friends = ['Joseph', 'Glenn', 'Sally']

# List自体をloopする
for friend in friends :
  print('Happy New Year:', friend)

# もう少し洗練されたloop
# リストの位置が分かる
for i in range(len(friends)) : # 位置を通過する独自の変数「i」 >>> 通過するのは[0 : 3]、つまり[0, 1, 2]
  friend = friends[i]
  print('Happy New Year:', friend)



# Concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]

# 「+」は、文字列、整数、浮動小数点、そして 'リスト' も追加できる
# 新しい変数を生成して、それを「c」に代入している
c = a + b

print(c) # リストの連結
print(a) # 他と同様、元の変数は変更されない



# Lists can be sliced using :
# listsのスライス
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])

print(t[:4])

print(t[3:])

print(t[:])



# List Methods
x = list()
print(type(x)) # 'list' class

print(dir(x)) # 「list」関数内のすべてのドキュメントを検索
# append listへ要素の追加
# count list内の特定の値を探す
# extend listの末尾に値を追加
# index list内の値を調べる
# insert 中央で展開されるlist
# pop 上部から項目を取り出す
# remove 中央の項目を削除
# reverse list内の順番を反転
# sort 値に基づいてそれらを並べ替える



# Building a List from Scrach

# 空のlistを作成
stuff = list() # コンストラクターフォーム　--  Pythonにlistを作成してくださいと命令を送るもの
# 変数「stuff」はリストオブジェクトになる
# リスト型

# ※以下でも空のlistを作成できる
# stuff = []

# appendからアイテムを取り出し、'book'を張り付けることができる
stuff.append('book')

# 99を追加
stuff.append(99)
print(stuff)

# 'cookie'を追加
stuff.append('cookie')
print(stuff)








# Is Something in a List?
some = [1, 9, 21, 10, 16]

# 「in」演算子で、リスト内に値があるか判定できる
print(9 in some) # true

print(15 in some) # false

print(20 not in some) # true





# Lists are in Order

# ❐ Listはmutable(可変可能)である ❐
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort() # アルファベット順に並び変えられる
print(friends)
print(friends[1])





# Built-in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]

# list内の要素数、項目の数を示します
print(len(nums))

# list内の最大値
print(max(nums))

# list内の最小値
print(min(nums))

# list内の値の合算
print(sum(nums))

# list内の値の平均値
print(sum(nums) / len(nums))



# 今までの方法  >>> while loop内のメモリの使用量が少ない
total = 0
count = 0
while True :
  inp = input('Enter a number: ')
  if inp == 'done' :
    break
  value = float(inp)
  total = total + value
  count = count + 1
  print(total)
  print(count)
average = total / count
print('Average:', average)



# listを使用した方法 >>> while loop内のメモリの使用量が多い
numlist = list()
while True :
  inp = input('Enter a number: ')
  if inp == 'done' :
    break
  print(inp)
  value = float(inp)
  numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average', average)






# Best Friends: Strings and Lists

abc = 'With three words'

# split関数 -- 文字列を空白で分割し、リストを返却する
stuff = abc.split()




print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff :
  print(w)

