# Disciplinary Grade


**List Disciplinary Grade**
## **<element class="http-get">GET<element>** - /cisciplinary_grade/list/


??? note "Description"
    
    ### Description
    Lista todos as notas disciplinares cadastrados no sistema referente ao modulo do colégio tiradentes


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `page`            | query param |string | 1 | Yes | |
| `page_size`       | query param |string | 30 | Yes | |
| `search`          | queary params| string | None | Yo | Nome ou Matricula do aluno.|



**List Disciplinary Grade**

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/disciplinary_grade/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/disciplinary_grade/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_ct_disciplinary_grade": 1,
                    "grade": 40.0,
                    "username": "Aluno 1",
                    "registration": "00011"
                }...
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
            "results": array [
                {
                    "pk_ct_disciplinary_grade": integet,
                    "grade": floating,
                    "username": string,
                    "registration": string
                }...
            ]
        }
        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os Disciplinary Grade.",
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


**Update Disciplinary Grade**
## **<element class="http-put">PUT<element>** - /cisciplinary_grade/<element class="path-put">pk_dg</element>/update/




??? note "Description"
    
    ### Description
    Rota para a atualização de nota disciplinar referente ao modulo do colégio tiradentes.


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string  | None     | No | Obtained in **Login** |
| `pk_dg`| path variables| string | None | No | Obtained in **_List Disciplinary Grade_**|


### **Request Body**


=== "application/json"

    ``` json
    {
        "grade": 40.0
    }
    ```
??? info "Body Schema"
    
    ```json
    {
        "grade": floating
    }
    ```

### **Response Body**

!!! success "200"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi encontrado a nota para edição.",
                "render": 0
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
                "detail": "Problemas ao editar Disciplinary Grade.",
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
