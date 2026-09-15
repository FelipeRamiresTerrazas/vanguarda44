# Vanguarda 44 - Instruções do Projeto

Este arquivo é lido automaticamente no início de cada sessão. Siga estas regras em qualquer edição, criação de arquivo ou revisão neste repositório, mesmo que o pedido do usuário não as repita explicitamente.

## O que é este projeto

Vanguarda 44 é um wargame de miniaturas da Segunda Guerra Mundial, inspirado no Bolt Action. O repositório contém:

- `main.tex` + `partes/00-introducao.tex` a `partes/08-jogando.tex`: o Livro de Regras completo.
- `cartoes/main.tex`: 10 cartões de referência rápida (A6, 2x2 por folha A4, com marcas de corte).
- `guia-rapido/main.tex`: guia de início rápido em prosa explicativa, layout de 2 colunas.
- `expansoes/<nome-do-mini-livro>/main.tex` + `expansoes/<nome-do-mini-livro>/cartoes/main.tex`: mini-livros de expansão (cenários históricos + doutrinas nacionais novas), cada um em sua própria pasta.
- `estilo/vanguarda44.sty`: estilo compartilhado por TODOS os documentos acima (cores, ambiente `nota`, cabeçalho/rodapé, textura de fundo). Mudanças aqui afetam todos os documentos, então só edite este arquivo quando o usuário pedir uma mudança explicitamente global.
- `estilo/cartoes.sty`: ajustes de layout específicos dos cartões (A6, marcas de corte). Não altera o estilo do livro.

## Regra Crítica - Travessões e Hífens

**Nunca escreva o caractere de travessão (—) nem a sequência `---` em nenhum texto novo**, seja no corpo de um `.tex`, num arquivo `.md`, ou em qualquer resposta. Isso vale por dois motivos:

1. **Bug de renderização**: a fonte Carlito usada neste projeto, compilada via `pdflatex`, às vezes não tem glifo mapeado para o caractere de travessão unicode (—), o que gera um quadrado vazio no PDF final em vez do traço.
2. **Estilo de escrita**: o uso excessivo de travessões é um dos sinais mais óbvios de texto gerado por IA. Queremos que o livro pareça escrito por uma pessoa.

**O hífen simples (`-`) é permitido e não tem nenhum dos dois problemas acima** — é um caractere ASCII comum, sem risco de glifo faltando. Use as opções abaixo dependendo do contexto:

- **Hífen simples (`-`)**: a escolha certa para títulos, cabeçalhos e rótulos curtos que precisam de um separador leve (ex.: "Vanguarda 44 - Livro de Regras"). Nunca empilhe separadores diferentes no mesmo título (ex.: NÃO faça "Vanguarda 44: O Wargame: Livro de Regras", com dois dois-pontos seguidos, nem misture dois-pontos com hífen desnecessariamente no mesmo título).
- **Vírgula**: para uma pausa curta dentro de uma frase. "O terreno afeta o movimento, e também a cobertura."
- **Dois pontos**: para introduzir uma explicação dentro do corpo de um parágrafo. "O resultado é claro: a unidade recua." (Evite usar dois pontos em títulos/cabeçalhos que já têm outro separador.)
- **Parênteses**: para um adendo. "A unidade recua (perdendo 1 nível de Stress)."
- **Duas frases separadas**: reestruturar com ponto final, quando nenhuma das opções acima soa natural.

Antes de finalizar qualquer texto novo (incluindo cabeçalhos, títulos de capa e rodapés), revise procurando por "—" e `---` fora de contextos puramente técnicos do LaTeX, e escolha a alternativa acima que fizer mais sentido para aquele contexto específico (hífen para títulos, as demais para prosa).

## Outros sinais de "escrita de IA" a evitar

- Não abra parágrafos com construções tipo "Não é apenas X, é Y" ou "Mais do que simplesmente X, Y representa...".
- Evite listas de 3 itens artificiais só para soar completas (ex.: "rápido, eficiente e envolvente"), quando 1 ou 2 adjetivos bastariam.
- Evite frases de efeito genéricas de encerramento tipo "E assim, a batalha continua..." repetidas em todo cenário. Cada cenário deve ter uma conclusão específica ao contexto histórico dele, não uma fórmula repetida.
- Prefira frases mais curtas e diretas a períodos longos e encadeados. O tom estabelecido no livro (nas aberturas de Parte e nos cenários) é envolvente mas econômico, não florido.

## Convenções de LaTeX

- **Referências cruzadas**: use sempre `\label{}` e `\ref{}` para apontar a outras seções (ex.: `\label{sec:perda-assistente}` e depois `\ref{sec:perda-assistente}`). Nunca escreva números de seção fixos no texto (tipo "veja a seção 14.3" ou "veja 20.1-20.3"): eles ficam desatualizados assim que qualquer conteúdo é adicionado antes daquele ponto no documento.
- **Tabelas**: use o padrão já estabelecido (`\toprule`/`\midrule`/`\bottomrule` do `booktabs`, ou o padrão de tabela usado nos arquivos existentes). Mantenha larguras de coluna consistentes com o resto do documento onde fizer sentido.
- **Caixas de nota**: use o ambiente `nota` já definido no `.sty` para observações e esclarecimentos táticos, não invente um novo estilo de caixa sem necessidade. O ambiente `nota` usa `breakable=false` de propósito (uma caixa que se parte ao meio de uma coluna ou página fica com aparência quebrada); não reative `breakable` nele sem testar antes.
- **Não reordene ou renumere Partes existentes** sem confirmação explícita do usuário: a estrutura atual (Fundamentos, Movimento, Combate, Esquadrão, Suporte, Comando, Exércitos, Jogando) foi mantida de propósito numa revisão anterior.

