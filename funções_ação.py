from chamar_banco import *


# cadastra novos usuários no sistema
def cadastrar_usuario():

    print("\n=== CADASTRAR USUÁRIO ===")

    # continua perguntando até receber um nome válido
    while True:
        nome = input("\nNome do usuário: ").strip()
        if nome and all(letra.isalpha() or letra.isspace() for letra in nome):
            break
        print("Nome inválido! Use apenas letras.")

    # abre conexão com o banco
    conn = conectar()
    cursor = conn.cursor()

    # busca os departamentos cadastrados
    cursor.execute("SELECT id, nome FROM departamentos")
    departamentos = cursor.fetchall()

    # verifica se há departamentos cadastrados
    if not departamentos:
        print("\nNenhum departamento cadastrado.")
        cursor.close()
        conn.close()
        return

    # exibe lista de departamentos disponíveis
    print("\n=== DEPARTAMENTOS ===")
    for d in departamentos:
        print(f"ID: {d[0]} - {d[1]}")

    # cria lista de IDs válidos
    ids_validos_dep = [d[0] for d in departamentos]

    # continua perguntando até receber ID válido
    while True:
        try:
            id_departamento = int(input("\nID do departamento: "))
            if id_departamento in ids_validos_dep:
                break
            print("ID inválido! Escolha um ID da lista.")
        except ValueError:
            print("Digite apenas números válidos!")

    # insere o usuário no banco
    cursor.execute("""
        INSERT INTO usuarios (nome, departamento_id)
        VALUES (%s, %s)
    """, (nome, id_departamento))

    # salva alterações
    conn.commit()

    print("\nUsuário cadastrado com sucesso!")

    # encerra conexão
    cursor.close()
    conn.close()


# registra novas solicitações no sistema
def registrar_solicitacao():

    print("\n=== ABRIR SOLICITAÇÃO ===")

    # abre conexão com o banco
    conn = conectar()
    cursor = conn.cursor()

    # busca os departamentos cadastrados
    cursor.execute("SELECT id, nome FROM departamentos")
    departamentos = cursor.fetchall()

    # verifica se há departamentos cadastrados
    if not departamentos:
        print("\nNenhum departamento cadastrado.")
        cursor.close()
        conn.close()
        return

    # exibe lista de departamentos para seleção
    print("\n=== DEPARTAMENTOS ===")
    for d in departamentos:
        print(f"ID: {d[0]} - {d[1]}")

    # cria lista de IDs válidos
    ids_validos_dep = [d[0] for d in departamentos]

    # continua perguntando até receber ID válido
    while True:
        try:
            id_departamento = int(input("\nID do seu departamento: "))
            if id_departamento in ids_validos_dep:
                break
            print("ID inválido! Escolha um ID da lista.")
        except ValueError:
            print("Digite apenas números válidos!")

    # busca usuários cadastrados no departamento escolhido
    cursor.execute("""
        SELECT id, nome
        FROM usuarios
        WHERE departamento_id = %s
    """, (id_departamento,))

    usuarios = cursor.fetchall()

    # verifica se há usuários nesse departamento
    if not usuarios:
        print("\nNenhum usuário cadastrado nesse departamento.")
        cursor.close()
        conn.close()
        return

    # exibe usuários do departamento para seleção
    print("\n=== USUÁRIOS DO DEPARTAMENTO ===")
    for u in usuarios:
        print(f"\nID: {u[0]}")
        print(f"Nome: {u[1]}")

    # cria lista de IDs válidos
    ids_validos_usuarios = [u[0] for u in usuarios]

    # continua perguntando até receber ID válido
    while True:
        try:
            id_usuario = int(input("\nID do solicitante: "))
            if id_usuario in ids_validos_usuarios:
                break
            print("ID inválido! Escolha um ID da lista.")
        except ValueError:
            print("Digite apenas números válidos!")

    # busca nome do usuário selecionado
    usuario = next(u for u in usuarios if u[0] == id_usuario)
    nome = usuario[1]

    # continua perguntando até receber uma descrição válida
    while True:
        descricao = input("\nDescreva o problema: ").strip()
        if descricao:
            break
        print("A descrição não pode ficar vazia!")

    # insere a solicitação no banco
    cursor.execute("""
        INSERT INTO solicitacoes
        (nome_solicitante, departamento_id, descricao, status)
        VALUES (%s, %s, %s, 'aberta')
    """, (nome, id_departamento, descricao))

    # salva alterações
    conn.commit()

    print("\nSolicitação registrada com sucesso!")

    # encerra conexão
    cursor.close()
    conn.close()


