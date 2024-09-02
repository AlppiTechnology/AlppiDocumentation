# User Group 

**List User Group**

---

## **<element class="http-get">GET<element>** - /groups/


??? note "Description"
    
    ### Description
    LRota para listagem de todos os Grupos cadastrados para colaboradores.


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": [
                "administrador",
                "coordenador",
                "avaliador",
                "professor",
                "superuser"
            ]
        }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
        {
            "results": array of strings
        }
        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos Grupos."
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

