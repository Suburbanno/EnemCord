import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="ping", description="Verifique a latência do bot.")
    async def ping(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title='🏓 Pong!',
            color=discord.Color.blue()
        )
        embed.set_author(name='EnemCord')
        embed.add_field(
            name='Latência',
            value=f"`{round(self.bot.latency * 1000)}ms 📊`",
            inline=True
        )
        await ctx.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Ping(bot))