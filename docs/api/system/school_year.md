# School Year

**Get School Year**

---

## **<element class="http-get">GET<element>** - /schoolyear/<element class="path-get">pk_school_year</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de um Ano Letivo específico.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_year` | path variables | string | None    | No       | Obtained in **_List School Year_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_year": 3,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_term_type": 1,
                "year": "2024",
                "total_grade": 100,
                "average_grade": 70,
                "created": "2024-06-01T15:42:56",
                "edited": "2024-06-01T15:42:56",
                "skill": 1,
                "status": 1,
                "dates": [
                    {
                        "pk_school_year_date": 9,
                        "grade": 20,
                        "init_date": "2024-06-02",
                        "final_date": "2024-06-30",
                        "fk_term": 1,
                        "term_name": "1-bimestre"
                    },
                    {
                        "pk_school_year_date": 10,
                        "grade": 20,
                        "init_date": "2024-07-01",
                        "final_date": "2024-07-31",
                        "fk_term": 2,
                        "term_name": "2-bimestre"
                    },
                    {
                        "pk_school_year_date": 11,
                        "grade": 30,
                        "init_date": "2024-08-01",
                        "final_date": "2024-08-31",
                        "fk_term": 3,
                        "term_name": "3-bimestre"
                    },
                    {
                        "pk_school_year_date": 12,
                        "grade": 30,
                        "init_date": "2024-09-01",
                        "final_date": "2024-09-30",
                        "fk_term": 4,
                        "term_name": "4-bimestre"
                    }
                ],
                "skill_list": [
                    {
                        "pk_school_year_skill": 5,
                        "fk_skill": 4,
                        "label_name": "Adaptabilidade"
                    },
                    {
                        "pk_school_year_skill": 3,
                        "fk_skill": 2,
                        "label_name": "Análise"
                    },
                    {
                        "pk_school_year_skill": 2,
                        "fk_skill": 1,
                        "label_name": "Teste 4"
                    },
                    {
                        "pk_school_year_skill": 4,
                        "fk_skill": 3,
                        "label_name": "Trab. Em Equipe"
                    }
                ]
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_school_year": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_term_type": integer,
                "year": string,
                "total_grade": integer,
                "average_grade": integer,
                "created": string,
                "edited": string,
                "skill": integer,
                "status": integer, // 1-True / 0-False
                "dates": array of objects {
                    "pk_school_year_date": integer,
                    "grade": integer,
                    "init_date": string,
                    "final_date": string,
                    "fk_term": integer,
                    "term_name": string
                },
                "skill_list": array of objects {
                    "pk_school_year_skill": integer,
                    "fk_skill": integer,
                    "label_name": string
                }
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SchoolYear."
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
                "detail": "Problemas ao listar SchoolYearDate",,
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
    === "Error 2"

        ``` json
            {
                "detail": "Problemas ao listar SchoolYearSkill",
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
    === "Error 3"

        ``` json
            {
                "detail":  "Problemas ao visualizar SchoolYear",
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

**List School Year**

## **<element class="http-get">GET<element>** - /schoolyear/list/

??? note "Description"

    ### Description
    Lista todos os Anos Letivos cadastrados no sistema

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
                "next": "http://alppi/sys/api/v1/schoolyear/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/schoolyear/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_school_year": 3,
                    "year": "2024",
                    "total_grade": 100.0,
                    "average_grade": 70.0,
                    "status": 1,
                    "menor_data_init": "2024-06-02",
                    "maior_data_final": "2024-09-30"
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
            "pk_school_year": integer,
            "year": string,
            "total_grade": number,
            "average_grade": number,
            "status": integer, // 1-True / 0-False
            "menor_data_init": string,
            "maior_data_final": string
        }
        }

        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os SchoolYear.",
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

**Create School Year**

## **<element class="http-post">POST<element>** - /schoolyear/create/

??? note "Description"

    ### Description
    Rota para criação de um novo Ano Letivo.

    **OBS: o campo "skill" no body define se voce deseja habilitar havaliação de habilidades no ano letivo. Se habilitado, é obrigatório que informe os IDs das skills na lista "skill_list"**

| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |
| `fk_term_type` | body | integer | None    | No       | Obtained in **List Term Type** |
| `fk_term` | body | integer | None    | No       | Obtained in **List Term** |
| `skill_list` | body | integer | None    | yes       | Obtained in **List Skill Settings** |

### **Request Body**

