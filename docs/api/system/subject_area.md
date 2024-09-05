# Subejct Area

**Get Subejct Area**

---

## **<element class="http-get">GET<element>** - /subjectarea/<element class="path-get">pk_subject_area</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma Area do Conhecimento específica.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject_area` | path variables | string | None    | No       | Obtained in **_List Subejct Area_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_subject_area": 2,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "name": "Ciências da Natureza",
                "created": "2024-06-01T15:44:46",
                "edited": "2024-06-01T15:44:46",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_subject_area": integer,
                "fk_campus": integer,
                "campus_name": string,
                "name": string,
                "created": string, // Data e hora no formato ISO 8601
                "edited": string, // Data e hora no formato ISO 8601
                "status": integer // 1-True / 0-False
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SubjectArea.",
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
                "detail":  "Problemas ao visualizar SubjectArea",
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

**List Subejct Area**

## **<element class="http-get">GET<element>** - /subjectarea/list/

??? note "Description"

    ### Description
    Lista todos as Area do Conhecimentos cadastrados no sistema

| Name            | In          | Type   | Default | Nullable | Description                 |
| :-------------- | :---------- | :----- | :------ | :------- | :-------------------------- |
| `Authorization` | header      | string | None    | No       | Obtained in **Login**       |
| `page`          | query param | string | 1       | Yes      |                             |
| `page_size`     | query param | string | 30      | Yes      |                             |


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/subjectarea/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/subjectarea/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_subject_area": 5,
                        "name": "Ciências da Exatas",
                        "status": 1
                    },
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
                "pk_subject_area": integer,
                "name": string,
                "status": integer // 1-True / 0-False
            }
        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao visualizar SubjectArea",
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

**Create Subejct Area**

## **<element class="http-post">POST<element>** - /subjectarea/create/

??? note "Description"

    ### Description
    Rota para criação de uma nova Area do Conhecimento.


| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |


### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "Ciências da Exatas"
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "name": string
    }

    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_subject_area": 5,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "name": "Ciências da Exatas",
                "created": "2024-08-12T21:40:52",
                "edited": "2024-08-12T21:40:52",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_subject_area": integer,
                "fk_campus": integer,
                "campus_name": string,
                "name": string,
                "created": string,
                "edited": string,
                "status": integer // 1-True / 0-False
            }
        }


        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Informe o nome da Area do Conhecimento",
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
                "detail": "Problemas ao cadastrar Subject Area",
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

**Update Subejct Area**

## **<element class="http-put">PUT<element>** - /subjectarea/<element class="path-put">pk_subject_area</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject_area` | path variables | string | None    | No       | Obtained in **_List Subejct Area_** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "linGuaGens de update",
        "status": 1
    }

    ```
    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "name": string,
            "status": integer
        }
                
        ```



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_subject_area": 6,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "name": "Linguagens de Update",
                "created": "2024-08-12T22:10:14",
                "edited": "2024-08-12T22:15:27",
                "status": 0
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_subject_area": integer,
                "fk_campus": integer,
                "campus_name": string,
                "name": string,
                "created": string,
                "edited": string,
                "status": integer // 1-True / 0-False
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Informe o nome da Area do Conhecimento",
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
            "detail": "Não foi possivel encontrar este SubjectArea.",
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
                "detail": "Problemas ao editar Subject Area",
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

**Change Status Subejct Area**

## **<element class="http-put">PUT<element>** - /subjectarea/<element class="path-put">pk_subject_area</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject_area` | path variables | string | None    | No       | Obtained in **_List Subejct Area_** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "status": 1 // 1 ou 0
    }
    ```

??? info "Body Schema"

    ```json
    {
        "status": integer
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Area do conhecimento atualizado com sucesso."
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
                "detail": "Não foi possivel encontrar este SubjectArea.",
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
                "detail": "Problemas ao alterar status do subject_area",
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

**Delete Subejct Area**

## **<element class="http-del">DELL<element>** - /subjectarea/<element class="path-del">pk_subject_area</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject_area` | path variables | string | None    | No       | Obtained in **_List Subejct Area_** |

### **Response Body**

!!! success "204 No Content"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este SubjectArea."
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
                "detail": "Problemas ao deletar SubjectArea",
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
