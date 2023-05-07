# String Data Type

str1 = "Hello"
str2 = "there"

bob = str1 + str2 # 文字列の連結
print(bob)

str3 = '123'
# str3 = str3 + 1　# 異なる型同士の連結は出来ず、トレースバックが起きる

x = int(str3) + 1 # int関数で文字列型から整数型に型変換
print(x)



# Reading and Converting
name = input('Enter:')
print(name)

apple = input('Enter:')
# x = apple - 10 # 入力された値は「文字列型」となる為、マイナス演算ができない

x = int(apple) - 10
print(x)



# Looking Insaide Strings

# ❐❐❐　各文字には個別の位置と、個別のインデックスがある　❐❐❐
fruit = 'banana'
# |b|a|n|a|n|a|
# |0|1|2|3|4|5|
#
# 基本的に、文字には位置がある
# ☆ PythonではListは「0」から始まる
# **********************************************************

letter = fruit[1] # []がインデックス演算子
# ブラケット構文を文字列変数の”末尾”に追加できる

print(letter)

x = 3
w = fruit[x - 1]
print(w)


# A Character Too Far
# 文字列の長さを超えてインデックスを作成することはできない
zot = 'abc'
# print(zot[5]) ← トレースバックが起きる


# String Have Length

fruit = 'banana'
# |b|a|n|a|n|a|
# |0|1|2|3|4|5|

print(len(fruit)) # len関数　文字列の長さを尋ねることができる
# 文字列変数をパラメータとしてlenに渡す
# lenは文字列の長さを返す


# Looping Through Strings

# while loop
fruit = 'banana'
index = 0
while index < len(fruit) :
  letter = fruit[index]
  print(index, letter)
  index = index + 1

# for loop
# for loopが使えるのであれば、通常はfor loopを使用する
# コードの記載量が少なければ少ないほど、間違いを犯す可能性が低くなる
fruit = 'banana'
for letter in fruit:
  print(index, letter)

# 0 b
# 1 a
# 2 n
# 3 a
# 4 n
# 5 a




# Loop and Counting
# ここでは「a」が何回使われたかをカウントしている
word = 'banana'
count = 0
for letter in word :
  if letter == 'a' : # カウントの条件
    count = count + 1
print(count)



# Looping deeprt into 「in」
# 代数の集合表記のよう

# for letter in 'banana' :
# 「進行する、printする、終了するかどうかを決定する」、「進行する、printする....
# したがって「for」は、
# 1.ループを実行する時間を決定する
# 2.終了するかどうかを決定する



# Slicing Strings

s = 'Monty Python'
# M\o\n\t\y\ \P\y\t\h\o \n
# 0\1\2\3\4\5\6\7\8\9\10\11

#[]演算子を使用する（インデックス演算子）
# ❐❐　まで、ただし含まない　❐❐
print(s[0:4]) # 0~4まで、ただし4は含まない
print(s[6:7]) # 6~7まで、ただし7は含まない
print(s[6:20]) # 6~20まで、ただし20は含まない　※ 20番目はないが、Pythonではトレースバックを起こさない



# 文字列のチャンクを引き出している
# ※ チャンク - あるいは連続した（終わりの決まっていない）データを先頭から一定の長さや内容上の区切りに従って分割した断片的なデータ集合を指すことが多い


# 省略
print(s[:2]) # 最初を省略すると、文字列の先頭とみなされる
print(s[8:]) #２番目を省略すると、文字列の末尾が想定される
print(s[:]) # 最初から最後まで、文字列全体とみなされる


# String Concatenation (文字列の連結)
a = 'Hello'
b = a + 'There'
print(b)
# 「print(X, Y)」なら、自動でカンマ(,)は半角スペースに代わる
# 文字列の連結では、スペースは追加されない

c = a + ' ' + 'There' # ☆スペースを追加したい場合は、スペースを明示的に連結する
print(c)


# オーバーロード - 引数の数とか型とかが違う、同じ名前の関数を複数個、用意すること




# Using 「in」 as a logical Operator
fruit = 'banana'
print('n' in fruit) # 変数「fruit」に格納されている文字列に'n'の文字列が含まれているか　→  「true」 ※boolean値で帰ってくる
print('m' in fruit) # 'm'は含まれていないから「false」
print('nan' in fruit) # 複数の文字も使用できる

