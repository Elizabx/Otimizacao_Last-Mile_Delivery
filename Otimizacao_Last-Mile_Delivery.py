import networkx as nx
import matplotlib.pyplot as plt

mapa_logistica = nx.DiGraph()

rotas = [
    ("Centro_Distribuicao", "Ponto_A", 10),
    ("Centro_Distribuicao", "Ponto_B", 15),
    ("Centro_Distribuicao", "Ponto_C", 35),
    ("Ponto_A", "Ponto_B", 5),
    ("Ponto_A", "Ponto_C", 12),
    ("Ponto_A", "Ponto_D", 25),
    ("Ponto_B", "Ponto_D", 8),
    ("Ponto_B", "Ponto_G", 65),  
    ("Ponto_C", "Ponto_D", 6),
    ("Ponto_C", "Ponto_E", 10),
    ("Ponto_D", "Ponto_E", 15),
    ("Ponto_D", "Ponto_F", 20),
    ("Ponto_E", "Ponto_F", 4),
    ("Ponto_E", "Ponto_G", 22),
    ("Ponto_F", "Ponto_G", 18),
    ("Ponto_C", "Ponto_H", 14),  
    ("Ponto_E", "Ponto_H", 8),   
    ("Ponto_F", "Ponto_I", 11),  
    ("Ponto_G", "Ponto_I", 25),  
    ("Ponto_H", "Ponto_J", 15),  
    ("Ponto_I", "Ponto_J", 6),   
    ("Ponto_G", "Ponto_J", 40)   
]

for origem, destino, tempo in rotas:
    mapa_logistica.add_edge(origem, destino, weight=tempo)

ponto_partida = "Centro_Distribuicao"
ponto_destino = "Ponto_J"

todas_as_opcoes = list(nx.shortest_simple_paths(mapa_logistica, source=ponto_partida, target=ponto_destino, weight="weight"))

rota_1 = todas_as_opcoes[0] if len(todas_as_opcoes) > 0 else []
rota_2 = todas_as_opcoes[1] if len(todas_as_opcoes) > 1 else []
rota_3 = todas_as_opcoes[2] if len(todas_as_opcoes) > 2 else []

tempo_r1 = nx.path_weight(mapa_logistica, rota_1, 'weight') if rota_1 else 0
tempo_r2 = nx.path_weight(mapa_logistica, rota_2, 'weight') if rota_2 else 0
tempo_r3 = nx.path_weight(mapa_logistica, rota_3, 'weight') if rota_3 else 0

arestas_rota_1 = list(zip(rota_1, rota_1[1:]))
arestas_rota_2 = list(zip(rota_2, rota_2[1:]))
arestas_rota_3 = list(zip(rota_3, rota_3[1:]))

rota_padrao = ["Centro_Distribuicao", "Ponto_B", "Ponto_G", "Ponto_J"]
tempo_padrao = (mapa_logistica["Centro_Distribuicao"]["Ponto_B"]["weight"] + 
                mapa_logistica["B_para_G_ou_similar"]["weight"] if "B_para_G_ou_similar" in mapa_logistica else 65 + 40) 

tempo_padrao = 120

economia_tempo = tempo_padrao - tempo_r1
percentual_melhoria = (economia_tempo / tempo_padrao) * 100

custo_por_minuto = 1.25  
custo_padrao = tempo_padrao * custo_por_minuto
custo_dijkstra = tempo_r1 * custo_por_minuto
economia_reais = custo_padrao - custo_dijkstra

co2_economizado = economia_tempo * 0.12

print("-"*120)
print("\nRELATÓRIO DE IMPACTO DA FEATURE")
print(f"Rota Tradicional: {' -> '.join(rota_padrao)} | Tempo: {tempo_padrao} min | Custo: R${custo_padrao:.2f}")
print(f"Rota com nosso sistema: {' -> '.join(rota_1)} | Tempo: {tempo_r1} min | Custo: R${custo_dijkstra:.2f}\n")
print("-"*120)
print(f"\nEFICIÊNCIA LOGÍSTICA GERADA:")
print(f"Tempo Poupado: {economia_tempo} minutos ({percentual_melhoria:.1f}% mais rápido)")
print(f"Economia Financeira: R$ {economia_reais:.2f} por entrega")
print(f"Sustentabilidade: {co2_economizado:.2f} kg de CO2 retidos\n")
print("-"*120)
print("\nOUTRAS ALTERNATIVAS CALCULADAS:")
print(f"Rota 2: {' -> '.join(rota_2)} ({tempo_r2} min)")
print(f"Rota 3: {' -> '.join(rota_3)} ({tempo_r3} min)\n")
print("-"*120)

plt.figure(figsize=(14, 8))

posicoes = nx.spring_layout(mapa_logistica, k=0.5, iterations=50, seed=42)

cores_nos = []
for no in mapa_logistica.nodes():
    if no == ponto_partida: cores_nos.append("darkgreen")
    elif no == ponto_destino: cores_nos.append("darkgreen")
    elif no in rota_1: cores_nos.append("green")
    elif no in rota_2: cores_nos.append("darkorange")
    elif no in rota_3: cores_nos.append("dodgerblue")
    else: cores_nos.append("gainsboro")

cores_arestas = []
largura_arestas = []

for u, v in mapa_logistica.edges():
    if (u, v) in arestas_rota_1:
        cores_arestas.append("green")
        largura_arestas.append(3.0)
    elif (u, v) in arestas_rota_2:
        cores_arestas.append("darkorange")
        largura_arestas.append(2.0)
    elif (u, v) in arestas_rota_3:
        cores_arestas.append("dodgerblue")
        largura_arestas.append(2.0)
    else:
        cores_arestas.append("#E0E0E0")
        largura_arestas.append(0.8)

nx.draw_networkx_nodes(mapa_logistica, posicoes, node_size=1500, node_color=cores_nos, edgecolors="black")
nx.draw_networkx_edges(mapa_logistica, posicoes, arrowstyle="->", arrowsize=15, edge_color=cores_arestas, width=largura_arestas)
nx.draw_networkx_labels(mapa_logistica, posicoes, font_size=8, font_weight="bold")

pesos_arestas = nx.get_edge_attributes(mapa_logistica, 'weight')
nx.draw_networkx_edge_labels(mapa_logistica, posicoes, edge_labels=pesos_arestas, font_size=8, font_color="dimgray")

plt.plot([], [], color="green", linewidth=3.0, label=f"1ª Opção (Mais Rápida): {tempo_r1} min")
plt.plot([], [], color="darkorange", linewidth=2.0, label=f"2ª Opção: {tempo_r2} min")
plt.plot([], [], color="dodgerblue", linewidth=2.0, label=f"3ª Opção: {tempo_r3} min")
plt.legend(loc="upper left", fontsize=10, frameon=True)

plt.title("Central de Operações Mercado Livre - Simulação Multirotas", fontsize=14, fontweight="bold")
plt.axis("off")
plt.show()