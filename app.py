import mysql.connector

# Create Querie

criar_tabela_job = """
    CREATE TABLE IF NOT EXISTS `Job` (
        `JobID` INT NOT NULL AUTO_INCREMENT,
        `Name` NVARCHAR(100) NOT NULL,
        `Description` NVARCHAR(100) NOT NULL,
    PRIMARY KEY (`JobID`))
"""

criar_tabela_employee = """
    CREATE TABLE IF NOT EXISTS `Employee` (
        `EmployeeID` INT NOT NULL AUTO_INCREMENT,
        `JobID` INT NOT NULL,
        `Name` NVARCHAR(100) NOT NULL,
        `Birthday` DATE NOT NULL,
        `Salary` FLOAT(10,2) NOT NULL,
        `Department` NVARCHAR(100) NOT NULL,
    PRIMARY KEY (`EmployeeID`),
    INDEX `job_employee_idx` (`JobID` ASC),
    CONSTRAINT `job_employee`
        FOREIGN KEY (`JobID`)
        REFERENCES `Job` (`JobID`)
        ON DELETE CASCADE
        ON UPDATE CASCADE)
"""

criar_tabela_jobhistory = """
    CREATE TABLE IF NOT EXISTS `JobHistory` (
        `JobHistoryID` INT NOT NULL AUTO_INCREMENT,
        `EmployeeID` INT NOT NULL,
        `Title` NVARCHAR(100) NOT NULL,
        `StartDate` DATE NOT NULL,
        `EndDate` DATE NOT NULL,
        `Salary` FLOAT(10,2) NOT NULL,
        `Job` NVARCHAR(100) NOT NULL,
    PRIMARY KEY (`JobHistoryID`),
    INDEX `employee_jobhistory_idx` (`EmployeeID` ASC),
    CONSTRAINT `employee_jobhistory`
        FOREIGN KEY (`EmployeeID`)
        REFERENCES `Employee` (`EmployeeID`)
        ON DELETE CASCADE
        ON UPDATE CASCADE)
"""

# Select Querie
 
tabela_job = """
    SELECT * FROM JOB
"""

tabela_employee = """
    SELECT E.EmployeeID, 
	   E.Name 'EmployeeName', 
       E.Birthday, 
       E.Salary, 
       E.JobID, 
       J.Name 'JobName', 
       J.Description "JobDescription",
       E.Department
	FROM employee E
    inner join job J on E.JobID = J.JobID
"""

tabela_jobhistory = """
    SELECT JH.JobHistoryID, 
	   JH.EmployeeID,
       E.Name,
       JH.Title,
       JH.StartDate,
       JH.EndDate,
       JH.Salary,
       JH.Job
	FROM jobhistory JH
    INNER JOIN employee E on JH.EmployeeID = E.EmployeeID;
"""

# Insert Querie

inserir_tabela_job = """
    INSERT INTO job (Name, Description)
        VALUES (%s, %s)
"""

inserir_tabela_employee = """
    INSERT INTO employee (JobID, Name, Birthday, Salary, Department)
        VALUES (%s, %s, %s, %s, %s)
"""

inserir_tabela_jobhistory = """
    INSERT INTO JobHistory (EmployeeID, Title, StartDate, EndDate, Salary, Job)
        VALUES (%s, %s, %s, %s, %s, %s)
"""

# Update Query

update_job = """
    UPDATE Job 
        SET Name = %s,
            Description = %s
    WHERE JobID = %s
"""

update_employee = """
    UPDATE employee 
        SET JobID = %s,
            Name = %s,
            Birthday = %s,
            Salary = %s,
            Department = %s
    WHERE EmployeeID = %s
"""

update_jobhistory = """
    UPDATE JobHistory 
        SET EmployeeID = %s,
            Title = %s,
            StartDate = %s,
            EndDate = %s,
            Salary = %s,
            Job = %s
    WHERE JobHistoryID = %s
"""

# Delete Querie

delete_job = """
    DELETE FROM Job
        WHERE JobID = %s
"""

delete_employee = """
    DELETE FROM employee
        WHERE EmployeeID = %s
"""

delete_jobhistory = """
    DELETE FROM JobHistory
        WHERE JobHistoryID = %s
"""

con = mysql.connector.connect(host='localhost', database='Job', user='root', password='root')

# Funções Create

def criarTabelas():
    cursor = con.cursor()

    cursor.execute(criar_tabela_job)
    cursor.execute(criar_tabela_employee)
    cursor.execute(criar_tabela_jobhistory)

    con.commit()

