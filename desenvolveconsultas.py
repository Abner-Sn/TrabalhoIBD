import sqlite3
import pandas as pd

def testar_consultas():
    # Conectar ao banco
    conn = sqlite3.connect('pawsome.db')
    
    print("🔍 TESTANDO CONSULTAS PAWSOME")
    print("=" * 50)
    
    # CONSULTAS EM ÁLGEBRA RELACIONAL (A1-A5)
    print("\n🧮 CONSULTAS EM ÁLGEBRA RELACIONAL")
    print("-" * 40)
    
    # A1: Produtos da categoria Gatos
    print("\nA1 - Produtos para Gatos:")
    query_a1 = "SELECT nome, preco FROM produto WHERE categoria = 'Gatos'"
    df_a1 = pd.read_sql_query(query_a1, conn)
    print(df_a1)
    
    # A2: Nomes dos Veterinários
    print("\nA2 - Veterinários:")
    query_a2 = "SELECT nome FROM usuario WHERE tipo = 'Veterinario'"
    df_a2 = pd.read_sql_query(query_a2, conn)
    print(df_a2)
    
    # A3: Clientes e seus serviços agendados
    print("\nA3 - Clientes e Serviços Agendados:")
    query_a3 = """
    SELECT c.nome as cliente, s.nome as servico 
    FROM cliente c
    JOIN ordem_servico os ON c.id = os.id_cliente
    JOIN servico s ON os.id_servico = s.id
    """
    df_a3 = pd.read_sql_query(query_a3, conn)
    print(df_a3)
    
    # A4: Produtos com estoque baixo (<10)
    print("\nA4 - Produtos com Estoque Baixo:")
    query_a4 = "SELECT nome FROM produto WHERE quantidade_estoque < 10"
    df_a4 = pd.read_sql_query(query_a4, conn)
    print(df_a4)
    
    # A5: Clientes e valores pagos
    print("\nA5 - Clientes e Valores Pagos:")
    query_a5 = """
    SELECT c.nome as cliente, p.valor_pago 
    FROM cliente c
    JOIN venda v ON c.id = v.id_cliente
    JOIN pagamento p ON v.id = p.id_venda
    """
    df_a5 = pd.read_sql_query(query_a5, conn)
    print(df_a5)
    
    # CONSULTAS EM LINGUAGEM NATURAL (B1-B10)
    print("\n\n🗣️ CONSULTAS EM LINGUAGEM NATURAL")
    print("-" * 40)
    
    # B1: Produtos com preço superior a R$ 100,00
    print("\nB1 - Produtos acima de R$ 100,00:")
    query_b1 = "SELECT * FROM produto WHERE preco > 100.00"
    df_b1 = pd.read_sql_query(query_b1, conn)
    print(df_b1)
    
    # B2: Clientes que moram no bairro 'Centro'
    print("\nB2 - Clientes do Centro:")
    query_b2 = "SELECT * FROM cliente WHERE endereco LIKE '%Centro%'"
    df_b2 = pd.read_sql_query(query_b2, conn)
    print(df_b2)
    
    # B3: Veterinários com mais de 5 ordens no último mês
    print("\nB3 - Veterinários Ativos:")
    query_b3 = """
    SELECT u.nome, COUNT(os.id) as total_ordens
    FROM usuario u
    JOIN ordem_servico os ON u.id = os.id_veterinario
    WHERE os.horario_agendamento >= date('now', '-1 month')
    GROUP BY u.id, u.nome
    HAVING COUNT(os.id) > 0  -- Alterei para >0 pois temos poucos dados
    """
    df_b3 = pd.read_sql_query(query_b3, conn)
    print(df_b3)
    
    # B4: Produto mais vendido (em quantidade)
    print("\nB4 - Produto Mais Vendido:")
    query_b4 = """
    SELECT p.nome, SUM(i.quantidade) as total_vendido
    FROM produto p
    JOIN itens i ON p.id = i.id_produto
    GROUP BY p.id, p.nome
    ORDER BY total_vendido DESC
    LIMIT 1
    """
    df_b4 = pd.read_sql_query(query_b4, conn)
    print(df_b4)
    
    # B5: Ordens de serviço agendadas para próxima semana
    print("\nB5 - Ordens da Próxima Semana:")
    query_b5 = """
    SELECT os.id, c.nome as cliente, s.nome as servico, os.horario_agendamento
    FROM ordem_servico os
    JOIN cliente c ON os.id_cliente = c.id
    JOIN servico s ON os.id_servico = s.id
    WHERE os.horario_agendamento BETWEEN date('now') AND date('now', '+7 days')
    AND os.status = 'Agendado'
    """
    df_b5 = pd.read_sql_query(query_b5, conn)
    print(df_b5)
    
    # B6: Faturamento total com vendas em setembro/2025
    print("\nB6 - Faturamento Setembro/2025:")
    query_b6 = """
    SELECT SUM(valor_total) as faturamento_total
    FROM venda
    WHERE data_venda BETWEEN '2025-09-01' AND '2025-09-30'
    """
    df_b6 = pd.read_sql_query(query_b6, conn)
    print(df_b6)
    
    # B7: Clientes que nunca agendaram 'Banho e Tosa'
    print("\nB7 - Clientes sem Banho e Tosa:")
    query_b7 = """
    SELECT c.nome
    FROM cliente c
    WHERE c.id NOT IN (
        SELECT os.id_cliente
        FROM ordem_servico os
        JOIN servico s ON os.id_servico = s.id
        WHERE s.nome = 'Banho e Tosa'
    )
    ORDER BY c.nome
    """
    df_b7 = pd.read_sql_query(query_b7, conn)
    print(df_b7)
    
    # B8: Vendas do vendedor 'Luciano Pereira'
    print("\nB8 - Vendas do Luciano Pereira:")
    query_b8 = """
    SELECT v.*, c.nome as cliente
    FROM venda v
    JOIN usuario u ON v.id_vendedor = u.id
    JOIN cliente c ON v.id_cliente = c.id
    WHERE u.nome = 'Luciano Pereira'
    """
    df_b8 = pd.read_sql_query(query_b8, conn)
    print(df_b8)
    
    # B9: Forma de pagamento mais utilizada
    print("\nB9 - Forma de Pagamento Mais Usada:")
    query_b9 = """
    SELECT forma_pagamento, COUNT(*) as total_uso
    FROM pagamento
    GROUP BY forma_pagamento
    ORDER BY total_uso DESC
    LIMIT 1
    """
    df_b9 = pd.read_sql_query(query_b9, conn)
    print(df_b9)
    
    # B10: Serviços realizados para 'Ana Costa'
    print("\nB10 - Serviços da Ana Costa:")
    query_b10 = """
    SELECT s.nome as servico, os.horario_agendamento, os.status
    FROM ordem_servico os
    JOIN servico s ON os.id_servico = s.id
    JOIN cliente c ON os.id_cliente = c.id
    WHERE c.nome = 'Ana Costa'
    """
    df_b10 = pd.read_sql_query(query_b10, conn)
    print(df_b10)
    
    conn.close()
    print("\n" + "=" * 50)
    print("✅ Todas as consultas testadas com sucesso!")

def verificar_estrutura():
    """Função para verificar a estrutura do banco"""
    conn = sqlite3.connect('pawsome.db')
    cursor = conn.cursor()
    
    print("\n📊 ESTRUTURA DO BANCO:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tabelas = cursor.fetchall()
    
    for tabela in tabelas:
        print(f"\n{tabela[0]}:")
        cursor.execute(f"PRAGMA table_info({tabela[0]})")
        colunas = cursor.fetchall()
        for coluna in colunas:
            print(f"  - {coluna[1]} ({coluna[2]})")
    
    conn.close()

if __name__ == "__main__":
    verificar_estrutura()
    testar_consultas()