=== "application/json (BIMESTRE)"

    ``` json
    {
        "fk_term_type": 1, // Bimestre
        "year": "2024/Bi",
        "total_grade": 100.0,
        "average_grade": 70.0,
        "skill": 1, 
        "dates": [
            {
                "fk_term": 1, // primeiro bimestre
                "init_date": "2024-08-01",
                "final_date": "2024-08-09",
                "grade": 20
            },
            {
                "fk_term": 2, // segundo bimestre
                "init_date": "2024-08-10",
                "final_date": "2024-08-11",
                "grade": 20
            },
            {
                "fk_term": 3,  // terceiro bimestre
                "init_date": "2024-08-12",
                "final_date": "2024-08-13",
                "grade": 30
            },
            {
                "fk_term": 4,  // quarto bimestre
                "init_date": "2024-08-20",
                "final_date": "2024-08-31",
                "grade": 30
            }
        ],
        "skill_list": [1,2,3,4]
    }
    ```

=== "application/json (TRIMESTRE)"

    ``` json
    {
        "fk_term_type": 2, // Trimestre
        "year": "2024/Tri",
        "total_grade": 100.0,
        "average_grade": 70.0,
        "skill": 1, 
        "dates": [
            {
                "fk_term": 5, // primeiro trimestre
                "init_date": "2024-08-01",
                "final_date": "2024-08-09",
                "grade": 40
            },
            {
                "fk_term": 6, // segundo trimestre
                "init_date": "2024-08-10",
                "final_date": "2024-08-11",
                "grade": 30
            },
            {
                "fk_term": 7,  // terceiro trimestre
                "init_date": "2024-08-12",
                "final_date": "2024-08-13",
                "grade": 30
            }
        ],
        "skill_list": [1,2,3,4]
    }
    ```

