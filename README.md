**Calculadora em Python**
---

Projeto de treino em Python para criar uma calculadora simples utilizando o Tkinter.

Aplicação prática de conceitos de Orientação a Objetos e GUI (Tkinter)


**O que é o Projeto**
---

O projeto consiste em implementar uma calculadora que efetue cálculos simples.

Posteriormente, serão adicionadas novas funcionalidades e melhorias.


**Principais funcionalidades**

As principais funcionalidades implementadas serão:
*  Soma
*  Subtração
*  Multiplicação
*  Divisão

Obs: para o cálculo da divisão, será mostrada mensagem de erro caso ocorra uma divisão por zero.

Obs2: uma limitação inicial será a falta de tratamento de números com notação científica.


**Esboço**
---

Esboço geral de implementação


![Esboço](Esboco.png)



---

**Diário de Bordo**
---

**Dia 1 - 07/02/2019**

*O que foi feito:*
*  Criação do arquivo Readme.
*  Esboço da aplicação.
*  Criação do repositório e ligação com máquina local.
*  Codificação preliminar do layout.

*Dificuldades*:
*  Utilizar os gerenciadores de geometria.
*  Dificuldade na escolha da melhor opção (grid , pack ou place) para os frames dentro da janela Tk() e widgets dentro de cada frame.


**Dia 2 - 11/02/2019**

*O que foi feito:*
*   Decisão do uso do gerenciador de geometria.
*   Uso do GRID como gerenciador de geometria, por ser o mais confiável de utilizar.

*Dificuldades*:
*  Utilizar o gerenciador de geometria GRID.
*  Dificuldade em como utilizar os comandos e como não quebrar o layout.


**Dia 3 - 20/02/2019**

*O que foi feito:*
*  Estudos sobre o gerenciador de geometria grid.
*  Rascunho do novo layout.
[Novo layout](novo_layout.png).
*  Implementação do layout.
*  Limpeza e organização do código.

*Dificuldades:*
*  Organizar a estrutura de nomes de classes e arquivos.


**Dia 4 - 21/02/2019**

*O que foi feito:*
* Implementação da lógica dos cálculos
* Reestruturação da aplicação

*Dificuldades:*
* Conflitos no código causados pelo uso de importação de módulos


**Dia 5 - 06/03/2019**

*O que foi feito:*
* Implementação da funcionalidade que aceita inputs do teclado

*Dificuldades:*
* 

**Maio/2019**

*O que foi feito:*
O código foi publicado no site https://codereview.stackexchange.com para avaliação sugestão de melhorias. Seguindo o feedback dos revisores (presente nas respostas ao tópico em https://codereview.stackexchange.com/questions/219124/calculator-in-python-3-using-tkinter), o código foi completamente refatorado. As principais mudanças implementadas foram:
* Remover o uso do eval para processar os cálculos por trazer vulnerabilidades à aplicação e ser uma solução simplista demais.
* Reduzir a quantidade de módulos. O excesso deles gerava problemas de importação circular.
* Reduzir repetição de código.

*Dificuldades:*
* Implementar o código mais limpo para o layout dos botões

