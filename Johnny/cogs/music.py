from discord.ext import commands
from Johnny.bot import Johnny
from Johnny.utils.getenv import getenv
from Johnny.utils.logger import Logger


class Music(commands.Cog):
    patching = False

    def __init__(self, bot: Johnny) -> None:
        self.bot = bot
        self.logger = Logger.cogLogger(self)

        self.bot.cjamm.register_node("localhost", "6974", password=getenv("DISCODO_PW"))


def setup(bot: Johnny):

    if not Music.patching:
        bot.add_cog(Music(bot))

    elif Music.patching:
        return bot.logger.warn(f"Music is in patching status.")
