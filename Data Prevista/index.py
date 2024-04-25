import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Função para criar o contrato em PDF
def criar_contrato(data, clausulas, nome_pessoa, naturalidade):
    nome_arquivo = f"contrato_{nome_pessoa}.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=letter)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(120, 720, "EXPRESS CONSULTORIA - CNPJ: 32.615.348/0001-80")
    c.drawString(220, 700, "CONTRATO")
    c.drawString(120, 680, f"Nome: {data['nome']} {data['sobrenome']}")
    c.drawString(120, 660, f"Telefone: {data['telefone']}")
    c.drawString(120, 640, f"Nome do Pai: {data['nome_pai']}")
    c.drawString(120, 620, f"Nome da Mãe: {data['nome_mae']}")
    c.drawString(120, 600, f"RG: {data['rg']}")
    c.drawString(300, 600, f"Naturalidade: {data['dados_crianca']['naturalidade']}")
    c.drawString(120, 580, f"CPF: {data['cpf']}")
    c.drawString(120, 560, f"Data de Nascimento: {data['data_nascimento']}")
    c.drawString(120, 540, "Endereço:")
    c.drawString(120, 520, f"Rua: {data['endereco']['rua']}")
    c.drawString(120, 500, f"CEP: {data['endereco']['cep']}")
    c.drawString(220, 480, "Dados da Criança:")
    c.drawString(120, 460, f"Data prevista de nascimento: {data['dados_crianca']['data_prevista_nascimento']}")

    # Título das cláusulas
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 400, "Cláusulas:")

    # Redefina o tamanho da fonte para as cláusulas
    c.setFont("Helvetica-Bold", 8)

    # Adicione as cláusulas ao contrato com quebra de linha
    y_position = 380  # Defina a posição inicial das cláusulas

    for clausula in clausulas:
        c.drawString(100, y_position, clausula)
        y_position -= 20  # Mude a posição para a próxima linha

    # Adicione espaços para as assinaturas
    c.drawString(100, 50, "Assinatura do Contratante: ____________________________")
    c.drawString(100, 20, "Assinatura do Contratado: ____________________________")

    c.save()

# Função para coletar os dados e chamar a função de criação de contrato
def coletar_dados():
    nome = nome_entry.get()
    telefone = telefone_entry.get()
    nome_pai = nome_pai_entry.get()
    nome_mae = nome_mae_entry.get()
    sobrenome = sobrenome_entry.get()
    rg = rg_entry.get()
    cpf = cpf_entry.get()
    data_nascimento = data_nascimento_entry.get()
    rua = rua_entry.get()
    cep = cep_entry.get()
    naturalidade = naturalidade_entry.get()
    data_nascimento_crianca = data_nascimento_crianca_entry.get()

    # Cláusulas do contrato
    clausulas = [
        "1. O CONTRATADO FARÁ TODO PROCESSO PARA O",
        "CONTRATANTE.",
        "2. O CONTRATANTE PAGARÁ PELOS SERVIÇOS PRESTADOS",
        "30% SE CONCEDIDO.",
        "3. O CONTRATANTE DEVERÁ FORNECER TODOS DOCUMENTOS",
        "NECESSÁRIOS.",
        "4. EM CASO DE DESISTÊNCIA DO PROCESSO EM ANÁLISE",
        "HAVERÁ MULTA DE 600 REAIS.",
        "5. O NÃO PAGAMENTO DO ESCRITÓRIO RESPONDERÁ POR",
        "PROCESSO DE ESTELIONATO, IMPLICANDO NOME NOS ÓRGÃOS DO SPC SERASA.",
        "6. EM CASO DE PAGAMENTO PARCELADO, SE O VALOR SAIR ACIMA DE 50%",
        "A REQUERENTE DEVERÁ PAGAR À VISTA O ESCRITÓRIO.",
        "SE RECEBER MENOS DE 50%, PAGARÁ PARCELADO DE ACORDO COM O VALOR.",
        "DAS PARCELAS. O PAGAMENTO DEVERÁ SER EFETUADO NO DIA COMBINADO",
        "COM JUROS DE 2% DE MORA AO DIA POR ATRASO.",
    ]

    # Verificar se algum dos campos está vazio
    if nome and telefone and nome_pai and nome_mae and sobrenome and rg and cpf and data_nascimento and rua and cep and data_nascimento_crianca and naturalidade:
        data = {
            'nome': nome,
            'telefone': telefone,
            'nome_pai': nome_pai,
            'nome_mae': nome_mae,
            'sobrenome': sobrenome,
            'rg': rg,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'endereco': {
                'rua': rua,
                'cep': cep
            },
            'dados_crianca': {
                'data_prevista_nascimento': data_nascimento_crianca,
                'naturalidade': naturalidade
            }
        }
        criar_contrato(data, clausulas, nome, naturalidade)
    else:
        # Tratar caso algum campo esteja vazio
        print("Preencha todos os campos antes de criar o contrato.")

