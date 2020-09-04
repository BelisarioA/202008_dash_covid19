# PRIMEIRA PROPOSTA DE DASH BOARD PARA APRESENTAÇÃO DOS RESULTADOS COVID 19
# ##Pacotes
import os
import pandas as pd
import numpy as np
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#Buscar no drive as planilhas
import gspread
from oauth2client.service_account import ServiceAccountCredentials

##### TESTE COM OS DADOS COVID
    ##  -----  DADOS NO COMPUTADOR  -----  ##
#Localizar arquivo para leitura
# path='/Users/anabelisario/DocumentsA/NumeraDrive/Projetos/COVID19/02Etapa/GitLab/2ageral_etapa_covid19/0-basesDeDados/'
# file='covid_dash.csv'
# treefile='covid_treemap.csv'
# #Ir para diretório com as bases de dados
# os.chdir(path)
# #Base de dados da pesquisa
# db=pd.read_csv(file)
# #Base de dados para o tree map
# db_arvore=pd.read_csv(treefile)

    ##  -----  DADOS NO DRIVE  -----  ##
## Orientações: https://medium.com/@karmennsalim/google-sheets-api-and-python-b45e076836d5
#1. Credenciais para permissão do acesso
jsondict= {
  "type": "service_account",
  "project_id": "dash-covid19",
  "private_key_id": "0ccdffb5feb5c99b3fb0eb8d9026f618cb981cf0",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDkhU7/hUUq7hFs\neotZWxZrD5TNiS/QOoJLYyqVlv6kzK0y0njEollOucWgvc/jLHZe1uxWJBsukOCp\n2KMHlLqvt3BEZE+XCguuuFae+qVvUUN4q91oWIINmpBv6uvFM39TJSrRmdAaMVSU\nnnQR6LNXrVt4wG3zYlwGlq7yGhLT3JRPiAoZJCN6CVOgUQMv+ZU8qvG8c9KycjjV\nbV2HVAoc1NM5LTOcRHDW/X7rHJfbKS321mnTLWAiSs+rTqxQfJO5a/nMVAJ5q8IK\nzS2VRp5f7pviQm1QFIiJAm9sGtxb5cWR9w4/oX1pYTcdc/PzLYq0hxgRuRL1bxEU\naOouhKVRAgMBAAECggEAMSC0qUu0IUTRk53rv8/Mi8MrhR1hXVV6xezBjqvJvlGv\nSX4Ejxds9jcLdOFhpC/emciAQgucmV/1oKYNdHeFw/l+hgF/t9Oly8/e9Woir0IL\n7JEcNg7TFMweEaVyPvCxhoU2xZ1Y5wykZ5gCEYiSp76B6/2IlbqXWKZD4ZH36ro4\nyOSM//5dotT64K/rn1S3GMr4MZLKQ61Bxx9yIniy/eWLCG8T+im9+rO6+ta0SEoE\nnww5M1SbT+ewfWps6g+9ogyE1okqHaa4G11ydJyx9G/DfyUv3nE2nY/rnYk75wk5\nByv5hCIho41VHoOBvhUpMYJZPS1M8K/CYN+6TiH27QKBgQD7NV83tZUFvcWsp2sI\nrJZa+6LXrazFfw7hLc2zewLSpu2lIIkpAC7wvbMvz1Oxk8WzN4Ab+qOvZ2H+J1gW\nrXQQZKJsCMKbAVyKMqSail0Kz11jnt/bAT/aYRG01RMRHUTLWEnVRKwpgsC0htV9\nuEX2zM1mRnpI0FEXukfQDWQVzQKBgQDo4SeJy30ZLiV8hj2xTV3xAa02NOXz0D+N\nmCE6n3EZ1TQUsM1synMU7xBvRJmdYHrzuc/PhyGWhRTF9SB0n1ZgYqAekVwp5m5W\npTRiLsgUO3pwxMdM8AFWFg0rq8dVNUva3IiC7y555TOAV7ZrMLVg4Y0n1rELVGVi\nkR+BIL7JlQKBgF5V/arrCsp8KJaczGoWfeQu6Uk7VE1aWJkhXUUQZc/7lfTT0g5O\nnlITuw2yOwjNqImTxw06w2tkVH1gAwmJG7PoRsJxS7tv+HOBbyUF3sjndHeruv8A\nah01JLQW7DEaH7KJNjjbsBdqnblthRDQOZ3j7SKCRvu/FyTk9IDh9nrlAoGANuHh\nJItNVyLV+MvWPDPEgOjpPk4nJ1ebsq34ns02pWTmmj20m//2MSfKEr7zCPDU6R2Q\nSRNKqiOA6spDNNjcTWjQ3YNaWhGRTWAvwTfPNV1zFKJ7abliRzx5LCKWnpEp6FFy\n5pChvl5yzbteJVLcXBGr54ikPsxL/HfBGfhyniUCgYEAm31KJrdcN4ojNVmXDRrR\nkd/hPhI4a4ixM4oNffU9R9/Qk5G1YawTZ/Ejhxm/0ZcOA79EulGIO6kIu5DnmFqM\nqF5YJKBX2fqSpjqubyGtp2qvQhsNVMazMM5AKLjO+khF2627d9WKQF7opwL39Qn6\nLUJ9R/vW8LCl1zJaXEuZ3+0=\n-----END PRIVATE KEY-----\n",
  "client_email": "dashcovid@dash-covid19.iam.gserviceaccount.com",
  "client_id": "100245555640992194069",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/dashcovid%40dash-covid19.iam.gserviceaccount.com"
}
#2. Define the scope and create credentials using that scope and the content of '.json' file, correspondent to API project.
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#3. Create a gspread client authorizing it using those credentials.
creds = ServiceAccountCredentials.from_json_keyfile_dict(jsondict, scope)
client = gspread.authorize(creds)

#4. Access google sheets -> call a client.open and pass it the spreadsheet name and getting access to sheet1
file = client.open('covid_dash_fase2').sheet1
treefile=client.open('covid_treemap_fase2').sheet1
#5. variable equal to all of the records inside that sheet and print them out to the terminal
db = file.get_all_records()  #Base de dados da pesquisa
db_arvore = treefile.get_all_records()  #Base de dados para o tree map
#Converter em dataframe
db=pd.DataFrame.from_dict(db)
db_arvore=pd.DataFrame.from_dict(db_arvore)

## Conversão de object para float, nas colunas necessárias
for i in db.columns:
    try:
        db[i]=pd.to_numeric(db[i])
    except:
        pass
for i in db_arvore.columns:
    try:
        db_arvore[i]=pd.to_numeric(db_arvore[i])
    except:
        pass

    ##  -----  INÍCIO DO CÓDIGO  -----  ##

#Cores numera - padrão
color3=['#5288db', '#d3d3d3', '#4D5C73']
colors= ['#5288DB','#90ACE0','#d3d3d3','#807f7f','#4d4d4d'] #,'#497ac5','#000000' #azul, azul claro, cinza claro, cinza medio, cinza escuro, azul escuro, preto
colors= ["#4d4d4d","#5288DB","#d3d3d3","white","#000000"] #azul, cinza escuro, cinza claro, branco, preto
color7=['#497ac5','#5288DB','#90ACE0','#d3d3d3','#807f7f','#4d4d4d','#000000']

# Categorias média satisfação, engajamento e produtividade - escalas Likert
cat_lprod=['muito pouco produtiva','pouco produtiva','neutra','produtiva','muito produtiva']
cat_lengaj=['muito pouco engajada','pouco engajada','neutra','engajada','muito engajada']
cat_lsatisf=['muito pouco satisfeita','pouco satisfeita','neutra','satisfeita','muito satisfeita']
catl_bestar=['muito pouco satisfeita','pouco satisfeita','neutra','satisfeita','muito satisfeita']
prodautoav=['indisponível','negativamente','neutra','positivamente']
satisfautoav=['indisponível','insatisfeita', 'neutra', 'satisfeita']

