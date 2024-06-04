# ChatNaRede

Este é um projeto desenvolvido como parte do currículo da disciplina de Redes de Computadores. O objetivo é demonstrar a comunicação entre computadores na mesma rede utilizando sockets.

![ChatNaRede Demo](https://caminho/para/a/imagem.jpg)

## Grupo
- Anna Beatryz
- Gustavo Felipe
- Victor Costa

## Ferramentas Utilizadas
- Python 3.12
- Pycharm e Visual Studio Code

## Bibliotecas Python
- sockets 
- threadsc

## Funcionamento
- **server.py:** Inicia uma conexão através de uma porta específica e um IP, aguardando conexões dos clientes.
- **cliente.py:** Conecta-se ao servidor e inicia uma simulação de chat no terminal.

## Manual de Uso
1. Execute o **server.py** (o IP da máquina atual será automaticamente identificado).
2. Anote o IP exibido no terminal ao executar o **server.py** para se conectar posteriormente.
![ip do servidor](https://caminho/para/a/imagem.jpg)
3. Configure o **cliente.py** para indicar o IP do servidor.
![Definição de ip](https://caminho/para/a/imagem.jpg)
4. Execute o **cliente.py** nas máquinas desejadas e inicie a troca de mensagens no terminal.
5. Todas as mensagens serão enviadas para todos os computadores conectados ao servidor.

*Observação:* Caso o **cliente.py** seja executado na mesma máquina que o **server.py**, não é necessário configurar o IP no **cliente.py**.
