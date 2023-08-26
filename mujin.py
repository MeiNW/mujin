from Py_Keyboard.HID import Keyboard
import time
import sys
import random
import openai

# あなたのOpenAI APIキーをセット
my_key = "put your api key"

# APIキーを使ってGPT-3エンドポイントに接続
openai.api_key = my_key

# キーボードオブジェクトの初期化
k = Keyboard()

# プロンプトとして使うテキストをセット
p1 = sys.argv[1]
p1 = p1 + "について日本語でレポートを書いてください。"
p1 = p1 + sys.argv[2] + "文字程度の文章量でお願いします。"

# GPT-3の`davinci`エンジンを使ってテキストを生成
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {
            "role": "user",
            "content": p1
        }
    ]
)

# 生成されたテキストを取得
text1 = response.choices[0].message.content

print("Generated text:", text1)

# 生成したテキストをASCII文字に変換するスクリプト
p2 = "次の文章をASCII文字のみでローマ字に変換してください。ローマ字は全て小文字でよいです"
p2 = p2 + "カタカナ用語の長音は「-」で表してください。例えば「データ」は「de-ta」と表します。"
p2 = p2 + "ひらがなや漢字の長音は母音で表してください。例えば「東京」は「toukyou」と表します。"
p2 = p2 + "¥n¥n" + text1

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {
            "role": "user",
            "content": p2
        }
    ]
)

# 生成されたテキストを取得
text2 = response.choices[0].message.content

print("Cvt text:", text2)

# ASCII文字を入力
for c in text2:
    time.sleep(random.uniform(0.1, 0.9))
    k.write(c)
    if c == ' ':
        k.press('ENTER')
    elif c == '.':
        k.press('ENTER')
    elif c == ',':
        k.write(' ')
        k.press('ENTER')

k.press('ENTER')

print("END¥n")
