import openai

API_KEY = "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"
openai.api_key = API_KEY

def text_summarize(input_text):

    def text_summary(prompt):
        # 分析の実施
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.8,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.2,
        presence_penalty=0.2,
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

csv_file = open("./processed_sammarized_data_100_ENandJP.csv", "r", encoding="UTF-8", errors="", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
# csvファイルのヘッダーをスキップ
header = next(f)
print(header)
# 出力データにヘッダーを追加
# data.append(header + ['EN_summarize_txt'])

cnt = 0

for row in f:
    # print(row)
    output_row = [row[-1] + "    _" + row[10]]
    print(output_row)
    data.append(output_row)

    cnt += 1
    print(f'cnt:{cnt}')
    print(output_row[-1])
    print()

print(data)
    



# -----------------------------------------------


# csvファイル出力
f = open('pekora_poem.csv', 'w', encoding='UTF-8')
writer = csv.writer(f)
writer.writerows(data)
f.close()