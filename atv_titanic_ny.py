# -*- coding: utf-8 -*-
"""exercício_titanic_numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/medllynthayna/Analise_Dados/blob/master/exerc%C3%ADcio_titanic_numpy.ipynb

![titanic](img/titanic_historical.jpg "Pintura do Titanic")

# EXERCÍCIOS: Análise de Dados do Titanic
"""

from google.colab import drive
drive.mount('/content/drive')

"""O RMS Titanic foi um navio de passageiros britânico operado pela empresa *White Star Line* que afundou no Oceano Atlântico Norte nas primeiras horas da manhã de 15 de abril de 1912, depois de atingir um iceberg durante sua viagem inaugural de Southampton a Nova York. Dos 2.224 passageiros e tripulantes a bordo, mais de 1.500 morreram, tornando o naufrágio um dos desastres marítimos comerciais mais mortais da história moderna em tempos de paz.

Neste estudo iremos explorar um conjunto de dados baseado na lista de passageiros do Titanic editada por Michael A. Findlay, publicada originalmente em Eaton & Haas (1994) Titanic: Triumph and Tragedy, Patrick Stephens Ltd, e expandida com a ajuda da comunidade da Internet. Os arquivos HTML originais foram obtidos por Philip Hind (1999) e o *dataset* descreve o status de sobrevivência de passageiros individuais no Titanic. Ele não contém informações para a tripulação, mas contém idades atuais e estimadas para quase 80% dos passageiros.

## Dicionário de Dados

Nesta seção será apresentado todo o processo de preparação, organização e limpeza de dados feito no *dataset* que possui os seguintes dados:

| Nº | Coluna          | Descrição                                                                 |
|:--:|:----------------|:--------------------------------------------------------------------------|
|  1 | id_passageiro   | Identficador único do passageiro.                                         |
|  2 | classe          | Classe social.                                                            |
|  3 | sobreviveu      | Sobrevivente? Sim (1), Não (0).                                           |
|  4 | nome            | Nome do passageiro.                                                       |
|  5 | sexo            | Masculino (male), Feminino (female).                                      |
|  6 | idade           | Idade do passageiro.                                                      |
|  7 | irmaos_conjuges | Número de irmãos e cônjuges a bordo.                                      |
|  8 | pais_filhos     | Número de pais e filhos a bordo.                                          |
|  9 | bilhete         | Número do bilhete                                                         |
| 10 | tarifa          | Preço da tarifa do passageiro.                                            |
| 11 | cabine          | Cabine.                                                                   |
| 12 | embarque        | Nome do porto de embarque: C = Cherbourg; Q = Queenstown; S = Southampton |
| 13 | bote            | Bote salva vidas.                                                         |
| 14 | corpo           | Número de identificação do corpo.                                         |
| 15 | destino         | Local de desembarque do passageiro.                                       |

### OBSERVAÇÕES

- `classe` é uma aproximação do status socioeconômico na época, onde: 1 = Classe Alta1; 2 = Classe Média e 3 = Classe Baixa;
- `idade` está representada em anos, porém, se a idade for menor que Um (1) ou caso tenha sido estimada, ela estará com casas decimais xx.5;
- `tarifa` está em Libras esterlinas (British Pounds - £) anteriores a 1970;
- `irmaos_conjuges` e `pais_filhos`: as variáveis de relação familiar de algumas relações foram ignoradas; a seguir estão as definições usadas:
    - **Irmão**: Irmão, irmã, meio-irmão ou meia-irmã do passageiro a bordo do Titanic;
    - **Cônjuge**: Marido ou esposa do passageiro a bordo do Titanic (amantes e noivos ignorados);
    - **Pai**: Mãe ou pai do passageiro a bordo do Titanic;
    - **Criança**: Filho, Filha, Enteado ou Enteada do Passageiro a bordo do Titanic;
    - Outros parentes excluídos deste estudo incluem primos, sobrinhos / sobrinhas, tias / tios e parentes;
    - Algumas crianças viajavam apenas com uma babá, portanto foi atribuído 0 para elas em pais_filhos; 
    - Alguns viajaram com amigos ou vizinhos muito próximos em uma vila, no entanto, as definições não apóiam essas relações.

## Exercícios
Faça as questões abaixo usando somente a biblioteca [Numpy](https://numpy.org/).

1. Importe o pacote numpy com o nome np.
"""

