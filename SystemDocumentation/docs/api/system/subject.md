# Subejct

**Get Subejct**

---

## **<element class="http-get">GET<element>** - /subject/<element class="path-get">pk_subject</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma Area do Conhecimento específica.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject` | path variables | string | None    | No       | Obtained in **_List Subejct_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_subject": 1,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_subject_area": 1,
                "subject_code": 1000,
                "subject_name": "Matemática",
                "created": "2024-06-01T15:46:00",
                "edited": "2024-06-01T15:46:00",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_subject": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_subject_area": integer,
                "subject_code": integer,
                "subject_name": string,
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
            "detail": "Não foi possivel encontrar este Subject."
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```


??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail":  "Problemas ao visualizar Subject",
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

**List Subejct**

## **<element class="http-get">GET<element>** - /subject/list/

??? note "Description"

    ### Description
    Lista todos as Area do Conhecimentos cadastrados no sistema

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `page`          | query param | string | 1       | Yes      |                               |
| `page_size`     | query param | string | 30      | Yes      |                               |
| `search`        | query param | string | None    | Yes      | Name of the subject to search |
| `status`        | query param | string | 1       | Yes      | 1-Active/0-Inative            |



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
                        "pk_subject": 1,
                        "subject_name": "Matemática",
                        "subject_code": 1000,
                        "status": 1
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
            "results": array of objects {
                "pk_subject": integer,
                "subject_name": string,
                "subject_code": integer,
                "status": integer // 1-True / 0-False
            }

        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao visualizar Subject",
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

**Create Subejct**

## **<element class="http-post">POST<element>** - /subject/create/

??? note "Description"

    ### Description
    Rota para criação de uma nova Area do Conhecimento.


| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |
| `fk_subject_area`| body | integer | None    | Yes      | Obtained in **List Subject Area** |


### **Request Body**

=== "application/json"

    ``` json
    {
        "fk_subject_area":1,
        "subject_name":"teste_exemple"
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "fk_subject_area": integer,
        "subject_name": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_subject": 7,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_subject_area": 1,
                "subject_code": 1006,
                "subject_name": "Teste_Exemple",
                "created": "2024-08-13T22:20:41",
                "edited": "2024-08-13T22:20:41",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_subject": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_subject_area": integer,
                "subject_code": integer,
                "subject_name": string,
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
            "detail": "Informe o nome da disciplina"
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 2"

        ``` json
        {
            "detail": "Informe a área do conhecimento da disciplina"
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
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

**Update Subejct**

## **<element class="http-put">PUT<element>** - /subject/<element class="path-put">pk_subject</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject`       | path variables | string | None    | No       | Obtained in **_List Subejct_**        |

### **Request Body**

=== "application/json"

    ``` json
    {
        "subject_name": "teste_example update",
        "status": 1 // 1 ou 0
    }

    ```
    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "subject_name": string,
            "status": integer
        }
                
        ```



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_subject": 7,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_subject_area": 1,
                "subject_code": 1006,
                "subject_name": "Materia 2 Update",
                "created": "2024-08-13T22:20:41",
                "edited": "2024-08-13T22:58:41",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_subject": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_subject_area": integer,
                "subject_code": integer,
                "subject_name": string,
                "created": string, // Data e hora no formato ISO 8601
                "edited": string, // Data e hora no formato ISO 8601
                "status": integer // 1 ou 0
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este Subject."
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 2"

        ``` json
        {
            "detail": "Informe o nome da disciplina"
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
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
                    "detail": string
                    "error": string
                }
            ```


---

**Change Status Subejct**

## **<element class="http-put">PUT<element>** - /subject/<element class="path-put">pk_subject</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject`       | path variables | string | None    | No       | Obtained in **_List Subejct_**        |

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
            "results": "Disciplina atualizado com sucesso."
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
                "detail": "Não foi possivel encontrar este Subject."
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este Subject.",
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

**Delete Subejct**

## **<element class="http-del">DELL<element>** - /subject/<element class="path-del">pk_subject</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_subject` | path variables | string | None    | No       | Obtained in **_List Subejct_** |

### **Response Body**

!!! success "204 No Content"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este Subject."
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao deletar Subject",
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
