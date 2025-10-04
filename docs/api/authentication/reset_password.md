# Title

**Request Password Reset**

---


{{ route("POST", "/request_password_reset/") }}


??? note "Description"
    
    ### Description
    Envia arequisição para reset de senha.

    Será enviado um email para o email cadastrado do usuario com um link para reset de senha. O link tem validade de somente um reset de senha.
    
    Esse link conterá um _token_ e um _uidb64_.
    - obs: esse link será para redirecionar a uma pagina onde o usuario deverá informar a nova senha



| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |


### **Request Body**


=== "application/json"

    ``` json
        {
            "registration":"00001",
            "email": "patrickbpiccini@hotmail.com"
        }
    ```

??? info "Schema"

    ```{ .json .no-copy}
        {
            "registration":string,
            "email": string
        }
    ```


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "results":"Foi enviado um link para resetar sua senha em seu email cadastrado."
            }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
            {
                "results":string
            }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Verifique os campos requeridos",
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
                "detail": "Verifique os campos requeridos",
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

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao requisitar reset de senha",
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
## **<element class="http-patch">PUT<element>** - /confirm_password_reset/




??? note "Description"
    
    ### Description
    Rota para a atualização dos dados de um campus


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |


### **Request Body**


=== "application/json"

    ``` json
    {
        "password": "nova_senha",
        "token": "coube8-cd2eda71d8b9233f738b08940c56d5f9",
        "uidb64": "MQ"
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "password": string,
        "token": string,
        "uidb64": string
    }
    ```

### **Response Body**

!!! success "200"



??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "O link de reset de senha esta inválido",
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
                "detail": "Problemas ao redefinir senha do usuario.",
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
