import asyncio

from Johnny.utils.getenv import getenv


async def run_discodo():
    cmd_line = f"python3 -m discodo --port 6974 --auth youshallnotpass"
    await asyncio.create_subprocess_shell(cmd_line)


async def check_voice_connection(ctx):
    if not ctx.bot.cjamm.getVC(ctx.guild.id, safe=True):
        if not ctx.author.voice:
            await ctx.send("> 먼저 음성 채널에 접속해주세요.")
            return False

        channel = ctx.author.voice.channel

        async with ctx.typing():
            await ctx.bot.cjamm.connect(channel)
        await ctx.send(f"> 성공적으로 {channel.mention}에 접속했습니다.")

    VC = ctx.bot.cjamm.getVC(ctx.guild.id, safe=True)
    if VC and not hasattr(VC, "channel"):
        VC.channel = ctx.channel

    return True
