# =============================================================================
# INSTRUÇÕES
# =============================================================================
# 1. Preencha as informações de identificação abaixo.
# 2. Escreva o código SQL para cada uma das 15 consultas nas variáveis designadas.
#    - As consultas de A1 a A5 são baseadas nas expressões em Álgebra Relacional.
#    - As consultas de B1 a B10 são baseadas nas perguntas em Linguagem Natural.
# 3. Salve o arquivo e o envie no Moodle. 
# 4. NÃO altere o nome das funções, das variáveis de consulta ou dos arquivos de saída.
# =============================================================================

# DADOS DO ALUNO
NOME_ALUNO = "SEU NOME COMPLETO AQUI"
MATRICULA_ALUNO = "SUA MATRÍCULA AQUI"

# =============================================================================
# CÓDIGO DE PREPARAÇÃO DO AMBIENTE (NÃO ALTERAR)
# =============================================================================
import sqlite3
import pandas as pd

def salvar_consulta(query, filename):
    """Função auxiliar para executar a consulta e salvar o resultado em um arquivo de texto."""
    try:
        # Conexão com o banco de dados
        con = sqlite3.connect('database.db')

        df = pd.read_sql_query(query, con)
        df.to_csv(filename, sep='|', index=False)
        print(f"Resultado para '{filename}' salvo com sucesso.")
        con.close()
    except Exception as e:
        # Garante que a conexão seja fechada mesmo em caso de erro
        if 'con' in locals() and con:
            con.close()
        print(f"Ocorreu um erro na consulta para '{filename}': {e}")

# =============================================================================
# Consultas baseadas em Álgebra Relacional
# =============================================================================

# A1
query_a1 = """
-- CONSULTA SQL

"""

# A2
query_a2 = """
-- CONSULTA SQL

"""

# A3
query_a3 = """
-- CONSULTA SQL

"""

# A4
query_a4 = """
-- CONSULTA SQL

"""

# A5
query_a5 = """
-- CONSULTA SQL

"""

# =============================================================================
# Consultas baseadas em Linguagem Natural
# =============================================================================

# B1. Liste todos os produtos com preço superior a R$ 100,00
query_b1 = """
-- CONSULTA SQL

"""

# B2. Encontre os clientes que moram no bairro 'Centro'.
query_b2 = """
-- CONSULTA SQL

"""

# B3. Mostre os veterinários que realizaram mais de 5 ordens de serviço no último mês.
query_b3 = """
-- CONSULTA SQL

"""

# B4. Qual o produto mais vendido (em quantidade)?
query_b4 = """
-- CONSULTA SQL

"""

# B5. Liste as ordens de serviço agendadas para a próxima semana.
query_b5 = """
-- CONSULTA SQL

"""

# B6. Calcule o faturamento total com vendas no mês de setembro de 2025.
query_b6 = """
-- CONSULTA SQL

"""

# B7. Encontre os clientes que nunca agendaram um serviço de 'Banho e Tosa'. 
query_b7 = """
-- CONSULTA SQL

"""

# B8. Liste todas as vendas realizadas pelo vendedor 'Luciano Pereira'.
query_b8 = """
-- CONSULTA SQL

"""

# B9. Qual a forma de pagamento mais utilizada? 
query_b9 = """
-- CONSULTA SQL

"""

# B10. Mostre todos os serviços realizados em um cliente específico, por exemplo, 'Ana Costa'.
query_b10 = """
-- CONSULTA SQL

"""


# =============================================================================
# EXECUÇÃO E SALVAMENTO (NÃO ALTERAR)
# =============================================================================
print("\nIniciando a execução e salvamento das consultas...")
salvar_consulta(query_a1, "output_A1.txt")
salvar_consulta(query_a2, "output_A2.txt")
salvar_consulta(query_a3, "output_A3.txt")
salvar_consulta(query_a4, "output_A4.txt")
salvar_consulta(query_a5, "output_A5.txt")
salvar_consulta(query_b1, "output_B1.txt")
salvar_consulta(query_b2, "output_B2.txt")
salvar_consulta(query_b3, "output_B3.txt")
salvar_consulta(query_b4, "output_B4.txt")
salvar_consulta(query_b5, "output_B5.txt")
salvar_consulta(query_b6, "output_B6.txt")
salvar_consulta(query_b7, "output_B7.txt")
salvar_consulta(query_b8, "output_B8.txt")
salvar_consulta(query_b9, "output_B9.txt")
salvar_consulta(query_b10, "output_B10.txt")
print("\nProcesso concluído.")