#Listas dos filtros
generos = ['feminino', 'masculino']
idades=['25 anos ou menos','entre 26 e 34 anos','entre 35 e 44 anos','entre 45 e 54 anos','55 anos ou mais']
filhos=['sim','não']
tempo_hoffice=['não estou de home office','há menos de 1 mês','entre 1 e 2 meses', 'entre 2 e 3 meses', 'entre 3 e 4 meses','há mais de 4 meses']

#Listas das variáveis categóricas
tamanhoempresa=['não informado','2-10','11-50','51-200','201-500','501-1.000','1.001-5.000','5.001-10.000','mais de 10.001']
estadocivil=['não quero declarar','solteira/o','casada/o','divorciada/o ou separada/o','viúva/o']

#Dicionário de construtos (para a aba de correlações)
dic_construtos={'interação com colegas': ['interação com colegas','reflete a eficiência da interação e da comunicação entre colegas de trabalho.'],
                'interação com lider': ['interação com lider','reflete a eficiência da interação e da comunicação entre o indivíduo e a liderança direta.'],
                'produtividade do time na<br>percepção do gestor': ['produtividade do time na percepção do gestor','reflete percepções do gestor sobre a produtividade de seus colaboradores diretos.'],
                'segurança': ['segurança','indica o quanto o indivíduo se sente seguro e estável em seu trabalho.'],
                'equilíbrio: vida pessoal e<br>vida profissional': ['equilíbrio: vida pessoal e vida profissional','percepção individual da habilidade de separar e estabelecer limites entre a vida pessoal e o trabalho.'],
                'bem estar': ['bem estar','um estado emocional positivo e prazeroso que resulta da avaliação que alguém faz sobre uma determinada experiência.'],
                'satisfação com<br>home office': ['satisfação com home office','reflete a satisfação individual com o trabalho remoto, tendo em vista seus pontos positivos e negativos.'],
                'engajamento': ['engajamento','sentimento de que existe conexão entre o colaborador e a organização e de que existe uma noção de pertencimento à cultura da organização.'],
                'percepção de<br>produtividade individual':['percepção de produtividade individual','percepção de entrega dos mesmos resultados (quantidade e qualidade) comparado com antes da quarentena, considerando o mesmo recurso de tempo.']}

#Filtro Slider: Faixa etária 
idadeslider={#1:{'label':'n.i.*','style': {'fontSize': '12px'}}, #-> obs: no caso, todos os respondentes informaram a idade
            1:{'label':'18','style': {'fontSize': '12px'}},
            2:{'label':'25','style': {'fontSize': '12px'}},
            3:{'label':'35','style': {'fontSize': '12px'}},
            4:{'label':'45','style': {'fontSize': '12px'}},
            5:{'label':'55','style': {'fontSize': '12px'}},
            6:{'label':'+55','style': {'fontSize': '12px'}}}
#Filtro Slider: Tempo em home office
tempohofslider={1:{'label':'n.d.','style': {'fontSize': '12px'}},
                2:{'label':'0','style': {'fontSize': '12px'}},
                3:{'label':'1','style': {'fontSize': '12px'}},
                4:{'label':'2','style': {'fontSize': '12px'}},
                5:{'label':'3','style': {'fontSize': '12px'}},
                6:{'label':'4','style': {'fontSize': '12px'}},
                7:{'label':'+4','style': {'fontSize': '12px'}}}

#   FUNÇÕES PARA CRIAÇÃO DOS GRÁFICOS DE BARRAS, COM FILTRO
## FUNÇÃO: CONSTRUÇÃO DAS TABELAS, CONSIDERANDO QUE SERÃO UTILIZADOS TODOS OS FILTROS PARA A CONSTRUÇÃO DOS GRÁFICOS
def gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof):
    tabela=db.groupby(coluna).size()
    tabela=tabela.reindex(niveis)
    tabela.name='todas as respostas'
    percentual=tabela/tabela.sum()
    percentual.name='percentual total'
    tabela_final=tabela.to_frame().join(percentual.to_frame())

    #Aplicação dos filtros - base de dados filtrada
    dbf=db[db['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    db_f1=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))].copy()

    #Adicionar as colunas considerando o filtro
    tabela_final['respostas filtradas']=db_f1.groupby(coluna).size()
    tabela_final['percentual filtrado']=tabela_final['respostas filtradas']/tabela_final['respostas filtradas'].sum()
    tabela_final=tabela_final.fillna(0)
    tabela_final
    
    return tabela_final

#FUNÇÃO: CRIAÇÃO DO GRÁFICO DE BARRAS A PARTIR DA TABELA GERADA POR OUTRA FUNÇÃO
def grafico_barra_comparacao(tabela,titulo,rotulo='auto',n_respondentes=[]):
    # if rotulo != 'auto':
    #     cor='#4d4d4d'
    # else: 
    #     cor='white'
    fig = go.Figure(data=[go.Bar(
                x=tabela['percentual total'],#['percentual total'], -> se é colocado o percentual total, o hover fica melhor, mas as barras ficam em escalas diferentes
                y=tabela.index,
                name='respostas completas',
                text=tabela['percentual total'].apply(lambda x: "{0:.1f}%".format(x*100)), #tabela['percentual total'].values,
                textposition=rotulo,
                orientation='h',
                # textfont={'color':cor},
                hoverinfo='skip'), #hovertemplate='%{x:.1%}', hoverinfo='all'),
                         go.Bar(
                x=tabela['percentual filtrado'],
                y=tabela.index,
                name='respostas filtradas',
                text=tabela['percentual filtrado'].apply(lambda x: "{0:.1f}%".format(x*100)), #tabela['percentual filtrado'].values,
                textposition=rotulo,
                orientation='h',
                # textfont={'color':cor},
                hoverinfo='skip')])

    if n_respondentes==[]:
        fig.update_layout(
                           barmode='group',bargap=0.15
                          ,annotations=[dict(text='número de respondentes <br> respostas completas: '+str(int(tabela.sum()[0]))+
                                                 '<br> respostas filtradas: '+str(int(tabela.sum()[2]))
                                             ,font_size=12,showarrow=False
                                             ,x=1.0,y=-0.03,xref='paper',yref='paper')]

                         ,yaxis={'title':' ','showgrid':False,'zeroline':True,'zerolinecolor':'#4d4d4d'}
                         ,xaxis={'showgrid':False,'visible':False,'zeroline':True,'zerolinecolor':'#4d4d4d'}
                         ,plot_bgcolor='white'
                         ,colorway=colors
                         ,showlegend=False
                         ,margin=dict(t=0,pad=5,r=5,b=15)
                         ,font=dict(color='#4d4d4d')
                         )
    else:
        fig.update_layout(
                       barmode='group',bargap=0.15
                      ,annotations=[dict(text='número de respondentes <br> respostas completas: '+str(n_respondentes[0])+
                                             '<br> respostas filtradas: '+str(n_respondentes[1])
                                         ,font_size=12,showarrow=False
                                         ,x=1.0,y=-0.03,xref='paper',yref='paper')]
                      
                     ,yaxis={'title':' ','showgrid':False,'zeroline':True,'zerolinecolor':'#4d4d4d'}
                     ,xaxis={'showgrid':False,'visible':False,'zeroline':True,'zerolinecolor':'#4d4d4d'}
                     ,plot_bgcolor='white'
                     ,colorway=colors
                     ,showlegend=False
                     ,margin=dict(t=0,pad=5,r=5,b=15)
                     ,font=dict(color='#4d4d4d')
                     )
    fig.add_shape(
                dict(type='rect', x0=0,x1=0,y0=-0.5,y1=len(tabela.index)-0.5,
                line=dict(color='#4d4d4d',width=0.5))
    )

    return fig

### --- ### --- ### --- ###
### INÍCIO DASH BOARD
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.YETI], suppress_callback_exceptions=True)
server = app.server
# Variáveis: filtro e conteúdo das abas
# Filtro para todas as abas
filtros = html.Div([
    #Filtros
    html.Div(children=[
    # Título
        html.Div(
            children=[
                    html.H4(
                        children='FILTROS DE SELEÇÃO',
                        style = dict(textAlign = 'center',
                        marginTop = "20px",
                        marginBottom="0px",
                        paddingBottom='0px')
                    ),
        ],className='titulo-area'),
    # Linhas com filtros
    #Filtro 1: Gênero
        html.Div([
            html.Div([
                html.P(
                children='gênero',
                style = dict(textAlign = 'center'),
                )
            ],className='titulo-filtro'),

            html.Div([
                dbc.Checklist(id = 'filtro_genero', 
                    options=[
                            {'label': i, 'value': i} for i in generos],
                    value=generos,
                    switch=True, 
                    inline=True,
                    style = dict(textAlign = 'center',
                            marginLeft=27,
                            marginRight=27),#dict(t=0,b=0,r=40,l=40)),
                    className='check-list',
                    inputClassName='input-check',
                )
            ],className='filtro-geral'),
        ],id='primeiro-filtro',
        className='filtro-mais-titulo',
        ),

        html.Br(),
    #Filtro 2: Faixa Etária
        html.Div([
            html.Div([
                html.P(
                children='faixa etária',
                style = dict(textAlign = 'center')
                )
            ],className='titulo-filtro'),
            html.Div([
                dcc.RangeSlider(id = 'filtro_idade',
                    marks=idadeslider,
                    min=1,
                    max=6,
                    value=[1,6],
                    step=None,
                    pushable=1
                ) ,
            ],className='filtro-geral'),
            # html.P(children='*n.a.: não informado', className='asterisco-ni')
        ],className='filtro-mais-titulo',
        ),

        html.Br(),
    #Filtro 3: Filhos
        html.Div([
            html.Div([
                html.P(
                children='mora com filhos?',
                style = dict(textAlign = 'center')
            )],className='titulo-filtro'),

            html.Div([
                dbc.Checklist(id = 'filtro_filhos',
                    options=[
                            {'label': i, 'value': i} for i in filhos],
                    value=filhos, 
                    switch=True,
                    inline=True,
                    style = dict(textAlign = 'center',
                            marginLeft=27,
                            marginRight=27),
                    className='check-list',
                    inputClassName='input-check', 
                )
            ],className='filtro-geral'),
        ],className='filtro-mais-titulo',
        ),

        html.Br(),
    #Filtro 4: Tempo em home office
        html.Div([
            html.Div([
                html.P(
                children='tempo em home office (em meses)',
                style = dict(textAlign = 'center')
                )
            ],className='titulo-filtro'),

            html.Div([
                dcc.RangeSlider(id = 'filtro_thof',
                    marks=tempohofslider,
                    min=1,
                    max=7,
                    value=[1,7],
                    step=None,
                    vertical=False,
                    pushable=1
                ),
                html.P(children='*n.d.: não estão de home office', className='asterisco-ni')
            ],className='filtro-geral'),
        ],className='filtro-mais-titulo',
        ),

        html.Br(),
    #Legenda dos gráficos - cores
        html.Div(children=[
            html.Div([
                    html.P(
                    children='legenda',
                    style = dict(textAlign = 'center'),
                    )
                ],className='titulo-filtro'),
            html.Div(children=[
                html.Div(children=[
                    html.Span(
                        style={'backgroundColor':colors[0]},
                        className='legenda-1'),
                    html.P('pesquisa completa')
                    ],className='grupo-legenda'),
                html.Div(children=[
                    html.Span(
                        style={'backgroundColor':colors[1]},
                        className='legenda-1'),
                    html.P('respostas filtradas')
                    ],className='grupo-legenda'),
                ],className='container-legenda')
        ],
        className='filtro-mais-titulo',),
    # Criar botão para resetar os valores iniciais
        html.Div([
            dbc.Button(
                children=['reiniciar valores'],
                id='botao_reset',
                className='botao-reset',
                color='primary',
                outline=True
            )
        ],className='botao-filtros'
        ),
        html.Br(),
        #Container para ver o slider Idade
        html.Div([html.Pre(id='container')], style={'width':'30%', 'float':'right'}),
    ], 
    className='conjunto-filtro',
    ),
    # Botão para ver os resultados da primeira fase da pesquisa
    html.Div([
        dbc.Button(children=['clique aqui para rever os resultados da primeira fase da pesquisa'],
            id='botao_pesquisa',
            className='botao-pesquisa',
            color= 'primary',
            outline=False,
            block=True,
            href='https://numera-covid.herokuapp.com/',
            target='_blank'
        )
    ],className='botao-pesquisa1'
    ),
],className='lateral')

