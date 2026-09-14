import mysql.connector
import time
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')
conexao = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
print('Conexão realizada com SUCESSO!')
cursor = conexao.cursor()

# Funções (def)
def pedir_valor():
    while True:
        try:
            valor = float(input('Valor: '))
            if valor > 0:
                break
            else:
                print('\033[4;33;41mO valor deve ser maior que zero!\033[m')
        except ValueError:
            print('\033[4;33;41mValor inválido, digite um valor válido!\033[m')

    return valor
# Adicionar lançamentos.
def adicionar_lancamentos():
    descricao = input('Descrição: ').strip()
    while descricao == '':
        print('\033[4;33;41mAdicione uma descrição:\033[m')
        descricao = input('Descrição: ').strip()

    valor = pedir_valor()

    tipo = input('Tipo (receita/despesa): ').upper().strip()
    while tipo not in ['RECEITA', 'DESPESA']:
        print('\033[4;33;41mTipo inválido, Digite receita ou despesa:\033[m')
        tipo = input('Tipo (receita/despesa): ').upper().strip()

    categoria = input('Categoria: ').strip() 
    while categoria == '':
        print('\033[4;33;41mAdicione uma categoria:\033[m')
        categoria = input('Categoria: ').strip()
# Execução do comando.
    cursor.execute(
    'INSERT INTO lancamentos (descricao, valor, tipo, categoria) VALUES (%s,%s,%s,%s)', (descricao, valor, tipo, categoria)
)   
    conexao.commit()
    print('\033[4;32;40mLançamento adicionado com sucesso!\033[m')

# Listar lançamentos.
def listar_lancamentos():
    cursor.execute(
        'SELECT * FROM lancamentos'
    )
    resultado = cursor.fetchall()
    for lancamentos in resultado:
        print('=' * 20)
        print('LANÇAMENTO')
        print('=' * 20)
        print(f'\nID: {lancamentos[0]}')
        print(f'Descrição: {lancamentos[1]}')
        print(f'Valor: R$ {lancamentos[2]}')
        print(f'Tipo: {lancamentos[3]}')
        print(f'Categoria: {lancamentos[4]}')
        print(f'Data: {lancamentos[5]}\n')

# Ver saldo.
def ver_saldo():
    cursor.execute(
        "SELECT SUM(valor) FROM lancamentos WHERE tipo = 'RECEITA'"
    )
    receita = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(valor) FROM lancamentos WHERE tipo = 'DESPESA'"
    )
    despesa = cursor.fetchone()[0] or 0

    total = receita - despesa
    print (f'Total em receita: R$ {receita}\nTotal em despesas R$ {despesa}\nSaldo restante R$ {total}')

# Excluir dados.
def excluir_lancamentos():
    id = input('Digite o ID do lançamento: ')
    cursor.execute(
        'SELECT ID FROM lancamentos WHERE ID = %s', (id,)
    )
    resultado = cursor.fetchone()
    if resultado is None:
        print('\033[4;33;41mID não encontrado!\033[m')
        return
    confirmacao = input('Tem certeza que deseja excluir? (sim/não): ').lower().strip()
    if confirmacao == 'sim':
        cursor.execute(
            'DELETE FROM lancamentos WHERE ID = %s', (id,)
        )
        conexao.commit()
        print('\033[4;32;40mLançamento excluído com sucesso!\033[m')

# Editar lançamentos.
def editar_lancamentos():
    id = input('Digite o ID de lançamento: ').strip()
    cursor.execute(
    'SELECT * FROM lancamentos WHERE ID = %s', (id,)
)
    resultado = cursor.fetchone()
    if resultado is None:
        print('\033[4;33;41mID não encontrado!\033[m')
        return
    print('===== LANÇAMENTO ATUAL =====')
    print(f'Descrição: {resultado[1]}')
    print(f'Valor: R$ {resultado[2]}')
    print(f'Tipo: {resultado[3]}')
    print(f'Categoria: {resultado[4]}')
    print(f'Data: {resultado[5]}')
    print('============================')

    nova_descricao = input('Nova descrição: ').strip()
    while nova_descricao == '':
        print('\033[4;33;41mAdicione uma descrição:\033[m')
        nova_descricao = input('Nova descrição: ').strip()

    novo_valor = pedir_valor()

    novo_tipo = input('Novo tipo (receita/despesa): ').upper().strip()
    while novo_tipo not in ['RECEITA', 'DESPESA']:
        print('\033[4;33;41mTipo inválido, Digite receita ou despesa:\033[m')
        novo_tipo = input('Novo tipo (receita/despesa): ').upper().strip()

    nova_categoria = input('Nova categoria: ').strip()
    while nova_categoria == '':
        print('\033[4;33;41mAdicione uma categoria:\033[m')
        nova_categoria = input('Nova categoria: ').strip()

    cursor.execute(
        "UPDATE lancamentos SET descricao = %s, valor = %s, tipo = %s, categoria = %s WHERE ID = %s",(nova_descricao, novo_valor, novo_tipo, nova_categoria, id)
    )
    conexao.commit()
    print('\033[4;32;40mLançamento editado com sucesso!\033[m')

# Menu
while True:
    print('\n===== CONTROLE FINANCEIRO =====')
    print('1 - Adicionar lançamentos')
    print('2 - Listar lançamentos')
    print('3 - Listar saldo')
    print('4 - Excluir lançamento')
    print('5 - Editar lançamento')
    print('6 - Sair')

    opcao = input('\nEscolha uma opção: ')
    print()
    if opcao == '1':
        adicionar_lancamentos()
    elif opcao == '2':
        listar_lancamentos()
    elif opcao == '3':
        ver_saldo()
    elif opcao == '4':
        excluir_lancamentos()
    elif opcao == '5':
        editar_lancamentos()
    elif opcao == '6':
        break
    else:
        print('\n\033[4;33;41mOpção inválida!\033[m')
    print('Voltando ao menu...')
    time.sleep(1.5)