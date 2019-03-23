# hackathon_speech

## Configuração inicial

Para configurar o projeto, comece clonando esse repositório:

```bash
$ git clone https://github.com/mauodias/hackathon_speech.git
```

Feito isso, entre na pasta do repositório e digite o comando `make` para configurar o ambiente: 

```bash
$ cd hackathon_speech
$ make
```

Nessa mesma pasta, crie um arquivo json chamado `times.json` contendo os grupos e os membros de cada grupo. O campo "primeiro_nome" deve ser único no arquivo inteiro. O modelo abaixo pode ser usado como base:

```json
{
  "times": [
    {
      "nome": "Time 1",
      "membros": [
        {"primeiro_nome": "fulano", "nome_completo": "Fulano de Tal Peçanha"},
        {"primeiro_nome": "sicrano", "nome_completo": "Sicrano da Silva Antão"}
      ]
    },
    {
      "nome": "Time 2",
      "membros": [
        {"primeiro_nome": "beltrano", "nome_completo": "Beltrano de Tal Peçanha"},
        {"primeiro_nome": "joano", "nome_completo": "Joano da Silva Antão"}
      ]
    },
    {
      "nome": "Time 3",
      "membros": [
        {"primeiro_nome": "albano", "nome_completo": "Albano de Tal Peçanha"},
        {"primeiro_nome": "todoano", "nome_completo": "Todoano da Silva Antão"}
      ]
    },
    {
      "nome": "Time 4",
      "membros": [
        {"primeiro_nome": "cansano", "nome_completo": "Cansano de Tal Peçanha"},
        {"primeiro_nome": "jonas", "nome_completo": "Jonas Glauber"}
      ]
    }
  ]
}
```

Com o ambiente configurado, digite `make run` para executar a aplicação:

```bash
$ make run
```

A aplicação consiste de uma CLI onde, ao inserir o primeiro nome de uma pessoa que conste no arquivo `times.json`, reproduzirá em voz alta e escreverá na tela uma frase informando a qual time a pessoa pertence:

```
> todoano
# Todoano da Silva Antão: você está no Time 3
```

Para sair da aplicação, basta digitar `q` e pressionar Enter.