# CONTAINER PARA VER O Slider
@app.callback(
    Output('container','children'),
    [Input('correlacao','clickData')])
def imprimir_click(var_interesse):
    #return html.Div([idadefiltro])
    print(var_interesse)

# Primira aba
tab1_content = html.Div(children=[
    # Título
        html.Div(
            children=[
                html.H5(children=
                'distribuição demográfica dos respondentes da pesquisa'),
                html.H6(children= 
                'comparação de todos os respondentes com as respostas selecionadas de acordo com os filtros aplicados')]
            ,className='titulo-tab1',
            style = dict(marginBottom = '15px')
        ),
    # Estrutura
    # Primeira linha de gráficos - cartões gênero
    # Cartão 1: GÊNERO FEMININO
        html.Div([
            dbc.Card(
                [dbc.CardHeader("feminino",
                className='card-header'),
                dbc.CardBody([
                    html.Div(id='card_feminino', className="card-title"),
                    ],className="card-0"
                ),
                ],className='card'
            )
        ],className='container-card0',
        ),
    # Cartão 2: GÊNERO MASCULINO
        html.Div([
            dbc.Card(
                [dbc.CardHeader("masculino",
                className='card-header'),
                dbc.CardBody(
                    [html.Div(id='card_masculino', className="card-title"),
                    ],className="card-0",
                ),
                ],className='card'
            )
        ],className='container-card1',
        ),
    # Cartão 3: MORAR COM FILHOS: SIM
        html.Div([
            dbc.Card(
                    [dbc.CardHeader("mora com filhos",
                    className='card-header'),
                    dbc.CardBody(
                        [html.Div(id='card_filhosim', className="card-title")
                        ],className="card-0"
                    ),
                    ],className='card'
                )
        ],className='container-card2',
        ),
    # Cartão 4: MORAR COM FILHOS: NÃO
        html.Div([
            dbc.Card(
                    [dbc.CardHeader("não mora com filhos",
                    className='card-header'),
                    dbc.CardBody(
                        [html.Div(id='card_filhonao', className="card-title")
                        ],className="card-0"
                    ),
                    ],className='card'
                )
        ],className='container-card3',
        ),
    # Segunda linha de gráficos: histograma
    # Gráfico1: histograma faixa etária
            html.Div([
                html.P(
                children='distribuição da idade',
                style = dict(textAlign = 'center',fontColor='#4d4d4d'),
                ),
                dcc.Graph(id='idade')
            ],
            className='idade graficos',#,style=dict(display='flex-direction', alignItem='center'),
            ),
        #Terceira linha de gráficos
        # Gráfico2: tempo em home office
            html.Div([
                html.P(
                    children='tempo em home office',
                    style = dict(textAlign = 'center'),
                    ),
                dcc.Graph(id='tempo_hof')
            ],
            className='tempo_hof graficos',
            ),
        # Quarta linha de gráficos
        # Gráfico3: estado civil
            html.Div([
                html.P(
                    children='estado civil',
                    style = dict(textAlign = 'center'),
                    ), 
                dcc.Graph(id='estadoCivil')
            ], 
            className='estado_civil graficos',
            ),
        # Gráfico4: tamanho das empresas
            # html.Div([
            #     html.P(
            #         children=['tamanho da empresa'],
            #         style = dict(textAlign = 'center'),
            #         ),
            #     dcc.Graph(id='tamanhoempresa')
            # ],
            # className='tamanho-empresa graficos',
            # ),
    ],
    className='tab1-content')

