# User Authentication
## Login Route

## **<element class="http-post">POST<element>** - `/login/`



??? note "Description"
    
    ### Description
    A rota de login é fundamental para autenticar o usuário no sistema, garantindo que ele tenha acesso apenas aos módulos que a instituição associada está autorizada a utilizar e visualizar no frontend. Durante o processo de login, dois tokens JWT são gerados e retornados na resposta:

    **_user_access:_** Este token concede ao usuário a permissão para acessar o sistema, encapsulando informações essenciais, como ID do usuário, nome, status, e o grupo ao qual ele pertence.

    **_system_modules:_** Este token define quais módulos do sistema estão disponíveis para o usuário, com base nas permissões concedidas à instituição.

    ### User Access


    ~~~ json
    {
    "pk_user": 1,
    "registration": "00001",
    "username": "Patrick Berlatto Piccini",
    "status": true,
    "campus_code": 1,
    "pk_campus": 1,
    "ip_adress": "131.221.12.242",
    "group": "superuser",
    "current_school_year": 3,
    "current_term": 2,
    "exp": 2081726873
    }
    ~~~

    ### System Modules

    ~~~ json
    {
    "absence": 1,
    "grade": 1,
    "graphic": 1,
    "home": 1,
    "register": 1,
    "campus_name": "Atiitus Educação Passo Fundo",
    "cnpj": "02353336035",
    "free_trial": "2024-01-29",
    "in_test": false
    }
    ~~~


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header |string | None | No | Obtained in **Login** |


### **Request Body**


=== "application/json"

    ``` json
    {
        "registration": "00001",
        "password": "admin"
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "registration": string,
        "password": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "user_access": "R5cCI6IkpXVCJ9.eyJwa191c2VyIjoxLCJyZWdpc3RyYXRpb24iOiIwMDAwM...",
                "system_modules": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhYn..."
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "registration": string,
                    "password": string
                }
            ```
    

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Informe o numero de matricula para o login."
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
                "detail": "Informe a senha para o login."
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
                "detail": "Este usuario não existe!"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 5"

        ``` json
            {
                "detail": "Não fio possivel encontrar um periodo no school_year_date com a data atual."
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 6"

        ``` json
            {
                "detail": "Este usuario não contem grupos!"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```

??? failure "401"

    === "Error 1"

        ``` json
            {
                "datail": "Credenciais incorretas!"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "datail": string
                }
            ```

??? failure "403"

    === "Error 1"

        ``` json
            {
                "datail": "Usuario Bloqueado!"
            }
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "datail": string
                }
            ```


??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas do servidor ao atualizar acesso do usuario.",
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
    === "Error 2"

        ``` json
            {
                "detail": "Problemas do servidor buscar grupos do usuario.",
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
    === "Error 3"

        ``` json
            {
                "detail": "Problemas do servidor buscar school_year_date",
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
    === "Error 4"

        ``` json
            {
                "detail": "Problemas do servidor ao autenticar usuario.",
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

