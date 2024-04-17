nomes = []
sobrenomes = []
datas = []
cpfs = []
ID = []
indice1=0
indice2=0
listaopcoes = [1,2,3,4,5,6]

nome = ""
nome1= ""
nome2= ""
sobrenome = ""
data = ""
CP = 0
cadastro = 0
cadastro_2 = 0



print("1.Inserir novo cadastro:")
print("2.Alterar CPF: ")
print("3.Trocar Sobrenomes: ")
print("4.Remover cadastro: ")
print("5. Listar todos os cadastros.")
print("6. Encerrar")


opcao = int(input("Insira o número da sua escolha: "))

while opcao in listaopcoes: 

  if opcao == 1 :

    cadastro = (input("Digite seu ID: "))

    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")

    else:
      if cadastro in ID:
        print(f"O ID {cadastro} já está cadastrado.")

      nome = input("Digite seu nome: ")
      nome = nome.capitalize()

      if " " in nome: 
        print("O nome não pode ter espaço.")

      else:
        sobrenome = input("Digite seu sobrenome: ")
        sobrenome.capitalize()

        if " " in sobrenome: 
          print("O sobrenome não pode ter espaço")

        else:
          data = input("Digite sua data de nascimento: ")
          CP = input("Digite seu CPF: ")
          
          print(f'O len de CP é: {len(CP)}, CP3: {CP[3]}, CP7: {CP[7]}, CP11: {CP[11]}')
          
          if len(CP) != 14 or CP[3] != "." or CP[7] != "." or CP[11] != "-" : 
            print("O CPF deve ter 11 dígitos e deve estar na formatação xxx.xxx.xxx-xx")
            
            print(cpfs[int(CP)])
            print(CP[10])
                          
          elif int(CP[10]) == 6 or int(CP[10]) == 7 or int(CP[10]) == 8: 
              print("Cpfs de ES, MG, RJ e SP não são aceitos, tente de novo.")
          
          elif cadastro in ID: 
            ID.insert(int(cadastro) -1, cadastro)
            nomes.insert(int(cadastro) -1, nome)
            sobrenomes.insert(int(cadastro) -1, sobrenome)
            cpfs.insert(int(cadastro) -1, CP)
            datas.insert(int(cadastro)-1 , data)

            print("O novo cadastro foi registrado. ")
          else :
            nomes.append(nome)
            sobrenomes.append(sobrenome)
            ID.append(cadastro)
            datas.append(data)
            cpfs.append(CP)

            print("Cadastro realizado com sucesso!")

  elif opcao == 2 : 
    
    valid=False
    while not valid:
      
      cadastro = (input("Digite seu ID: "))

      if not cadastro.isdigit():
        print("O ID precisa ser um número inteiro e positivo, tente de novo.")

      else:
        if cadastro not in ID:
          print(f"O ID {cadastro} não está cadastrado, tente de novo.")
          
        else: 
          CP = (input("Digite o novo CPF: "))
          
          if len(CP) != 14 or CP[3] != "." or CP[7] != "." or CP[11] != "-" : 
            print("O CPF deve ter 11 dígitos e deve estar na formatação xxx.xxx.xxx-xx")
            
            print(cpfs[int(CP)])
            print(CP[10])

          elif int(CP[10]) == 6 or int(CP[10]) == 7 or int(CP[10]) == 8: 
              print("Cpfs de ES, MG, RJ e SP não são aceitos, tente de novo.")
        
          else:
            valid=True 
            
            if cadastro in ID:
              cpfs[int(cadastro) -1] = CP

              print(f"O CPF {cpfs[int(cadastro)-1]} foi alterado com sucesso!")
            else: 
              print("O CPF não está cadastrado, tente de novo.")
            
  elif opcao == 3: 
    
    cadastro = (input("Digite seu ID: "))

    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")

    else:
      if cadastro in ID:

        print(f"O ID {cadastro} já está cadastrado.")
        
        cadastro2 = input("Digite o 2o ID de registro: ")
        
        nome1 = sobrenomes[int(cadastro) -1]
        nome2 = sobrenomes[int(cadastro_2) -1]

        print(f"nome1: {nome1}, nome2 : {nome2}")

        sobrenomes[int(cadastro) -1] = nome2
        sobrenomes[int(cadastro_2) -1] = nome
        
        print(f"sobrenome1: {sobrenomes[int(cadastro) -1]} e sobrenome 2 : {sobrenomes[int(cadastro_2) -1]}")

      

      else:
        print(f"O sobrenome não está registrado, tente de novo!")

  elif opcao == 4  : 
    cadastro = (input("Digite seu ID: "))

    if not cadastro.isdigit():
      print("O ID precisa ser um número inteiro e positivo, tente de novo.")

    else:
      if cadastro in ID:

        print(f"O ID {cadastro} já está cadastrado.")
        del nomes[int(cadastro)-1]
        del sobrenomes[int(cadastro)-1]
        del datas[int(cadastro)-1]
        del cpfs[int(cadastro)-1]
        del ID[int(cadastro)-1]
        print(f"O ID {cadastro} foi removido!")

      else: 
        print(f"O ID {cadastro} não está registrado, tente de novo.")

  elif opcao == 5:
    for i in range(len(ID)):
      print(f"Nome : {nomes[int(i)]},Sobrenome: {sobrenomes[int(i)]}, CPF : {cpfs[int(i)]}, Data de nascimento : {datas[int(i)]}, ID : {ID[int(i)]}")
    else: 
      print("Não há cadastros registrados.")

  elif opcao == 6:
    
    print("O programa está sendo encerrado.")
    break

  print("1.Inserir novo cadastro:")
  print("2.Alterar CPF: ")
  print("3.Trocar Sobrenomes: ")
  print("4.Remover cadastro: ")
  print("5. Listar todos os cadastros.")
  print("6. Encerrar")
  opcao = int(input("Escolha uma opção: "))