# Funções Insert 

def criarJob(Nome, Descricao):
    cursor = con.cursor()

    cursor.execute(inserir_tabela_job, (Nome, Descricao))

    con.commit()

def criarEmployee(JobID, Nome, Aniversario, Salario, Departamento):
    cursor = con.cursor()

    cursor.execute(inserir_tabela_employee, (JobID, Nome, Aniversario, Salario, Departamento))

    con.commit()

def criarJobHistory(EmployeeID, Titulo, Inicio, Fim, Salario, Job):
    cursor = con.cursor()

    cursor.execute(inserir_tabela_jobhistory, (EmployeeID, Titulo, Inicio, Fim, Salario, Job))

    con.commit()

# Funções Select

def buscarJobs():
    cursor = con.cursor()

    cursor.execute(tabela_job)

    return cursor.fetchall()

def buscarEmployees():
    cursor = con.cursor()

    cursor.execute(tabela_employee)

    return cursor.fetchall()

def buscarJobHistorys():
    cursor = con.cursor()

    cursor.execute(tabela_jobhistory)

    return cursor.fetchall()

# Função Update

def updateJob(JobID, Nome, Descricao):
    cursor = con.cursor()

    cursor.execute(update_job, (Nome, Descricao, JobID))

    con.commit()

def updateEmployee(EmployeeID, JobID, Nome, Aniversario, Salario, Departamento):
    cursor = con.cursor()

    cursor.execute(update_employee, (JobID, Nome, Aniversario, Salario, Departamento, EmployeeID))

    con.commit()


def updateJobHistory(JobHistoryID, EmployeeID, Titulo, Inicio, Fim, Salario, Job):
    cursor = con.cursor()

    cursor.execute(update_jobhistory, (EmployeeID, Titulo, Inicio, Fim, Salario, Job, JobHistoryID))

    con.commit()

# Função Delete

def deleteJob(JobID):
    cursor = con.cursor()

    cursor.execute(delete_job, (JobID,))

    con.commit()
    
def deleteEmployee(EmployeeID):
    cursor = con.cursor()

    cursor.execute(delete_employee, (EmployeeID,))

    con.commit()

def deleteJobHistory(JobHistoryID):
    cursor = con.cursor()

    cursor.execute(delete_jobhistory, (JobHistoryID,))

    con.commit()


# Programa
criarTabelas()

