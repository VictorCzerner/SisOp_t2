# Manual de execução do programa
O programa foi desenvolvido em Python 3.12.10 e a sua execução não exige a instalação de bibliotecas adicionais.

Para testar o programa é necessário executar o arquivo `main.py` com os argumentos:

### `--input`: Define o caminho relativo para o arquivo .txt que será utilizado como entrada, os exemplos utilizados para teste estão no na pasta `entradas/`.

### `--method`: Define o método de alocação que será executando, as opções válidas deste argumento são `worst-fit`, `circular-fit` e `buddy`

### `--size`: Define o tamanho da memória principal a ser empregada.

# exemplos de execução

#### Exemplo para alocação dinâmica em memória de 16 posições presente no enunciado do trabalho:
```sh 
python main.py --method worst-fit --size 16 --input entradas\exemplo_enunciado.txt
```

#### Exemplo para o sistema buddy, também baseado no exemplo do enunciado:
```sh 
python main.py --method buddy --size 256 --input entradas\buddy.txt
```
