import discord
import platform
import os
import time
from discord import app_commands
from discord.ext import commands
class PingInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="ping", description="Verifique a latência e exiba as informações técnicas do bot.")
    async def ping(self, ctx: discord.Interaction):

        start_time = time.time()
        await ctx.response.send_message("Verificando...")
        end_time = time.time()

        discord_version = discord.__version__
        python_version = platform.python_version()
        os_info = f"{platform.system()} {platform.release()} ({os.name})"

        embed = discord.Embed(title="📊 Informações Técnicas e Latência", color=discord.Color.blue())
        embed.set_author(name="EnemCord")
        embed.add_field(name="Latência do WebSocket", value=f"`{round(self.bot.latency * 1000)}ms 📊`", inline=False)
        embed.add_field(name="Latência da API", value=f"`{round((end_time - start_time) * 1000)}ms 🚀`", inline=False)
        embed.add_field(name="Versão da API Discord.py", value=f"`{discord_version}`", inline=False)
        embed.add_field(name="Versão do Python", value=f"`{python_version}`", inline=False)
        embed.add_field(name="Sistema Operacional", value=f"`{os_info}`", inline=False)

        await ctx.edit_original_response(content=None, embed=embed)

async def setup(bot):
    await bot.add_cog(PingInfo(bot))