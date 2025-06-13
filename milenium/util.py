import time, os

class Information:
    name = "Дополнительные команды"
    description = "Дополнительные команды (Необходим NextLib)"
    author = "eachcart"
    version = "1.0.0"
    icon = ""
    banner = ""

try:
    from Luminate.Modules.nextlib import Utils
except ImportError:
    raise ImportError(f"Модуль не может быть загружен: требуется NextLib. Установите его через @modlumi.")

class Module:
    def __init__(self, commands, lumi, restart, get_uptime, prefix):
        self.commands = commands
        self.lumi = lumi
        self.restart = restart
        self.get_uptime = get_uptime
        self.prefix = prefix

    async def ping(self, message):
        start = time.perf_counter()
        msg = await self.lumi.edit_message(message, message.chat.id, "⌛")
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        await self.lumi.edit_message(message, message.chat.id, f"{Utils.emoji(5028487082398451141, 'ℹ️')} Пинг: {elapsed_ms:.2f} мс.", use_id=True, msg_id=msg.id)

    async def uptime(self, message):
        await self.lumi.edit_message(message, message.chat.id, f"{Utils.emoji(5028564640917882035, '⌛️')} Аптайм: {self.get_uptime()}")

    def _(self):
        self.commands["ping"] = (self.ping, "Проверить пинг.")
        self.commands["uptime"] = (self.uptime, "Проверить пинг.")
