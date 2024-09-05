# School Level

**Get School Level**

---

## **<element class="http-get">GET<element>** - /schoollevel/<element class="path-get">pk_school_level</nt>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma Area do Conhecimento específica.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_level`  | path variables | string | None    | No       | Obtained in **_List School Level_**   |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_level": 2,
                "name": "ensino fundamental II"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_school_level": integer,
                "name": string
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SchoolLevel.",
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
                "detail":  "Problemas ao visualizar SchoolLevel",
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

**List School Level**

## **<element class="http-get">GET<element>** - /schoollevel/list/

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
                "next": "http://alppi/sys/api/v1/schoollevel/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/schoollevel/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_school_level": 1,
                        "name": "ensino fundamental I"
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
                   {
                        "pk_school_level": integer,
                        "name": string
                    }
            }

        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os SchoolLevel.",
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

**Create School Level**

## **<element class="http-post">POST<element>** - /schoollevel/create/

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
                "pk_school_level": 6,
                "name": "Create"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_school_level": integer,
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
                "detail": "Problemas ao cadastrar SchoolLevel",
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

**Update School Level**

## **<element class="http-put">PUT<element>** - /schoollevel/<element class="path-put">pk_school_level</nt>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_level`  | path variables | string | None    | No       | Obtained in **_List School Level_**        |

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
                "pk_school_level": 5,
                "name": "Update"
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_school_level": integer,
                "name": string
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SchoolLevel.",
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
            "render": 0|
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
                "detail":  "Não foi possivel encontrar este SchoolLevel.",
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


**Delete School Level**

## **<element class="http-del">DELL<element>** - /schoollevel/<element class="path-del">pk_school_level</nt>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_level` h variables | string | None    | No       | Obtained in **_List School Level_** |

### **Response Body**

!!! success "204 No Content"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este SchoolLevel."
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
                "detail": "Problemas ao deletar SchoolLevel",
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
