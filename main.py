'''codigo hospedado em https://repl.it/JAQr/69´´´´
from datetime import *
'''PROJETO DESENVOLVIDO POR:ADAURI BISPO SILVA, JULLYANE,LUCAS PEREIRA DE SANTANA E MAISE ARAUJO ALVES
  AS DATAS DEVEM SER INSERIDAS NO FORMATO ANO-MES-DATA'''
lista=""
produtos=[['NOME DO PRODUTO: ','VALIDADE: ','ESTADO: 1-SOLIDO 2-LIQUIDO 3-GASOSO','MASSA(Kg): ','PRECO (EM REAIS POR GRAMA): ']]
medicamentos=[['NOME DO MEDICAMENTO: ','PRINCIPIO ATIVO: ','CONCENTRACAO: ','VALIDADE: ','COMPOSICAO']]
funcionarios=[['NOME DO FUNCIONARIO: ','SALARIO (EM REAIS): ','MEDICAMENTO: ']]
composicao=[[]]
relatorios=[]
segmento=[]
top10=[['ITEM','DIAS PARA VENCER']]
Xtop10=[['ITEM','DIAS PARA VENCER']]

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
  print("1 - Producao de Medicamentos")
  print("2 - Medicamentos a Vencer")
  print("3 - Produtos Quimicos a Vencer")
  print("4 - Maximizar Producao do Medicamento")
  print("5 - Voltar")
  opcao_s=raw_input("Digite a opção desejada: ")
  if opcao_s=="1":
    print 'Producao de Medicamentos em implentacacao'
  if opcao_s=="2":
    for remedio in medicamentos:
      if (remedio[0])!='NOME DO PRODUTO: ':
        RelatorioData(remedio[3],remedio[0])
    print top10
    
  if opcao_s=="3":
    for Xremedio in produtos:
      if (Xremedio[0])!='NOME DO PRODUTO: ':
        XRelatorioData(Xremedio[1],Xremedio[0])
    print Xtop10

    
  if opcao_s=="9":
    print 'Produtos Quimicos a Vencer em implementacao'
  if opcao_s=="4":
    print 'Maximizar Producao do Medicamento em implementacao'
  if opcao_s=="5":
    menu_principal(lista,segmento)
  
def menu_sec(lista,segmento):
  print("1 - Cadastrar")
  print("2 - Buscar")
  print("3 - Atualizar")
  print("4 - Remover")
  print("5 - Voltar")
  opcao_s=raw_input("Digite a opção desejada: ")
  if opcao_s=="1":
    cadastro(segmento,lista)
  if opcao_s=="2":
     busca(lista,segmento)
  if opcao_s=="3":
    atualiza(segmento,lista)
  if opcao_s=="4":
    remove(segmento,lista)
  if opcao_s=="5":
    menu_principal(lista,segmento)
  menu_sec(lista,segmento) 

def remove(base,titulo):
  print '***** REMOVER - ',titulo,' *****'
  tempMax=base[0]
  print 'DIGITE O ',tempMax[0],':'
  modificar=raw_input()
  for olhar in base:
    if olhar[0]==modificar:
      base.remove(olhar)
  menu_principal(lista,segmento)


def atualiza(base,titulo):
  print '***** ATUALIZAR - ',titulo,' *****'
  tempMax=base[0]
  print 'DIGITE O ',tempMax[0],':'
  modificar=raw_input()
  for olhar in base:
    tempCelula=[]
    if olhar[0]==modificar:
      base.remove(olhar)
      for h in tempMax:
        if (h=='MEDICAMENTO: '):
          medikit(tempCelula)
        elif (h=='COMPOSICAO'):
          composikit(tempCelula)
        else:
          print 'NOVO VALOR PARA',h,':'
          sky=raw_input()
          tempCelula.append(sky)
      base.append(tempCelula)
  menu_principal(lista,segmento)


def cadastro(original,lista):
  print '***** CADASTRAR - ',lista,' *****'
  add=[]
  referencia=original[0]
  for campo in referencia:
    if (campo=='MEDICAMENTO: '):
      medikit(add)
    elif (campo=='COMPOSICAO'):
      composikit(add)
    else:
      x=raw_input(campo)
      add.append(x)
  original.append(add)
  menu_principal(lista,segmento)

def busca(lista,segmento):
  print '***** BUSCAR - ',lista
  elemento=[]
  elemento=segmento[0]
  print 'DIGITE O ',elemento[0]
  alvo=raw_input()
  for x in segmento:
    cell=[]
    cell=x
    for k in cell:
      if (k==alvo):
        print elemento
        print cell
  menu_principal(lista,segmento)


def medikit(add): 
      simples=[]
      qtdHabilidade=input("Qtd de produtos que conhece:  ")
      for i in range(qtdHabilidade):
        tempMedic=raw_input("Digite o nome do medicamento: ")
        simples.append(tempMedic)
      add.append(simples)

def composikit(add): 
      simpRef=[]
      qtdProdutoQuimico=input("Qtd de produtos quimicos usados:  ")
      for i in range(qtdProdutoQuimico):
        chave=[]
        tempProQui=raw_input("Digite o nome do Produto Quimico: ")
        tempQTDProQui=raw_input("Digite a qtd do Produto Quimico: ")
        chave.append(tempProQui)
        chave.append(tempQTDProQui)
        simpRef.append(chave)
      add.append(simpRef)

def RelatorioData(val,prodMed):
  star=[]
  prazo=0
  formato = '%Y-%m-%d'
  dataConvertida= datetime.strptime(val, formato) 
  data1=date.toordinal(dataConvertida)
  data2=date.toordinal(date.today())
  prazo=data1-data2
  if prazo<=10:
    star.append(prodMed)
    star.append(prazo)
    top10.append(star)

def XRelatorioData(Xval,XprodMed):
  Xstar=[]
  Xprazo=0
  formato = '%Y-%m-%d'
  XdataConvertida= datetime.strptime(Xval, formato) 
  Xdata1=date.toordinal(XdataConvertida)
  Xdata2=date.toordinal(date.today())
  Xprazo=Xdata1-Xdata2
  if Xprazo<=10:
    Xstar.append(XprodMed)
    Xstar.append(Xprazo)
    Xtop10.append(Xstar)


menu_principal(lista,segmento)
