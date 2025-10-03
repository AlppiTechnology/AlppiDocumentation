# Employee

**Get Employee**

---

## **<element class="http-get">GET<element>** - /empoyee/<element class="path-get">pk_user</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de um colaborador específico.

| Name            | In             | Type   | Default | Nullable | Description                     |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**           |
| `pk_user`       | path variables | string | None    | No       | Obtained in **_List Employee_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_user": 2,
                "registration": "00002",
                "username": "Administrador",
                "cpf": "02353336035",
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "phone": "54992358847",
                "email": "admin@admin.com",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2024-05-27T23:29:45",
                "edited": "2024-05-27T23:29:40",
                "last_login": "2024-06-28T18:12:15",
                "is_superuser": false,
                "is_staff": false,
                "is_active": true,
                "employee_groups": [
                    "Administrador"
                ]
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_user": integer,
                "registration": string,
                "username": string,
                "cpf": string,
                "fk_campus": integer,
                "campus_name": string,
                "phone": string,
                "email": string,
                "fk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string,
                "sex": string,
                "birth_date": string,
                "created": string,
                "edited": string,
                "last_login": string,
                "is_superuser": boolean,
                "is_staff": boolean,
                "is_active": boolean,
                "employee_groups": list
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este User.",
                "render": 1
            }
        ```

        ??? info "Schema"

            ``` { .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail":  "Este usuario não é um Colaborador"
            }
        ```

        ??? info "Schema"

            ``` { .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao visualizar Usuario.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---

**List Employee**

## **<element class="http-get">GET<element>** - /empoyee/list/

??? note "Description"

    ### Description
    Lista todos os colaboradores cadastrados no sistema.

| Name            | In          | Type   | Default | Nullable | Description           |
| :-------------- | :---------- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header      | string | None    | No       | Obtained in **Login** |
| `page`          | query param | string | 1       | Yes      |                       |
| `page_size`     | query param | string | 30      | Yes      |                       |
| `search`        | query param | string | None    | Yes      | Name user to search   |
| `status`        | query param | string | 1       | Yes      | 1-Active/0-Inative    |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/employee/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/empoyee/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_user": 5,
                    "registration": "00003",
                    "username": "Professor 2",
                    "is_active": true
                },
                {
                    "pk_user": 7,
                    "registration": "00005",
                    "username": "Professor 3",
                    "is_active": true
                },
                {
                    "pk_user": 8,
                    "registration": "00006",
                    "username": "Professor 4",
                    "is_active": true
                }
            ]
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
        "navigation": {
            "next": string,
            "previous": string
        },
        "next": integer,
        "previous": integer,
        "count": integer,
        "results": list
        }

        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os Usuarios.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---


**Get Employee File Template**

---

## **<element class="http-get">GET<element>** - /empoyee/gettemplate/

??? note "Description"

    ### Description
    Baixa o arquivo de template para criação em massa de usuarios

| Name            | In             | Type   | Default | Nullable | Description                     |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**           |

### **Response Body**

??? success "200"

    === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        ```
        Arquivo cadastro-employee.xlsx
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        N/A
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Arquivo não encontrado",
                "render": 0
            }
        ```

        ??? info "Schema"

            ``` { .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao buscar arquivo para Download",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---



**Upload EmployeeFile Template**

## **<element class="http-post">POST<element>** - /empoyee/uploadfile/

??? note "Description"

    ### Description
    Rota para criação de colaboradores em massa.

| Name            | In     | Type    | Default | Nullable | Description               |
| :-------------- | :----- | :------ | :------ | :------- | :------------------------ |
| `Authorization` | header | string  | None    | No       | Obtained in **Login**     |

### **Request Body**

=== "multipart/form-data"

    ``` 
    File Template com campos preenchidos
    ```

??? info "Body Schema"

    ```{ .form-data .no-copy}
    File Template
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Criados X usuários."
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": string
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "CNPJ-CPF invalido",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail": "Numero de registration ja cadastrada!",
                "render": 1
            }

        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 3"

        ``` json
            {
                "detail": "Erro nas linhas do arquivo: Linha X: Campos faltantes: X,Y,Z",
                "render": 1
            }

        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 4"

        ``` json
            {
                "detail": {
                    "username": [
                        "This field is required."
                    ]
                },
                "render": 0
            }

        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao criar colaboradores em massa.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---

**Create Employee**

## **<element class="http-post">POST<element>** - /empoyee/create/

??? note "Description"

    ### Description
    Rota para criação de um novo colaborador.

