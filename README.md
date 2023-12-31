# Hakai-Project
[yukicoder No.10214](https://yukicoder.me/problems/10214)の各種ツールです。

## generator
正しい入力を生成します。

## in
`seed=0`~`seed=99`の入力です。

## judge_code
ジャッジコードです。yukicoderの仕様に則っているため、単体では使いにくいかもしれません。

## score_calc
出力が正当かを判定したうえで、得点計算とコスト計算をするコードです。ジャッジコードと実装はほとんど変わっていません。正しい入力とそれに対する出力をこの順につなげたものを標準入力に与えて実行してください。

## sample_code
C++とPythonで動くコードです。以下の処理を実装しており、そのまま提出することで得点は低いですが`AC`することが可能です。
* 左上から順に見ていき、最初に見つけた爆弾屋に移動する
* 爆弾 $1$ を $2500$ 個購入する
* $(0,0)$ に戻る
* すべてのマスへ行き、それぞれの場所で爆弾を起動する

## sample_input
`seed=0`の入出力例です。

## visualizer
ビジュアライザです。Python3で動きます。`pip3 install pygame`などとして`pygame`をインストールする必要があります。

正しい入力を`in.txt`に、それに対する正しい出力を`out.txt`に書き込んでください。このとき、ファイル名やフォルダ名を変更してはいけません。(動かない場合は、プログラムの7行目、19行目を少し書きかえて参照するファイルをいじってください。)

見方は以下の通りです。
* マップの上の四角…爆弾1~20の所持数
* 橙四角…はるく君の位置
* 茶四角…空き地
* 灰四角…建物
* 紫四角…爆弾屋
* 赤四角…そのターンに爆破された場所

操作方法は以下の通りです。
* Pキー...再生/停止する。
* Sキー...再生速度を変更する。
* 左右キー...1ターン進める/戻す。このとき、最終ターンと1ターン目はループしている。

**ビジュアライザの結果は、コンテスト中はseed=0のもののみ共有可能とします。** コンテスト後は自由な盤面を共有してかまいません。

共有する際は、ぜひ[#yukicoder](https://twitter.com/search?q=%23yukicoder&src=typed_query)と[#HakaiProject](https://twitter.com/search?q=%23HakaiProject&src=typed_query&f=top)を使用してください！