# Segunda aba
tab2_content = html.Div(children=[
                #Título
                html.Div(
                    children=[
                        html.H5(children=[
                        'sentimento dos respondentes quanto aos aspectos relacionados ao trabalho em meio a pandemia']),
                        html.H6(children= 
                        'percepção de produtividade, engajamento e satisfação com trabalho remoto foram avaliados por meio de perguntas indiretas'),
                        ]
                ,className='titulo-tab',
                    style = dict(marginBottom = '15px')
                ),
                #Estrutura
                html.Div([
                    html.P(['produtividade é resultado da capacidade de produzir, de gerar um produto, fruto do trabalho, associado à técnica e ao capital empregado'],
                    ),
                    dcc.Graph(id='prodLikert'),
                ],className='prod-likert graficos',
                ),
                html.Div([
                    html.P(['engajamento do colaborador se apresenta através do envolvimento psicológico, físico e cognitivo com o trabalho'],
                    ),
                    dcc.Graph(id='engajamentoLikert'),
                ],className='engaj-likert graficos',
                ),
                html.Div([
                    html.P(children=['satisfação dos respondentes com relação ao trabalho remoto',
                        html.Br([]),
                        html.Span(['aplicado apenas às pessoas que estão integral ou parcialmente em home office'],style=dict(fontSize='10px'))]),
                    dcc.Graph(id='satisfacaoLikert'),
                ],className='satisf-likert graficos',
                ),
                html.Div([
                    html.P(['médias dos respondentes para cada esfera abordada na pesquisa',
                        html.Br([]),
                        html.Span(['definições apresentadas na aba "correlações"'],style=dict(fontSize='10px'))]
                    ),
                    dcc.Graph(id='mediasLikert'),
                ],className='medias-likert graficos',
                ),
            ],
            className='tab2-content')

# Terceira aba
tab3_content = html.Div(children=[
                # Título
                html.Div(
                    children=[
                        html.H5(children=
                        'influência da quarentena sobre a percepção de produtividade dos respondentes'),
                        html.H6(children= 
                        'a percepção de mudanças na produtividade e seus motivos foram avaliados através de perguntas diretas')]
                ,className='titulo-tab',
                    style = dict(marginBottom = '15px')
                ),
                html.Div([
                    html.P(['clique para explorar os motivos']), # que afetam a produtividade
                    html.Span(html.Img(src = "https://imagizer.imageshack.com/img923/1116/887us6.png", id = 'img-observacao'))
                    ], className='observacao'),
                # Estrutura
                html.Div([
                    # Cartão : PERCEPÇÃO DE PRODUTIVIDADE AFETADA: SIM/NÃO
                    html.Div(
                        id='card_produtividadeSN'
                    ),
                ], className='tree-simnao grafico-prod'),
                html.Div([
                    html.Div([
                        dcc.Graph(id='treemap'),
                    ]),
                ],className='tree-map grafico-prod'),
            ],
            className='tab3-content')

# Quarta aba
tab4_content = html.Div(children=[
                # Título
                html.Div(
                    children=[
                        html.H5(children=
                        'satisfação dos respondentes quanto à política de home office'),
                        html.H6(children= 
                        'a satisfação e os aspectos que os respondentes mais gostam e que menos gostam foram avaliados por meio de perguntas diretas')]
                ,className='titulo-tab4',
                    style = dict(marginBottom = '15px')
                ),
                html.Div([
                    html.P(['clique para explorar os motivos']), # que afetam a produtividade
                    html.Span(html.Img(src = "https://imagizer.imageshack.com/img923/1116/887us6.png", id = 'img-observacao'))
                    ], className='observacao-satisf'),
                # Estrutura
                html.Div([
                    # Cartão : PERCEPÇÃO DE PRODUTIVIDADE AFETADA: SIM/NÃO
                    html.Div(
                        id='card_satisfacao'
                    ),
                ], className='tree-simnao grafico-satisf'),
                html.Div([
                    html.Div([
                        dcc.Graph(id='treemap-satisf'),
                    ]),
                ],className='tree-map grafico-satisf'),
            ],
            className='tab4-content')

# Quinta aba
tab5_content = html.Div(children=[
                # Título
                html.Div(
                    children=[
                        html.H5(children=
                        'correlação linear entre os aspectos investigados'),
                        html.H6(children= 
                        'a correlação pode variar entre -1 (tendências opostas) e 1 (tendências similares), sendo que quanto mais próximo de zero menor é o grau de relação')]
                ,className='titulo-tab',
                    style = dict(marginBottom = '15px')
                ),
                # Estrutura
                #G0: Gráfico de Correlações
                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Graph(
                                id='correlacao',
                                clickData={'points':[{'x':'engajamento','y':'percepção de<br>produtividade individual'}]},
                            ),]),
                        html.Div([
                            html.A(children=html.P(['sugestão de leitura:',html.Br(),'aprofundamento em gráficos de correlação']),#,html.Br(),' \"Uma ferramenta simples para direcionar',html.Br(),'e fortalecer suas análises\"']),
                            href = 'https://www.numerapeopleanalytics.com/blog/tutorial-matriz-de-correlao',
                            target='_blank'),
                            ],className='comentario-link'),
                    ],
                    className='correlacao',
                    ),
                    html.Div([
                            html.H5('clique nas correlações para verificar os conceitos',id='aspectos'),
                        html.Div(id='primeiro-construto'
                                ,className='t-construto'),
                        html.Div(id='segundo-construto'
                                ,className='t-construto')
                    ],className='construtos'),
                ],className='correlacao-construtos'),
                # Título
                html.Div(
                    children=[
                        html.H5(children=
                        'regressão linear'),
                        html.H6(children= 
                        'clique nas correlações do gráfico acima para investigar a relação entre os aspectos selecionados')]
                ,className='titulo-tab',
                    style = dict(marginBottom = '15px')
                ),
                #G1: Gráfico dependente das correlações - dispersão
                html.Div([
                    dcc.Graph(
                        id='dispersao',
                        clickData={'points':[{'x':'engajamento','y':'percepção de<br>produtividade individual'}]}
                    ),
                ],
                className='dispersao'
                ),
            ],
            className='tab5-content')

# titulo da aba
app.title = 'pesquisa covid-19 segunda fase'                  
# Esqueleto da página
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
# CAPA
capa = html.Div([
    # Imagem da capa está colocada no css
    html.Div([
        html.Div(children=[
            html.H4(['Pesquisa COVID-19',html.Br()]),
            html.Br(),
            html.H5('SEGUNDA FASE'),
            html.Br(),
            html.Br(),
            html.P(['MUDANÇAS NO TRABALHO EM ÉPOCA',html.Br(),'DE DISTANCIAMENTO SOCIAL']),
        ]),
        html.Br(),
        html.Br(),
        dbc.Button(
            ['clique para',html.Br(),'explorar os resultados'], 
            href='/covid19-fase2',
            className='botao-conteudo',
            ),
        # html.Div(children=[
        #     html.H6(['*pesquisa desenvolvida pela numera com apoio da especialista em psicometria Ana Crispim'])])
    ],className='ir-conteudo'
    ),
])
# CONTEÚDO - FASE 2
conteudo = html.Div([
    #Navbar
        dbc.Navbar(
            [html.Div(
                [html.A(html.Img(
                    src = 'http://static1.squarespace.com/static/5b04780f75f9ee0e09a28d07/t/5b047d026d2a73a2f0b7392c/1527020806867/Logo_basic.png?format=1500w', 
                    height =  '30px'),
                    href = 'https://www.numerapeopleanalytics.com/',
                    target='_blank',
                    className='image-logo'
                )],className='logo'),
            html.Div([
                dbc.NavbarBrand(children=
                [html.H3(['PESQUISA COVID-19 | FASE 2'],className='texto-titulo-navbar')])
                ],className='titulo-navbar'),
            # html.Div([
            #     dbc.Button(children=['clique aqui para rever os resultados da primeira fase da pesquisa'],
            #         id='botao_pesquisa',
            #         className='botao-pesquisa',
            #         color= 'primary',
            #         outline=False,
            #         block=True,
            #         href='https://numera-covid.herokuapp.com/',
            #         target='_blank'
            #     )
            # ],className='botao-pesquisa1'
            # ),
            ],className='navbar'
        ),
    # Informações
        html.Div([
         #filtro
            html.Div(
                children=[filtros]),
                #className='col-3'),
            
        #Layout com abas
            html.Div([
            #Abas
                dcc.Tabs(id='tabs-geral',#value='tab0',
                children=[
            #Primeira Tab: tab0
                    dcc.Tab(label='demografias',id='tab0',
                    children = [tab1_content],
                    className='custom-tab'
                    ),
            #Segunda Tab: tab1
                    dcc.Tab(label='relações com trabalho na pandemia',id='tab1',
                    children = [tab2_content],
                    className='custom-tab'
                    ),
            #Terceira Tab: tab2
                    dcc.Tab(label='impactos na produtividade',id='tab2',
                    children = [tab3_content],
                    className='custom-tab'
                    ),
            #Quarta Tab: tab3
                    dcc.Tab(label='satisfação com trabalho remoto',id='tab3',
                    children = [tab4_content],
                    className='custom-tab'
                    ),
            #Quinta Tab: tab4
                    dcc.Tab(label='correlações',id='tab4',
                    children = [tab5_content],
                    className='custom-tab'
                    ),
                    ]),
            ]),#,className='col-9'),
            html.Div(id='tabs-content-inline')
        ],className='dash-completo')
])
        
