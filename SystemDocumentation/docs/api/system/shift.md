# Shift

**Get Shift**

---


**List Shift**

## **<element class="http-get">GET<element>** - /shift/list/

??? note "Description"

    ### Description
    Lista todos as Area do Conhecimentos cadastrados no sistema

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/subject/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/subject/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_shift": 1,
                        "name": "matutino"
                    },
                    {
                        "pk_shift": 2,
                        "name": "vespertino"
                    },
                    {
                        "pk_shift": 3,
                        "name": "noturno"
                    }
                ]
            }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "navigation": {
                "next": null,
                "previous": null
            },
            "next": null,
            "previous": null,
            "count": integer,
            "results": [
                {
                    "pk_shift": integer,
                    "name": string
                }
            ]
        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os Shift.",
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