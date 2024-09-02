# City

**Get City**

---

## **<element class="http-get">GET<element>** - /city/


??? note "Description"
    
    ### Description
    Lista de cidades cadastradas filtradas pelos nomes


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `search`| query params | string | None | No | Name of the city to search|


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": [
                {
                    "pk_city": 1721,
                    "city_name": "Passo de Camaragibe",
                    "fk_fu": 14,
                    "fu_name": "Alagoas"
                },
                {
                    "pk_city": 2803,
                    "city_name": "Passos",
                    "fk_fu": 17,
                    "fu_name": "Minas Gerais"
                }
            ]
        }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
        {
            "results": array of objects {
                "pk_city": integer,
                "city_name": string,
                "fk_fu": integer,
                "fu_name": string
            }
        }
        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os City.",
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