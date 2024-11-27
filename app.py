import tkinter as tk
import pandas as pd
import mysql.connector
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
from dateutil.relativedelta import relativedelta

def conectar_banco():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="sistema_academia"
        )
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None

# Cadastro de Aluno
def cadastrar_aluno():
    def mostrar_preco(event):
        plano_selecionado = combo_plano.get()
        connection = conectar_banco()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT preco FROM planos WHERE nome = %s", (plano_selecionado,))
            resultado = cursor.fetchone()
            if resultado:
                valor_label.config(text=f"Valor: R${resultado[0]}")
            connection.close()

    def salvar_aluno():
        nome = entry_nome.get()
        data_nascimento = entry_data_nascimento.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        plano_selecionado = combo_plano.get()

        # Converter a data para o formato correto (YYYY-MM-DD)
        try:
            data_nascimento_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Aviso", "Data inválida. Use o formato DD/MM/YYYY.")
            return

        # Buscar o plano_id do plano selecionado
        connection = conectar_banco()
        plano_id = None
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM planos WHERE nome = %s", (plano_selecionado,))
            resultado = cursor.fetchone()
            if resultado:
                plano_id = resultado[0]
            connection.close()

        if nome and data_nascimento and telefone and email:
            connection = conectar_banco()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO alunos (nome, data_nascimento, telefone, email, plano_id) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (nome, data_nascimento_formatada, telefone, email, plano_id))
                connection.commit()
                messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
                connection.close()
                janela_cadastro.destroy()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    # Criando a janela de cadastro
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title("Cadastrar Aluno")
    janela_cadastro.geometry('350x300')

    label_nome = tk.Label(janela_cadastro, text="Nome:")
    label_nome.pack()
    entry_nome = tk.Entry(janela_cadastro)
    entry_nome.pack()

    label_nascimento = tk.Label(janela_cadastro, text="Data de Nascimento (DD/MM/YYYY):")
    label_nascimento.pack()
    entry_data_nascimento = tk.Entry(janela_cadastro)
    entry_data_nascimento.pack()

    label_telefone = tk.Label(janela_cadastro, text="Telefone:")
    label_telefone.pack()
    entry_telefone = tk.Entry(janela_cadastro)
    entry_telefone.pack()

    label_email = tk.Label(janela_cadastro, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(janela_cadastro)
    entry_email.pack()

    label_plano = tk.Label(janela_cadastro, text="Plano:")
    label_plano.pack()

    connection = conectar_banco()
    planos = []
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT nome FROM planos")
        planos = [plano[0] for plano in cursor.fetchall()]
        connection.close()

    combo_plano = tk.StringVar()
    combo_plano.set(planos[0] if planos else "Selecione um plano") 
    plano_menu = tk.OptionMenu(janela_cadastro, combo_plano, *planos)
    plano_menu.pack()

    # Exibir o valor do plano selecionado
    valor_label = tk.Label(janela_cadastro, text="Valor: ")
    valor_label.pack()

    plano_menu.bind("<Configure>", mostrar_preco)

    botao_salvar = tk.Button(janela_cadastro, text="Salvar", command=salvar_aluno)
    botao_salvar.pack(pady=10)


# Função para listar alunos
def listar_alunos():
    def pesquisar_alunos():
        # Pegando o texto da pesquisa
        pesquisa = entry_pesquisa.get().lower()

        # Reexecutando a consulta com filtro baseado na pesquisa
        connection = conectar_banco()
        if connection:
            cursor = connection.cursor()
            # Modificando a query para adicionar o filtro de pesquisa
            cursor.execute("""
                SELECT alunos.id, alunos.nome, alunos.telefone, alunos.email, planos.nome, planos.duracao, alunos.data_matricula, alunos.ativo
                FROM alunos
                LEFT JOIN planos ON alunos.plano_id = planos.id
                WHERE LOWER(alunos.nome) LIKE %s
            """, ('%' + pesquisa + '%',))
            registros = cursor.fetchall()

            # Limpando os registros exibidos antes de mostrar os novos resultados
            for widget in frame_itens.winfo_children():
                widget.destroy()

            # Adicionando os registros encontrados
            for i, aluno in enumerate(registros):
                # Recuperando a data de matrícula e a duração do plano
                data_matricula = aluno[6]  # Supondo que a coluna 6 seja a data de matrícula
                duracao_plano = int(aluno[5])  # Duração do plano em meses
                ativo = "Sim" if aluno[7] == 1 else "Não"

                # Verificando se a data de matrícula está no formato correto
                if isinstance(data_matricula, str):
                    try:
                        data_matricula = datetime.strptime(data_matricula, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        # Caso o valor não seja uma data válida, usar uma data padrão ou logar erro
                        print(f"Erro ao converter a data de matrícula: {data_matricula}")
                        data_matricula = datetime.now()  # Usar a data atual como fallback
                
                # Calculando o vencimento
                vencimento = data_matricula + relativedelta(months=+duracao_plano)
                vencimento_formatado = vencimento.strftime("%d/%m/%Y")

                # Exibindo os dados do aluno
                label = tk.Label(frame_itens, text=f"Matricula: {aluno[0]} - Nome: {aluno[1]} - Telefone: {aluno[2]} - Email: {aluno[3]} - Plano: {aluno[4]} - Vencimento: {vencimento_formatado} - Ativo: {ativo}")
                label.pack(anchor="w")

            # Ajustando a área de rolagem do canvas para o novo conteúdo
            frame_itens.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

            connection.close()

    janela_lista = tk.Toplevel()
    janela_lista.title("Listar Alunos")
    janela_lista.geometry("950x400")
    janela_lista.resizable(False, False)

    frame = tk.Frame(janela_lista)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    canvas.config(yscrollcommand=scrollbar.set)

    frame_itens = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_itens, anchor="nw")

    label_pesquisa = tk.Label(janela_lista, text="Pesquisar por nome:")
    label_pesquisa.pack(pady=10)

    entry_pesquisa = tk.Entry(janela_lista)
    entry_pesquisa.pack(fill=tk.X, padx=10)

    botao_pesquisar = tk.Button(janela_lista, text="Pesquisar", command=pesquisar_alunos)
    botao_pesquisar.pack(pady=10)

    connection = conectar_banco()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT alunos.id, alunos.nome, alunos.telefone, alunos.email, planos.nome, planos.duracao, alunos.data_matricula, alunos.ativo
            FROM alunos
            LEFT JOIN planos ON alunos.plano_id = planos.id
        """)

        registros = cursor.fetchall()

        for i, aluno in enumerate(registros):
            # Recuperando a data de matrícula e a duração do plano
            data_matricula = aluno[6]  # Supondo que a coluna 6 seja a data de matrícula
            duracao_plano = int(aluno[5])  # Duração do plano em meses
            ativo = "Sim" if aluno[7] == 1 else "Não"

            # Verificando se a data de matrícula está no formato correto
            if isinstance(data_matricula, str):
                try:
                    data_matricula = datetime.strptime(data_matricula, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    # Caso o valor não seja uma data válida, usar uma data padrão ou logar erro
                    print(f"Erro ao converter a data de matrícula: {data_matricula}")
                    data_matricula = datetime.now()  # Usar a data atual como fallback
            
            # Calculando o vencimento
            vencimento = data_matricula + relativedelta(months=+duracao_plano)
            vencimento_formatado = vencimento.strftime("%d/%m/%Y")

            # Exibindo os dados do aluno
            label = tk.Label(frame_itens, text=f"Matricula: {aluno[0]} - Nome: {aluno[1]} - Telefone: {aluno[2]} - Email: {aluno[3]} - Plano: {aluno[4]} - Vencimento: {vencimento_formatado} - Ativo: {ativo}")
            label.pack(anchor="w")

        connection.close()

    # Ajustando a área de rolagem do canvas
    frame_itens.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# função para editar aluno: 
def editar_aluno():
    def buscar_aluno():
        aluno_id = entry_id.get()
        if aluno_id:
            connection = conectar_banco()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM alunos WHERE id = %s", (aluno_id,))
                aluno = cursor.fetchone()

                if aluno:
                    entry_nome.delete(0, tk.END)
                    entry_nome.insert(0, aluno[1])

                    # Convertendo data de nascimento de string para datetime
                    data_nascimento = aluno[2]  # O índice pode variar dependendo da estrutura
                    if isinstance(data_nascimento, str):
                        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")

                    entry_data_nascimento.delete(0, tk.END)
                    entry_data_nascimento.insert(0, data_nascimento.strftime("%d/%m/%Y"))

                    entry_telefone.delete(0, tk.END)
                    entry_telefone.insert(0, aluno[3])
                    
                    entry_email.delete(0, tk.END)
                    entry_email.insert(0, aluno[4])
                    
                    # Mapeando os planos de ID para os nomes correspondentes
                    planos_map = {1: "Mensal", 2: "Trimestral", 3: "Anual"}
                    plano_nome = planos_map.get(aluno[5], "Desconhecido")  # Se não encontrar, coloca "Desconhecido"
                    plano_id.set(plano_nome)  # Atualiza o plano selecionado

                    # Ativo (verifica se o aluno está ativo ou inativo)
                    if aluno[6] == 1:
                        ativo.set("Ativo")
                    else:
                        ativo.set("Inativo")

                    botao_atualizar.config(state=tk.NORMAL)
                else:
                    messagebox.showwarning("Aviso", "Aluno não encontrado.")
                connection.close()

    def atualizar_aluno():
        aluno_id = entry_id.get()
        nome = entry_nome.get()
        data_nascimento = entry_data_nascimento.get()
        telefone = entry_telefone.get()
        email = entry_email.get()
        plano = plano_id.get()
        ativo_status = ativo.get()

        if aluno_id and nome and telefone and email and data_nascimento and plano and ativo_status:
            connection = conectar_banco()
            if connection:
                cursor = connection.cursor()
                
                # Convertendo data de nascimento para o formato correto
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

                ativo_valor = 1 if ativo_status == "Ativo" else 0

                # Mapeando os planos de nome para os IDs correspondentes
                planos_map = {"Mensal": 1, "Trimestral": 2, "Anual": 3}
                plano_id_valor = planos_map.get(plano, 1)  # Default para "Mensal" (ID 1) se não encontrar

                query = """
                    UPDATE alunos 
                    SET nome = %s, data_nascimento = %s, telefone = %s, email = %s, plano_id = %s, ativo = %s 
                    WHERE id = %s
                """
                cursor.execute(query, (nome, data_nascimento, telefone, email, plano_id_valor, ativo_valor, aluno_id))
                connection.commit()
                messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
                connection.close()
                janela_edicao.destroy()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    # Criando a janela de edição
    janela_edicao = tk.Toplevel()
    janela_edicao.title("Editar Aluno")
    janela_edicao.geometry("300x400")

    label_id = tk.Label(janela_edicao, text="Matricula do Aluno:")
    label_id.pack()
    entry_id = tk.Entry(janela_edicao)
    entry_id.pack()

    botao_buscar = tk.Button(janela_edicao, text="Buscar", command=buscar_aluno)
    botao_buscar.pack(pady=5)

    label_nome = tk.Label(janela_edicao, text="Nome:")
    label_nome.pack()
    entry_nome = tk.Entry(janela_edicao)
    entry_nome.pack()

    label_data_nascimento = tk.Label(janela_edicao, text="Data de Nascimento (DD/MM/AAAA):")
    label_data_nascimento.pack()
    entry_data_nascimento = tk.Entry(janela_edicao)
    entry_data_nascimento.pack()

    label_telefone = tk.Label(janela_edicao, text="Telefone:")
    label_telefone.pack()
    entry_telefone = tk.Entry(janela_edicao)
    entry_telefone.pack()

    label_email = tk.Label(janela_edicao, text="Email:")
    label_email.pack()
    entry_email = tk.Entry(janela_edicao)
    entry_email.pack()

    # Plano (Combobox com planos, com "readonly" para evitar digitação)
    label_plano = tk.Label(janela_edicao, text="Plano:")
    label_plano.pack()
    plano_id = ttk.Combobox(janela_edicao, values=["Mensal", "Trimestral", "Anual"], state="readonly")
    plano_id.pack()

    # Ativo (Combobox com status ativo, com "readonly" para evitar digitação)
    label_ativo = tk.Label(janela_edicao, text="Status do Plano:")
    label_ativo.pack()
    ativo = ttk.Combobox(janela_edicao, values=["Ativo", "Inativo"], state="readonly")
    ativo.pack()

    # Botão para atualizar
    botao_atualizar = tk.Button(janela_edicao, text="Atualizar", command=atualizar_aluno, state=tk.DISABLED)
    botao_atualizar.pack(pady=10)

# Função para excluir aluno
def excluir_aluno():
    def confirmar_exclusao():
        aluno_id = entry_id.get()
        if aluno_id:
            # Exibe uma caixa de confirmação
            resposta = messagebox.askyesno("Confirmação", f"Tem certeza de que deseja excluir o aluno com ID {aluno_id}?")
            if resposta:  # Se o usuário clicar em "Sim"
                connection = conectar_banco()
                if connection:
                    cursor = connection.cursor()
                    cursor.execute("DELETE FROM alunos WHERE id = %s", (aluno_id,))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
                    janela_exclusao.destroy()
            else:
                messagebox.showinfo("Cancelado", "A exclusão foi cancelada.")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira o ID do aluno.")

    # Criando a janela de exclusão
    janela_exclusao = tk.Toplevel()
    janela_exclusao.title("Excluir Aluno")
    janela_exclusao.geometry("350x80")

    label_id = tk.Label(janela_exclusao, text="ID do Aluno:")
    label_id.pack()
    entry_id = tk.Entry(janela_exclusao)
    entry_id.pack()

    botao_confirmar = tk.Button(janela_exclusao, text="Excluir", command=confirmar_exclusao)
    botao_confirmar.pack(pady=10)

def exportar_dados():
    connection = conectar_banco()
    if connection:
        cursor = connection.cursor()
        # Consulta os dados necessários
        cursor.execute("""
            SELECT alunos.id, alunos.nome, alunos.telefone, alunos.email, 
                   planos.nome AS plano, 
                   CASE WHEN alunos.ativo = 1 THEN 'Sim' ELSE 'Não' END AS ativo,
                   alunos.data_matricula
            FROM alunos
            LEFT JOIN planos ON alunos.plano_id = planos.id
        """)
        dados = cursor.fetchall()

        connection.close()
        
        colunas = ["ID", "Nome", "Telefone", "Email", "Plano", "Ativo", "Data de Matrícula"]
        df = pd.DataFrame(dados, columns=colunas)

        # Escolher o local e nome do arquivo
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )

        # Salvar o arquivo CSV
        if file_path:
            df.to_csv(file_path, index=False, encoding="utf-8-sig")
            messagebox.showinfo("Exportação Concluída", f"Dados exportados com sucesso para: {file_path}")


# Painel Principal
def painel_principal():
    frame_principal = tk.Frame(root)
    frame_principal.pack(pady=20)

    btn_cadastrar = tk.Button(frame_principal, text="Cadastrar Aluno", command=cadastrar_aluno, width=20)
    btn_cadastrar.pack(pady=10)

    btn_listar = tk.Button(frame_principal, text="Listar Alunos", command=listar_alunos, width=20)
    btn_listar.pack(pady=10)

    btn_editar = tk.Button(frame_principal, text="Editar Aluno", command=editar_aluno, width=20)
    btn_editar.pack(pady=10)

    btn_excluir = tk.Button(frame_principal, text="Excluir Aluno", command=excluir_aluno, width=20)
    btn_excluir.pack(pady=10)

    botao_exportar = tk.Button(frame_principal, text="Exportar Dados", command=exportar_dados, width=20)
    botao_exportar.pack(pady=10)

root = tk.Tk()
root.title("Sistema de Gestão de Alunos")
root.geometry("380x300")
root.resizable(False, False)
painel_principal()
root.mainloop()