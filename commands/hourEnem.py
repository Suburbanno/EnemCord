import discord
from discord import app_commands
from discord.ext import commands
class HorariosENEM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="horarios", description="Informações sobre os horários do Enem.")
    async def horarios(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Horários do Exame Nacional do Ensino Médio (Enem)",
            description="O Enem segue o horário de Brasília.",
            color=discord.Color.blue()
        )

        embed.add_field(name="1º Prova", value="**1º Domingo**", inline=False)
        embed.add_field(name="Abertura dos portões", value="12h", inline=True)
        embed.add_field(name="Fechamento dos portões", value="13h", inline=True)
        embed.add_field(name="Início das provas", value="13h30", inline=True)
        embed.add_field(name="Término das provas", value="19h", inline=True)
        embed.add_field(name="Término tempo adicional", value="20h", inline=True)
        embed.add_field(name="Término videoprova em Libras", value="21h", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="2º Prova", value="**2º Domingo**", inline=False)
        embed.add_field(name="Abertura dos portões", value="12h", inline=True)
        embed.add_field(name="Fechamento dos portões", value="13h", inline=True)
        embed.add_field(name="Início das provas", value="13h30", inline=True)
        embed.add_field(name="Término das provas", value="18h30", inline=True)
        embed.add_field(name="Término tempo adicional", value="19h30", inline=True)
        embed.add_field(name="Término videoprova em Libras", value="20h30", inline=True)
        embed.add_field(name="Atenção!", value=(
            "Às 13h, começam os procedimentos de identificação realizados na sala de provas. "
            "A ida ao banheiro após esse horário requer nova identificação do participante para retorno à sala de provas."
        ), inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(HorariosENEM(bot))