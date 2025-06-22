# Regulaments

**List Regulaments**

--- 

## **<element class="http-get">GET<element>** - /regulamens/list/


??? note "Description"
    
    ### Description
    Lista todos os regulamens cadastrados no sistema


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `page`   | query param |string | 1 | Yes | |
| `page_size`   | query param |string | 30 | Yes | |
| `search`| query params | string | None | No | Tree ID, Title or Description of the regulaments to search|



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/regulamens/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/regulamens/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_regulaments": 1,
                    "tree_id": "001",
                    "title": "TÍTULO l",
                    "description": "DISPOSIÇÕES GERAIS",
                    "type": 0
                },
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
                    "pk_regulaments": integer,
                    "tree_id": string,
                    "title": string,
                    "description": string,
                    "type": integer
                }
            ]
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar todos os Regulaments.",
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
                "detail": "Problemas ao listar todos os Regulaments.",
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