#REINICIAR
#Tab0  Botão Reiniciar
@app.callback(
    Output('filtro_genero','value'),
    [Input('botao_reset','n_clicks')])
def update_filtro_genero(reinicia):
    return generos
@app.callback(
    Output('filtro_idade','value'),
    [Input('botao_reset','n_clicks')])
def update_filtro_idade(reinicia):
    return [1,6]
@app.callback(
    Output('filtro_filhos','value'),
    [Input('botao_reset','n_clicks')])
def update_filtro_filhos(reinicia):
    return filhos
@app.callback(
    Output('filtro_thof','value'),
    [Input('botao_reset','n_clicks')])
def update_filtro_thof(reinicia):
    return [1,7]

### PRIMEIRA ABA
## CONSTRUÇÃO DOS GRÁFICOS
#Tab0 Card 0 - todos filtros - cartão genero
@app.callback(
    Output('card_feminino','children'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_cartao_genero_f(fgenero,fidade,ffilhos,ftempohof):
    ## gêneros: feminino
    coluna='genero'
    niveis=generos
    tgenero=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    resultado_filtro=str("{0:.1%}".format(tgenero.loc['feminino','percentual filtrado']))
    resultado_total=str("{0:.1%}".format(tgenero.loc['feminino','percentual total']))
    
    return html.Div([
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img922/6883/ts2hNp.png',
            height =  '105px', #140px
            className='img-genero')],
            className='div-img'),
        html.Div([
            html.H4([resultado_total],className='card-value'),
            html.P(['pesquisa completa'],className='card-result')
            ], 
            className="card-content sem-filtro"),
        html.Div([
            html.H4([resultado_filtro],className='card-value'),
            html.P(['respostas filtradas'],className='card-result')
            ], 
            className="card-content resultado-filtro"),
    ],className='card-1')

#Tab0 Card 1 - todos filtros - cartão genero - masculino
@app.callback(
    Output('card_masculino','children'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_cartao_genero_m(fgenero,fidade,ffilhos,ftempohof):
    ## gêneros: masculino
    coluna='genero'
    niveis=generos
    tgenero=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    resultado_filtro=str("{0:.1%}".format(tgenero.loc['masculino','percentual filtrado']))
    resultado_total=str("{0:.1%}".format(tgenero.loc['masculino','percentual total']))

    return html.Div([
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img924/7890/59E4tc.png',
            height =  '90px',#'120px',
            className='img-genero')],
            className='div-img'),
        html.Div([
            html.H4([resultado_total],className='card-value'),
            html.P(['pesquisa completa'],className='card-result')
            ], 
            className="card-content sem-filtro"),
        html.Div([
            html.H4([resultado_filtro],className='card-value'),
            html.P(['respostas filtradas'],className='card-result')
            ], 
            className="card-content resultado-filtro"),
    ],className='card-1')