# encaminha solicitações para técnicos
def encaminhar_solicitacao():

    # abre conexão com o banco
    conn = conectar()
    cursor = conn.cursor()

    print("\n=== SOLICITAÇÕES ABERTAS ===")

    # busca solicitações abertas com nome do departamento
    cursor.execute("""
        SELECT s.id, s.nome_solicitante, d.nome, s.descricao
        FROM solicitacoes s
        JOIN departamentos d ON s.departamento_id = d.id
        WHERE s.status = 'aberta'
    """)

    solicitacoes = cursor.fetchall()

    # verifica se existem solicitações
    if not solicitacoes:

        print("\nNenhuma solicitação aberta.")

        cursor.close()
        conn.close()

        return

    # exibe solicitações encontradas
    for s in solicitacoes:

        print(f"\nID: {s[0]}")
        print(f"Solicitante: {s[1]}")
        print(f"Departamento: {s[2]}")
        print(f"Descrição: {s[3]}")

    # cria lista de IDs válidos
    ids_validos_solicitacoes = [s[0] for s in solicitacoes]

    # continua perguntando até receber ID válido
    while True:

        try:

            id_sol = int(input("\nID da solicitação: "))

            # verifica se o ID existe
            if id_sol in ids_validos_solicitacoes:
                break
            print("ID inválido! Escolha um ID da lista.")
        except ValueError:
            print("Digite apenas números válidos!")

    print("\n=== IMPACTO E DIFICULDADE ===")

    # continua perguntando até receber valor válido
    while True:
        try:
            impacto = int(input("Impacto: (1) Baixo, (2) Médio, (3) Alto: \n"))
            if impacto in [1, 2, 3]:
                break
            print("Valor inválido! Digite 1, 2 ou 3.")
        except ValueError:
            print("Valor inválido! Não são aceitas palavras, digite 1, 2 ou 3.")

    # continua perguntando até receber valor válido
    while True:
        try:
            dificuldade = int(input("Dificuldade: (1) Fácil, (2) Média, (3) Difícil: \n"))
            if dificuldade in [1, 2, 3]:
                break
            print("Valor inválido! Digite 1, 2 ou 3.")
        except ValueError:
            print("Valor inválido! Não são aceitas palavras, digite 1, 2 ou 3.")

    # define prioridade com base na matriz de impacto e dificuldade
    # impacto tem peso maior que dificuldade
    matriz = {
        (1, 1): "Baixa",
        (1, 2): "Baixa",
        (1, 3): "Média",
        (2, 1): "Média",
        (2, 2): "Média",
        (2, 3): "Alta",
        (3, 1): "Alta",
        (3, 2): "Alta",
        (3, 3): "Alta",
    }

    prioridade = matriz[(impacto, dificuldade)]

    # exibe a prioridade calculada
    print(f"\nPrioridade definida: {prioridade}")

    print("\n=== TÉCNICOS DISPONÍVEIS ===")

    # busca técnicos compatíveis com a prioridade
    if prioridade == "Baixa":
        cursor.execute("""
        SELECT id, nome, nivel
        FROM tecnicos
        WHERE nivel = 'junior' or nivel = 'estagiario'
    """)
    elif prioridade == "Média":
        cursor.execute("""
        SELECT id, nome, nivel
        FROM tecnicos
        WHERE nivel = 'pleno' or nivel = 'junior'
    """)
    else:
        cursor.execute("""
        SELECT id, nome, nivel
        FROM tecnicos
        WHERE nivel = 'senior' or nivel = 'pleno'
    """)

    tecnicos = cursor.fetchall()

    # verifica se existem técnicos
    if not tecnicos:

        print("\nNenhum técnico cadastrado.")

        cursor.close()
        conn.close()

        return

    # exibe técnicos encontrados
    for t in tecnicos:

        print(f"\nID: {t[0]}")
        print(f"Técnico: {t[1]}")
        print(f"Nível: {t[2]}")

    # cria lista de IDs válidos
    ids_validos_tecnicos = [t[0] for t in tecnicos]

    # continua perguntando até receber ID válido
    while True:

        try:

            id_tec = int(input("\nID do técnico responsável: "))

            # verifica se o técnico existe
            if id_tec in ids_validos_tecnicos:
                break

            print("ID inválido! Escolha um técnico da lista.")

        except ValueError:

            print("Digite apenas números válidos!")

    # busca o próximo número de atendimento
    cursor.execute("SELECT COALESCE(MAX(num_atendimento), 0) + 1 FROM solicitacoes")
    num_atendimento = cursor.fetchone()[0]

    # atualiza a solicitação com técnico, prioridade e número de atendimento
    cursor.execute("""
        UPDATE solicitacoes
        SET tecnico_id = %s, prioridade = %s, status = 'em andamento', num_atendimento = %s
        WHERE id = %s
    """, (id_tec, prioridade, num_atendimento, id_sol))

    # salva alterações
    conn.commit()

    print("\nSolicitação encaminhada com sucesso!")

    # encerra conexão
    cursor.close()
    conn.close()


