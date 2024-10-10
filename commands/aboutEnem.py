import discord
from discord import app_commands
from discord.ext import commands

class SobreENEM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sobre", description="Informações sobre o Exame Nacional do Ensino Médio (Enem).")
    async def sobre(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Sobre o Exame Nacional do Ensino Médio (Enem)",
            color=discord.Color.blue()
        )
        
        texto = (
            "O Exame Nacional do Ensino Médio (Enem) foi instituído em 1998, "
            "com o objetivo de avaliar o desempenho escolar dos estudantes ao término "
            "da educação básica. Em 2009, o exame aperfeiçoou sua metodologia e passou "
            "a ser utilizado como mecanismo de acesso à educação superior.\n\n"
            
            "As notas do Enem podem ser usadas para acesso ao Sistema de Seleção Unificada (Sisu) "
            "e ao Programa Universidade para Todos (ProUni). Elas também são aceitas em instituições "
            "de educação superior portuguesas que têm acordo com o Instituto Nacional de Estudos e "
            "Pesquisas Educacionais Anísio Teixeira (Inep). Além disso, os participantes do Enem "
            "podem pleitear financiamento estudantil em programas do governo, como o Fundo de "
            "Financiamento Estudantil (Fies). Os resultados do Enem possibilitam, ainda, o "
            "desenvolvimento de estudos e indicadores educacionais.\n\n"
            
            "Qualquer pessoa que já concluiu o ensino médio ou está concluindo a etapa pode fazer "
            "o Enem para acesso à educação superior. Os participantes que ainda não concluíram o "
            "ensino médio podem participar como 'treineiros', e seus resultados no exame servem "
            "somente para autoavaliação de conhecimentos.\n\n"
            
            "A aplicação do Enem ocorre em dois dias. A Política de Acessibilidade e Inclusão do "
            "Inep garante atendimento especializado e tratamento pelo nome social, além de diversos "
            "recursos de acessibilidade. Há também uma aplicação para pessoas privadas de liberdade.\n\n"
            
            "Os participantes fazem provas de quatro áreas de conhecimento: linguagens, códigos e "
            "suas tecnologias; ciências humanas e suas tecnologias; ciências da natureza e suas "
            "tecnologias; e matemática e suas tecnologias, totalizando 180 questões objetivas. "
            "Os participantes também são avaliados por meio de uma redação, que exige o desenvolvimento "
            "de um texto dissertativo-argumentativo a partir de uma situação-problema."
        )

        embed.description = texto
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(SobreENEM(bot))