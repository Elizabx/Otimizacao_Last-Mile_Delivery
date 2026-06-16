# 🚚 Otimização de Last-Mile Delivery com Grafos

## 📝 Integrantes

* Débora Bruna Lourenço de Melo
* Vinícius Cavalcante Lima
* Jeanny Elizabete da Silva Bezerra

---

## 📋 Sobre o Projeto

Este projeto simula um sistema inteligente de otimização de rotas para entregas de última milha (*Last-Mile Delivery*), utilizando conceitos de **Teoria dos Grafos** e algoritmos de **Caminho Mínimo**.

A aplicação representa uma rede logística composta por um Centro de Distribuição e diversos pontos de entrega, calculando automaticamente as melhores rotas disponíveis com base no tempo de deslocamento entre os pontos.

Além de encontrar a rota mais eficiente, o sistema também:

* Exibe as três melhores alternativas de rota;
* Calcula economia de tempo;
* Estima redução de custos operacionais;
* Simula impacto ambiental através da redução da emissão de CO₂;
* Gera uma visualização gráfica da rede logística.

---

## 🎯 Objetivo

Demonstrar como algoritmos de grafos podem ser aplicados em problemas reais de logística, auxiliando empresas de transporte e comércio eletrônico a:

* Reduzir tempo de entrega;
* Diminuir custos operacionais;
* Melhorar a eficiência logística;
* Reduzir impactos ambientais.

---

## 🛠 Tecnologias Utilizadas

* Python 3
* NetworkX
* Matplotlib

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta do projeto:

```bash
cd seu-repositorio
```

Instale as dependências:

```bash
pip install networkx matplotlib
```

---

## ▶️ Como Executar

Execute o arquivo principal:

```bash
python main.py
```

O programa exibirá:

1. Relatório de desempenho das rotas;
2. Comparação com uma rota tradicional;
3. Economia financeira simulada;
4. Redução de emissão de CO₂;
5. Grafo visual destacando as melhores rotas encontradas.

---

## 🧠 Conceitos Aplicados

### Grafos Direcionados

A rede logística é modelada como um grafo direcionado (*Directed Graph*), onde:

* Cada nó representa um ponto de entrega;
* Cada aresta representa uma rota possível;
* O peso da aresta representa o tempo de deslocamento.

Exemplo:

```text
Centro_Distribuicao → Ponto_A (10 min)
Ponto_A → Ponto_B (5 min)
Ponto_B → Ponto_D (8 min)
```

---

### Algoritmo de Caminho Mínimo

O sistema utiliza:

```python
nx.shortest_simple_paths()
```

para encontrar as rotas ordenadas pelo menor custo (tempo).

As três melhores opções são selecionadas para análise e comparação.

---

## 📊 Métricas Geradas

### Eficiência Logística

Calcula:

```text
Tempo Poupado = Tempo da rota tradicional - Tempo da rota otimizada
```

### Economia Financeira

Considerando um custo operacional por minuto:

```text
Custo = Tempo × Valor por minuto
```

### Sustentabilidade

Estimativa simplificada da redução de emissão de CO₂:

```text
CO₂ Economizado = Tempo poupado × 0,12 kg
```

---

## 📈 Exemplo de Saída

```text
RELATÓRIO DE IMPACTO DA FEATURE

Rota Tradicional:
Centro_Distribuicao -> Ponto_B -> Ponto_G -> Ponto_J
Tempo: 120 min

Rota com nosso sistema:
Centro_Distribuicao -> Ponto_A -> Ponto_B -> Ponto_D -> Ponto_E -> Ponto_H -> Ponto_J
Tempo: 61 min

EFICIÊNCIA LOGÍSTICA GERADA:

Tempo Poupado: 59 minutos
Economia Financeira: R$ 73,75
Sustentabilidade: 7,08 kg de CO₂ retidos
```

---

## 🎨 Visualização

O grafo gerado utiliza cores para diferenciar as rotas:

| Cor        | Significado          |
| ---------- | -------------------- |
| 🟢 Verde   | Melhor rota          |
| 🟠 Laranja | Segunda melhor rota  |
| 🔵 Azul    | Terceira melhor rota |
| ⚪ Cinza    | Demais conexões      |

---

## 🏗 Estrutura do Projeto

```text
📁 projeto
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 📚 Aplicações Reais

Este tipo de solução pode ser utilizado por empresas como:

* E-commerce;
* Transportadoras;
* Serviços de entrega rápida;
* Distribuidores de medicamentos;
* Redes de supermercados;
* Operadores logísticos.

---

## 👨‍💻 Autores

Projeto desenvolvido para fins acadêmicos na disciplina de Grafos, demonstrando a aplicação prática de algoritmos de otimização em problemas de logística e transporte.

---

## 📄 Licença

Este projeto é destinado para fins educacionais e acadêmicos.
