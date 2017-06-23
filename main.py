#-*-coding:utf8;-*- apenas no Qpython mobile
lista=""
produtos=[['NOME DO PRODUTO: ','VALIDADE: ','ESTADO: 1-SOLIDO 2-LIQUIDO 3-GASOSO','MASSA(Kg): ','PRECO (EM REAIS POR GRAMA): ']]
medicamentos=[['NOME DO MEDICAMENTO: ','PRINCIPIO ATIVO: ','CONCENTRACAO: ','VALIDADE: ','COMPOSICAO']]
funcionarios=[['NOME: ','SALARIO (EM REAIS): ','MEDICAMENTO: ']]
relatorios=[]
segmento=[]
def menu_principal(lista,segmento):
    print("***** MENU PRINCIPAL *****")
    print("1 - Produtos Químicos")
    print("2 - Medicamentos")
    print("3 - Funcionários")
    print("4 - Relatórios")
    opcao=raw_input("Digite a opção desejada: ")
    if opcao=="1":
        lista='PRODUTO'
        segmento=produtos
        menu_produto(lista,segmento)
    if opcao=="2":
        lista='MEDICAMENTO'
        segmento=medicamentos
        menu_medicamento(lista,segmento)
    if opcao=="3":
        lista='FUNCIONARIO'
        segmento=funcionarios
        menu_funcionario(lista,segmento)
    if opcao=="4":
        lista='RELATORIO'
        segmento=relatorios
        menu_relatorio(lista,segmento)
    menu_principal(lista,segmento)

def menu_produto(lista,segmento):
    print("***** PRODUTOS *****")
    menu_sec(lista,segmento)   
def menu_medicamento(lista,segmento):
    print("***** MEDICAMENTOS *****")
    menu_sec(lista,segmento)         
def menu_funcionario(lista,segmento):
    print("***** FUNCIONÁRIOS *****")
    menu_sec(lista,segmento)      
def menu_relatorio(lista,segmento):
    print("***** RELATÓRIOS *****")
    print("Informa se um quantidade N de unidades comerciais de um dado medicamento pode ser ou nao")
    print("fabricadaconsiderando o a disponibilidade de produtos quımicos necessarios e de funcionarios habilitados")
    print("Informa os produtos quımicos e medicamentos a vencerem nos proximos 10 dias")
    print("Informa qual medicamento possui o maior numero de funcionarios habilitados para sua producao,")
    print("independentemente da existencia de produtos quımicos em estoque.")
    menu_principal(lista,segmento)    
def cadastro(lista,segmento):
    print '***** CADASTRAR - ',lista,' *****'
 
def busca(lista,segmento):
    print '***** BUSCAR - ',lista,' *****'

def atualiza(lista,segmento):
    print '***** ATUALIZAR - ',lista,' *****'
 
def remove(lista,segmento):
    print '***** REMOVER - ',lista,' *****'

def menu_sec(lista,segmento):
    print("1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Atualizar")
    print("4 - Remover")
    opcao_s=raw_input("Digite a opção desejada: ")
    if opcao_s=="1":
        cadastro(segmento)
    if opcao_s=="2":
        busca(lista)
    if opcao_s=="3":
        atualiza(lista)
    if opcao_s=="4":
        remove(lista)
    menu_sec(lista,segmento) 

def cadastro(original):
  add=[]
  referencia=original[0]
  for campo in referencia:
    if campo=='MEDICAMENTO: ':
      med=[]
      qtdHabilidade=input("Qtd de produtos que conhece:  ")
      for i in range(qtdHabilidade):
        tempMedic=raw_input("Digite o nome do medicamento: ")
        med.append(tempMedic)
      add.append(med)
    else:
      x=raw_input(campo)
      add.append(x)
  original.append(add)

menu_principal(lista,segmento)