import numpy as np

"""2. Carregue o conjunto de dados disponível na pasta [data/titanic3.csv](data/titanic3.csv), ignorando as colunas: `cabine`, `bote`, `corpo` e `destino`. **Importante:** o arquivo `.csv` usa tabulação (`\t`) como delimitador de campos."""

dados = np.genfromtxt('/content/titanic3.csv',
                      delimiter='\t',
                      encoding='utf-8',
                      dtype=object,
                      skip_header=True,
                      usecols=[0, 1, 2, 4, 5, 6, 7, 8, 9, 11])
dados

"""3. Quantas linhas foram lidas do arquivo?"""

import numpy as np

dados = np.array(dados)
len(dados)

"""4. Quantas dimensões sua variável dados possui?"""

np.ndim(dados)

"""5. Obtenha os índices das posições onde existam dados ausentes."""

dados_ausentes = np.where(dados == '')
print(dados_ausentes)

"""6. Remova todas as linhas que possuem dados ausentes."""

np.delete(dados,dados_ausentes,axis=0)

"""7. Mostre todos os dados das 5 primeiras linhas do dataset."""

dados[:5]

"""8. Crie as variáveis: `idade`, `irmaos_conjuges`, `pais_filhos` e `tarifa`; com todos os dados dessas colunas, e, tipos de dados conforme a tabela abaixo:

| Nº | Coluna          | Tipo de Dados |
|:--:|-----------------|---------------|
|  6 | idade           | int           |
|  7 | irmaos_conjuges | int           |
|  8 | pais_filhos     | int           |
| 10 | tarifa          | float         |
"""

idade = dados[:,5]
irmaos_conjuges = dados[:,6]
pais_filhos = dados[:,7]
tarifa = dados[:,9]
print(idade, irmaos_conjuges,pais_filhos,tarifa)

"""9. Selecione as primeiras 5 linhas dos dados."""

dados[:5]
dados

"""10. Considerando o vetor `idades`, selecione todas as idades das crianças a bordo menores de 12 anos inclusive."""

idade_maior = 12
idades = np.array(dados[:,6], dtype = int)
condicao = idades == idade_maior
dados[condicao,:]

"""11. Qual é a média das idades?"""

idades.mean()

"""12. Quais é a maior e menor idade?"""

idade_max = idades.max()
print(idade_max)
idade_min = idades.min()
print(idade_min)

"""13. Crie um vetor chamado `sobreviventes` com todos os dados das pessoas que sobreviveram ao naufrágio."""

sobrevivente = 1
condicao = dados[:,2].astype(int) == sobrevivente
sobrevivente = dados[condicao,:]
print(sobrevivente)

"""14. Segundo este conjunto de dados, quantas pessoas sobreviveram ao naufrágio?"""

len(sobrevivente)

"""15.  Considerando a coluna `idade` dos sobreviventes calcule:
    - Média
    - Mediana
    - Máximo
    - Mínimo
"""

idade_sobrevivente = sobrevivente[:,5]
idade_sobrevivente
np.mean(idade_sobrevivente)
idade_sobrevivente.max()
idade_sobrevivente.min()
np.median(idade_sobrevivente)

"""16. Crie um vetor chamado `vitimas_naufragio` com todos os dados das pessoas que não sobreviveram ao naufrágio."""



"""17. Considerando a coluna `vitimas_naufragio` dos sobreviventes calcule:
    - Média
    - Mediana
    - Máximo
    - Mínimo
"""



"""18. Qual era o preço médio das tarifas?"""



"""19. Crie os vetores `classe_alta`, `classe_media` e `classe_baixa`, com os respectivos dados da coluna `classe` no qual:
    - 1 = Classe Alta
    - 2 = Classe Média
    - 3 = Classe Baixa
"""



"""20. Qual é o número total de passageiros por classe social?"""



"""# REFERÊNCIAS

- [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
- [Encyclopedia Titanica](https://www.encyclopedia-titanica.org/)
- [Basic Feature Engineering with the Titanic Data](https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/)
- Hind, Philip.  "Encyclopedia Titanica."  Online.  Internet. n.p.  02 Aug 1999.
"""