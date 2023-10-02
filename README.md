# Hakai-Project
[yukicoder No.10214](https://yukicoder.me/problems/10214)の各種ツールです。

## generator
正しい入力を生成します。

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
