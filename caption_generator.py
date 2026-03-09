from openai import OpenAI

client = OpenAI()

def gerar_legenda(info):

    prompt = f"""
Crie legenda para Instagram.

Filme: {info['titulo']}
Ano: {info['ano']}
Sinopse: {info['sinopse']}

Inclua 5 hashtags.
"""

    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return r.choices[0].message.content