# finaliza solicitações em andamento
def concluir_solicitacao():

    # abre conexão com o banco
    conn = conectar()
    cursor = conn.cursor()

    print("\n=== SOLICITAÇÕES EM ANDAMENTO ===")

    # busca solicitações em andamento com nome do técnico e do departamento
    cursor.execute("""
        SELECT s.id, s.num_atendimento, t.nome, d.nome, s.descricao, s.status, s.tecnico_id
        FROM solicitacoes s
        JOIN tecnicos t ON s.tecnico_id = t.id
        JOIN departamentos d ON s.departamento_id = d.id
        WHERE s.status = 'em andamento'
    """)

    solicitacoes = cursor.fetchall()

    # verifica se existem solicitações em andamento
    if not solicitacoes:

        print("\nNenhuma solicitação em andamento.")

        cursor.close()
        conn.close()

        return

    # exibe solicitações encontradas
    for s in solicitacoes:

        print(f"\nNº Atendimento: {s[1]}")
        print(f"Solicitação ID: {s[0]}")
        print(f"Técnico: {s[2]}")
        print(f"Departamento: {s[3]}")
        print(f"Problema: {s[4]}")
        print(f"Status: {s[5]}")

    # cria lista de IDs válidos
    ids_validos = [s[0] for s in solicitacoes]

    # continua perguntando até receber ID válido
    while True:

        try:

            id_solicitacao = int(input("\nID da solicitação: "))

            # verifica se o ID existe
            if id_solicitacao in ids_validos:
                break

            print("ID inválido!")

        except ValueError:

            print("Digite apenas números válidos!")

    # continua perguntando até receber descrição válida
    while True:

        descricao_final = input("\nDescreva a solução aplicada: ").strip()

        # impede descrição vazia
        if descricao_final:
            break

        print("A descrição da solução não pode ficar vazia!")

    # busca o tecnico_id da solicitação selecionada
    solicitacao = next(s for s in solicitacoes if s[0] == id_solicitacao)
    id_tecnico = solicitacao[6]

    # insere no histórico
    cursor.execute("""
        INSERT INTO historico (solicitacao_id, tecnico_id, descricao_final)
        VALUES (%s, %s, %s)
    """, (id_solicitacao, id_tecnico, descricao_final))

    # atualiza status da solicitação para finalizada
    cursor.execute("""
        UPDATE solicitacoes
        SET status = 'finalizada'
        WHERE id = %s
    """, (id_solicitacao,))

    # salva alterações
    conn.commit()

    print("\nSolicitação finalizada com sucesso!")

    # encerra conexão
    cursor.close()
    conn.close()


