# Term (Unused)


**Get Term**

---

## **<element class="http-get">GET<element>** - /term/<element class="path-get">pk_term</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma Etapa específica.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_term`          | path variables | string | None    | No       | Obtained in **_List Term_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_term": 1,
                "fk_term_type": 1,
                "name": "1-bimestre",
                "term_type": "bimestre"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_term": integer,
                "fk_term_type": integer,
                "name": string,
                "term_type": string
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este Term."
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
                "detail": "Problemas ao visualizar Term",
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

**List Term**

## **<element class="http-get">GET<element>** - /term/list/

??? note "Description"

    ### Description
    Lista todos as Etapas cadastradas no sistema

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
                "next": "http://alppi/sys/api/v1/term/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/term/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_term_type": 1,
                        "fk_term_type": 1,
                        "name": "1-bimestre",
                        "term_type": "bimestre"
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
                "fk_term_type": integer,
                "name": string,
                "term_type": string
            }
        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os Term.",
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

**Create Term**

## **<element class="http-post">POST<element>** - /term/create/

??? note "Description"

    ### Description
    Rota para criação de uma nova Etapa.


| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |
| `fk_term_type`  | body   | integer| None    | No      | Obtained in **List Term Type** |


### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "create",
        "fk_term_type": 1
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "name": string,
        "fk_term_type": integer
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_term": 10,
                "fk_term_type": 1,
                "name": "Create",
                "term_type": "bimestre"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_term": integer,
                "fk_term_type": integer,
                "name": string,
                "term_type": string
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
            }
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao cadastrar Term",
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

**Update Term**

## **<element class="http-put">PUT<element>** - /term/<element class="path-put">pk_term</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Etapa.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_term`          | path variables | string | None    | No       | Obtained in **_List Term_**           |
| `fk_term_type`     | body           | integer| None    | No       | Obtained in **List Term Type**        |

### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "update",
        "fk_term_type": 1
    }
    ```
    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "name": string,
            "fk_term_type": integer
        }
        ```



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_term": 10,
                "fk_term_type": 1,
                "name": "Update",
                "term_type": "bimestre"
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_term": integer,
                "fk_term_type": integer,
                "name": string,
                "term_type": string
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este Term."
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
            "detail": {
                "name": [
                    "This field is required."
                ]
            }
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": object
                }
            ```



??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao editar Term",
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

**Delete Term**

## **<element class="http-del">DELL<element>** - /term/<element class="path-del">pk_term</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Etapa.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_term`          | path variables | string | None    | No       | Obtained in **_List Term_**      |

### **Response Body**

!!! success "204 No Content"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este Term."
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
                "detail": "Problemas ao deletar Term",
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
