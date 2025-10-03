# Campus Settings


**Update Campus Settings**
## **<element class="http-put">PUT<element>** - /campussettings/<element class="path-put">pk_campus</element>/update/




??? note "Description"
    
    ### Description
    Rota para a atualização de senha padrão da instituição


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_campus`| path variables| string | None | No | Obtained in **_List Campus Settings_**|


### **Request Body**


=== "application/json"

    ``` json
    {
        "password": "senha_padrão_dos_usuario_cadastrados",
        "email_password": "Senha_do_email",
        "email_user": "email@gmail.com",
        "smpt_host": "smtp.gmail.com",
        "smpt_port": "587",
        "use_tls": true
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "password": string,
        "email_password": string,
        "email_user": string,
        "smpt_host": string,
        "smpt_port": string,
        "use_tls": boolean
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        ```

    ??? info "Schema"
    
        ```json
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este CampusSettings.",
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
                "detail": {
                    "password": [
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
                "detail": "Problemas ao editar CampusSettings",
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



**Change Passwrod Campus Settings**

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
                "detail": "Não foi possível encontrar este Campus.",
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
                "detail": "Problemas ao mudar senha do Campus",
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
