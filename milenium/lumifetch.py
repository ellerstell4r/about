import subprocess

class Information:
    name = "Lumifetch"
    description = "Neofetch-подобный модуль"
    author = "ellerstell4r"
    version = "1.0.0"
    icon = ""
    banner = ""

class Module:
    def __init__(self, commands, lumi, restart, get_uptime, prefix):
        self.commands = commands
        self.lumi = lumi
        self.restart = restart
        self.get_uptime = get_uptime
        self.prefix = prefix

    async def lumifetch(self, message):
        subprocess.run(["which", "neofetch"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        neofetch_process = subprocess.Popen("neofetch", stdout=subprocess.PIPE)
        sed_process = subprocess.Popen(["sed", r"s/\x1B\[[0-9;\?]*[a-zA-Z]//g"], stdin=neofetch_process.stdout, stdout=subprocess.PIPE, text=True)
        neofetch_process.stdout.close()
        result, _ = sed_process.communicate()

        await self.lumi.edit_message(message, message.chat.id, f"<pre><code class='language-stdout'>{result}</code></pre>")

    def _(self):
        self.commands["lumifetch"] = (self.lumifetch, "Lumifetch (neofetch).")
        self.commands["lf"] = (self.lumifetch, "Alias -> lumifetch.")
