import discord
from discord import app_commands
from discord.ext import commands

class Datas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="calendario", description="Informações sobre as datas, disciplinas e duração das provas do ENEM.")
    async def enem_datas(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="ENEM 2024 - Datas, Disciplinas e Duração",
            description="Aqui estão as datas e disciplinas que serão abordadas nos dias de prova do ENEM 2024:",
            color=discord.Color.blue()
        )

        embed.add_field(
            name="1º Dia: 05 de Novembro",
            value="**Duração:** 5h30\n**Total de Questões:** 90",
            inline=False
        )
        embed.add_field(
            name="Linguagens, Códigos e suas Tecnologias",
            value="**Questões:** 45\n- Língua Portuguesa\n- Língua Estrangeira\n- Literatura\n- Artes\n- Educação Física\n- TICs",
            inline=True
        )
        embed.add_field(
            name="Ciências Humanas e suas Tecnologias",
            value="**Questões:** 45\n- História\n- Geografia\n- Filosofia\n- Sociologia",
            inline=True
        )
        embed.add_field(
            name="Redação",
            value="**Questões:** 1\n- Argumentativa-dissertativa",
            inline=True
        )

        embed.add_field(
            name="2º Dia: 12 de Novembro",
            value="**Duração:** 5h\n**Total de Questões:** 90",
            inline=False
        )
        embed.add_field(
            name="Ciências da Natureza e suas Tecnologias",
            value="**Questões:** 45\n- Física\n- Biologia\n- Química",
            inline=True
        )
        embed.add_field(
            name="Matemática e suas Tecnologias",
            value="**Questões:** 45\n- Matemática",
            inline=True
        )

        embed.set_footer(text="Foco, organização e bons estudos! Boa sorte no ENEM 2024!")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Datas(bot))
