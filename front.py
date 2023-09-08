import back as bk

class Front:

    def hello():

        print('=' * 100)
        print('Olá!\n')
        company = input('Favor informe o nome da empresa: ')
        location = input('Favor informe a localização da empresa: ')

        data = {}
        data['Empresa'] = company
        data['Localizacao'] = location

        return data
    
    def typeOperation(company, location):

        print('=' * 100)
        print(f'Empresa: {company}. Localização: {location}.')
        print('\nQual tipo de operação deseja realizar?')
        type_operation = int(input('1 - Consultar Registros\n2 - Registrar\n3 - Excluir Registros\n0 - Sair\n'))

        return type_operation
    
    def getData(company, location):
        
        data = {}
        data['Empresa'] = company
        data['Localizacao'] = location

        while True:

            print('=' * 100)
            print(f'Empresa: {company}. Localização: {location}.')
            print('Qual tipo de colaborador abaixo, deseja registrar?')
            worker_type = int(input('1 - Estagiario\n2 - Integral\n3 - Pessoa Juridica\n0 - Cancelar\n'))                       

            if worker_type == 0:
                break

            elif worker_type == 1:
                
                print('Informe os dados abaixo:') 
                worker  = input('Nome: ')
                age     = int(input('Idade: '))
                post    = input('Cargo: ')
                level   = input('Nivel (Trainee, Junior, Pleno ou Senior): ').lower()
                course  = input('Curso: ')
                salary  = float(input('Salario: '))            
                
                data['Tipo']                = 'Estagiario'
                data['Nome']                = worker
                data['Idade']               = age
                data['Cargo']               = post
                data['Nivel']               = level
                data['Departamento']        = ''
                data['Salario Hora']        = ''
                data['Horas Trabalhadas']   = ''
                data['Salario']             = salary
                data['Curso']               = course     

                break

            elif worker_type == 2:
                
                print('Informe os dados abaixo:') 
                worker  = input('Nome: ')
                age     = int(input('Idade: '))
                post    = input('Cargo: ')
                level   = input('Nivel (Trainee, Junior, Pleno ou Senior): ').lower()
                depart  = input('Departamento: ')
                salary  = float(input('Salario: ')) 

                data['Tipo']                = 'Integral'
                data['Nome']                = worker
                data['Idade']               = age
                data['Cargo']               = post
                data['Nivel']               = level
                data['Departamento']        = depart
                data['Salario Hora']        = ''
                data['Horas Trabalhadas']   = ''
                data['Salario']             = salary
                data['Curso']               = ''

                break

            elif worker_type == 3:
                
                print('Informe os dados abaixo:') 
                worker  = input('Nome: ')
                age     = int(input('Idade: '))
                post    = input('Cargo: ')
                level   = input('Nivel (Trainee, Junior, Pleno ou Senior): ').lower()
                shour   = float(input('Salario Hora: '))
                whour   = int(input('Horas Trabalhadas: '))

                data['Tipo']                = 'Pessoa Juridica'
                data['Nome']                = worker
                data['Idade']               = age
                data['Cargo']               = post
                data['Nivel']               = level
                data['Departamento']        = ''
                data['Salario Hora']        = shour
                data['Horas Trabalhadas']   = whour
                data['Salario']             = ''
                data['Curso']               = ''

                break

            else:
                print('Favor, informe uma operação válida!')

        if 'Tipo' in data:    
            data_company = bk.Company
            data_company.register(
                data['Empresa'], data['Localizacao'], data['Tipo'], data['Nome'],
                data['Idade'], data['Cargo'], data['Nivel'], data['Departamento'],
                data['Salario Hora'], data['Horas Trabalhadas'], data['Salario'] ,
                data['Curso']
            )

    def deleteID(company, location):

        print('=' * 100)
        print(f'Empresa: {company}. Localização: {location}.')
        register_id = input('\nInforme o ID do registro que deseja excluir ou 0 para cancelar a operação?\n')

        if register_id != '0':
            data_company = bk.Company
            data_company.deleteRegister(register_id)