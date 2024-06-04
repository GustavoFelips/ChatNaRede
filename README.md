# ChatNaRede

Este é um projeto desenvolvido para a disciplina de Redes de Computadores, com o propósito de demonstrar a comunicação entre computadores na mesma rede utilizando sockets.

## Grupo
- Anna Beatryz
- Gustavo Felipe
- Victor Costa

## Ferramentas Utilizadas
- Python 3.12
- Pycharm e Visual Studio Code

## Bibliotecas Python
- sockets 
- threads

## Código base
- https://github.com/MattCrook/python_sockets_multi_threading

## Funcionamento
- **server.py:** Inicia uma conexão através de uma porta específica e um IP, aguardando conexões dos clientes.
- **cliente.py:** Conecta-se ao servidor e inicia uma simulação de chat no terminal.

## Manual de Uso
1. Execute o **server.py** (o IP da máquina atual será automaticamente identificado).
2. Anote o IP exibido no terminal ao executar o **server.py** para se conectar posteriormente.
   ![ip do servidor](https://github.com/GustavoFelips/ChatNaRede/blob/main/ImageREADME/IpServer.png)
3. Configure o **cliente.py** para indicar o IP do servidor:
   - Descomente a linha que adiciona o IP manualmente e comente a linha que pega automaticamente (linha 11).
   - Entre as aspas, coloque o IP do servidor.
   ![Definição de IP](https://github.com/GustavoFelips/ChatNaRede/blob/main/ImageREADME/ConfigIp.png)
4. Execute o **cliente.py** nas máquinas desejadas e inicie a troca de mensagens no terminal.
   ![Envio de mensagem](https://github.com/GustavoFelips/ChatNaRede/blob/main/ImageREADME/Console.png)
5. Todas as mensagens serão enviadas para todos os computadores conectados ao servidor.

*Observação:* Caso o **cliente.py** seja executado na mesma máquina que o **server.py**, não é necessário configurar o IP no **cliente.py**.

*Observação:* Deve haver um único servidor rodando, em uma única máquina. E os clientes podem ser executados em diversos computadores.

