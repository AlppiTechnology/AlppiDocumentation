# Internal Note Comment


**Create Internal Note Comment**
## **<element class="http-post">POST<element>** - /internal_note/<element class="path-post">pk_internal_note</element>/comment/create/



??? note "Description"
    
    ### Description
    Rota para criação de comentário em uma nota interna

| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_internal_note`| path variables| string | None | No | Obtained in **Get Internal Note_**|


### **Request Body**


=== "application/json"

    ``` json
    {
        "comment":"seu comentário"
    }
    ```
??? info "Body Schema"
    
    ```{ .json .no-copy}
    {
        "comment": string,
    }
    ```

### **Response Body**

!!! success "201"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": {
                    "comment": [
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
                "detail": "Problemas ao cadastrar Comentario",
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

**Update Internal Note Comment**
## **<element class="http-put">PUT<element>** - /internal_note/<element class="path-put">pk_internal_note</element>/comment/<element class="path-put">pk_ct_comment</element>/update/




??? note "Description"
    
    ### Description
    Rota para a atualização de um comentário específico.


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_internal_note`| path variables| string | None | No | Obtained in **Get Internal Note_**|
| `pk_ct_comment`| path variables| string | None | No | Obtained in **Get Internal Note_**|



### **Request Body**


=== "application/json"

    ``` json
    {
        "comment":"seu comentário"
    }
    ```
??? info "Body Schema"
    
    ```{ .json .no-copy}
    {
        "comment": string,
    }
    ```

### **Response Body**

!!! success "200"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Comentario não encontrado",
                "render": 1
            }
            
        ```

        ??? info "Schema"
        
            ```{ .json .no-copy}
                {
                    "detail": object,
                    "render": integer
                }
            ```

    === "Error 2"

        ``` json
            {
                "detail": {
                    "comment": [
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
                "detail": "Problemas ao cadastrar Comentario",
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



**Delete Internal Note Comment**
## **<element class="http-del">DELL<element>** - /internal_note/<element class="path-del">pk_internal_note</element>/comment/<element class="path-del">pk_ct_comment</element>/delete/



??? note "Description"
    
    ### Description
    Rota para exclusão de um comentário específico.


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header |string | None | No | Obtained in **Login** |
| `pk_internal_note`| path variables| string | None | No | Obtained in **Get Internal Note_**|
| `pk_ct_comment`| path variables| string | None | No | Obtained in **Get Internal Note_**|


### **Response Body**

!!! success "204"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Comentario não encontrado",
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
                "detail": "Problemas ao deletar Comentario.",
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



