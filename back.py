import os, json

class Register:

    def createFileJSON(self):        
    # Verifica se o arquivo .json existe
    # Caso não, cria o arquivo no diretorio raiz e retorna 0
    # Caso sim, retorna o ultimo id do arquivo

        file_name = 'fichas.json'

        if not os.path.exists(file_name):
            data_json = {}
            with open(file_name, 'w') as file:
                json.dump(data_json, file, indent=4)
            return 0
        else:
            with open(file_name, 'r') as file:
                data_json = json.load(file)
            max_id = max(data_json, key=int)
            return max_id
        
    def registerWorker(self, data):
    # Registra os dados no arquivo .json

        file_name = 'fichas.json'
        file_json = self.createFileJSON()
        
        with open(file_name, 'r') as file:
            data_json = json.load(file)

        if file_json == 0:
            id = 1
        else:
            id = int(file_json) + 1

        data_json[id] = data

        with open(file_name, 'w') as file:
            json.dump(data_json, file, indent=4)

        return id
    
class Worker(Register):

    def __init__(self, worker, age, post, level) -> None:
        self.__worker = worker
        self.__age = age
        self.__post = post
        self.__level = level

    def showInfo(self):

        return {
            "Nome":  self.__worker,
            "Idade": self.__age,
            "Cargo": self.__post,
            "Nivel": self.__level
        }
    
    def calculateBonus(self):

        if self.__level == 'trainee':
            bonus = 1
        elif self.__level == 'junior':
            bonus = 1.5
        elif self.__level == 'pleno':
            bonus = 2
        elif self.__level == 'senior':
            bonus = 2.5
        else:
            bonus = 1

        return bonus
    
class Integral(Worker):

    def __init__(self, company, location, worker, age, post, level, department, salary) -> None:
        super().__init__(worker, age, post, level)
        self.__company = company
        self.__location = location
        self.__worker = worker
        self.__age = age
        self.__post = post
        self.__level = level
        self.__department = department
        self.__salary = salary

    def registerIntegral(self):

        bonus = self.calculateBonus()
        to_receive = self.__salary * bonus

        data = {
            "Empresa":              self.__company,
            "Localizacao":          self.__location,  
            "Tipo":                 "Integral",
            "Nome":                 self.__worker,
            "Idade":                self.__age,
            "Cargo":                self.__post,
            "Nivel":                self.__level,
            "Departamento":         self.__department,
            "Salario":              self.__salary,
            "Salario Hora":         "",
            "Horas Trabalhadas":    "",
            "Curso":                "",
            "Bonus":                bonus,
            "Valor a Receber":      to_receive,
            "Delete":               "n"
        }

        self.registerWorker(data)
        return data
    
class LegalPerson(Worker):

    def __init__(self, company, location, worker, age, post, level, hour_salary, worked_hours) -> None:
        super().__init__(worker, age, post, level)
        self.__company = company
        self.__location = location
        self.__worker = worker
        self.__age = age
        self.__post = post
        self.__level = level
        self.__hour_salary = hour_salary
        self.__worked_hours = worked_hours
        
    def calculateSalary(self):
        return self.__hour_salary * self.__worked_hours

    def registerLegalPerson(self):

        salary = self.calculateSalary()
        bonus = self.calculateBonus()
        to_receive = salary * bonus

        data = {
            "Empresa":              self.__company,
            "Localizacao":          self.__location,  
            "Tipo":                 "Pessoa Juridica",
            "Nome":                 self.__worker,
            "Idade":                self.__age,
            "Cargo":                self.__post,
            "Nivel":                self.__level,
            "Departamento":         "",
            "Salario":              salary,
            "Salario Hora":         self.__hour_salary,
            "Horas Trabalhadas":    self.__worked_hours,
            "Curso":                "",
            "Bonus":                bonus,
            "Valor a Receber":      to_receive,
            "Delete":               "n"
        }

        self.registerWorker(data)
        return data
    
class Trainee(Worker):

    def __init__(self, company, location, worker, age, post, level, salary, course) -> None:
        super().__init__(worker, age, post, level)
        self.__company = company
        self.__location = location
        self.__worker = worker
        self.__age = age
        self.__post = post
        self.__level = level
        self.__salary = salary
        self.__course = course

    def registerTrainee(self):

        bonus = self.calculateBonus()
        to_receive = self.__salary * bonus

        data = {
            "Empresa":              self.__company,
            "Localizacao":          self.__location,  
            "Tipo":                 "Estagiario",
            "Nome":                 self.__worker,
            "Idade":                self.__age,
            "Cargo":                self.__post,
            "Nivel":                self.__level,
            "Departamento":         "",
            "Salario":              self.__salary,
            "Salario Hora":         "",
            "Horas Trabalhadas":    "",
            "Curso":                self.__course,
            "Bonus":                bonus,
            "Valor a Receber":      to_receive,
            "Delete":               "n"
        }

        self.registerWorker(data)
        return data

class Company:

    def register(company, location, worker_type, worker, age, post, level, department, hour_salary, worked_hours, salary, course):

        if worker_type == 'Estagiario':
            data = Trainee(company, location, worker, age, post, level, salary, course)
            data.registerTrainee()
        elif worker_type == 'Integral':
            data = Integral(company, location, worker, age, post, level, department, salary)
            data.registerIntegral()
        elif worker_type == 'Pessoa Juridica':
            data = LegalPerson(company, location, worker, age, post, level, hour_salary, worked_hours)
            data.registerLegalPerson()

    def showRegisters():

        file_name = 'fichas.json'

        if os.path.exists(file_name):

            with open(file_name, 'r') as file:
                data_json = json.load(file)

            file_json = {}
            for row in data_json:
                if data_json[row]['Delete'] == 'n':
                    file_json[row] = data_json[row]

            return file_json
        
        else:
            
            return 'Não há registros!'
    
    def deleteRegister(id):

        file_name = 'fichas.json'
        with open(file_name, 'r') as file:
            data_json = json.load(file)

        data_json[str(id)]['Delete'] = 's'

        with open(file_name, 'w') as file:
            json.dump(data_json, file, indent=4)