# Internal Note Settings


**Update Internal Note**
## **<element class="http-put">PUT<element>** - /internal_note/<element class="path-put">pk_internal_note</element>/update/




??? note "Description"
    
    ### Description
    Rota para a atualização dos dados da nota padrão da nota disciplinar ao cadastrar novos alunos na instituição


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |




### **Request Body**


=== "application/json"

    ``` json
        {
        "disciplinary_grade": 70.0
    }


    ```
??? info "Body Schema"
    
    ```json
    {
        "disciplinary_grade": integer
    }


    ```

### **Response Body**

??? success "200"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar nota para esse campus.",
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
                "detail": "Nota não informada."
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
                "detail": "Problemas ao editar InternalNoteSettings",
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