# Cria uma janela
janela = tk.Tk()
janela.title("Dados da Criança")

cor_rosa = "#FF69B4"
cor_roxa = "#483D8B"
cor_branca = "white"

janela.configure(bg=cor_roxa)

# Estilo para widgets
font_style = ("Inconsolata", 12)

# Personalize a aparência dos widgets com as cores
tk.Label(janela, text="Nome:", font=font_style, bg=cor_roxa).grid(row=0, column=0)
nome_entry = tk.Entry(janela, bg=cor_branca)
nome_entry.grid(row=0, column=1)

# Adicione uma entrada para o telefone
tk.Label(janela, text="Telefone:", font=font_style, bg=cor_roxa).grid(row=13, column=0)
telefone_entry = tk.Entry(janela)
telefone_entry.grid(row=13, column=1)

tk.Label(janela, text="Sobrenome:", font=font_style, bg=cor_roxa).grid(row=2, column=0)
sobrenome_entry = tk.Entry(janela, bg=cor_branca)
sobrenome_entry.grid(row=2, column=1)

tk.Label(janela, text="Nome do Pai:", font=font_style, bg=cor_roxa).grid(row=3, column=0)
nome_pai_entry = tk.Entry(janela, bg=cor_branca)
nome_pai_entry.grid(row=3, column=1)

tk.Label(janela, text="Nome da Mãe:", font=font_style, bg=cor_roxa).grid(row=4, column=0)
nome_mae_entry = tk.Entry(janela, bg=cor_branca)
nome_mae_entry.grid(row=4, column=1)

tk.Label(janela, text="RG:", font=font_style, bg=cor_roxa).grid(row=5, column=0)
rg_entry = tk.Entry(janela)
rg_entry.grid(row=5, column=1)

tk.Label(janela, text="CPF:", font=font_style, bg=cor_roxa).grid(row=6, column=0)
cpf_entry = tk.Entry(janela)
cpf_entry.grid(row=6, column=1)

tk.Label(janela, text="Data de Nascimento:", font=font_style, bg=cor_roxa).grid(row=7, column=0)
data_nascimento_entry = tk.Entry(janela)
data_nascimento_entry.grid(row=7, column=1)

tk.Label(janela, text="Rua:", font=font_style, bg=cor_roxa).grid(row=8, column=0)
rua_entry = tk.Entry(janela)
rua_entry.grid(row=8, column=1)

tk.Label(janela, text="CEP:", font=font_style, bg=cor_roxa).grid(row=9, column=0)
cep_entry = tk.Entry(janela)
cep_entry.grid(row=9, column=1)


# Botão para coletar os dados
coletar_button = tk.Button(janela, text="Criar Contrato", font=font_style, command=coletar_dados, bg="#FF8C00")
coletar_button.grid(row=15, column=0, columnspan=2)

tk.Label(janela, text="Naturalidade:", font=font_style, bg=cor_roxa).grid(row=14, column=0)
naturalidade_entry = tk.Entry(janela)
naturalidade_entry.grid(row=14, column=1)

tk.Label(janela, text="Data prevista de nascimento:", font=font_style, bg=cor_roxa).grid(row=12, column=0)
data_nascimento_crianca_entry = tk.Entry(janela)
data_nascimento_crianca_entry.grid(row=12, column=1)


# Inicia a interface
janela.mainloop()
