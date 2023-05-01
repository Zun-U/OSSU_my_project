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
  print('Bigger')
else :
  print('Smaller')
print('All done')
