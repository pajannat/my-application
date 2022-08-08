import openai

API_KEY = "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"
openai.api_key = API_KEY

def text_summarize(input_text):

    def text_summary(prompt):
        # 分析の実施
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        )

        # 分析結果の出力
        return response["choices"][0]["text"].replace('\n','')

    def crean_text(txt):
        txt= txt.replace('　',' ')

        return txt


    # 出力の調整
    prompt ='''
    Tl;dr
    '''

    prompt = crean_text(input_text) +  prompt

    # 要約実行
    return text_summary(prompt)


# -----------------------------------------------


# 出力するデータ
data = []


# -----------------------------------------------


# csvファイル受け取り
import csv

csv_file = open("./pre_processed_data.csv", "r", encoding="UTF-8", errors="", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
# csvファイルのヘッダーをスキップ
header = next(f)
print(header)
# 出力データにヘッダーを追加
data.append(header + ['summarize_txt'])

for row in f:
    output_row = row + [text_summarize(row[10])]
    data.append(output_row)


# -----------------------------------------------


# csvファイル出力
f = open('out2.csv', 'w', encoding='UTF-8')
writer = csv.writer(f)
writer.writerows(data)
f.close()