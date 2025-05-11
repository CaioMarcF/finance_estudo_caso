from bcb import sgs
import matplotlib.pyplot as plt


################IPCA

ipca = sgs.get({'ipca':433}, start='1990-01-01', end='2000-01-01')
df_ipca = ipca.reset_index()
df_ipca.columns = ['data', 'taxa']

plt.figure(figsize=(10, 6))  
plt.plot(df_ipca['data'], df_ipca['taxa'], linestyle='-', color='b', label='Taxa ao longo do tempo')

#Primeiro mês do ano
for ano in df_ipca['data'].dt.year.unique():
    
    primeiro_mes = df_ipca[df_ipca['data'].dt.year == ano].iloc[0]
    x = primeiro_mes['data']
    y = primeiro_mes['taxa']
    
    #Texto ao lado do ponto
    plt.annotate(
        text=f"{y}",
        xy=(x, y),
        xytext=(0, 7),  
        textcoords='offset points',
        bbox=dict(boxstyle='round',pad=0.5, fc='white', alpha=0.5),
        fontsize=9
    )

plt.title('IPCA Mensal', fontsize=14)
plt.xlabel('')
plt.ylabel('Variação (%)')
plt.grid(True, linestyle='--')
plt.tight_layout()

plt.savefig('ipca.png', dpi=300, bbox_inches='tight')
plt.show()

################Taxa de Câmbio

cambio_dol = sgs.get({'cambio':11753}, start='1995-01-01', end='2000-01-01')
df_cambio_dol = cambio_dol.reset_index()
df_cambio_dol.columns = ['data', 'taxa']

plt.figure(figsize=(10, 6))  
plt.plot(df_cambio_dol['data'], df_cambio_dol['taxa'], linestyle='-', color='y')

#Primeiro mês do ano
for ano in df_cambio_dol['data'].dt.year.unique():
    
    primeiro_mes = df_cambio_dol[df_cambio_dol['data'].dt.year == ano].iloc[0]
    x = primeiro_mes['data']
    y = primeiro_mes['taxa']
    
    #Texto ao lado do ponto
    plt.annotate(
        text=f"{y}",
        xy=(x, y),
        xytext=(-15, 7), 
        textcoords='offset points',
        bbox=dict(boxstyle='round',pad=0.5, fc='white', alpha=0.5),
        fontsize=9
    )

plt.title('Taxa de Câmbio Real-Dolar Mensal', fontsize=14)
plt.xlabel('')
plt.ylabel('Taxa de Câmbio')
plt.grid(True, linestyle='--')

plt.savefig('cambio.png', dpi=300, bbox_inches='tight')
plt.show()

################ Balança comercial

balanca = sgs.get({'balanca':2517}, start='1990-01-01', end='2000-01-01')
df_balanca = balanca.reset_index()
df_balanca.columns = ['data', 'taxa']

plt.figure(figsize=(10, 6))
plt.fill_between(df_balanca['data'], df_balanca['taxa'], color='#ADD8E6', alpha=0.3)  # Área preenchida
plt.plot(df_balanca['data'], df_balanca['taxa'], linestyle='-', color='b', linewidth=1) 

# Primeiro trimestre do ano 
for ano in df_balanca['data'].dt.year.unique():
    primeiro_tri = df_balanca[df_balanca['data'].dt.year == ano].iloc[0]
    x = primeiro_tri['data']
    y = primeiro_tri['taxa']
    
    # Posição vertical do texto para barras positivas/negativas
    #Para cima ou para baixo
    va = 'bottom' if y >= 0 else 'top' 
    offset = 5 if y >= 0 else -5
    
    plt.annotate(
        text=f"{y}",
        xy=(x, y),
        xytext=(0, offset), 
        textcoords='offset points',
        ha='center',
        va=va,
        bbox=dict(boxstyle='round', pad=0.5, fc='white', alpha=0.5),
        fontsize=9
    )

