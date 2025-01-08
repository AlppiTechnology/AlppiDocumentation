# Pedagogical

**Get Pedagogical**

---

**List Pedagogical**

## **<element class="http-get">GET<element>** - /pedagogical/

??? note "Description"

    ### Description
    Lista todas as turmas que o usuario (Employee) ministra aula.

    Caso seja um usuário SUPERUSER ou ADMINISTRATOR poderá ver todas as turmas e todos os professores

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `page`          | query param | string | 1       | Yes      |                               |
| `page_size`     | query param | string | 30      | Yes      |                               |
| `search`        | query param | string | None    | Yes      | Name of the subject to search |
| `status`        | query param | string | 1       | Yes      | 1-Active/0-Inative            |
| `fk_school_year`| query param | string | None    | Yes      | Filter per School Year. Obtained in **List School Year**|
| `fk_school_grade`| query param | string | None   | Yes      | Filter per School Grade. Obtained in **List School Grade**|


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/pedagogical/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/pedagogical/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_pedagogical_setting": 7,
                    "class_status": 1,
                    "pk_class_setting": 3,
                    "name": "Teste",
                    "school_grade_name": "1-semestre",
                    "school_level_name": "ensino superior",
                    "school_year_name": "2024/2",
                    "subject_name": "Física"
                }
                ]
            }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "navigation": {
                "next": string,
                "previous": string
            },
            "next": integer,
            "previous": integer,
            "count": integer,
            "results": array of objects {
                "pk_event": integer,
                "class_status": integer, // 1-Active / 0-Inactive
                "event_name": string,
                "event_date": string, // Date in YYYY-MM-DD format
                "event_location": string,
                "organizer_name": string,
                "target_audience": string
            }

        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todas as turomas dos professores.",
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
