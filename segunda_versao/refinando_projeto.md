## Refinando um Sistema Bancário
### Objetivo:
Deixar o código mais modularizado:
Através das funções 'Sacar', 'Depositar' e 'Vizualizar Histórico'
Criar duas novas funções: 'Criar Usuário', vinculada ao cliente; e 'Criar Conta Corrente', vinculada ao Usuário 

### Requisitos:
Utilizando os conhecimentos de separação de funções, através de argumentos posicionais, nomeados e híbridos

#### Operação de depósito (Função depositar):
Deve receber apenas argumentos posicionais
  Argumentos utilizados: 'saldo', 'valor' e 'extrato'
  Retornos informados: 'saldo' e 'extrato'

#### Operação de saque (Função sacar):
Deve receber apenas argumentos nomeados
  Argumentos utilizados: 'saldo', 'valor', 'extrato', 'limite', 'numero_saques' e 'limite_saques'
  Retornos informados: 'saldo' e 'extrato'

#### Operação de extrato (Função exibir_extrato):
Deve receber agumentos tanto nomeados, quanto posicionais
  Argumentos Posicionais utilizados: 'saldo'
  Argumentos Nomeados utilizados: 'extrato'

#### Operação de cadastro de cliente (Função criar_usuario):
Deve armazanar os usuários em lista. Um usuário é composto por 'nome', 'data_nascimento', 'endereço' e 'cpf'
Não é possível cadastrar dois usuários com o mesmo CPF
O 'endereço' e 'cpf' serão em formato String: "Logradouro, nº - Bairro - Cidade/UF" e "somente nmúeros", respectivamente

#### Operação de cadastro de conta bancária (Função criar_conta):
Será uma função vinculada ao usuário (utilização de filtro por CPF informado) e composto por:
  'Titular': O usuário poderá ter mais de uma conta, mas uma conta pertencerá somente à 1 usuário
  'Agência': Será um número fixo "0001"
  'C/C.': começará com "1" e as demais contas serão números sequenciais