=== "application/json (SEMESTRE)"

    ``` json
    {
        "fk_term_type": 3, // Semestre
        "year": "2024",
        "total_grade": 100.0,
        "average_grade": 70.0,
        "skill": 1, 
        "dates": [
            {
                "fk_term": 8, // primeiro semestre
                "init_date": "2024-08-01",
                "final_date": "2024-08-09",
                "grade": 50
            },
            {
                "fk_term": 9, // segundo semestre
                "init_date": "2024-08-10",
                "final_date": "2024-08-11",
                "grade": 50
            }
        ],
        "skill_list": [1,2,3,4]
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "fk_term_type": integer, // Bimestre
        "year": string,
        "total_grade": number,
        "average_grade": number,
        "skill": integer,
        "dates": array of objects {
            "fk_term": integer, // Termo ou bimestre
            "init_date": string,
            "final_date": string,
            "grade": integer
        },
        "skill_list": array of integers
    }

    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_year": 4,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_term_type": 1,
                "year": "2024/Bi",
                "total_grade": 100.0,
                "average_grade": 70.0,
                "created": "2024-08-07T21:30:04",
                "edited": "2024-08-07T21:30:04",
                "skill": 1,
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_school_year": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_term_type": integer, // Bimestre
                "year": string,
                "total_grade": number,
                "average_grade": number,
                "created": string,
                "edited": string,
                "skill": integer,
                "status": integer // 1-True / 0-False
            }
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Etapa não corresponsdente ao Tipo de Etapa"
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
            "detail":  "É nescessário ter data para 4 etapas."
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
            {
                "detail": string
            }
            ```
    === "Error 3"

        ``` json
        {
            "detail":   "A data 2024-08-12 Precisa ser maior que a 2024-08-13"
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
            {
                "detail": string
            }
            ```
    === "Error 4"

        ``` json
        {
            "detail":   "A soma das etapas não totalizam 100.0"
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
                "detail": "Problemas ao cadastrar SchoolYearDate",
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
    === "Error 2"

        ``` json
            {
                "detail": "Problemas ao cadastrar SchoolYearSkill",
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
    === "Error 3"

        ``` json
            {
                "detail": "Problemas ao deletar SchoolYearDate",
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
    === "Error 3"

        ``` json
            {
                "detail": "Problemas ao cadastrar SchoolYear",
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

**Update School Year**

## **<element class="http-put">PUT<element>** - /schoolyear/<element class="path-put">pk_school_year</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de um Ano Letivo.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_year` | path variables | string | None    | No       | Obtained in **_List School Year_** |

### **Request Body**

=== "application/json (BIMESTRE)"

    ``` json
    {

        "fk_campus": 1,
        "fk_term_type": 1,
        "year": "2028",
        "total_grade": 100.0,
        "average_grade": 70.0,
        "skill": 1,
        "status": 1,
        "dates": [
            {
                "pk_school_year_date": 13,
                "grade": 30.0,
                "init_date": "2024-08-01",
                "final_date": "2024-08-09",
                "fk_term": 1
            },
            {
                "pk_school_year_date": 14,
                "grade": 30.0,
                "init_date": "2024-08-10",
                "final_date": "2024-08-11",
                "fk_term": 2
            },
            {
                "pk_school_year_date": 15,
                "grade": 20.0,
                "init_date": "2024-08-12",
                "final_date": "2024-08-13",
                "fk_term": 3
            },
            {
                "pk_school_year_date": 16,
                "grade": 20.0,
                "init_date": "2024-08-20",
                "final_date": "2024-08-31",
                "fk_term": 4
            }
        ],
        "skill_list": [1,2,3,4]
        
    }
    ```

=== "application/json (TRIMESTRE)"

    ``` json
    {
        "fk_campus": 1,
        "fk_term_type": 2,
        "year": "2029",
        "total_grade": 100.0,
        "average_grade": 70.0,
        "skill": 1,
        "status": 1,
        "dates": [
            {
                "pk_school_year_date": 17,
                "grade": 60.0,
                "init_date": "2024-08-01",
                "final_date": "2024-08-09",
                "fk_term": 5
            },
            {
                "pk_school_year_date": 18,
                "grade": 20.0,
                "init_date": "2024-08-10",
                "final_date": "2024-08-11",
                "fk_term": 6
                },
            {
                "pk_school_year_date": 19,
                "grade": 20.0,
                "init_date": "2024-08-12",
                "final_date": "2024-08-13",
                "fk_term": 7
            }
        ],
        "skill_list": [1,2,3,4]

    }
    ```

=== "application/json (SEMESTRE)"

    ``` json
    {
        "fk_campus": 1,
        "fk_term_type": 3,
        "year": "2030",
        "total_grade": 100.0,
        "average_grade": 70.0,
        "skill": 1,
        "status": 1,
        "dates": [
            {
                "pk_school_year_date": 20,
                "grade": 50.0,
                "init_date": "2024-08-01",
                "final_date": "2024-08-09",
                "fk_term": 8            },
            {
                "pk_school_year_date": 21,
                "grade": 50.0,
                "init_date": "2024-08-10",
                "final_date": "2024-08-11",
                "fk_term": 9            }
        ],
        "skill_list": [1,2,3,4]
        
    }
    ```

??? info "Body Schema"

    ```json
    {
        "fk_campus": integer,
        "fk_term_type": integer, // Bimestre
        "year": string,
        "total_grade": number,
        "average_grade": number,
        "skill": integer,
        "status": integer, // 1-True / 0-False
        "dates": array of objects {
            "pk_school_year_date": integer,
            "grade": number,
            "init_date": string,
            "final_date": string,
            "fk_term": integer
        },
        "skill_list": array of integers
    }


    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_school_year": 4,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "fk_term_type": 1,
                "year": "2028",
                "total_grade": 100,
                "average_grade": 70,
                "created": "2024-08-07T21:30:04",
                "edited": "2024-08-12T18:02:52",
                "skill": 1,
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_school_year": integer,
                "fk_campus": integer,
                "campus_name": string,
                "fk_term_type": integer, // Bimestre
                "year": string,
                "total_grade": integer,
                "average_grade": integer,
                "created": string, // Data e hora no formato ISO 8601
                "edited": string, // Data e hora no formato ISO 8601
                "skill": integer,
                "status": integer // 1-True / 0-False
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SchoolYear."
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
            "detail": "A data 2024-08-10 Precisa ser maior que a 2024-08-09"
        }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 3"

        ``` json
            {
                "detail": "A soma das etapas não totalizam 100.0"
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 4"

        ``` json
            {
                "detail": "Não foi possivel encontrar este SchoolYearDate."
            }
        ```

        ??? info "Schema"

            ```{ .json .no-copy}
                {
                    "detail": string
                }
            ```
    === "Error 5"

        ``` json
        {
            "detail": {
                "year": [
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
                "detail": "Problemas ao Atualizar SchoolYearDate",
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
    === "Error 2"

        ``` json
            {
                "detail": "Problemas ao deletar SchoolYearDate",
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

    === "Error 3"

        ``` json
            {
                "detail": "Problemas ao cadastrar SchoolYearSkill",
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

    === "Error 4"

        ``` json
            {
                "detail": "Problemas ao editar SchoolYear",
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

**Change Status School Year**

## **<element class="http-put">PUT<element>** - /schoolyear/<element class="path-put">pk_school_year</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de um Ano Letivo.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_year` | path variables | string | None    | No       | Obtained in **_List School Year_** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "status": 1
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
            "results": "SchoolYear atualizado com sucesso."
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
                "detail": "Não foi possivel encontrar este SchoolYear."
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
                "detail": "Problemas ao alterar status do school_year",
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

**Delete School Year**

## **<element class="http-del">DELL<element>** - /schoolyear/<element class="path-del">pk_school_year</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir um Ano Letivo.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_school_year` | path variables | string | None    | No       | Obtained in **_List School Year_** |

### **Response Body**

!!! success "204 No Content"



??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail":  "Não foi possivel encontrar este SchoolYear."
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
                "detail": "Problemas ao deletar SchoolYear",
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
