import sqlite3
from datetime import datetime, timedelta

def inserir_dados_exemplo():
    conn = sqlite3.connect('pawsome.db')
    cursor = conn.cursor()
    
    print("📝 Inserindo dados de exemplo...")
    
    # 1. Inserir usuários
    usuarios = [
        ('Ana Silva', 'ana@pawsome.com', '123', 'Administrador'),
        ('Carlos Santos', 'carlos@pawsome.com', '123', 'Vendedor'),
        ('Mariana Lima', 'mariana@pawsome.com', '123', 'Vendedor'),
        ('Dr. Pedro Costa', 'pedro@pawsome.com', '123', 'Veterinario'),
        ('Dra. Julia Oliveira', 'julia@pawsome.com', '123', 'Veterinario'),
        ('Luciano Pereira', 'luciano@pawsome.com', '123', 'Vendedor')
    ]
    cursor.executemany('INSERT INTO usuario (nome, email, senha, tipo) VALUES (?, ?, ?, ?)', usuarios)
    
    # 2. Inserir clientes
    clientes = [
        ('João Almeida', '(11) 9999-1111', 'Rua das Flores, 123 - Centro', 'joao@email.com'),
        ('Maria Souza', '(11) 9999-2222', 'Av. Principal, 456 - Jardins', 'maria@email.com'),
        ('Ana Costa', '(11) 9999-3333', 'Rua Secundária, 789 - Centro', 'ana@email.com'),
        ('Paulo Mendes', '(11) 9999-4444', 'Alameda Santos, 321 - Centro', 'paulo@email.com'),
        ('Fernanda Rocha', '(11) 9999-5555', 'Rua das Árvores, 654 - Parque', 'fernanda@email.com')
    ]
    cursor.executemany('INSERT INTO cliente (nome, telefone, endereco, email) VALUES (?, ?, ?, ?)', clientes)
    
    # 3. Inserir produtos
    produtos = [
        ('Ração Premium Cães', 'Ração premium para cães adultos', 120.00, 25, 'Cães'),
        ('Ração Econômica Gatos', 'Ração econômica para gatos', 45.00, 8, 'Gatos'),
        ('Brinquedo Pelúcia', 'Brinquedo de pelúcia para cães', 25.00, 15, 'Cães'),
        ('Areia Sanitária', 'Areia sanitária para gatos', 35.00, 30, 'Gatos'),
        ('Gaiola Pássaros', 'Gaiola para pássaros pequenos', 89.00, 5, 'Pássaros'),
        ('Coleira Couro', 'Coleira de couro para cães', 45.00, 12, 'Cães'),
        ('Shampoo Hidratante', 'Shampoo para banho de cães e gatos', 28.00, 20, 'Cães'),
        ('Ração Pássaros', 'Ração para pássaros ornamentais', 15.00, 18, 'Pássaros'),
        ('Osso Artificial', 'Osso artificial para cães', 18.00, 7, 'Cães'),
        ('Arranhador Gatos', 'Arranhador para gatos', 65.00, 4, 'Gatos')
    ]
    cursor.executemany('INSERT INTO produto (nome, descricao, preco, quantidade_estoque, categoria) VALUES (?, ?, ?, ?, ?)', produtos)
    
    # 4. Inserir serviços
    servicos = [
        ('Banho e Tosa', 'Banho completo e tosa higiênica', 80.00),
        ('Consulta Veterinária', 'Consulta de rotina com veterinário', 120.00),
        ('Vacinação', 'Aplicação de vacinas', 60.00),
        ('Exame Laboratorial', 'Exames de sangue e urina', 150.00),
        ('Tosa Completa', 'Tosa estética completa', 100.00)
    ]
    cursor.executemany('INSERT INTO servico (nome, descricao, preco_base) VALUES (?, ?, ?)', servicos)
    
    # 5. Inserir vendas
    vendas = [
        (1, 2, '2025-09-20 10:30:00', 145.00),  # João comprou com Carlos
        (2, 3, '2025-09-21 14:15:00', 70.00),   # Maria comprou com Mariana
        (3, 6, '2025-09-22 09:45:00', 165.00),  # Ana comprou com Luciano
        (1, 2, '2025-09-25 16:20:00', 53.00),   # João comprou novamente
        (4, 3, '2025-10-01 11:00:00', 89.00)    # Paulo comprou com Mariana
    ]
    cursor.executemany('INSERT INTO venda (id_cliente, id_vendedor, data_venda, valor_total) VALUES (?, ?, ?, ?)', vendas)
    
    # 6. Inserir itens das vendas
    itens_venda = [
        (1, 1, 1, 120.00),  # Venda 1: 1 Ração Premium Cães
        (1, 3, 1, 25.00),   # Venda 1: 1 Brinquedo Pelúcia
        (2, 2, 1, 45.00),   # Venda 2: 1 Ração Econômica Gatos
        (2, 7, 1, 25.00),   # Venda 2: 1 Shampoo (preço promocional)
        (3, 1, 1, 120.00),  # Venda 3: 1 Ração Premium Cães
        (3, 6, 1, 45.00),   # Venda 3: 1 Coleira Couro
        (4, 9, 2, 18.00),   # Venda 4: 2 Ossos Artificiais
        (4, 8, 1, 15.00),   # Venda 4: 1 Ração Pássaros
        (5, 5, 1, 89.00)    # Venda 5: 1 Gaiola Pássaros
    ]
    cursor.executemany('INSERT INTO itens (id_venda, id_produto, quantidade, preco_unitario) VALUES (?, ?, ?, ?)', itens_venda)
    
    # 7. Inserir ordens de serviço
    ordens_servico = [
        (1, 4, 1, '2025-10-05 09:00:00', None, 'Agendado'),        # João - Consulta
        (2, 5, 2, '2025-10-03 14:30:00', 'Animal saudável', 'Concluído'),  # Maria - Banho
        (3, 4, 3, '2025-10-10 10:00:00', None, 'Agendado'),        # Ana - Vacinação
        (4, 5, 1, '2025-09-28 16:00:00', 'Necessita exames', 'Concluído'), # Paulo - Consulta
        (2, 4, 2, '2025-10-15 11:30:00', None, 'Agendado')         # Maria - Banho
    ]
    cursor.executemany('INSERT INTO ordem_servico (id_cliente, id_veterinario, id_servico, horario_agendamento, relatorio, status) VALUES (?, ?, ?, ?, ?, ?)', ordens_servico)
    
    # 8. Inserir pagamentos
    pagamentos = [
        (1, None, 145.00, '2025-09-20 10:35:00', 'Crédito'),
        (2, None, 70.00, '2025-09-21 14:20:00', 'Débito'),
        (3, None, 165.00, '2025-09-22 09:50:00', 'PIX'),
        (None, 2, 80.00, '2025-10-03 15:00:00', 'Dinheiro'),
        (None, 4, 120.00, '2025-09-28 16:30:00', 'Crédito'),
        (4, None, 53.00, '2025-09-25 16:25:00', 'Débito')
    ]
    cursor.executemany('INSERT INTO pagamento (id_venda, id_ordem_servico, valor_pago, data_pagamento, forma_pagamento) VALUES (?, ?, ?, ?, ?)', pagamentos)
    
    conn.commit()
    conn.close()
    print("✅ Dados de exemplo inseridos com sucesso!")
    print("📊 Resumo:")
    print("   - 6 usuários (2 veterinários, 3 vendedores, 1 admin)")
    print("   - 5 clientes")
    print("   - 10 produtos")
    print("   - 5 serviços")
    print("   - 5 vendas")
    print("   - 5 ordens de serviço")
    print("   - 6 pagamentos")

if __name__ == "__main__":
    inserir_dados_exemplo()