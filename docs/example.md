# Title

**Get Campus**

---

## **<element class="http-get">GET<element>** - /campus/<element class="path-get">pk_campus</element>/


??? note "Description"
    
    ### Description
    Captura as informações detalhadas em do campus


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_campus`| path variables| string | None | No | Obtained in **_List Campus_**|


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "results": {
                    "pk_campus": 1,
                    "cnpj": "02353336035",
                    "campus_code": 1,
                    "campus_name": "Atitus Educação Passo Fundo",
                    "trading_name": "Atitus Educação",
                    "company_name": "Atitus Educação",
                    "public_place": "Av. brasil",
                    "fk_city": 4911,
                    "city_name": "Passo Fundo",
                    "fk_fu": 23,
                    "fu_name": "Rio Grande do Sul",
                    "email": "atitus.passofundo@atitus.com",
                    "phone": "54992358847",
                    "created": "2024-05-27T23:13:43",
                    "edited": "2024-05-27T23:13:43",
                    "status": 1
                }
            }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
            {
                "results": {
                    "pk_campus": integer,
                    "cnpj": string,
                    "campus_code": integer,
                    "campus_name": string,
                    "trading_name": string,
                    "company_name": string,
                    "public_place": string,
                    "fk_city": integer,
                    "city_name": string,
                    "fk_fu": integer,
                    "fu_name": string,
                    "email": string,
                    "phone": string,
                    "created": string,
                    "edited": string,
                    "status": integer
                }
            }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este Campus."
            }
        ```

        ??? info "Schema"
        
            ``` { .json .no-copy}
                {
                    "detail": string
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao visualizar Campus",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                    "error": string
                }
            ```

---

**List Campus**
## **<element class="http-get">GET<element>** - /campus/list/


??? note "Description"
    
    ### Description
    Lista todos os campus cadastrados no sistema


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `page`   | query param |string | 1 | Yes | |
| `page_size`   | query param |string | 30 | Yes | |



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/campus/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/campus/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_campus": 1,
                    "cnpj": "02353336035",
                    "campus_code": 1,
                    "campus_name": "Atitus Educação Passo Fundo",
                    "trading_name": "Atitus Educação",
                    "company_name": "Atitus Educação",
                    "public_place": "Av. brasil",
                    "fk_city": 4911,
                    "city_name": "Passo Fundo",
                    "fk_fu": 23,
                    "fu_name": "Rio Grande do Sul",
                    "email": "atitus.passofundo@atitus.com",
                    "phone": "54992358847",
                    "created": "2024-05-27T23:13:43",
                    "edited": "2024-05-27T23:13:43",
                    "status": 1
                }
            ]
        }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
        {
            "navigation": {
                "next": string
                "previous": string
            },
            "next": integer
            "previous": integer
            "count": integer
            "results": [
                {
                    "pk_campus": integer,
                    "cnpj": string,
                    "campus_code":integer,
                    "campus_name": string,
                    "trading_name": string,
                    "company_name": string,
                    "public_place": string,
                    "fk_city": integer,
                    "city_name": string,
                    "fk_fu": integer,
                    "fu_name": string,
                    "email": string,
                    "phone": string,
                    "created": string,
                    "edited": string",
                    "status": integer
                }
            ]
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar todos os Campus."
            }
        ```

        ??? info "Schema"
        
            ``` { .json .no-copy}
                {
                    "detail": string
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os Campus.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                    "error": string
                }
            ```

---

**Create Campus**
## **<element class="http-post">POST<element>** - /campus/create/



??? note "Description"
    
    ### Description
    Rota para criação de um novo campus


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `fk_city`   | body |integer | None | No | Obtained in **List City** |
| `fk_fu`   | body |integer | None | No | Obtained in **List City** |


### **Request Body**


=== "application/json"

    ``` json
    {
        "cnpj": "02353336035",
        "campus_code": 1,
        "campus_name": "Atitus Educação Passo Fundo",
        "trading_name": "Atitus Educação",
        "company_name": "Atitus Educação",
        "public_place": "Av. brasil",
        "fk_city": 4911,
        "fk_fu": 23,
        "email": "atitus.passofundo@atitus.com",
        "phone": "54992358847"
    }
    ```
??? info "Body Schema"
    
    ```{ .json .no-copy}
    {
        "cnpj": string,
        "campus_code": integer,
        "campus_name": string,
        "trading_name": string,
        "company_name": string,
        "public_place": string,
        "fk_city": integer,
        "fk_fu": integer,
        "email": string,
        "phone": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_campus": 2,
                "cnpj": "02353336035",
                "campus_code": 2,
                "campus_name": "Atitus Educação Passo Fundo",
                "trading_name": "Atitus Educação",
                "company_name": "Atitus Educação",
                "public_place": "Av. brasil",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "email": "atitus.passofundo@atitus.com",
                "phone": "54992358847",
                "created": "2024-07-23T17:49:24",
                "edited": "2024-07-23T17:49:22",
                "status": 1
            }
        }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
        {
            "results": {
                "pk_campus": integer,
                "cnpj": string,
                "campus_code": integer,
                "campus_name": string,
                "trading_name": string,
                "company_name": string,
                "public_place": string,
                "fk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string,
                "email": string,
                "phone": string,
                "created": string,
                "edited": string,
                "status": integer
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "CNPJ-CPF invalido"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail": {
                    "campus_code": [
                        "campus with this campus code already exists."
                    ]
                }
            }
            
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": dict
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao cadastrar Campus.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                    "error": string
                }
            ```

---

**Update Campus**
## **<element class="http-put">PUT<element>** - /campus/<element class="path-put">pk_campus</element>/update/




??? note "Description"
    
    ### Description
    Rota para a atualização dos dados de um campus


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_campus`| path variables| string | None | No | Obtained in **_List Campus_**|
| `fk_city`   | body |integer | None | No | Obtained in **List City** |
| `fk_fu`   | body |integer | None | No | Obtained in **List City** |


