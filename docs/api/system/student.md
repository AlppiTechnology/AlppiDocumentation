# Student

**Get Student**

---

## **<element class="http-get">GET<element>** - /student/<element class="path-get">pk_user</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de um estudante específico.

| Name            | In             | Type   | Default | Nullable | Description                    |
| :-------------- | :------------- | :----- | :------ | :------- | :----------------------------- |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**          |
| `pk_user`       | path variables | string | None    | No       | Obtained in **_List Student_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_user": 10,
                "registration": "00008",
                "username": "Aluno 2",
                "cpf": "02353336035",
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "phone": "54992358847",
                "email": "patrick@piccini.com",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2024-05-27T23:32:47",
                "edited": "2024-05-27T23:32:46",
                "last_login": "2024-05-27T23:32:46",
                "is_active": true
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
                "is_active": boolean
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
                "detail":  "Este usuario não é Estudante"
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

**List Student**

## **<element class="http-get">GET<element>** - /student/list/

??? note "Description"

    ### Description
    Lista todos os estudantes cadastrados no sistema.

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
                "next": "http://alppi/sys/api/v1/student/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/student/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_user": 12,
                        "registration": "00012",
                        "username": "Aluno 1",
                        "is_active": true
                    },
                    {
                        "pk_user": 21,
                        "registration": "00021",
                        "username": "Aluno 10",
                        "is_active": true
                    },
                    {
                        "pk_user": 13,
                        "registration": "00013",
                        "username": "Aluno 2",
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


**Get Student File Template**

---

## **<element class="http-get">GET<element>** - /student/gettemplate/

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
        Arquivo cadastro-student.xlsx
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



**Upload Student File Template**

## **<element class="http-post">POST<element>** - /student/uploadfile/

??? note "Description"

    ### Description
    Rota para criação estudantes em massa.

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
                "detail": "Problemas ao criar estudantees em massa.",
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


**Create Student**

## **<element class="http-post">POST<element>** - /student/create/

??? note "Description"

    ### Description
    Rota para criação de um novo estudante.

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
        "username": "Aluno 18",
        "phone": "54992358847",
        "email": "patrick@piccini.com",
        "fk_city": 4911,
        "fk_fu": 23,
        "sex": "M",
        "birth_date": "1999-12-14"
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
        "birth_date": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_user": 22,
                "registration": "00022",
                "username": "Aluno 19",
                "cpf": "02353336035",
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "phone": "54992358847",
                "email": "patrick@piccini.com",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2024-08-31T16:24:47",
                "edited": "2024-08-31T16:24:46",
                "last_login": "2024-08-31T16:24:46",
                "is_active": true,
                "groups": [
                    "estudante"
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
                "is_active": boolean,
                "groups": array of strings
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

**Update Student**

## **<element class="http-put">PUT<element>** - /student/<element class="path-put">pk_user</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de um estudante.

| Name            | In             | Type    | Default | Nullable | Description                    |
| :-------------- | :------------- | :------ | :------ | :------- | :----------------------------- |
| `Authorization` | header         | string  | None    | No       | Obtained in **Login**          |
| `pk_user`       | path variables | string  | None    | No       | Obtained in **_List Student_** |
| `fk_city`       | body           | integer | None    | No       | Obtained in **List City**      |
| `fk_fu`         | body           | integer | None    | No       | Obtained in **List City**      |

### **Request Body**

=== "application/json"

    ``` json
    {
        "pk_user": 22,
        "username": "Aluno 19",
        "cpf": "02353336035",
        "phone": "54992358847",
        "email": "patrick@piccini.com",
        "fk_city": 4911,
        "fk_fu": 23,
        "sex": "M",
        "birth_date": "1999-12-14",
        "is_active": true
    }
    ```

??? info "Body Schema"

    ```json
    {
        "pk_user": integer,
        "username": string,
        "cpf": string,
        "phone": string,
        "email": string,
        "fk_city": integer,
        "fk_fu": integer,
        "sex": string,
        "birth_date": string,
        "is_active": boolean
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_user": 22,
                "registration": "00022",
                "username": "Aluno 19",
                "cpf": "02353336035",
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "phone": "54992358847",
                "email": "patrick@piccini.com",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2024-08-31T16:24:47",
                "edited": "2024-08-31T16:24:46",
                "last_login": "2024-08-31T16:24:46",
                "is_active": true,
                "groups": [
                    "estudante"
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
                "is_active": boolean,
                "groups": array of strings
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


**Update Student**

## **<element class="http-put">PUT<element>** - /student/change-password/

??? note "Description"

    ### Description
    Rota para mudar senha do estudante.
    
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


**Change Status Student**

## **<element class="http-put">PUT<element>** - /student/<element class="path-put">pk_user</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de um estudante.

| Name            | In             | Type   | Default | Nullable | Description                    |
| :-------------- | :------------- | :----- | :------ | :------- | :----------------------------- |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**          |
| `pk_user`       | path variables | string | None    | No       | Obtained in **_List Student_** |

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
                "detail": "Problemas ao alterar status de usuario",
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

**Delete Student**

## **<element class="http-del">DELL<element>** - /student/<element class="path-del">pk_user</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir um estudante.

| Name            | In             | Type   | Default | Nullable | Description                    |
| :-------------- | :------------- | :----- | :------ | :------- | :----------------------------- |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**          |
| `pk_user`       | path variables | string | None    | No       | Obtained in **_List Student_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Estudante deletado com sucesso"
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
