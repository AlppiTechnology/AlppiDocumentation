# Flow Disciplinary Grade

**List Campus**
## **<element class="http-get">GET<element>** - /flow_disciplinary_grade/list/


??? note "Description"
    
    ### Description
    Lista todos os campus cadastrados no sistema


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header      | string | None | No | Obtained in **Login** |
| `page`            | query param | string | 1 | Yes | |
| `page_size`       | query param | string | 30 | Yes | |
| `search`          | query params| string | None    | No       | Filtragem pelo nome de aluno ou Matricula|



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1//flow_disciplinary_grade/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1//flow_disciplinary_grade/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "from_grade": 78.0,
                    "to_grade": 77.7,
                    "edited": "2025-08-24T23:39:30.534313Z",
                    "registration": "03100",
                    "student_name": "Vitor Silva",
                    "student_status": true,
                    "reporter_name": "Patrick Berlatto Piccini"
                }
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
                    "from_grade": floating,
                    "to_grade": floating,
                    "edited": string,
                    "registration": string,
                    "student_name": string,
                    "student_status": boolean,
                    "reporter_name": string
                }
            ]
        }
        ```


??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os FlowDisciplinaryGrade.",
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
