# Functions
# ❐❐❐　「function」は「保存」と「再利用」　❐❐❐
# 同じような機能を一か所に集約すれば、そこを回収するだけで済む



# コードを覚えるフェーズ「ストアフェーズ」※コードの実行は "しない"
# ::::::::::::::::::::::::::::::::::::::::::::::::::::
# def
# 定義済みの関数を表すキーワード
def thing() : # 任意の名前を付ける。※ここでは「thing」

  # if statementの様にインデントでブロックを形成する
  print('Hello')
  print('Fun')
# インデントが解除されるとそこで関数の終わり

# ::::::::::::::::::::::::::::::::::::::::::::::::::::
# 重要なのはこの「def」ブロック部分は "コードを実行していない" ということ
# ❐ 何もしないが覚えている ❐
# つまり、「thing」が呼び出されたときに、実行させたいコードを覚えさせている、これが「保存」


# functionの呼び出し
thing()  # ここで初めてコードが実行される。

# 「thing()」はPythonの一部のように見えるが、def statementでPythonを拡張している


print('Zip')

# functionの『再利用』
# 一回定義したものを再度実行する
thing()


# 「print()」はPythonの組み込みfunction
# ()はfunctionの構文
# int()、type()、input()...


# ❐「def」はPython言語を拡張する新しい予約語を作成できる ❐
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# 「def」はキーワードを使用して定義し、それを呼び出す
# 実際にコードを実行するのではなく、コードを記憶するだけの定義フェーズがあり、
# 次に呼び出しフェーズがある
# 一度定義してから、一回以上呼び出す
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊


# 「max」　Pythonの組み込み関数
# いくつかのパラメータをmax関数に渡すことができる
# 「割り当てステートメント」だから、まず右辺を評価する必要がある
big = max('Hello World')
# 戻り値は「r」
# そしてその戻り値「r」は、「big」に格納される

print(big)


tiny = min('Hello World')
print(tiny)


# 独自の関数構築

# 「def」はストアであり、呼び出しは「再利用」

x = 5
print('Hello')

# ストアフェーズ
def print_lyrics() :
  print("I'm a lumberjack, and I'm okay. ")
  print('I sleep all night and I work all day. ')

print('Yo!')

# functionのinvoke(呼び出し)(call, return, invoke)
print_lyrics()
x = x + 2
print(x)


# 引数を利用して、微妙に調整することではるかに便利で再利用な関数になる

def greet(lang) :
  # ❐❐ 引数であるlang変数は、ある意で関数の存続期間中にのみ存在する ❐❐
  # 一種のプレイスホルダーを表す（正式な値が入るまで一時的に場所を確保しておく措置「で仮に入れておく値」のこと）
  # ※実際の変数ではない
  if lang == 'es':
    print('Hola')
  elif lang == 'fr':
    print('Bonjour')
  else:
    print('Hello')

greet('es') # ここでdefで定義した(lang)は('en')のエイリアスになる。（enはlangとして関数に渡される）
greet('fr')
greet('abc123')

# 「alias」 エイリアス -- ある対象や実体を、複数の異なるシンボルや識別子で同じように参照できるする仕組みを指す
# 「別名」のこと




# Return Values

def greet2() :

  # return statement
  # ********************************************************
  # 1.「終了する」
  # Pythonがreturn statementに入ると次の行に進まない、戻るだけ
  # これで、特定の関数の呼び出しが終了する
  # ☆重要なことは、パラメーターなしで「return」ということができる。つまり、関数の実行を「停止」する意味合いもある

  # 2.「値を呼び出し元へ返す」
  #「残差値」
  return "Hello"
  # ********************************************************

print(greet2(), "Glenn")
print(greet2(), "Sally")


# 値を返す関数は、returnというだけ、もしくは関数の最後の行で自動的にreturnを行う

# 「return」を使用することでより関数のようになる
# 入力を受け取り、単に出力するだけでなく、戻り値として出力を生成するため、関数が出力するのは少し粘着性がある
def greet3(lang):
  if lang == 'es':
    return 'Hola'
  elif lang == 'fr':
    return 'Bonjour'
  else:
    return 'Hello'

print(greet3('en'), 'Glenn')
print(greet3('es'), 'Sally')
print(greet3('fr'), 'Micheal')

# returnがある場合があれば、returnがない場合もある


# Multiple Parameters / Arguments
# 複数の引数を指定できる（好きな数だけ）
# ただし、「順番」が大切
def addtwo(a, b):
  added = a + b
  return added

# パラメーターが必要な関数にパラメーターを渡さないと爆発する（トレースバックが起る）
x = addtwo(3, 5)
print(x)



# Void(non-fruitful) Functions
# 値を指定して、戻り値を呼び出さない関数
# ❐❐　戻り値は関数の最後の行として暗黙的に発生する　❐❐