| Name            | In     | Type    | Default | Nullable | Description               |
| :-------------- | :----- | :------ | :------ | :------- | :------------------------ |
| `Authorization` | header | string  | None    | No       | Obtained in **Login**     |
| `fk_city`       | body   | integer | None    | No       | Obtained in **List City** |
| `fk_fu`         | body   | integer | None    | No       | Obtained in **List City** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "password": "123",
        "cpf":"02353336035",
        "username": "Sargento 3",
        "phone": "54992358847",
        "email": "coordenador@atitus.com",
        "fk_city": 4911,
        "fk_fu": 23,
        "sex": "M",
        "birth_date": "1999-12-14",
        "is_superuser": false,
        "is_staff": false,
        "groups":[
            "coordenador"
        ]
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
    "password": string,
    "cpf": string,
    "username": string,
    "phone": string,
    "email": string,
    "fk_city": integer,
    "fk_fu": integer,
    "sex": string,
    "birth_date": string,
    "is_superuser": boolean,
    "is_staff": boolean,
    "groups": list
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_user": 32,
                "registration": "00028",
                "username": "Professor 10",
                "cpf": "02353336123",
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "phone": "54992358847",
                "email": "professor@professor.com",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2024-07-23T23:23:20",
                "edited": "2024-07-23T23:23:19",
                "last_login": "2024-07-23T23:23:19",
                "is_superuser": false,
                "is_staff": false,
                "is_active": true,
                "groups": [
                    "professor"
                ]
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_user": integer,
                "registration": string,
                "username": string,
                "cpf": string,
                "fk_campus": integer,
                "campus_name": string,
                "phone": string,
                "email": string,
                "fk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string,
                "sex": string,
                "birth_date": string,
                "created": string,
                "edited": string,
                "last_login": string,
                "is_superuser": boolean,
                "is_staff": boolean,
                "is_active": boolean,
                "groups": list
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "CNPJ-CPF invalido",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail": "Numero de registration ja cadastrada!",
                "render": 1
            }

        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 3"

        ``` json
            {
                "detail": "Não foi possivel encontrar este User.",
                "render": 1
            }

        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 4"

        ``` json
            {
                "detail": {
                    "username": [
                        "This field is required."
                    ]
                },
                "render": 0
            }

        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao criar usuario",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---

**Update Employee**

## **<element class="http-put">PUT<element>** - /empoyee/<element class="path-put">pk_user</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de um colaborador.

| Name            | In             | Type    | Default | Nullable | Description                     |
| :-------------- | :------------- | :------ | :------ | :------- | :------------------------------ |
| `Authorization` | header         | string  | None    | No       | Obtained in **Login**           |
| `pk_user`       | path variables | string  | None    | No       | Obtained in **_List Employee_** |
| `fk_city`       | body           | integer | None    | No       | Obtained in **List City**       |
| `fk_fu`         | body           | integer | None    | No       | Obtained in **List City**       |

### **Request Body**

=== "application/json"

    ``` json
    {
        "cpf":"02353336035",
        "username": "Professor 3",
        "phone": "54992358847",
        "email": "professor@professor.com",
        "fk_city": 4911,
        "fk_fu": 23,
        "sex": "M",
        "birth_date": "1999-12-14",
        "is_superuser": false,
        "is_staff": false,
        "groups":[
            "professor"
        ]
    }
    ```

??? info "Body Schema"

    ```json
    {
    "cpf": string,
    "username": string,
    "phone": string,
    "email": string,
    "fk_city": integer,
    "fk_fu": integer,
    "sex": string,
    "birth_date": string,
    "is_superuser": boolean,
    "is_staff": boolean,
    "groups": list
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_user": 31,
                "registration": "00027",
                "username": "Professorteste",
                "cpf": "02353336035",
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "phone": "54992358847",
                "email": "professor@professor.com",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2024-07-23T23:01:15",
                "edited": "2024-07-24T22:05:58",
                "last_login": "2024-07-23T23:01:13",
                "is_superuser": false,
                "is_staff": false,
                "is_active": true,
                "groups": [
                    "professor"
                ]
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_user": integer,
                "registration": string,
                "username": string,
                "cpf": string,
                "fk_campus": integer,
                "campus_name": string,
                "phone": string,
                "email": string,
                "fk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string,
                "sex": string,
                "birth_date": string,
                "created": string,
                "edited": string,
                "last_login": string,
                "is_superuser": boolean,
                "is_staff": boolean,
                "is_active": boolean,
                "groups": list
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este User.",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail": "CNPJ-CPF invalido",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 3"

        ``` json
            {
                "detail": {
                    "username": [
                        "This field is required."
                    ]
                },
                "render": 0
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao editar usuario",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---


**Change Passwrod Employee**

## **<element class="http-put">PUT<element>** - /empoyee/change-password/

??? note "Description"

    ### Description
    Rota para mudar senha do colaborador.
    
    É mudado a senha do proprio usuario.

| Name            | In             | Type    | Default | Nullable | Description                     |
| :-------------- | :------------- | :------ | :------ | :------- | :------------------------------ |
| `Authorization` | header         | string  | None    | No       | Obtained in **Login**           |

### **Request Body**

=== "application/json"

    ``` json
    {
        "old_password" : "EscolaTiradentes@2025",
        "new_password": "Teste@2025"
    }
    ```

??? info "Body Schema"

    ```json
    {
        "old_password" : string,
        "new_password": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Senha atualizada com sucesso."
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": string
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este User.",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail": "Senha atual incorreta.",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```


??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao mudar senha do usuario",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---


**Change Status Employee**

## **<element class="http-put">PUT<element>** - /empoyee/<element class="path-put">pk_user</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de um colaborador.

| Name            | In             | Type   | Default | Nullable | Description                     |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**           |
| `pk_user`       | path variables | string | None    | No       | Obtained in **_List Employee_** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "is_active": 1
    }
    ```

??? info "Body Schema"

    ```json
    {
        "is_active": integer
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Usuário atualizado com sucesso."
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": string
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este User.",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao alterar status de usuario"
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---

**Delete Employee**

## **<element class="http-del">DELL<element>** - /empoyee/<element class="path-del">pk_user</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir um colaborador.

| Name            | In             | Type   | Default | Nullable | Description                     |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**           |
| `pk_user`       | path variables | string | None    | No       | Obtained in **_List Employee_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Usuario deletado com sucesso"
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": string
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este User.",
                "render": 1
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao deletar Usuario",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string,
                    "error": string
                }
            ```

---
