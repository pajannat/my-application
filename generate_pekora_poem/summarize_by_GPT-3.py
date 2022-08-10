import openai

API_KEY = "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"
openai.api_key = API_KEY

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

def crean_text(text):
    text= text.replace('　',' ')

    return text


# 要約対象の文章をここに入力
text = '''
Spies are everywhere. Maybe someone close to you is really a spy. Why should I be scared? I'm just innocent... I don't know what to do now that I'm on trial. How can I improve my impression? Can you tell me? Pekoara! Take your innocence into my hands ！！！！！！！
'''

prompt ='''
Tl;dr
'''

prompt = crean_text(text) +  prompt


# 結果出力
print(text_summary(prompt))
# print(text_summary(text))