while True:
    print("""
1- Cargos
2- Funcionários
3- Histórico
4- Finalizar   
    """)
    opcao = int(input("Qual opção deseja? "))

    if opcao == 1:
        while True:
            print("""
                Cargos:
                    1- Cadastrar 
                    2- Atualizar
                    3- Listar
                    4- Deletar
                    5- Voltar 
            """)
            
            opcao1 = int(input("                Qual opção deseja? "))

            if opcao1 == 1:
                nome = input("\n                   Qual o nome do cargo? ")
                descricao = input("                   Qual o nome da descricao? ")

                criarJob(nome, descricao)
                print(f"\n                Cargo {nome} cadastrado com sucesso!")
            elif opcao1 == 2:
                id = int(input("\n                   Qual o ID do cargo que deseja atualizar? "))
                nome = input("                   Qual o nome do cargo? ")
                descricao = input("                   Qual o nome da descricao? ")

                updateJob(id, nome, descricao)
                print(f"\n                Cargo {nome} atualizado com sucesso!")

            elif opcao1 == 3:    
                cargos = buscarJobs()
                funcionarios = buscarEmployees()
                print("\n                Cargos:")
                for cargo in cargos:
                    id = cargo[0]
                    nome = cargo[1]
                    descricao = cargo[2]
                    print(f"                  #{id}:")
                    print(f"                     Nome: {nome}")
                    print(f"                     Descrição: {descricao}")
                    print("                     Funcionários:")
                    for funcionario in funcionarios:
                        idFunc = funcionario[0]
                        nomeF = funcionario[1]
                        idJob = funcionario[4]
                        if idJob == id:
                            print(f"                       #{idFunc} - {nomeF}")
            elif opcao1 == 4:
                id = int(input("\n                   Qual o ID do cargo que deseja deletar? "))

                deleteJob(id)
                
                print(f"\n                Cargo {id} deletado com sucesso!")
            elif opcao1 == 5:    
                break
    elif opcao == 2: 
        while True:
            print("""
                Funcionários:
                    1- Cadastrar 
                    2- Atualizar
                    3- Listar
                    4- Deletar
                    5- Voltar 
            """)

            opcao2 = int(input("                Qual opção deseja? "))
            if opcao2 == 1:
                Nome = input("\n                   Qual o nome do funcionário? ")
                Aniversario = input("                   Qual a data de aniversário? (AAAA-mm-dd) ")
                Salario = float(input("                   Qual o salário? "))
                JobID = int(input("                   Qual o ID do cargo? "))
                Departamento = input("                   Qual o departamento? ")

                criarEmployee(JobID, Nome, Aniversario, Salario, Departamento)
                print(f"\n               Funcionário {Nome} cadastrado com sucesso!")
            elif opcao2 == 2:
                id = int(input("\n                   Qual o ID do funcionário que deseja atualizar? "))
                Nome = input("                   Qual o nome do funcionário? ")
                Aniversario = input("                   Qual a data de aniversário? (AAAA-mm-dd) ")
                Salario = float(input("                    Qual o salário? "))
                JobID = int(input("                   Qual o ID do cargo? "))
                Departamento = input("                   Qual o departamento? ")

                updateEmployee(id, JobID, Nome, Aniversario, Salario, Departamento)
                print(f"\n               Funcionário {Nome} atualizado com sucesso!")

            elif opcao2 == 3:    
                funcionarios = buscarEmployees()
                historicos = buscarJobHistorys()
                print("\n                  Funcionários:")
                for funcionario in funcionarios:
                    id = funcionario[0]
                    nome = funcionario[1]
                    aniversario = funcionario[2]
                    salario = funcionario[3]
                    cargo = funcionario[5]
                    departamento = funcionario[6]
                    print(f"                    #{id}:")
                    print(f"                        Nome: {nome}")
                    print(f"                        Aniversário: {aniversario}")
                    print(f"                        Salário: {salario}")
                    print(f"                        Cargo: {cargo}")
                    print(f"                        Departamento: {departamento}")
                    print(f"                        Histórico:")
                    
                    for historico in historicos:
                        idE = historico[1]
                        if idE == id:
                            print(f"                          ID #{historico[0]}:")
                            print(f"                            Titulo: {historico[3]}")
                            print(f"                            Início: {historico[4]}")
                            print(f"                            Fim: {historico[5]}")
                            print(f"                            Salário: {historico[6]}")
                            print(f"                            Cargo: {historico[7]}")
            elif opcao2 == 4:
                id = int(input("\n                   Qual o ID do funcionário que deseja deletar? "))

                deleteEmployee(id)
                
                print(f"\n                Funcionário {id} deletado com sucesso!")
                
            elif opcao2 == 5:    
                break
    elif opcao == 3: 
        while True:
            print("""
                Histórico:
                    1- Cadastrar 
                    2- Atualizar
                    3- Deletar
                    4- Voltar 
            """)
            
            opcao3 = int(input("                Qual opção deseja? "))
            if opcao3 == 1:
                idFunc = input("\n                   Qual o ID do funcionário? ")
                titulo = input("                   Qual o titulo? ")
                inicio = input("                   Qual a data de ínicio? (AAAA-mm-dd) ")
                fim = input("                   Qual a data de fim? (AAAA-mm-dd) ")
                salario = float(input("                   Qual o salário? "))
                cargo = input("                   Qual o cargo? ")

                criarJobHistory(idFunc, titulo, inicio, fim, salario, cargo)
                print(f"\n               Historico {titulo} cadastrado com sucesso!")
            elif opcao3 == 2:
                id = int(input("\n                   Qual o ID do histórico que deseja atualizar? "))
                idFunc = input("\n                   Qual o ID do funcionário? ")
                titulo = input("                   Qual o titulo? ")
                inicio = input("                   Qual a data de ínicio? (AAAA-mm-dd) ")
                fim = input("                   Qual a data de fim? (AAAA-mm-dd) ")
                salario = float(input("                   Qual o salário? "))
                cargo = input("                   Qual o cargo? ")

                updateJobHistory(id, idFunc, titulo, inicio, fim, salario, cargo)
                print(f"\n               Histórico {Nome} atualizado com sucesso!")

            elif opcao3 == 3:
                id = int(input("\n                   Qual o ID do histórico que deseja deletar? "))

                deleteJobHistory(id)
                
                print(f"\n                Histórico {id} deletado com sucesso!")
                
            elif opcao3 == 4:    
                break
    elif opcao == 4:
        print("\nPrograma Finalizado!")
        break