from discord.ext import commands
from Johnny.bot import Johnny
from Johnny.utils.logger import Logger


class Music(commands.Cog):
    patching = False

    def __init__(self, bot: Johnny) -> None:
        self.bot = bot
        self.logger = Logger.cogLogger(self)


def setup(bot: Johnny):

    if not Music.patching:
        bot.add_cog(Music(bot))
        bot.cjamm.register_node("127.0.0.1", "6974", password="youshallnotpass")

    elif Music.patching:
        return bot.logger.warn(f"Music is in patching status.")
