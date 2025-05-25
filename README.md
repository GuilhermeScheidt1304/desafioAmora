**AMORA: Simulador de Compras**

Bem-vindo ao AMORA, um simulador de compras simples que ajuda a visualizar as parcelas de um imóvel corrigidas ao longo dos anos, considerando tanto o IGPM quanto uma taxa de juros personalizada.

**Como funciona?**
O simulador solicita algumas informações essenciais para calcular e projetar os valores das parcelas:

Valor do Imóvel: O preço total do imóvel que você deseja simular.
Percentual de Entrada: A porcentagem do valor do imóvel que você pretende dar como entrada.
Duração do Contrato (em anos): O período total em que o financiamento será pago.
Taxa de Juros Anual: Uma taxa de juros personalizada que será aplicada para correção das parcelas. Para garantir uma simulação realista, a taxa deve estar entre 5% e 12%.
Cálculos Realizados
Com base nas informações fornecidas, o AMORA calcula:

Valor da Entrada: O montante correspondente ao percentual de entrada.
Total a Guardar: Um valor base para simulação, correspondente a 15% do valor do imóvel.
Parcela Mensal Base: A parcela inicial calculada com base no "total a guardar" dividido pelo número total de meses do contrato.
Projeção de Parcelas
O grande diferencial do AMORA é a projeção anual das parcelas, mostrando como elas seriam corrigidas de duas formas:

Corrigida pelo IGPM: Utiliza um fator de correção anual de 6% (simulando a inflação do IGPM) para mostrar o aumento da parcela ao longo do tempo.
Corrigida pela Taxa de Juros Informada: Aplica a taxa de juros anual que você digitou, demonstrando o impacto dessa taxa nas parcelas futuras.

**Como usar o simulador?**
Para rodar o simulador, basta executar o script Python e seguir as instruções no console. Ele pedirá que você insira os valores solicitados passo a passo.
