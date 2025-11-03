---
status: new
---

# Profile

**Get Campus**

---

## {{ route("GET", "/profile/", new=True) }}

??? note "Description"
    
    ### Description
    Retorna os dados pessoais do usuarios. 


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "pk_user": 1,
                "username": "Administrador Alppi",
                "cpf": "02353336035",
                "phone": "54992358847",
                "email": "admin@alppi.com",
                "fk_city": 4911,
                "city_name": "Pejuçara",
                "fk_fu": 23,
                "fu_name": "Rio Grande do Sul",
                "sex": "M",
                "birth_date": "1999-12-14",
                "created": "2025-09-17T22:53:47",
                "edited": "2025-09-20T01:44:04"
            }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
            {
                "pk_user": integer,
                "username": string,
                "cpf": string,
                "phone": string,
                "email": string,
                "fk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string,
                "sex": string,
                "birth_date": string,
                "created": string,
                "edited": string
            }

        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este usuário.",
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
                "detail": "Problemas ao visualizar Profile",
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


## {{ route("PUT", "/profile/", new=True) }}

??? note "Description"
    
    ### Description
    Rota para a atualização dos dados pessoais do usuários. 


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |


### **Request Body**


=== "application/json"

    ``` json
    {
    "username": "Administrador Alppi",
    "cpf": "02353336035",
    "phone": "54992358847",
    "email": "admin@alppi.com",
    "fk_city": 4911,
    "fk_fu": 23,
    "sex": "M",
    "birth_date": "1999-12-14"
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "username": string,
        "cpf": string,
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
            "pk_user": 1,
            "username": "Administrador Alppi",
            "cpf": "02353336035",
            "phone": "54992358847",
            "email": "admin@alppi.com",
            "fk_city": 4913,
            "city_name": "Picada Café",
            "fk_fu": 23,
            "fu_name": "Rio Grande do Sul",
            "sex": "M",
            "birth_date": "1999-12-14",
            "created": "2025-09-17T22:53:47",
            "edited": "2025-11-02T23:29:02"
        }
        ```

    ??? info "Schema"
    
        ```json
        {
            "pk_user": integer,
            "username": string,
            "cpf": string,
            "phone": string,
            "email": string,
            "fk_city": integer,
            "city_name": string,
            "fk_fu": integer,
            "fu_name": string,
            "sex": string,
            "birth_date": string,
            "created": string,
            "edited": string
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possível encontrar este usuário.",
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
                "render": 0|
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
                "detail": "Problemas ao editar este perfil.",
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
