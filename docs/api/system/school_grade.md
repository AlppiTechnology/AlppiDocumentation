# School Grade

**Get School Grade**

---

## **<element class="http-get">GET<element>** - /schoolgrade/<element class="path-get">pk_school_grade</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma Area do Conhecimento específica.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_grade`  | path variables | string | None    | No       | Obtained in **_List School Grade_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_grade": 10,
                "name": "1-serie",
                "fk_school_level": 3,
                "school_level": "ensino medio"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_school_grade": integer,
                "name": string,
                "fk_school_level": integer,
                "school_level": string
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SchoolGrade.",
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
                "detail":  "Não foi possivel encontrar este SchoolGrade.",
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

**List School Grade**

## **<element class="http-get">GET<element>** - /schoolgrade/list/

??? note "Description"

    ### Description
    Lista todos as Area do Conhecimentos cadastrados no sistema

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `page`          | query param | string | 1       | Yes      |                               |
| `page_size`     | query param | string | 30      | Yes      |                               |
| `level`         | query param | string | None    | Yes      | Name of the subject to search |




### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/schoolgrade/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/schoolgrade/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_school_grade": 1,
                        "name": "1-ano",
                        "fk_school_level": 1,
                        "school_level": "ensino fundamental I"
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
                "pk_school_grade": integer,
                "name": string,
                "fk_school_level": integer,
                "school_level": string
            }
        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os SchoolGrade.",
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

**Create School Grade**

## **<element class="http-post">POST<element>** - /schoolgrade/create/

??? note "Description"

    ### Description
    Rota para criação de uma nova Area do Conhecimento.


| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |
| `fk_school_level`| body | integer | None    | No      | Obtained in **List School Level** |


### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "create",
        "fk_school_level": 1
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "fk_school_level": integer,
        "name": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_grade": 25,
                "name": "Create",
                "fk_school_level": 1,
                "school_level": "ensino fundamental I"
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_school_grade": integer,
                "name": string,
                "fk_school_level": integer,
                "school_level": string
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
                "detail": "Problemas ao cadastrar SchoolGrade",
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

**Update School Grade**

## **<element class="http-put">PUT<element>** - /schoolgrade/<element class="path-put">pk_school_grade</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_grade`  | path variables | string | None    | No       | Obtained in **_List School Grade_**   |

### **Request Body**

=== "application/json"

    ``` json
    {
        "name": "1-ano",
        "fk_school_level": 1
    }
    ```
    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "name": string,
            "fk_school_level": integer
        }
        ```



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_grade": 1,
                "name": "1-Ano",
                "fk_school_level": 1,
                "school_level": "ensino fundamental I"
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_school_grade": integer,
                "name": string,
                "fk_school_level": integer,
                "school_level": string
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SchoolGrade.",
            "render": 1|
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
                "detail": "Problemas ao editar SchoolGrade",
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

**Delete School Grade**

## **<element class="http-del">DELL<element>** - /schoolgrade/<element class="path-del">pk_school_grade</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_grade` | path variables | string | None    | No       | Obtained in **_List School Grade_** |

### **Response Body**

!!! success "204 No Content"


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este SchoolGrade."
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
                "detail": "Não foi possivel encontrar este SchoolGrade.",
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
