import back as bk
import front as ft

if __name__ == '__main__':

    front       = ft.Front
    company     = front.hello()
    data        = bk.Company
    
    while True:
        
        operation = front.typeOperation(company['Empresa'], company['Localizacao'])

        if operation == 0:
            print('Sistema finalizado!')
            break

        elif operation == 1:            
            print(data.showRegisters())

        elif operation == 2:
            worker_type = front.getData(company['Empresa'], company['Localizacao'])

        elif operation == 3:
            front.deleteID(company['Empresa'], company['Localizacao'])

        else:
            print('Favor, informe uma operação válida!')