if 'a' in fruit : # 論理演算子として「in」を使用できる(含むかどうかを「true」か「false」で返す)
  print('Fount it!')


# String Comparison (文字列の比較)
word = input('Your Word:')
# ☆大文字と小文字は区別される(予測不可能、なぜならコンピュータの文字セットの設定に依存するため)
# 一般的に大文字は小文字より小さくなっている

if word == 'banana' :
  print('All right, bananas.')

if word < 'banana' :
  print('Your word,' + word + ', comes before banana.')
elif word > 'banana' :
  print('Your word,' + word + ', comes after banana.')
else:
  print('All right, bananas.')




# String Library
# 多くは文字列ライブラリを使用しているため、文字列は『オブジェクト』である
# ❐❐❐　オブジェクトには『メソッド』と呼ばれるものがある　❐❐❐
# したがって、文字列オブジェクトにはいくつかの組み込み機能があり、

greet = 'Hello Bob' # 「greet」は文字列オブジェクト
zap = greet.lower() # 「.lower」　自分の小文字バージョンを作成する。そしてその小文字のコピーを変数「zap」に与える
print(zap)

# greetは変更され"ない"
print(greet)

# 定数に対しても、これらのメソッドを呼び出すこともできる
print('Hi There'.lower())
# ☆つまり、定数もオブジェクトである

# これらは、「文字列変数」と「定数」に組み込まれている
# 文字列を作成すると、すぐに文字列はその一部になる

# ❐ メソッドの呼び出しは、関数の呼び出しの特殊な形式の一種　❐
# メソッドは「.メソッド名」で呼び出す


stuff = 'Hello There'
print(type(stuff)) # stuffはstrタイプ
print(dir(stuff)) #「dir」でstuffオブジェクトで使えるメソッド一覧が見れる
# 「X.〇〇()」
# Xに付属している、組み込みのXに対して実行できる事のすべて
# ビルド時に文字列が付属している


# String Library

# よく使用されるメソッド

# Serching a String
fruit = 'banana'
# |b|a|n|a|n|a|
# |0|1|2|3|4|5|

# findメソッド　文字列の位置を返す
pos = fruit.find('na')
print(pos)

# 該当する文字列が無ければ負の値が返却される
aa = fruit.find('z')
print(aa)




# Maknig everything UPPER CASE
greet = 'Hello Bob'
nnn = greet.upper() # 全部大文字にして、そのコピーを返す
print(nnn)

www = greet.lower() # 全部小文字にして、そのコピーを返す
print(www)

# これらの各メソッドは基本的には、元のものを変更せず『コピー』を返却する



# Serch and Replace (非常に便利)
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane') # replaeメソッド ('古いもの' , '新しいもの')　→　古いものを新しいものに置換する
print(nstr)

nstr = greet.replace('o', 'X') # もう一つの意味合いは、文字「o」を"探して"、文字「X」に"すべて"置き換える
print(nstr)

# このメソッドも元のものを変更しない
print(greet)



# Stripping Whitespace (空白の削除)
greet = '    Hello Bob  '
print(greet.lstrip()) # 文字列より前のスペースがすべて破棄される(L、左ストリップ)

print(greet.rstrip()) # 文字列より後のスペースがすべて破棄される(R、右ストリップ)

print(greet.strip()) # 両サイドの空白をすべて破棄する

# 空白が無ければ何も起きない
# このメソッドもまた、元のものを変更しない




# prefixes (プレフィックス)
line = 'Please have a nice day'

# この行は特定の文字列で始まっているかを調べるメソッド
# 「true」、「false」を返す
print(line.startswith('Please'))

# 文字列オブジェクトは大文字、小文字を区別する
print(line.startswith('p'))



# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos) # 二つ目の引数は開始位置を表す(つまりここでは、「'@'から開始して空白の位置を見つけてください」の意になる)
print(sppos)

# Sliceを行っている
host = data[atpos + 1 : sppos] # '@'より一個先の文字から初めて、'@'以降の空白まで（含まない）の文字列
print(host)



# Two Kinds of Strings
x = 'あいう'
print(type(x))

x = u'あいう'
print(type(x))

# ❐　Python3では、すべての内部文字列がUnicodeである　❐