#Tab0 Card 2 - todos filtros - cartão morar com filhos
@app.callback(
    Output('card_filhosim','children'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_cartao_filhos_s(fgenero,fidade,ffilhos,ftempohof):
    ## morar com filhos: sim
    coluna='filhos'
    niveis=filhos
    tfilhos=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    resultado_filtro=str("{0:.1%}".format(tfilhos.loc['sim','percentual filtrado']))
    resultado_total=str("{0:.1%}".format(tfilhos.loc['sim','percentual total']))
    resultado_filtro,resultado_total
    return html.Div([
        html.Div([
            html.Img(src='https://imageshack.com/i/pnOF4ihUp', 
            id='img-outro',
            height = '95px',#'130px',
            className='img-genero') 
            ],className='div-img'),
        html.Div([
            html.H4([resultado_total],className='card-value'),
            html.P(['pesquisa completa'],className='card-result')
            ], 
            className="card-content sem-filtro"),
        html.Div([
            html.H4([resultado_filtro],className='card-value'),
            html.P(['respostas filtradas'],className='card-result')
            ], 
            className="card-content resultado-filtro"),
    ],className='card-1')

#Tab0 Card 3 - todos filtros - cartão morar com filhos
@app.callback(
    Output('card_filhonao','children'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_cartao_filhos_n(fgenero,fidade,ffilhos,ftempohof):
    ## morar com filhos: não
    coluna='filhos'
    niveis=filhos
    tfilhos=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    resultado_filtro=str("{0:.1%}".format(tfilhos.loc['não','percentual filtrado']))
    resultado_total=str("{0:.1%}".format(tfilhos.loc['não','percentual total']))
    resultado_filtro,resultado_total
    return html.Div([
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img922/7706/Ge0JOq.png',
            id='img-outro',
            height = '95px',# '130px',
            className='img-genero') 
            ],className='div-img'),
        html.Div([
            html.H4([resultado_total],className='card-value'),
            html.P(['pesquisa completa'],className='card-result')
            ], 
            className="card-content sem-filtro"),
        html.Div([
            html.H4([resultado_filtro],className='card-value'),
            html.P(['respostas filtradas'],className='card-result')
            ], 
            className="card-content resultado-filtro"),
    ],className='card-1')

#Tab0 Gráfico1 - respostas filtradas - grafico idade
@app.callback(
    Output('idade','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_grafico_idade(fgenero,fidade,ffilhos,ftempohof):
    ## Idade - histograma
    # Base completa
    idadec=db['idade'].copy()

    #Base filtrada
    dbf=db[db['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    idadef=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))]['idade'].copy()

    #Gráfico
    fig=go.Figure(data=[
            go.Histogram(x=idadec, name='pesquisa completa', xbins=dict(size=2), #nbinsx=75,#opacity=0.5,
                                text='idade',
                                hovertemplate = "%{y} </br> "),
        ],
        layout=go.Layout(
                #title= 'distribuição da idade',
                barmode='overlay',
                yaxis={'showline': True,
                        'linecolor': "#4d4d4d",
                        'showgrid':False,'visible':True,'title':'número respondentes'}, 
                xaxis={'showline': True,
                        'linecolor': "#4d4d4d",
                        'showgrid':False,'visible':True,'title':'idade'},
                plot_bgcolor='white',
                colorway=colors,hovermode="x unified",
                legend_orientation='h',
                showlegend=False,
                margin=dict(t=0,pad=5,r=10),
                font=dict(color='#4d4d4d')
                ))

    if not (fidade[0]+fidade[1]-1==2):
        fig.add_trace(go.Histogram(x=idadef, name='respostas filtradas',  xbins=dict(size=2), #nbinsx=75,#opacity=0.5,
                        text='idade',
                        hovertemplate = "%{y}"))
    
    return fig
 
#Tab0 Gráfico2 - respostas filtradas - grafico tempo em home office
@app.callback(
    Output('tempo_hof','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_grafico_thof(fgenero,fidade,ffilhos,ftempohof):
    ## tempo em home office - barras
    coluna='tempo_hof'
    niveis=tempo_hoffice
    # Tabela para construção dos gráficos - a partir da função criada
    tthof=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    # Gráfico
    titulo='há quanto tempo está em home office?'
    grafico=grafico_barra_comparacao(tthof,titulo,rotulo='auto')
    
    return grafico
      
#Tab0 Gráfico3 - respostas filtradas - grafico estado civil
@app.callback(
    Output('estadoCivil','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_grafico_estadoCivil(fgenero,fidade,ffilhos,ftempohof):
    ## estado civil - barras
    coluna='estado_civil'
    niveis=estadocivil
    # Tabela para construção dos gráficos - a partir da função criada
    testado_civil=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    # Gráfico
    titulo='estado civil'
    grafico=grafico_barra_comparacao(testado_civil,titulo,rotulo='auto')
    
    return grafico

### SEGUNDA ABA
## GRÁFICO - PRODUTIVIDADE E ENGAJAMENTO - comparativo: base completa e filtro
# Tab1 Gráfico 1 - filtros Produtividade
@app.callback(
    Output('prodLikert','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_grafico_prodlikert(fgenero,fidade,ffilhos,ftempohof):
    ## PRODUTIVIDADE LIKERT
    ## percepção de produtividade - likert - barras
    coluna='prod_likert'
    niveis=cat_lprod
    # Tabela para construção dos gráficos - a partir da função criada
    tprod=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    # Gráfico
    titulo='percepção de produtividade'
    grafico=grafico_barra_comparacao(tprod,titulo,rotulo='auto')
    return grafico

# Tab1 Gráfico 2 - filtros Engajamento
@app.callback(
    Output('engajamentoLikert','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_grafico_engajlikert(fgenero,fidade,ffilhos,ftempohof):
    ## ENGAJAMENTO LIKERT
    ## engajamento - likert - barras
    coluna='engaj_likert'
    niveis=cat_lengaj
    # Tabela para construção dos gráficos - a partir da função criada
    tengaj=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    # Gráfico
    titulo='engajamento'
    grafico=grafico_barra_comparacao(tengaj,titulo,rotulo='auto')
    return grafico

# Tab1 Gráfico 3 - filtros Satisfação
@app.callback(
    Output('satisfacaoLikert','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_grafico_satisflikert(fgenero,fidade,ffilhos,ftempohof):
    ## SATISFAÇÃO LIKERT
    ## satisfação - likert - barras
    coluna='satisf_likert'
    niveis=cat_lsatisf
    # Tabela para construção dos gráficos - a partir da função criada
    tsatisf=gerar_tabela(db,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    # Gráfico
    titulo='satisfação'
    grafico=grafico_barra_comparacao(tsatisf,titulo,rotulo='auto')
    return grafico

# Tab1 Gráfico 4 - filtros Médias construtos
@app.callback(
    Output('mediasLikert','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_grafico_mediaslikert(fgenero,fidade,ffilhos,ftempohof):
    ## MÉDIAS POR LIKERT
    ## médias por construto
    lista_construtos=['interação com colegas', 'interação com lider', 'produtividade do time na<br>percepção do gestor', 'segurança', 'equilíbrio: vida pessoal e<br>vida profissional', 
                    'bem estar','satisfação com<br>home office', 'engajamento', 'percepção de<br>produtividade individual']

    # todas as respondentes
    medias_construtos=db[['media_interacao_colegas', 'media_interacao_lider', 'media_prod_gestor', 'media_seguranca', 'media_wlbalance', 
                        'media_bem_estar', 'media_satisfacao', 'media_engajamento', 'media_produtividade']].mean()
    medias_construtos.name='média geral'
    percent_nota=(medias_construtos-1)/(5-1)
    percent_nota.name='percentual total'
    tabela_construtos=medias_construtos.to_frame().join(percent_nota.to_frame())

    # Aplicação dos filtros - base de dados filtrada
    dbf=db[db['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    db_f1=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))].copy()

    tabela_construtos['média filtrado']=db_f1[['media_produtividade','media_engajamento','media_satisfacao','media_bem_estar','media_wlbalance','media_seguranca',
                        'media_prod_gestor','media_interacao_lider','media_interacao_colegas']].mean()
    tabela_construtos['percentual filtrado']=(tabela_construtos['média filtrado']-1)/(5-1)

    tabela_construtos.index=lista_construtos
    tabela_construtos1=tabela_construtos.sort_values(by='percentual total', ascending = True)
    titulo='construtos'
    grafico=grafico_barra_comparacao(tabela_construtos1,titulo,rotulo='auto',n_respondentes=[db.shape[0],db_f1.shape[0]])
    return grafico

### TERCEIRA ABA
## GRÁFICO DE ÁRVORE - PRODUTIVIDADE E MOTIVAÇÕES
# Tab2 Cartão 1 - produtividade sim/não
@app.callback(
    Output('card_produtividadeSN','children'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_cartao_produtividadeSN(fgenero,fidade,ffilhos,ftempohof):
    ## Produtividade - autoavaliação
    # Retiram as pessoas que não estão de home office
    db0=db[db['prod_autoav']!='indisponível'].copy()
    coluna='prod_autoav'
    niveis=prodautoav
    # Tabela para construção dos gráficos - a partir da função criada
    prodsimnao=gerar_tabela(db0,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    #Resultados - todas respondentes
    porcentagem_afetada_total=str("{0:.1%}".format(prodsimnao.loc[['negativamente','positivamente'],'percentual total'].sum()))
    porcentagem_naoafetada_total=str("{0:.1%}".format(prodsimnao.loc['neutra','percentual total']))
    #Resultados - respostas filtradas
    porcentagem_afetada_filtro=str("{0:.1%}".format(prodsimnao.loc[['negativamente','positivamente'],'percentual filtrado'].sum()))
    porcentagem_naoafetada_filtro=str("{0:.1%}".format(prodsimnao.loc['neutra','percentual filtrado']))

    return html.Div([
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img923/6488/UmbaBL.png',#'https://image.flaticon.com/icons/svg/876/876220.svg',#'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Imbalanced_justice_scale_silhouette.svg/1024px-Imbalanced_justice_scale_silhouette.svg.png',#'https://w7.pngwing.com/pngs/327/703/png-transparent-judge-court-law-computer-icons-prosecutor-libra-symbol-angle-text-monochrome.png',
            height =  '130px',
            className='img-prod'),
            html.H4([porcentagem_afetada_filtro],className='card-value'),
            ], 
            className="card-content resultado-filtro bgazul card-coluna", style=dict(color = "#ffffff")
            ),
        html.Div([
            html.H5(['dos respondentes afirmaram que têm a ',html.B('produtividade afetada')],className='card-result')
            ], 
            className="card-content resultado-filtro bgazul espaco", style=dict(color = "#ffffff")
            ),
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img923/3451/cOmByl.png',#'https://image.flaticon.com/icons/svg/18/18613.svg',#'https://cdn.pixabay.com/photo/2018/02/26/14/19/libra-3183164_1280.png',
            height =  '130px',
            className='img-prod'),
            html.H4([porcentagem_naoafetada_filtro],className='card-value'),
            ], 
            className="card-content card-coluna bgcinza", style=dict(color = "#4d4d4d")
            ),
        html.Div([
            html.H5(['dos respondentes afirmaram que conseguem ',html.B('manter a produtividade')],className='card-result')
            ], 
            className="card-content bgcinza ", style=dict(color = "#4d4d4d")),
    ],className='card-prod')

# Tab2 Gráfico 2 - filtros tree map
@app.callback(
    Output('treemap','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_grafico_treemap(fgenero,fidade,ffilhos,ftempohof):
    #Filtrar a base
    dbf=db_arvore[db_arvore['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    db_f1=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))].copy()

    #Teste - produtividade_positivamente
    db_tree=db_f1[db_f1['o_que']=='produtividade'][['prod_autoav','como','genero', 'motivo','peso','fracao']].copy()

    ttree=db_tree.groupby(['prod_autoav','como','genero','motivo'], as_index=False)['fracao'].count()
    ttree['fracao']=(np.where(ttree['como']=='negativamente',
                            ttree['fracao']*len(db_arvore[db_arvore['como']=='negativamente'].index.unique())/db_arvore[db_arvore['como']=='negativamente'].shape[0],
                            ttree['fracao']*len(db_arvore[db_arvore['como']=='positivamente'].index.unique())/db_arvore[db_arvore['como']=='positivamente'].shape[0]))
    ttree['pergunta']='como a produtividade foi afetada?'
    #Gráfico
    #Treemap motivos que impactam a produtividade
    fig = px.treemap(ttree, path=['pergunta','como', 'motivo'], #,'genero'
                    color = 'fracao', 
                    values = 'fracao', 
                    color_continuous_scale=["#95acc7","#83b4fc","#90ACE0",'#5b90de'], #"#5288DB"],"#4d4d4d",
                    #color_discrete_map={'impactoSN':'black', 'positivamente':'gold', 'motivo':'darkblue'},
                    color_continuous_midpoint= 2.5,
                    maxdepth=2)
    fig.update_traces(textinfo = 'label+percent parent', 
                    textposition='middle center', 
                    textfont_color="#ffffff",
                    textfont_size=22, 
                    textfont_family= 'open sans')
    fig.update(layout_coloraxis_showscale=False)
    fig.update_layout(margin=dict(pad = 0, t=0, r=0, b=0, l=0),
                        height=520)
    fig.layout.hovermode = False
    return fig

### QUARTA ABA
## GRÁFICO DE ÁRVORE - SATISFAÇÃO E ASPECTOS
# Tab3 Cartão 1 - satisfacao 
@app.callback(
    Output('card_satisfacao','children'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_cartao_satisfacao(fgenero,fidade,ffilhos,ftempohof):
    ## satisfação - likert - barras
    # Retiram as pessoas que não estão de home office
    db0=db[db['satisf_autoav']!='indisponível'].copy()
    coluna='satisf_autoav'
    niveis=satisfautoav
    # Tabela para construção dos gráficos - a partir da função criada
    prodsimnao=gerar_tabela(db0,coluna,niveis,fgenero,fidade,ffilhos,ftempohof)
    #Resultados - todas respondentes
    porcentagem_satisf_total=str("{0:.1%}".format(prodsimnao.loc['satisfeita','percentual total'].sum()))
    porcentagem_neutra_total=str("{0:.1%}".format(prodsimnao.loc['neutra','percentual total']))
    porcentagem_insatisf_total=str("{0:.1%}".format(prodsimnao.loc['insatisfeita','percentual total']))
    #Resultados - respostas filtradas
    porcentagem_satisf_filtro=str("{0:.1%}".format(prodsimnao.loc['satisfeita','percentual filtrado'].sum()))
    porcentagem_neutra_filtro=str("{0:.1%}".format(prodsimnao.loc['neutra','percentual filtrado']))
    porcentagem_insatisf_filtro=str("{0:.1%}".format(prodsimnao.loc['insatisfeita','percentual filtrado']))

    return html.Div([
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img923/6633/cg9ALA.png',
            height =  '130px',
            className='img-satisf'),
            html.H4([porcentagem_satisf_filtro],className='card-value'),
            ], 
            className="card-content resultado-filtro card-coluna-satisf bgazul", style=dict(color = "#ffffff")
            ),
        html.Div([
            html.H5(['dos respondentes afirmaram que estão ',html.B('satisfeitos'),' com o trabalho remoto'],className='card-result')
            ], 
            className="card-content resultado-filtro bgazul espaco-s", style=dict(color = "#ffffff")
            ),
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img923/4962/V8LmI9.png',
            height =  '130px',
            className='img-satisf'),
            html.H4([porcentagem_neutra_filtro],className='card-value'),
            ], 
            className="card-content card-coluna-satisf bgcinza", style=dict(color = "#4d4d4d")
            ),
        html.Div([
            html.H5(['dos respondentes ',html.B('não estão satisfeitos nem insatisfeitos'),' com o trabalho remoto'],className='card-result')
            ], 
            className="card-content bgcinza espaco-s", style=dict(color = "#4d4d4d")),        
        html.Div([
            html.Img(src='https://imagizer.imageshack.com/img923/2833/QSw2Yd.png',
            height =  '130px',
            className='img-satisf'),
            html.H4([porcentagem_insatisf_filtro],className='card-value'),
            ], 
            className="card-content card-coluna-satisf bgcinza1", style=dict(color = "#ffffff")
            ),
        html.Div([
            html.H5(['dos respondentes afirmaram que estão ',html.B('insatisfeitos'),' com o trabalho remoto'],className='card-result')
            ], 
            className="card-content bgcinza1 espaco-s", style=dict(color = "#ffffff")),
    ],className='card-satisf')

# Tab3 Gráfico 2 - filtros tree map
@app.callback(
    Output('treemap-satisf','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def upgrade_grafico_treemap_satisf(fgenero,fidade,ffilhos,ftempohof):
    #Satisfação
    #Filtrar a base
    dbf=db_arvore[db_arvore['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    db_f1=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))].copy()
    #Aspectos - home office
    db_tree=db_f1[db_f1['o_que']=='aspectos'][['prod_autoav','como','genero', 'motivo','peso','fracao']].copy()

    ttree=db_tree.groupby(['prod_autoav','como','genero','motivo'], as_index=False)['fracao'].count()
    ttree['fracao']=(np.where(ttree['como']=='negativamente',
                            ttree['fracao']*len(db_arvore[db_arvore['como']=='negativos'].index.unique())/db_arvore[db_arvore['como']=='negativos'].shape[0],
                            ttree['fracao']*len(db_arvore[db_arvore['como']=='positivos'].index.unique())/db_arvore[db_arvore['como']=='positivos'].shape[0]))
    ttree['pergunta']='aspectos do home office'
    #Gráfico
    #Treemap motivos que impactam a produtividade
    fig = px.treemap(ttree, path=['pergunta','como', 'motivo'], #,'genero'
                    color = 'fracao', 
                    values = 'fracao', 
                    color_continuous_scale=["#95acc7","#83b4fc","#90ACE0",'#5b90de'], #"#5288DB"],"#4d4d4d",
                    #color_discrete_map={'impactoSN':'black', 'positivamente':'gold', 'motivo':'darkblue'},
                    color_continuous_midpoint= 2.5,
                    maxdepth=2)
    fig.update_traces(textinfo = 'label+percent parent', 
                    textposition='middle center', 
                    textfont_color="#ffffff",
                    textfont_size=22, 
                    textfont_family= 'open sans')
    fig.update(layout_coloraxis_showscale=False)
    fig.update_layout(margin=dict(pad = 0, t=0, r=0, b=0, l=0),
                        height=520)
    fig.layout.hovermode = False
    return fig

### QUINTA ABA
## CONSTRUÇÃO DOS GRÁFICOS
#Tab4 Gráfico 1 - filtros - mapa de correlações
@app.callback(
    Output('correlacao','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value')])
def update_grafico_correlacao(fgenero,fidade,ffilhos,ftempohof):
    ## matriz de correlações
    # Filtrar a base
    dbf=db[db['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    db_filtro=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))].copy()

    #Construção da matriz de correlações
    db_var1=db_filtro.loc[:,['media_interacao_colegas', 'media_interacao_lider', 'media_prod_gestor', 'media_seguranca', 'media_wlbalance', 
                            'media_bem_estar', 'media_satisfacao', 'media_engajamento', 'media_produtividade']]
    var_names=['interação com colegas', 'interação com lider', 'produtividade do time na<br>percepção do gestor', 'segurança', 'equilíbrio: vida pessoal e<br>vida profissional', 
                'bem estar','satisfação com<br>home office', 'engajamento', 'percepção de<br>produtividade individual']
    db_var1.columns = var_names

    #Matriz de correlações
    corMetodo='spearman' #'spearman' #'pearson'
    db_corr=db_var1.corr(method=corMetodo) 
    #Matriz triangular inferior
    db_cor=db_corr.where(np.triu(np.ones(db_corr.shape)).astype(np.bool))
    db_cor=db_cor[db_cor.columns[::-1]] #Inverte a ordem das colunas
    # Escala de cor
    colorscale = [[0, '#4d4d4d'],[0.2,'#edf3fb'],[0.7,'#5288db'] ,[1, '#182841']] #[[0, '#edf3fb'],[0.5,'#5288db'] ,[1, '#182841']]

    #Anotações das correlações no mapa de calor
    texto=[dict(
        x = db_cor.columns[i],
        y = db_cor.index[j], # + 1,
        text=format([db_cor.loc[db_cor.index[j],db_cor.columns[i]].round(2)][0],".2f")
        , xref="x",
        yref="y",
        showarrow=False,
        font={'color':'white'},
    ) for i in range(len(db_cor.columns)) for j in range(len(db_cor.index))]

    fig=go.Figure(data=[go.Heatmap(z=db_cor,x=db_cor.columns,y=db_cor.index,
                                zmin=-1,zmax=1,
                                hoverongaps = False,text=(db_cor.values.round(3))
                                , hoverinfo='x+y+text'
                                , hovertemplate="<b> coef. correlação </b><br>" +
                                                "var1: %{x}<br>" +
                                                "var2: %{y}<br>" +
                                                "coef correlação: %{text:.1%}" +
                                                "<extra></extra>"
                                , colorscale=colorscale,reversescale = False
                                , connectgaps= False,zsmooth=False
                                ,showscale=False
                            )
        ],
        layout=go.Layout(
            xaxis={'showgrid':False,'tickangle':-30}
            ,yaxis={'showgrid':False,'automargin':True}
            ,autosize= True
            ,annotations=texto
            ,plot_bgcolor='white'
            ,clickmode='event + select'
            ,hovermode='closest' #False #
            ,height=500
            ,margin={'b':120, 't':0,'r':0, 'pad':5}
        ))
    return fig

#Tab4 Gráfico 2 - filtros - dispersão
@app.callback(
    Output('dispersao','figure'),
    [Input('filtro_genero','value'),
    Input('filtro_idade','value'),
    Input('filtro_filhos','value'),
    Input('filtro_thof','value'),
    Input('correlacao','clickData'),])
def update_grafico_dispersao(fgenero,fidade,ffilhos,ftempohof,corhover):
    #Aplicação dos filtros - base de dados filtrada
    # Dispersão construtos
    corhover={'points': [{'curveNumber': 0, 'x': 'percepção de<br>produtividade individual', 'y': 'engajamento', 'z': 0.1712258220532262, 'text': 0.171}]}
    #Aplicação dos filtros - base de dados filtrada
    dbf=db[db['genero'].isin(list(fgenero))].copy()
    db_f=dbf[dbf['faixa_etaria'].isin(list(idades[fidade[0]-1:fidade[1]-1]))].copy()
    db_f2=db_f[db_f['filhos'].isin(list(ffilhos))].copy()
    db_filtro=db_f2[db_f2['tempo_hof'].isin(list(tempo_hoffice[ftempohof[0]-1:ftempohof[1]-1]))].copy()

    #Construção da matriz de correlações
    db_var1=db_filtro.loc[:,['media_interacao_colegas', 'media_interacao_lider', 'media_prod_gestor', 'media_seguranca', 'media_wlbalance', 
                            'media_bem_estar', 'media_satisfacao', 'media_engajamento', 'media_produtividade']]
    var_names=['interação com colegas', 'interação com lider', 'produtividade do time na<br>percepção do gestor', 'segurança', 'equilíbrio: vida pessoal e<br>vida profissional', 
                'bem estar','satisfação com<br>home office', 'engajamento', 'percepção de<br>produtividade individual']
    db_var1.columns = var_names

    ##Par selecionado no grafico de correlacoes
    if corhover != None:
        nameX = corhover['points'][0]['x']
        nameY = corhover['points'][0]['y']
        variaveis=[nameX,nameY]
    else:
        nameX = 'engajamento'
        nameY = 'percepção de<br>produtividade individual'
        variaveis=[nameX,nameY]

    teste=db_var1.copy()
    tbolha=db_var1.groupby(variaveis).size()#.count()#

    if variaveis[0]==variaveis[1]:
        variaveis[1]='y'+variaveis[1]
        tbolha.index.set_names([variaveis[0], variaveis[1]], inplace=True)
        tbolha=tbolha.reset_index()
        teste=teste.merge(tbolha, how = 'inner', on = variaveis[0])
    else:
        tbolha=tbolha.reset_index()
        teste=teste.merge(tbolha, how = 'inner', on = variaveis)

    if nameX == nameY:
        fig = px.scatter(teste,
                    x=teste[variaveis[0]].round(2), 
                    y=teste[variaveis[1]].round(2), 
                    trendline = "ols", trendline_color_override = '#5288DB',
                    opacity = 0.6
                            )
        fig.update_traces(marker = dict(color = '#4d4d4d'),
                        hovertemplate= nameX+": %{x:.1f}<br>" +
                                        nameY+": %{y:.1f}<br>")
        fig.update_xaxes(
                    linecolor = '#4d4d4d',
                    showgrid = False,
                    tickmode = "array", tickvals = (1,2,3,4,5), 
                    ticktext = ("muito baixo","baixo","neutro","alto","muito alto")
                    )
        fig.update_yaxes(
                    linecolor = "#4d4d4d",
                    showgrid = False,
                    tickmode = "array", tickvals = (1,2,3,4,5), 
                    ticktext = ("muito baixo","baixo","neutro","alto","muito alto"))
        fig.update_layout(
            xaxis_title = dict(text = nameX),
            yaxis_title = dict(text = nameY),
            plot_bgcolor = 'white',
            paper_bgcolor = 'white',
            font = dict(
                family = 'open sans',
                size = 14,
                color = '#4d4d4d'),
            height=500,
            margin=dict(pad=5,t=25)
        )
    else:        
        fig = px.scatter(teste,
                    x=teste[variaveis[0]].round(2)+np.random.uniform(low = -0.17, high = 0.13, size= len(teste.index)), 
                    y=teste[variaveis[1]].round(2)-np.random.uniform(low = -0.17, high = 0.13)-np.random.uniform(low = -0.17, high = 0.13, size= len(teste.index)), 
                    trendline = "ols", trendline_color_override = '#5288DB',
                    opacity = 0.6
                            )
        fig.update_traces(marker = dict(color = '#4d4d4d'),
                        hovertemplate= nameX+": %{x:.1f}<br>" +
                                        nameY+": %{y:.1f}<br>")
        fig.update_xaxes(
                    linecolor = '#4d4d4d',
                    showgrid = False,
                    tickmode = "array", tickvals = (1,2,3,4,5), 
                    ticktext = ("muito baixo","baixo","neutro","alto","muito alto")
                    )
        fig.update_yaxes(
                    linecolor = "#4d4d4d",
                    showgrid = False,
                    tickmode = "array", tickvals = (1,2,3,4,5), 
                    ticktext = ("muito baixo","baixo","neutro","alto","muito alto"))
        fig.update_layout(
            xaxis_title = dict(text = nameX),
            yaxis_title = dict(text = nameY),
            plot_bgcolor = 'white',
            paper_bgcolor = 'white',
            font = dict(
                family = 'open sans',
                size = 14,
                color = '#4d4d4d'),
            height=500,
            margin=dict(pad=5,t=25)
        )
        return fig

#Tab4 Cartões - filtros - conceitos contrutos
@app.callback(
    Output('primeiro-construto','children'),
    [Input('correlacao','clickData')])
def update_cartao_construto1(corhover):
    nameX = corhover['points'][0]['x']
    texto=[html.H5(dic_construtos[nameX][0]),
            html.P(dic_construtos[nameX][1])]
    return texto

@app.callback(
    Output('segundo-construto','children'),
    [Input('correlacao','clickData')])
def update_cartao_construto2(corhover):
    nameY = corhover['points'][0]['y']
    texto=[html.H5(dic_construtos[nameY][0]),
            html.P(dic_construtos[nameY][1])]
    return texto

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/covid19-fase2':
        return conteudo
    else:
        return capa
    # You could also return a 404 "URL not found" page here

# Rodar o script e gerar a página
if __name__ == '__main__':
    app.run_server(debug=True)