## Mudanças visuais/de layout em todo o projeto: sempre testar antes de aplicar

Qualquer mudança que afete `estilo/vanguarda44.sty` ou `estilo/cartoes.sty` (cores, fontes, texturas de fundo, número de colunas, espaçamento) impacta múltiplos documentos de uma vez. Antes de aplicar uma mudança desse tipo em todo o projeto:

1. Crie uma cópia de teste isolada (um `.sty` e um `.tex` de exemplo, fora da estrutura principal, ou num branch/pasta temporária) reproduzindo uma página real do livro com o conteúdo já existente (não invente conteúdo novo só para o teste).
2. Compile e gere uma imagem da página de teste.
3. Só aplique a mudança nos arquivos reais do projeto depois que o usuário confirmar visualmente que gostou do resultado.

Isso já economizou retrabalho nas mudanças de paleta de cores e no teste de layout em duas colunas: encontramos e corrigimos um bug real (caixa de Nota quebrando ao meio numa coluna) antes dele chegar ao livro publicado.

## Decisões de design já testadas e descartadas (não reabrir sem pedido explícito)

- **Layout de duas colunas no Livro de Regras principal**: foi testado (com tabelas largas quebrando para ocupar a página inteira) e funcionou tecnicamente, mas o usuário achou o resultado visual estranho. O livro principal permanece em coluna única. O Guia Rápido continua sendo a exceção que já usa duas colunas de propósito.

## Cuidado com custo de impressão em mudanças visuais

Este livro é feito para ser impresso fisicamente pelo usuário. Qualquer elemento visual que cubra a página inteira (cor de fundo, textura, imagem) deve usar tons muito claros (próximos de branco, brilho médio de pixel acima de ~230/255) para não gastar tinta desnecessariamente. Já reduzimos a intensidade de uma textura de fundo por esse motivo; trate isso como um princípio permanente de design para qualquer proposta futura, não só para essa vez.

## Estrutura de um Cenário (mini-livros de expansão)

Todo cenário histórico, em qualquer mini-livro atual ou futuro, segue exatamente esta ordem de campos:

1. **Contexto Histórico**: 1 parágrafo curto, factual, sem diálogos inventados atribuídos a pessoas reais.
2. **Data e Local**
3. **Forças** (quem ataca, quem defende, ou "Simétrico/Encontro")
4. **Terreno**
5. **Implantação**
6. **Qualidade de Tropa** por lado (ver regra abaixo, isso é sempre definido no cenário, nunca fixo por exército)
7. **Regra Especial do Cenário** (a assimetria histórica específica daquele confronto)
8. **Objetivo e Condições de Vitória**
9. **Duração Sugerida** (limite de turnos)

Cada cenário também deve gerar 1 cartão de referência correspondente (A6), na pasta `cartoes/` do mini-livro, contendo: nome, data/local resumidos, Qualidade de Tropa, Regra Especial completa, Objetivo e Duração (sem o Contexto Histórico, que fica só no texto do mini-livro).

## Regras de design já fechadas (não reabrir sem pedido explícito)

- **Qualidade de Tropa (Inexperiente/Regular/Veterana) nunca é fixa por exército ou doutrina.** É sempre definida pelo cenário escolhido. As mesmas miniaturas podem ser Veteranas num cenário e Regulares em outro.
- **Esquadrão de Infantaria sempre ocupa exatamente 10 espaços de dado**, nunca mais, nunca menos. O número de homens varia conforme o equipamento escolhido, mas o total de slots é sempre 10.
- **Sistema de Stress usa um único dado d6 vermelho por unidade** (Nível de Stress de 1 a 6), não marcadores empilhados. Veteranos ignoram o 1º nível de Stress recebido por turno.
- **Sequência de Disparo**: Passo A (Acerto, base 4+), depois Passo B (Dano, TN por qualidade de tropa), depois Passo C (Stress). Bazooka contra infantaria e Granadas usam um perfil simplificado à parte (1D6 acerto + 1D6 dano), documentado na Parte V do livro principal.
- **Perda do Assistente** (regra geral para LMG, Bazooka, HMG, Sniper, Morteiros): a arma nunca para de atirar, mas sofre -1 permanente no Acerto e perde o direito de usar a ordem Avançar.
- **Convenção Universal de Dados**: um resultado natural de 6 em qualquer rolagem de acerto/teste sempre é sucesso (ignorando modificadores), e um natural 1 sempre é falha. Isso vale para todo o livro, não só para a Sequência de Disparo padrão (inclui Bazooka, Granadas, Tiro Selecionado do Sniper, Ajuste de Mira de Morteiro).

## Processo de trabalho

- Depois de qualquer criação ou edição, **sempre recompile** o(s) documento(s) afetado(s) e confirme que não há erros antes de reportar como concluído.
- Sempre informe o número final de páginas do(s) PDF(s) afetado(s) ao concluir uma tarefa.
- Não modifique `main.tex`, `cartoes/main.tex`, `guia-rapido/main.tex` ou `estilo/vanguarda44.sty` ao trabalhar em um mini-livro de expansão, a menos que isso seja pedido explicitamente.
