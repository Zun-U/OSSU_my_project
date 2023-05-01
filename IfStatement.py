# if statement
# pythonがどちらの方向にも進める場所であり、これが始まりであり、pythonに意思決定させる方法の一種

# pythonの条件付きステップ

x = 5

# ifは予約語
# 変数「x」が10未満かどうかを訪ねている
# コロン(:)はif statementの終わり
if x < 10 :
  # インデントされたブロックを開始する
  print('Smaller') # 質問が「true」の場合は行が実行され、質問が「false」の場合は行は"スキップ"される

if x > 20 :
  print('Bigger')

# if statementが終わったらインデントを解除する
print('Finis')



# Comparison Operetors 比較演算子
# :::::::::::::::::::::::::::::
# < less than
# <= less than or equal to
# == equal to
# >= greater than or equal to
# > greater than
# != not equal
# :::::::::::::::::::::::::::::
# 真偽の判定(if statement)に用いる



# 「=」は代入演算子
# 「==」は比較演算子(is equal to)

y = 5

if y == 5 :
  print('Equal to')
if y > 4 :
  print('Greater than 4')
if y >= 5 :
  print('Greater than or Equal 5')

# ショートハンドのように1ラインで記述できる
if x < 6 :  print('Less than 6')

if x <= 5 :
  print('Less than or Equals 5')
if x != 6 :
  print('Not equal 6')




# One-Way Decisions

z = 5

print('Before 5')

if z == 5 :
  # ☆ インデントされている限り、ifブロックにとどまる
  print('Is 5')
  print('Is Still 5')
  print('Third 5')
print('Afterwards 5')
print('Before 6')
if z == 6 :
  print('Is 6')
  print('Is Still 6')
  print('Third 6')
print('Afterword 6')


# Indentation
# インデントを使用して、ブロックを区別する
# ❐　ブロックの開始位置と終了位置を示す　❐
# ※空白とコメントはインデントが無視される


# Nested Decisions(入れ子構造)

v = 42

# ::::::::::::::::::::::::::::: first if statement section
if v > 1 :
  print('More than onw')
  # --------------------------- second if statement section
  if v < 100 :
    print('Less than 100')
  # --------------------------- end seconde section
# ::::::::::::::::::::::::::::: end first section

print('All done')



# Two-way Decisions

q = 4

if q > 2 :
  print('Bigger q')
else :
  print('Smaller q')
print('All done q')



# Multi-way
# それぞれが順番に評価されて、falseなら行がスキップされる。（つまり、評価は『全部』行われる）

n = 5

if n < 2 : # 評価する
  print('small n')
elif n < 10 : # 評価する
  print('Medium n')
else : # 評価する
  print('LARGE')
print('All done n')


# 実行できないパターンもある　No Else

p = 50
if p < 2 :
  print('small p')
elif p < 10 :
  print('Medium p')
print('All done p')

# 「else」がないと評価式のいずれか一つは実行されるという『保証が無い』
# ❐ すべてのものがfalseの場合、elseが実行される ❐



# 多くの「elif」を持つことができる

g = 5
if g < 2 :
  print('small g')
elif g < 10 :
  print('Medium g')
elif g < 40 :
  print('big')
else :
  print('Ginormous')


# Multi-way Pazzles
# case1
a = 4

if a < 2 :
  print('Below 2')
elif a >= 2 :
  print('Two or more')
# elseを通ることはない
else :
  print('some thing else')

# case2

if a < 2 :
  print('Below 2')
elif a < 20 :
  print('Below 20')

# この「elif」は通らない
# なぜなら、上の評価式でtrue判定が出たから
# ❐❐　trueがでるとそこで分岐が終了し、以下の評価式は何も実行されない　❐❐
elif a < 10 :
  print('Below 10')

else :
  print('some thing else')



# The try / except Structure
# 壊れて爆発する可能性のあるコードを上手く処理する方法

astr = 'Hello Bob'

try:
  # 数値以外の文字列が代入されたため、『トレースバック』が実行される
  # ※例外の原因となる自分のコードに辿り着きます 。 この呼び出し履歴を遡って追跡することを「Traceback」といいます。
  istr = int(astr)

# 「try」が動作すると、「except」が無視される
# 「try」が失敗すると、「expect」、例外が実行される
except:
  # 例外が発生したことを知らせる『フラグ』の様なものとして「-1」を代入している（ここでは、「-1」が代入されたら例外処理flagが立ちましたよの意味としている）
  istr = -1
print('First', istr)

astr = '123'
try:
  istr = int(astr)
# 「expect」はコードで問題が発生した場合のみトリガーされる
except:
  istr = -1
print('Second', istr)



# try / except

astr = 'Bob'
try:
  print('Hello', 'ここまでは実行される')
  # コードが爆発(エラー発生)するまでは処理しようと試みる
  # ❐ 爆発が発生した箇所以降のtryブロックは実行されない　❐
  istr = int(astr)
  print('There')
except:
  istr = -1
print('Done', istr, 'tryの途中から爆発が発生し、exceptに移行')


# try / exceptを正しい形にしたのが↓
print('Hello')
try:
  istr = int(astr)
except:
  istr = -1
print('There')
print('Done', istr)





# Simple try /except
# より実世界のコード

rawstr = input('Enter a number')
try:
  ival = int(rawstr)
except:
  ival = -1
if ival > 0 :
  print('Nice work')
else:
  print('Not a number')