# exibe estatísticas das solicitações por status
def estatisticas():

    print("\n=== ESTATÍSTICAS ===")
    print("1 - Estatísticas Gerais")
    print("2 - Solicitações em Aberto")
    print("3 - Solicitações em Andamento")
    print("4 - Solicitações Concluídas")
    print("5 - Voltar ao Menu Principal")

    # abre conexão com o banco
    conn = conectar()
    cursor = conn.cursor()

    # busca e exibe solicitações de acordo com o status recebido
    def exibir_solicitacoes(status, titulo):

        cursor.execute("""
            SELECT s.id, s.num_atendimento, s.nome_solicitante, d.nome,
                   s.descricao, s.status, t.nome, s.prioridade
            FROM solicitacoes s
            JOIN departamentos d ON s.departamento_id = d.id
            LEFT JOIN tecnicos t ON s.tecnico_id = t.id
            WHERE s.status = %s
        """, (status,))

        registros = cursor.fetchall()

        print(f"\n=== {titulo} ===")

        # verifica se existem registros
        if not registros:
            print("Nenhuma solicitação encontrada.")
            return

        # exibe registros encontrados
        for s in registros:
            print(f"\nID: {s[0]}")
            if s[1]:
                print(f"Nº Atendimento: {s[1]}")
            print(f"Solicitante: {s[2]}")
            print(f"Departamento: {s[3]}")
            print(f"Descrição: {s[4]}")
            print(f"Status: {s[5]}")
            if s[6]:
                print(f"Técnico: {s[6]}")
            if s[7]:
                print(f"Prioridade: {s[7]}")

    # impede erro ao digitar letra no input
    try:
        escolha = int(input("\nDigite o número da opção desejada: "))
    except ValueError:
        print("Opção inválida!")
        cursor.close()
        conn.close()
        return

    if escolha == 1:

        exibir_solicitacoes('aberta', 'SOLICITAÇÕES EM ABERTO')
        exibir_solicitacoes('em andamento', 'SOLICITAÇÕES EM ANDAMENTO')
        exibir_solicitacoes('finalizada', 'SOLICITAÇÕES CONCLUÍDAS')

    elif escolha == 2:

        exibir_solicitacoes('aberta', 'SOLICITAÇÕES EM ABERTO')

    elif escolha == 3:

        exibir_solicitacoes('em andamento', 'SOLICITAÇÕES EM ANDAMENTO')

    elif escolha == 4:

        exibir_solicitacoes('finalizada', 'SOLICITAÇÕES CONCLUÍDAS')

    elif escolha == 5:

        print("Voltando ao Menu Principal...\n")

    else:

        print("Opção inválida!")

    # encerra conexão
    cursor.close()
    conn.close()


# exibe histórico das solicitações finalizadas
def ver_historico():

    # abre conexão com o banco
    conn = conectar()
    cursor = conn.cursor()

    print("\n=== HISTÓRICO DE SOLICITAÇÕES ===")

    # busca histórico de solicitações com nome do técnico e do departamento
    cursor.execute("""
        SELECT
            h.id,
            s.id,
            s.num_atendimento,
            s.nome_solicitante,
            d.nome,
            t.nome,
            s.descricao,
            h.descricao_final,
            h.data_finalizacao
        FROM historico h
        JOIN solicitacoes s ON h.solicitacao_id = s.id
        JOIN tecnicos t ON h.tecnico_id = t.id
        JOIN departamentos d ON s.departamento_id = d.id
        ORDER BY h.data_finalizacao DESC
    """)

    historico = cursor.fetchall()

    # verifica se existem registros
    if not historico:

        print("\nNenhuma solicitação finalizada.")

        cursor.close()
        conn.close()

        return

    # exibe histórico encontrado
    for h in historico:

        print(f"\nHistórico ID: {h[0]}")
        print(f"Solicitação ID: {h[1]}")
        print(f"Nº Atendimento: {h[2]}")
        print(f"Solicitante: {h[3]}")
        print(f"Departamento: {h[4]}")
        print(f"Técnico responsável: {h[5]}")
        print(f"Problema: {h[6]}")
        print(f"Solução aplicada: {h[7]}")
        print(f"Finalizado em: {h[8]}")

    # encerra conexão
    cursor.close()
    conn.close()
