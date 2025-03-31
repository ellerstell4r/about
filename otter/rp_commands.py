from misc.anti_spam_block import AntiSpamBlock

asb = AntiSpamBlock()

async def kiss_command(message, client):
    if message.reply_to_message:
        kissed_user = message.reply_to_message.from_user
        await asb.fast_edit(message, client, f"💋 • {message.from_user.first_name} поцеловала {kissed_user.first_name}.")
    else:
        await asb.fast_edit(message, client, "❌ Ответьте на сообщение пользователя, чтобы поцеловать его.")

async def hug_command(message, client):
    if message.reply_to_message:
        hugged_user = message.reply_to_message.from_user
        await asb.fast_edit(message, client, f"🤗 • {message.from_user.first_name} обняла {hugged_user.first_name}.")
    else:
        await asb.fast_edit(message, client, "❌ Ответьте на сообщение пользователя, чтобы обнять его.")

async def greet_command(message, client):
    if message.reply_to_message:
        greeted_user = message.reply_to_message.from_user
        await asb.fast_edit(message, client, f"👋 • {message.from_user.first_name} приветствует {greeted_user.first_name}.")
    else:
        await asb.fast_edit(message, client, "❌ Ответьте на сообщение пользователя, чтобы поприветствовать его.")

def register_commands(custom_commands):
    custom_commands['kiss'] = (kiss_command, "Поцеловать пользователя.")
    custom_commands['hug'] = (hug_command, "Обнять пользователя.")
    custom_commands['greet'] = (greet_command, "Поздороваться с пользователем.")
