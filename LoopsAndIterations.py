# シーケンシャル、条件付き、保存と再利用、ループと反復

# 本チャプターは「ループと反復」
# これはコンピューターに多くのことを教える方法（何百回も何かをするように言うことができる）

# Repeated Steps
# while loop
n = 5

# *****************************************************
# 「n > 0」はループを制御しており、「反復変数」と呼ばれる
while n > 0 : # if statementの様に「真、 true」または「偽、 false」の答えにつながる質問をしている行
  # whileの問いが「true」の場合、インデントされたブロックが実行され、「false」の場合はコードがスキップされる
  # つまり、質問の結果が「false」の場合はループが停止する
  print(n)
  n = n - 1
  # if statementの違いは、もう一度「while」が質問するところ

# 「while」もコロン(:)とインデントされたブロックがある
# インデントを解除してループの長さを決定する（インデントの終わりがループの終わり）
# *****************************************************
print('Blastoff!')
print(n)


# An Infinite Loop
# n = 5
# while n > 0 : # 無限ループの問題は、反復変数で「何もしなかった」こと
#   print('Lather')
#   print('Rinse')
# print('Dry off!')



# Another Loop
# n = 0
# while n > 0 : # ループが実行されず、スキップされる
#   print('Lather')
#   print('Rinse')
# print('Dry off!')
#
# 「ゼロトリップ」と呼ばれるループになる（一度実行されることさえ保証されていない）


# Breaking Out of a Loop
while True:
  line = input('>')
  if line == 'done':
    break # 内側のループを終了（ループの最後を超えた次の行に終了すること）
  print(line)
print('Done!')





# Finishing an Iteration with continue
while True:
  line = input('>')
  if line[0] == '#' :
    continue # この反復を停止して、この反復を終了する。☆そして、ループの一番上(whileの質問)に戻る☆
  if line == 'done' :
    break # 「break」はループから抜け出す事を意味している
  print(line)
print('Done!')


# whileは「無限ループ」とよばれる
# しかし、ほとんどのループは「確定ループ」と呼ばれるものを使用する


# Definite Loops (確定ループ)
# 「有限回」実行するループ

# forループ
# キーワードは「for」、「in」
for i in [5, 4, 3, 2, 1] : # 「i」は反復変数
  print(i) # 「5」「4」「3」「2」「1」でそれぞれ１回ずつ実行される
print('Blastoff!')


# 数字でなくても良い
friends = ['Joseph', 'Glenn', 'Sally']

# Pythonは単数形、複数形を理解できない
# 単数形、複数形は人間が読みやすくするため
for friend in friends : # 「friend」が反復変数となる（ニーモニックな変数名をつけるため、単数形と複数形を分けている）
# 変数「friend」が配列「friends」の連続したバージョンを取得するたびに実行する

  print('Happy New Year', friend) # インデントされたコードを３回実行する
print('Done!')


# ****************************
# for loopは、まず、ループを実行する回数を決定する
for i in [5, 4, 3, 2, 1] : # 反復変数と反復するものがセット(「i」が反復変数、[5, 4, 3, 2, 1]が反復するもの)
# 「in」は数学的には"集合"
  print(i)
  # 実際に行っている事は
  # i = 5 # iを「5」に設定する
  # print(i) # コードの実行
  # i = 4
  # print(i)
  # i = 3
  # print(i)
  # i = 2
  # print(i)
  # i = 1
  # print(i)
  #
  # 契約によって連続するたびに「i」の異なる値が得られ
  # 「i」の値は[5, 4, 3, 2, 1]のセットから取られる

print('Done')
# ****************************

# Loops Idioms
print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
  print(thing)
print('After')


# What is the Largest Number?
# Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] : # 「the_num」は反復変数
  if the_num > largest_so_far :
    largest_so_far = the_num
  print(largest_so_far, the_num)

print('After', largest_so_far)


# Counting in a Loop (回数)
zork = 0 # この変数は記憶術で「カウント」と呼ばれることがよくある
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
  zork = zork + 1
  print(zork, thing)
print('After', zork)


# Summing in a Loop (合計)
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
  zork = zork + thing
  print(zork, thing)
print('After', zork)



# Finding the Average in a Loop (平均)
count = 0
sum = 0
# 「count」、「sum」はニーモニック変数（人間が分かりやすい変数"名"。Pythonの予約語ではない）

print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
  count = count + 1
  sum = sum + value
  print(count, sum)
print('After', count, sum, sum / count)



# Filtering in a Loop (仕分け)
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
  if value > 20 : # if statementの部分がFilterの機能をしている
    print('Large number', value)
print('After')



# Serch Using a Boolean Variable (検索)
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
  if value == 3 : # 「3」が見つかったかどうかの判断
    found = True
    # break # 「break」を入れるとループを抜け出すことができる
  print(found, value)
print('After', value)



# How to find the smallest value (最小値)

# 最大値のループ
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
  if the_num > largest_so_far :
    largest_so_far = the_num
  print(largest_so_far, the_num)

print('After', largest_so_far)


# 最小値のループ

# 最初の値を取得するテクニック
smallest = None # None型(値が１つしかないという点で特別なマーカー。booleanには「true」、「false」の２つがある。)
# ❐❐  大文字「None」は定数　❐❐
# Noneは存在しないのではなく、「空であることを示す」ためによく使用される（数字ですらない）
# ※ループが始まる前は、これまで見た最小の数はどれも私たちが見たことのない数ではないという概念を実際にとらえる

print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15] : # 最初の番号が分かれば、それ以降の番号と比較ができる(ここでは「9」)
  if smallest is None : # 「is」演算子  等号「==」よりも強い
    smallest = value
  elif value < smallest :
    smallest = value
  print(smallest, value)

print('After', smallest)


# 「smallest = None」はマーカーの設置、「if smallest is None :」は最初にそれを引っかけるための手法



# The "is" and "is not" Operators (「is」演算子、「is not」演算子)
# 「0 == 0.0」は「true」になる
# 「0 is 0.0」は「false」になる、つまり型に厳密になる

# Pythonでは「==」の使用を控えめにする
# 「〇〇 is true」、「◇◇ is false」といったboolean型のチェックに使われることが多い
# is >>> 「boolean型」、「None型」、「float型」
# == >>> 「int型」、「string型」