### **Request Body**


=== "application/json"

    ``` json
    {
        "cnpj": "02353336035",
        "campus_code": 1,
        "campus_name": "Atitus Educação Passo Fundo update",
        "trading_name": "Atitus Educação",
        "company_name": "Atitus Educação",
        "public_place": "Av. brasil",
        "fk_city": 4911,
        "fk_fu": 23,
        "email": "atitus.passofundo@atitus.com",
        "phone": "54992358847",
        "status": 1
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "cnpj": string,
        "campus_code": integer,
        "campus_name": string,
        "trading_name": string,
        "company_name": string,
        "public_place": string,
        "fk_city": integer,
        "fk_fu": integer,
        "email": string,
        "phone": string,
        "status": integer
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_campus": 2,
                "cnpj": "02353336035",
                "campus_code": 2,
                "campus_name": "Atitus Educação Passo Fundo update",
                "trading_name": "Atitus Educação",
                "company_name": "Atitus Educação",
                "public_place": "Av. brasil",
                "fk_city": 4911,
                "city_name": "Passo Fundo",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "email": "atitus.passofundo@atitus.com",
                "phone": "54992358847",
                "created": "2024-07-23T17:49:24",
                "edited": "2024-07-23T18:04:17",
                "status": 1
            }
        }
        ```

    ??? info "Schema"
    
        ```json
        {
            "results": {
                "pk_campus": integer,
                "cnpj": string,
                "campus_code": integer,
                "campus_name": string,
                "trading_name": string,
                "company_name": string,
                "public_place": string,
                "fk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string,
                "email": string,
                "phone": string,
                "created": string,
                "edited": string,
                "status": integer
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar todos os Campus."
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 2"

        ``` json
            {
                "detail": "CNPJ-CPF invalido"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 3"

        ``` json
            {
                "detail": {
                    "campus_name": [
                        "This field is required."
                    ]
                }
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": dict
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao editar Campus.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                    "error": string
                }
            ```

---

**Change Status Campus**
## **<element class="http-put">PUT<element>** - /campus/<element class="path-put">pk_campus</element>/changestatus/




??? note "Description"
    
    ### Description
    Rota para a atualização de status de um campus


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_campus`| path variables| string | None | No | Obtained in **_List Campus_**|



### **Request Body**


=== "application/json"

    ``` json
    {
        "status": 0
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "status": integer
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Status do campus atualizado com sucesso."
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
                "detail": "Não foi possivel encontrar este Campus."
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```


??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao alterar status do campus.",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                    "error": string
                }
            ```

---

**Delete Campus**
## **<element class="http-del">DELL<element>** - /campus/<element class="path-del">pk_campus</element>/delete/



??? note "Description"
    
    ### Description
    A rota de login é fundamental


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header |string | None | No | Obtained in **Login** |
| `pk_campus`| path variables| string | None | No | Obtained in **_List Campus_**|


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Campus deletado com sucesso."
        }
        ```

    ??? info "Schema"
    
        ```json
        {
            "results": "Campus deletado com sucesso."
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar todos os Campus."
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao deletar Campus",
                "error": "descrição do erro interno"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                    "error": string
                }
            ```

---





??? success "200"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? warning "400"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? danger "501"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```



??? abstract "502"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? info "503"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? question "504"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```


??? warning "505"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```


??? failure "506"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? danger "507"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? bug "508"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? example "509"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? quote "510"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
        ~~~


??? success "200"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? warning "400"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? danger "501"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```



??? abstract "502"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? info "503"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? question "504"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```


??? warning "505"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```


??? failure "506"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? danger "507"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? bug "508"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? example "509"

    === "application/json"

        ``` json
            {
                "registration": "00001",
                "password": "admin"
            }
        ```

    ??? info "Schema"
    
        ```json
            {
                "registration": string,
                "password": string
            }
        ```

??? quote "510"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
        ~~~