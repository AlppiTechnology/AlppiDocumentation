# Term Type (Unused)

**Get Term Type**

---

## **<element class="http-get">GET<element>** - /termtype/<element class="path-get">pk_term_type</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de um Tipo de Etapa específico.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_term_type`     | path variables | string | None    | No       | Obtained in **_List Term Type_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_term_type": 1,
                "name": "bimestre"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_term_type": integer,
                "name": string
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este TermType.",
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
                "detail": "Problemas ao visualizar TermType",
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

**List Term Type**

## **<element class="http-get">GET<element>** - /termtype/list/

??? note "Description"

    ### Description
    Lista todos os Tipo de Etapa cadastrados no sistema

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `page`          | query param | string | 1       | Yes      |                               |
| `page_size`     | query param | string | 30      | Yes      |                               |


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/termtype/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/termtype/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_term_type": 1,
                        "name": "bimestre"
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
                "pk_term_type": integer,
                "name": string
            }
        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os TermType.",
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

**Create Term Type**

## **<element class="http-post">POST<element>** - /termtype/create/

??? note "Description"

    ### Description
    Rota para criação de um novo Tipo de Etapa.


| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |
| `fk_subject_area`| body | integer | None    | Yes      | Obtained in **List Subject Area** |


### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "create"
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
                "pk_term_type": 4,
                "name": "Create"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_term_type": integer,
                "name": string
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": {
                "name": [
                    "This field is required."
                ]
            },
            "render": 0
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao cadastrar TermType",
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

**Update Term Type**

## **<element class="http-put">PUT<element>** - /termtype/<element class="path-put">pk_term_type</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de um Tipo de Etapa.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_term_type`           | path variables | string | None    | No       | Obtained in **_List Term Type_**        |

### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "update"
    }
    ```
    ??? info "Schema"

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
                "pk_term_type": 4,
                "name": "Update"
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_term_type": integer,
                "name": string
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este TermType.",
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
            "detail": {
                "name": [
                    "This field is required."
                ]
            },
            "render": 0
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object,
                    "render": integer
                }
            ```



??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao editar TermType",
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

**Delete Term Type**

## **<element class="http-del">DELL<element>** - /termtype/<element class="path-del">pk_term_type</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir um Tipo de Etapa.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_term_type`     | path variables | string | None    | No       | Obtained in **_List Term Type_**      |

### **Response Body**

!!! success "204 No Content"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este TermType."
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
                "detail": "Problemas ao deletar TermType",
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
