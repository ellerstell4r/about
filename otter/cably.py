# Not a property of otter userbot and eachcart.
# Licensed under https://github.com/mead0wsss/mead0wsMods/blob/modules/LICENSE.md.

import requests
from misc.anti_spam_block import AntiSpamBlock

asb = AntiSpamBlock()

_CABLY_API_URL = "https://cablyai.com/v1/chat/completions"
_CABLY_API_KEY = "Bearer sk-csPV6DEqRj07V4jGxPvq0NomUcfo6LIxO_rlxBMuenGaebco"

async def cably_command(message, client, id):
    if not _CABLY_API_KEY:
        await asb.fast_edit(message, client, id, "❌ Ошибка: API-ключ Cably отсутствует.")
        return

    query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None

    if not query:
        await asb.fast_edit(message, client, id, "❌ Ошибка: Напишите запрос после команды.")
        return

    await asb.fast_edit(message, client, id, "🤖 Думаю...")

    try:
        response = requests.post(
            _CABLY_API_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {_CABLY_API_KEY}"
            },
            json={
                "messages": [{"role": "user", "content": query}],
                "model": "gpt-4o"
            }
        )

        data = response.json()

        if "choices" in data and data["choices"]:
            answer = data["choices"][0]["message"]["content"]
        else:
            answer = "❌ Cably AI не дал ответа."

        await asb.fast_edit(message, client, id, f"🗨️: {query}\n🧠 Cably:\n{answer}")

    except Exception as e:
        await asb.fast_edit(message, client, id, f"❌ Ошибка запроса: {e}")

def register_commands(custom_commands):
    custom_commands['cably'] = (cably_command, "Запрос к Cably AI.")
