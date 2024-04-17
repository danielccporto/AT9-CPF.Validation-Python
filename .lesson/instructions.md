<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 9

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar uma nova versão do programa do Exercício 8, incluindo a validação de CPF conforme a descrição a seguir.

## Validação de entrada

Caso um valor de entrada inválido seja detectado, o programa deverá notificar o usuário, **detalhando o problema identificado**, e encerrar a funcionalidade que estava sendo executada, retornando ao menu.

**Atenção:**

- Apenas as validações especificadas a seguir são necessárias. Considere que o usuário respeitará todos os demais aspectos não cobertos por estas especificações.
- Uma revisão dos métodos de strings pode ser útil: https://www.w3schools.com/python/python_ref_string.asp

### CPF

O CPF deverá ser composto por exatamente 11 dígitos e respeitar as regras de formação de um CPF válido.

Além disso, o sistema **NÃO** deve aceitar CPFs emitidos na Região Sudeste (ES, MG, RJ e SP).

*Observações:*

- As regras de formação de um CPF podem ser consultadas em: http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-cpf
- Você pode usar a seguinte ferramenta para gerar CPFs para usar nos testes:
https://www.4devs.com.br/gerador_de_cpf