plt.title('Saldo da Balança Comercial Trimestral', fontsize=14)
plt.xlabel('')
plt.ylabel('Saldo (Milhões US$)')
plt.grid(True, linestyle='--')
plt.savefig('balanca_barras.png', dpi=300, bbox_inches='tight')
plt.show()

################selic

selic = sgs.get({'selic':4390}, start='1995-01-01', end='2000-01-01')
df_selic = selic.reset_index()
df_selic.columns = ['data', 'taxa']

plt.figure(figsize=(10, 6))  
plt.plot(df_selic['data'], df_selic['taxa'], linestyle='-', color='#00008B')

#Primeiro mês do ano
for ano in df_selic['data'].dt.year.unique():
    
    primeiro_mes = df_selic[df_selic['data'].dt.year == ano].iloc[0]
    x = primeiro_mes['data']
    y = primeiro_mes['taxa']
    
    #Texto ao lado do ponto
    plt.annotate(
        text=f"{y}",
        xy=(x, y),
        xytext=(0, 7),  
        textcoords='offset points',
        bbox=dict(boxstyle='round',pad=0.5, fc='white', alpha=0.5),
        fontsize=9
    )

plt.title('Taxa de Juros - Selic Acumulada no Mês', fontsize=14)
plt.xlabel('')
plt.ylabel('Variação (%)')
plt.grid(True, linestyle='--')

plt.savefig('selic.png', dpi=300, bbox_inches='tight')
plt.show()

################ Desemprego

desemprego = sgs.get({'desemprego':	1621}, start='1990-01-01', end='2000-01-01')
df_desemprego = desemprego.reset_index()
df_desemprego.columns = ['data', 'taxa']

plt.figure(figsize=(10, 6))  
plt.plot(df_desemprego['data'], df_desemprego['taxa'], linestyle='-', color='b')

#Primeiro mês do ano
for ano in df_desemprego['data'].dt.year.unique():
    
    primeiro_mes = df_desemprego[df_desemprego['data'].dt.year == ano].iloc[0]
    x = primeiro_mes['data']
    y = primeiro_mes['taxa']
    
    #Texto ao lado do primeiro mes do ano
    plt.annotate(
        text=f"{y}",
        xy=(x, y),
        xytext=(0, 7),  
        textcoords='offset points',
        bbox=dict(boxstyle='round',pad=0.5, fc='white', alpha=0.5),
        fontsize=9
    )

plt.title('Taxa de Desemprego da Região Metropolitana Brasileira ao Mês', fontsize=14)
plt.xlabel('')
plt.ylabel('Variação (%)')
plt.grid(True, linestyle='--')

plt.savefig('desemprego.png', dpi=300, bbox_inches='tight')
plt.show()

################## dívida líquida

divida = sgs.get({'divida': 2053}, start='1995-01-01', end='1999-01-01')
df_divida = divida.reset_index()
df_divida.columns = ['data', 'taxa']

plt.figure(figsize=(10, 6))  
plt.plot(df_divida['data'], df_divida['taxa'], linestyle='-', color='black')

#Primeiro mês do ano
for ano in df_divida['data'].dt.year.unique():
    
    primeiro_mes = df_divida[df_divida['data'].dt.year == ano].iloc[0]
    x = primeiro_mes['data']
    y = primeiro_mes['taxa']
    
    #Texto ao lado do primeiro mes do ano
    plt.annotate(
        text=f"{y}",
        xy=(x, y),
        xytext=(-22, 7),  
        textcoords='offset points',
        bbox=dict(boxstyle='round',pad=0.5, fc='white', alpha=0.5),
        fontsize=9,
        clip_on=True
    )

plt.title('Dívida Líquida do Setor Público ao Mês', fontsize=14)
plt.xlabel('')
plt.ylabel('Milhões de Reais')
plt.grid(True, linestyle='--')

plt.savefig('divida.png', dpi=300, bbox_inches='tight')
plt.show()