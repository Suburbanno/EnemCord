import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Modal, TextInput

class enemCalc(Modal):
    def __init__(self):
        super().__init__(title="Calcular Média do ENEM")

        self.redacao = TextInput(
            label="Redação",
            style=discord.TextStyle.short,
            placeholder="Insira a nota da redação (0 a 1000)",
            required=True,
            max_length=4
        )
        self.add_item(self.redacao)

        self.ciencias_natureza = TextInput(
            label="Ciências da Natureza",
            style=discord.TextStyle.short,
            placeholder="Insira a nota de Ciências da Natureza (0 a 1000)",
            required=True,
            max_length=4
        )
        self.add_item(self.ciencias_natureza)

        self.ciencias_humanas = TextInput(
            label="Ciências Humanas",
            style=discord.TextStyle.short,
            placeholder="Insira a nota de Ciências Humanas (0 a 1000)",
            required=True,
            max_length=4
        )
        self.add_item(self.ciencias_humanas)

        self.linguagens = TextInput(
            label="Linguagens, Códigos",
            style=discord.TextStyle.short,
            placeholder="Insira a nota de Linguagens (0 a 1000)",
            required=True,
            max_length=4
        )
        self.add_item(self.linguagens)

        self.matematica = TextInput(
            label="Matemática",
            style=discord.TextStyle.short,
            placeholder="Insira a nota de Matemática (0 a 1000)",
            required=True,
            max_length=4
        )
        self.add_item(self.matematica)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            redacao = float(self.redacao.value)
            ciencias_natureza = float(self.ciencias_natureza.value)
            ciencias_humanas = float(self.ciencias_humanas.value)
            linguagens = float(self.linguagens.value)
            matematica = float(self.matematica.value)

            media = (redacao + ciencias_natureza + ciencias_humanas + linguagens + matematica) / 5

            await interaction.response.send_message(f"{interaction.user.mention} Sua média do ENEM é: `{media:.2f}`", ephemeral=True)

        except ValueError:
            await interaction.response.send_message("Por favor, insira apenas números válidos.", ephemeral=True)

class enemMedia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="media", description="Calcule sua média do ENEM.")
    async def media(self, interaction: discord.Interaction):
        await interaction.response.send_modal(enemCalc())

async def setup(bot):
    await bot.add_cog(enemMedia(bot))