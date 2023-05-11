# programの流れ

# [Input and Output Devices]
# ↓↑
# [Software] :Central Processing Unit  : Main Memory
# ↓↑
# [Secondary Memory] <<< 今回のテーマ



# File Procesiing
# Fileは一連の行と考えることができる

# Opening a File
# ファイルを読み取るには「open関数」を呼び出す必要がある
# 「open関数」は、実際にはファイルを読み取らない
# 「open関数」を使用すると、ファイルを読み取ることができるようになる


# Using open()

# ::::::::::::::::::::::::::::::
#
# open関数の書き方
# handle = open(filename, mode)
#
# 引数1. ファイルの名前
# 引数2. 読み取り、または書き込みを行うかどうかを指定するオプション
#
# 例)
# fhand = open('mbox.txt', 'r')


fhand = open('mbox.txt')
print(fhand)
# >>> <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp932'>
# ファイル自体でなく、ファイル内のデータでも無い
# これは、それを可能にする単なるラッパー


# When Files are Missing
#
# 例)
# fhand = open('stuff.txt')
# 存在しないテキストファイルを開こうとすると、トレースバックが起きる


# The newline Character

# ++++++++++++++
# 「\n」は別の行に移動することを示す文字
#
# ❐ ポイントは、「\n」で一文字とカウントされること❐
# ++++++++++++++


# 改行文字は、ファイル読み取りの重要な部分
stuff = 'Hello\nWorld!'
print(stuff)

stuff = 'X\nY'
print(stuff)
print(len(stuff))


# ==============================================
# File Processing
# 行を読み込む、次の行を読み込む、次の行を読み込む、次の行を読み込む....
# "行"単位で読み込むのが一般的
# ==============================================


# Pythonの授業
# FileOpenについて
# \n
# 改行文字

# ↓↓↓

# Pythonの授業\n
# FileOpenについて\n
# \n
# 改行文字\n


# ★★★　実際は改行文字が入る　★★★
# ★★★　そして、すべての行が改行で終わっている　★★★


# For Handle as a Sequence
#
# ファイルの読み取りには「確定ループ、forループ」用いる。

# ❐❐❐　Windowsではデフォルトの標準出力がcp932(byte型)になる　❐❐❐
# Windowsはstr型（UTF-8）をbyte型（cp932）に勝手に変換しようするが、変換できないためUnicodeDecodeErrorが発生する

# open関数に「encoding="utf-8"」を指定すれば読み取れるようになる。
xfile = open('mbox.txt', encoding="utf-8")

# 変数「xfile」はデータではないが、「シーケンス」である
for cheese in xfile: # 「cheese」が反復変数
  print(cheese)
  # 一行ずつprintされる（"一行ずつというのがポイント"）


# ❐ >>>
#
# シーケンス -- 連続（しているもの）、一続き（のもの）、順序、順番、並び、配列（する）
# ハンドラ -- 何かと何かの間に立って橋渡しをするもので、通常のプログラムの流れには組み込まれずに、何らかの処理要求が発生したときに起動される
# ハンドリング -- ハンドラが行うことをハンドリングと呼ぶ
# ハンドル -- 複数のハンドリングを行いたい時に、個々のハンドリングが識別できるよう各々のハンドリングに一意の番号をつける。この番号をハンドル、あるいはポインタのポインタとも呼ばれる。
#
# ファイルハンドル -- プログラムからファイルの読み書きを便利に便利にこなしてくれるイベントハンドルのひとつであるファイルハンドラの固有識別番号のこと（pythonではopen関数）
#
# ❐ <<<




# Counting Lines in a File (基本的なループカウントパターン)
fhand = open('mbox.txt', encoding='utf-8')
count = 0
for line in fhand:
  count = count + 1
print('Line Count:', count)



# Reading the *Whole* File (ファイルを一連の文字として"一度"に読み取ることもできる)(---行ごとではない)
fhand = open('mbox.txt', encoding='utf-8') # 変数「fhand」には、ファイルハンドルオブジェクトが入っている
inp = fhand.read() #「fhand」のオブジェクトのreadメソッド呼び出し　>>> "すべて"のテキストを読み取り、大きなブロック、一つの大きな文字列で返却する
# 変数「inp」には文字列が入っている

print(len(inp))
print(inp[:12])

# ※ただしこの方法は、10000行程度なら問題ないが、1000万行読み込むのであれば、確定ループが良い






# Searching Through a File (行検索)
fhand = open('mbox.txt', encoding='utf-8')
for line in fhand:
  if line.startswith('こ') : # プレフィックスとして文字列「こ」を持つ文字列に一致する行を探している
    print(line)

# プレフィックス -- 接頭辞、前につける、などの意味を持つ英単語。 “prefix” の “pre” （「前」「先」などの意）




# Searching Through a File (Fixed)
fhand = open('mbox.txt', encoding='utf-8')
for line in fhand:
  line = line.rstrip() # 改行を取り消す
  if line.startswith('こ') :
    print(line) # print関数は呼び出し時に「\n、改行」を自動で挿入する


# ::::::::::::::::::::::::::
# これはテキストです。\n
# 読み取り２行目です。\n
# ３行目になります。\n
#
# ↓
#
# これはテキストです。\n (ファイルそのもの改行)
# \n (print関数で自動挿入)
# 読み取り２行目です。\n (ファイルそのもの改行)
# \n (print関数で自動挿入)
# ３行目になります。\n (ファイルそのもの改行)
# \n (print関数で自動挿入)
# ::::::::::::::::::::::::::