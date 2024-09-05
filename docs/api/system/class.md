# Class Settings

**Get Class Settings**

---

## **<element class="http-get">GET<element>** - /class/<element class="path-get">pk_class</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma Area do Conhecimento específica.

| Name            | In             | Type   | Default | Nullable | Description                           |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_class`      | path variables | string | None    | No       | Obtained in **_List Class Settings_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_class_setting": 1,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_school_grade": 10,
                "school_grade_name": "1-serie",
                "fk_shift": 1,
                "shift_name": "matutino",
                "fk_school_year": 1,
                "school_year_name": "2024/1",
                "name": "Turma 1",
                "edited": "2024-09-04T22:10:41",
                "status": 1,
                "pedagogical": [
                    {
                        "pk_pedagogical_setting": 2,
                        "fk_subject": 2,
                        "fk_employee_user": 4,
                        "subject_name": "Física",
                        "employee_name": "Professor 2"
                    },
                    {
                        "pk_pedagogical_setting": 1,
                        "fk_subject": 1,
                        "fk_employee_user": 3,
                        "subject_name": "Matemática",
                        "employee_name": "Professor 1"
                    },
                    {
                        "pk_pedagogical_setting": 3,
                        "fk_subject": 3,
                        "fk_employee_user": 9,
                        "subject_name": "Sociologia",
                        "employee_name": "Sargento 1"
                    }
                ],
                "students": [
                    {
                        "pk_student_class": 1,
                        "fk_student_user": 5,
                        "status": 1,
                        "student_name": "Professor 3"
                    },
                    {
                        "pk_student_class": 2,
                        "fk_student_user": 6,
                        "status": 1,
                        "student_name": "Professor 4"
                    },
                    {
                        "pk_student_class": 3,
                        "fk_student_user": 7,
                        "status": 1,
                        "student_name": "Professor 5"
                    }
                ]
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_class_setting": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_school_grade": integer,
                "school_grade_name": string,
                "fk_shift": integer,
                "shift_name": string,
                "fk_school_year": integer,
                "school_year_name": string,
                "name": string,
                "edited": string, // Representando data e hora em formato ISO 8601
                "status": integer,
                "pedagogical": array of objects [
                    {
                        "pk_pedagogical_setting": integer,
                        "fk_subject": integer,
                        "fk_employee_user": integer,
                        "subject_name": string,
                        "employee_name": string
                    }
                ],
                "students": array of objects [
                    {
                        "pk_student_class": integer,
                        "fk_student_user": integer,
                        "status": integer,
                        "student_name": string
                    }
                ]
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este ClassSetting.",
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
                "detail":  "Problemas ao listar PedagogicalSettings",
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

    === "Error 2"

        ``` json
            {
                "detail":  "Problemas ao listar StudentClass",
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

    === "Error 3"

        ``` json
            {
                "detail":  "Problemas ao visualizar ClassSetting",
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

**List Class Settings**

## **<element class="http-get">GET<element>** - /class/list/

??? note "Description"

    ### Description
    Lista todos as Area do Conhecimentos cadastrados no sistema

| Name            | In          | Type   | Default | Nullable | Description                   |
| :-------------- | :---------- | :----- | :------ | :------- | :---------------------------- |
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `page`          | query param | string | 1       | Yes      |                               |
| `page_size`     | query param | string | 30      | Yes      |                               |
| `search`        | query param | string | None    | Yes      | Name of the class to search   |
| `status`        | query param | string | 1       | Yes      | 1-Active/0-Inative            |
| `fk_school_year`| query param | string | None    | Yes      | PK - Obtained in **List School Year** |
| `fk_school_grade`| query param | string | None    | Yes      | PK - Obtained in **List School Grade** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/class/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/class/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_class_setting": 1,
                        "name": "Turma 1",
                        "fk_school_grade": 10,
                        "fk_school_year": 1,
                        "status": 1,
                        "school_grade_name": "1-serie",
                        "school_level_name": "ensino medio",
                        "school_year_name": "2024/1"
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
            "results": array of objects [
                    {
                        "pk_class_setting": integer,
                        "name": string,
                        "fk_school_grade": integer,
                        "fk_school_year": integer,
                        "status": integer,
                        "school_grade_name": string,
                        "school_level_name": string,
                        "school_year_name": string
                    }
                ]

        }


        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os ClassSetting.",
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

**Create Class Settings**

## **<element class="http-post">POST<element>** - /class/create/

??? note "Description"

    ### Description
    Rota para criação de uma nova Area do Conhecimento.

| Name              | In     | Type    | Default | Nullable | Description                       |
| :---------------- | :----- | :------ | :------ | :------- | :-------------------------------- |
| `Authorization`   | header | string  | None    | No       | Obtained in **Login**             |
| `fk_school_grade` | body   | integer | None    | No      | Obtained in **List School Grade**  |
| `fk_school_year`  | body   | integer | None    | No      | Obtained in **List School Year**   |
| `fk_shift`        | body   | integer | None    | No      | Obtained in **List Shift**         |
| `fk_subject`      | body   | integer | None    | No      | Obtained in **List Subject**       |
| `fk_employee_user`| body   | integer | None    | No      | Obtained in **List Employee**      |
| `students`        | body   | integer | None    | No      | Obtained in **List Student**       |

### **Request Body**

=== "application/json"

    ``` json
    {
        "fk_school_grade": 10,
        "fk_school_year": 1,
        "fk_shift": 1,
        "name": "Turma 1",
        "pedagogical": [
            {"fk_subject": 1,"fk_employee_user": 3},
            {"fk_subject": 2,"fk_employee_user": 4},
            {"fk_subject": 3,"fk_employee_user": 9}
        ],
        "students": [
            5,6,7
        ]
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "school_grade": integer,
        "school_year": integer,
        "shift": integer,
        "class_name": string,
        "pedagogical_assignments": array of objects [
            {
                "subject_id": integer,
                "teacher_id": integer
            }
        ],
        "students": array of integer
    }
    ```

### **Response Body**

??? success "201"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_class_setting": 2,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_school_grade": 10,
                "school_grade_name": "1-serie",
                "fk_shift": 1,
                "shift_name": "matutino",
                "fk_school_year": 1,
                "school_year_name": "2024/1",
                "name": "Turma 1",
                "edited": "2024-09-04T22:28:29",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_class_setting": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_school_grade": integer,
                "school_grade_name": string,
                "fk_shift": integer,
                "shift_name": string,
                "fk_school_year": integer,
                "school_year_name": string,
                "name": string,
                "edited": string, // Representando data e hora em formato ISO 8601
                "status": integer
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não é possivel possível cadastrar a diciplina NOME DA DISCIPLINA duas vezes na mesma turma. Mude a disciplina deste professor ou desative a que está cadastrada para que possa inserir a nova.",
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
            "detail": "Não foi possivel encontrar todos os PedagogicalSetting.",
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
    === "Error 3"

        ``` json
        {
            "detail": {
                "class_name": [
                    "campus with this campus code already exists."
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
    === "Error 4"

        ``` json
        {
            "detail": "Não é possivel possível cadastrar o aluno NOME ALUNO duas vezes na mesma turma.",
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
    === "Error 5"

        ``` json
        {
            "detail": "Não foi possivel encontrar todos os StudentClass.",
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
                "detail": "Problemas ao cadastrar ClassSetting",
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

**Update Class Settings**

## **<element class="http-put">PUT<element>** - /class/<element class="path-put">pk_class</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name              | In     | Type    | Default | Nullable | Description                       |
| :---------------- | :----- | :------ | :------ | :------- | :-------------------------------- |
| `Authorization`   | header | string  | None    | No       | Obtained in **Login**             |
| `fk_school_grade` | body   | integer | None    | No      | Obtained in **List School Grade**  |
| `fk_school_year`  | body   | integer | None    | No      | Obtained in **List School Year**   |
| `fk_shift`        | body   | integer | None    | No      | Obtained in **List Shift**         |
| `fk_subject`      | body   | integer | None    | No      | Obtained in **List Subject**       |
| `fk_employee_user`| body   | integer | None    | No      | Obtained in **List Employee**      |
| `students`        | body   | integer | None    | No      | Obtained in **List Student**       |

### **Request Body**

=== "application/json"

    ``` json
    {
        "fk_campus": 1,
        "fk_school_grade": 10,
        "fk_shift": 1,
        "fk_school_year": 1,
        "name": "Turma update",
        "status": 1,
        "pedagogical": [
            {
                "pk_pedagogical_setting": 2,
                "fk_subject": 2,
                "fk_employee_user": 4
            },
            {
                "pk_pedagogical_setting": 1,
                "fk_subject": 1,
                "fk_employee_user": 3
            },
            {
                "pk_pedagogical_setting": 3,
                "fk_subject": 3,
                "fk_employee_user": 9
            }
        ],
        "students": [13,14,15,16]
    }

    ```
    ??? info "Schema"

        ```{ .json .no-copy}
{
    "fk_campus": integer,
    "fk_school_grade": integer,
    "fk_shift": integer,
    "fk_school_year": integer,
    "name": string,
    "status": integer,
    "pedagogical": array of objects [
        {
            "pk_pedagogical_setting": integer,
            "fk_subject": integer,
            "fk_employee_user": integer
        }
    ],
    "students": array of integer
}
        ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_class_setting": 1,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_school_grade": 10,
                "school_grade_name": "1-serie",
                "fk_shift": 1,
                "shift_name": "matutino",
                "fk_school_year": 1,
                "school_year_name": "2024/1",
                "name": "Turma update",
                "edited": "2024-09-04T23:14:03",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_class_setting": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_school_grade": integer,
                "school_grade_name": string,
                "fk_shift": integer,
                "shift_name": string,
                "fk_school_year": integer,
                "school_year_name": string,
                "name": string,
                "edited": string,
                "status": integer
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este ClassSetting.",
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
            "detail": "Não é possivel possível cadastrar a diciplina NOME DA DISCIPLINA duas vezes na mesma turma. Mude a disciplina deste professor ou desative a que está cadastrada para que possa inserir a nova.",
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
    === "Error 3"

        ``` json
        {
            "detail": "Não foi possivel encontrar todos os PedagogicalSetting.",
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
    === "Error 4"

        ``` json
        {
            "detail": {
                "class_name": [
                    "campus with this campus code already exists."
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
    === "Error 5"

        ``` json
        {
            "detail": "Não é possivel possível cadastrar o aluno NOME ALUNO duas vezes na mesma turma.",
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
    === "Error 6"

        ``` json
        {
            "detail": "Não foi possivel encontrar todos os StudentClass.",
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
                "detail": "Problemas ao editar ClassSetting",
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
    === "Error 2"

        ``` json
            {
                "detail": "Problemas ao Atualizar SchoolYearDate",
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
    === "Error 3"

        ``` json
            {
                "detail": "Problemas ao editar StudentClass.",
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

**Change Status Class Settings**

## **<element class="http-put">PUT<element>** - /class/<element class="path-put">pk_class</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de uma Area do Conhecimento.

| Name            | In             | Type   | Default | Nullable | Description                           |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_class`      | path variables | string | None    | No       | Obtained in **_List Class Settings_** |

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
            "results": "Turma atualizada com sucesso."
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
                "detail": "Não foi possivel encontrar este ClassSetting.",
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
                "detail": "Problemas ao alterar status do PenagogicalSetting.",
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

    === "Error 2"

        ``` json
            {
                "detail": "Problemas ao alterar status do StudentClass.",
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

    === "Error 3"

        ``` json
            {
                "detail": "Problemas ao alterar status da Turma",
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

**Delete Class Settings**

## **<element class="http-del">DELL<element>** - /class/<element class="path-del">pk_class</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Area do Conhecimento.

| Name            | In             | Type   | Default | Nullable | Description                           |
| :-------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization` | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_class`      | path variables | string | None    | No       | Obtained in **_List Class Settings_** |

### **Response Body**

!!! success "204 No Content"

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar esta Turma.",
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
                "detail": "Problemas ao deletar ClassSetting.",
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
