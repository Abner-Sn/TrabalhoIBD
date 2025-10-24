import sqlite3

def criar_banco_pawsome():
    # Conectar/criar o banco de dados
    conn = sqlite3.connect('pawsome.db')
    cursor = conn.cursor()
    
    print("🐾 Criando banco de dados Pawsome...")
    
    # 1. Tabela usuario
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        tipo TEXT CHECK(tipo IN ('Administrador', 'Vendedor', 'Veterinario')) NOT NULL
    )
    ''')
    
    # 2. Tabela cliente
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        endereco TEXT,
        email TEXT
    )
    ''')
    
    # 3. Tabela produto
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        quantidade_estoque INTEGER DEFAULT 0,
        categoria TEXT CHECK(categoria IN ('Cães', 'Gatos', 'Pássaros')) NOT NULL
    )
    ''')
    
    # 4. Tabela servico
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS servico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco_base REAL NOT NULL
    )
    ''')
    
    # 5. Tabela venda
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS venda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_vendedor INTEGER NOT NULL,
        data_venda TEXT NOT NULL,
        valor_total REAL NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente (id),
        FOREIGN KEY (id_vendedor) REFERENCES usuario (id)
    )
    ''')
    
    # 6. Tabela itens
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS itens (
        id_venda INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        PRIMARY KEY (id_venda, id_produto),
        FOREIGN KEY (id_venda) REFERENCES venda (id),
        FOREIGN KEY (id_produto) REFERENCES produto (id)
    )
    ''')
    
    # 7. Tabela ordem_servico
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ordem_servico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_veterinario INTEGER NOT NULL,
        id_servico INTEGER NOT NULL,
        horario_agendamento TEXT NOT NULL,
        relatorio TEXT,
        status TEXT CHECK(status IN ('Agendado', 'Em Andamento', 'Concluído')) DEFAULT 'Agendado',
        FOREIGN KEY (id_cliente) REFERENCES cliente (id),
        FOREIGN KEY (id_veterinario) REFERENCES usuario (id),
        FOREIGN KEY (id_servico) REFERENCES servico (id)
    )
    ''')
    
    # 8. Tabela pagamento
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pagamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_venda INTEGER,
        id_ordem_servico INTEGER,
        valor_pago REAL NOT NULL,
        data_pagamento TEXT NOT NULL,
        forma_pagamento TEXT CHECK(forma_pagamento IN ('Crédito', 'Débito', 'Dinheiro', 'PIX')) NOT NULL,
        FOREIGN KEY (id_venda) REFERENCES venda (id),
        FOREIGN KEY (id_ordem_servico) REFERENCES ordem_servico (id),
        CHECK ((id_venda IS NOT NULL) OR (id_ordem_servico IS NOT NULL))
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Banco 'pawsome.db' criado com sucesso!")
    print("📊 Tabelas criadas: usuario, cliente, produto, servico, venda, itens, ordem_servico, pagamento")

if __name__ == "__main__":
    criar_banco_pawsome()