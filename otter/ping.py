from misc.anti_spam_block import AntiSpamBlock
from ping3 import ping
import time

asb = AntiSpamBlock()

async def ping_ip_list(message, client):
    ip_list = [
        "149.154.175.53",
        "149.154.167.51",
        "149.154.175.100",
        "149.154.167.91",
        "91.108.56.130",
    ]

    ping_results = []
    full_ping_duration = 0

    for ip in ip_list:
        try:
            start_time = time.time()
            ping_duration = ping(ip)
            if ping_duration is None:
                ping_results.append(f"{ip}: ❌: Нет ответа")
            else:
                ping_duration = round(ping_duration * 1000, 2)
                full_ping_duration += ping_duration
                ping_results.append(f"{ip}: ✅: {ping_duration} ms")
        except Exception as e:
            ping_results.append(f"{ip}: ❌: Ошибка: {str(e)}")

    result_text = "\n".join(ping_results)
    full_result_text = f"⏰: {full_ping_duration} ms\n{result_text}"
    await asb.fast_edit(message, client, full_result_text)

def register_commands(custom_commands):
    custom_commands['pingdcs'] = (ping_ip_list, "Проверить пинг телеграма. (DC Серверов)")
