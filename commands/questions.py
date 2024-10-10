import discord
from discord import app_commands
from discord.ext import commands
import requests
import re

class Enem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_question(self, ano, numero):
        url = f"https://api.enem.dev/v1/exams/{ano}/questions/{numero}"
        response = requests.get(url)
        return response.json()

    @app_commands.command(name="questao", description="Obtenha questões por ano e número.")
    @app_commands.describe(ano="Ano da prova", numero="Número da questão")
    async def enem(self, interaction: discord.Interaction, ano: str, numero: str):
        question = self.get_question(ano, numero)

        if 'error' in question or not question:
            await interaction.response.send_message("Questão não encontrada.", ephemeral=True)
            return

        context = question.get('context', 'Contexto não disponível.')
        if not isinstance(context, str):
            context = str(context)
        context = re.sub(r'!\[.*?\]\(.*?\)', '', context).strip()

        title = question.get('title', 'Questão')
        alternatives = question.get('alternatives', [])
        correct_answer = question.get('correctAlternative', 'N/A')

        alternatives_text = "\n".join([f"{alt['letter']}: {alt['text']}" for alt in alternatives])

        embed = discord.Embed(
            title=title,
            description=f"{context}\n\n{question.get('alternativesIntroduction', '')}\n\n{alternatives_text}",
            color=discord.Color.blue()
        )

        files = question.get('files', [])
        if files:
            embed.set_image(url=files[0])
            for file_url in files[1:]:
                embed.add_field(name="Imagem", value=file_url, inline=False)

        await interaction.response.send_message(
            embed=embed,
            view=Enem.QuestionButtons(correct_answer=correct_answer)
        )

    class QuestionButtons(discord.ui.View):
        def __init__(self, correct_answer):
            super().__init__()
            self.correct_answer = correct_answer

        @discord.ui.button(label="A", style=discord.ButtonStyle.primary)
        async def button_a(self, interaction: discord.Interaction, button: discord.ui.Button):
            await self.check_answer(interaction, "A")

        @discord.ui.button(label="B", style=discord.ButtonStyle.primary)
        async def button_b(self, interaction: discord.Interaction, button: discord.ui.Button):
            await self.check_answer(interaction, "B")

        @discord.ui.button(label="C", style=discord.ButtonStyle.primary)
        async def button_c(self, interaction: discord.Interaction, button: discord.ui.Button):
            await self.check_answer(interaction, "C")

        @discord.ui.button(label="D", style=discord.ButtonStyle.primary)
        async def button_d(self, interaction: discord.Interaction, button: discord.ui.Button):
            await self.check_answer(interaction, "D")

        @discord.ui.button(label="E", style=discord.ButtonStyle.primary)
        async def button_e(self, interaction: discord.Interaction, button: discord.ui.Button):
            await self.check_answer(interaction, "E")

        async def check_answer(self, interaction: discord.Interaction, answer: str):
            if answer == self.correct_answer:
                await interaction.response.send_message(
                    f"{interaction.user.mention}, ✅ Você respondeu corretamente!",
                    ephemeral=False
                )
            else:
                await interaction.response.send_message(
                    f"{interaction.user.mention}, ❎ Resposta errada!\nA resposta correta era: {self.correct_answer}",
                    ephemeral=False
                )

async def setup(bot):
    await bot.add_cog(Enem(bot))