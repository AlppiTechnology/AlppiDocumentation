# Student Presence

**Get Student Presence**


## **<element class="http-get">GET<element>** - /studentpresence/<element class="path-get">pk_class_setting</element>/<element class="path-get">fk_pedagogical</element>/

??? note "Description"

    ### Description
    Mostra as notas dos alunos de uma Turma e Disciplina especifica, informando tambem a Etapa(Term) que deseja visualizar.

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `pk_class_setting`| path param| string | None    | No       |Obtained in **List Class Settings** |
| `fk_pedagogical`| path param  | string | None    | No       |Obtained in **List Pedagogical** |
| `date`          | query param | string | None    | No       |Date you want to see the precences for.|



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "editable": true,
            "presences": [
                {
                    "pk_student_presence": 4,
                    "fk_student_user": 23,
                    "student_name": "Aluno 1",
                    "registration": "00023",
                    "presence": 100
                }
            ]
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
            {
                "editable": boolean, // parametro para sinalizar se as notas desta Etapa estão disponiveis para edição
                "presences": [
                    {
                        "pk_student_presence": integer,
                        "fk_student_user": integer,
                        "student_name": string,
                        "registration": string,
                        "presence": integer
                    }
                ]
            }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar esta Turma",
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
            "detail": "Não foi possivel encontrar esta turma vinculada a turma.",
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
            "detail": "Este usuario não é autorizado a ver as notas desta disciplina!.",
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
            "detail": "A data escolhida não está presente neste ano letivo.",
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
                "detail": "Problemas ao cadastrar SchoolYearDate",
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
                "detail": "Problemas ao listar StudentClass",
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
                "detail": "Problemas ao visualizar StudentPresence.",
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


**Update Student Presence**

## **<element class="http-put">PUT<element>** - /studentpresence/<element class="path-put">pk_class_setting</element>/<element class="path-put">fk_pedagogical</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_class_setting` | path param     | string | None    | No       |Obtained in **List Class Settings**    |
| `fk_pedagogical`   | path param     | string | None    | No       |Obtained in **List Pedagogical**       |
| `date`             | body           | string | None    | No       |Date you want to modify the precences for.|



### **Request Body**

=== "application/json"

    ``` json
        {   
            "date": "2024-09-24",
            "presences": [
                {
                    "pk_student_presence": 4,
                    "fk_student_user": 23,
                    "presence": 80
                },//other users datas
            ]
        }

    ```
    ??? info "Schema"

        ```{ .json .no-copy}
            {   
                "date": "string,
                "presences": [
                    {
                        "pk_student_presence": integer,
                        "fk_student_user": integer,
                        "presence": integer
                    }...
                ]
            }

                
        ```



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Presencas editadas com sucesso"
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
            "detail": "Não foi possivel encontrar esta Turma",
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
            "detail": "Não foi possivel encontrar esta turma vinculada a turma.",
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
            "detail": "Este usuario não é autorizado a ver as notas desta disciplina!.",
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
            "detail": "A data escolhida não está presente neste ano letivo.",
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
            "detail": "Porcentagem de presença deve ser maior ou igual que 0 e menor ou igual a 100.",
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
            "detail": "Não é possivel editar as presenças nesse momento.",
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
    === "Error 7"

        ``` json
        {
            "detail": "Não é autorizado aplicar presença a datas posteriores à atual",
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
    === "Error 8"

        ``` json
        {
            "detail": "Formato de data inválido. O formato esperado é 'YYYY-MM-DD'.",
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
                "detail": "Problemas ao cadastrar SchoolYearDate",
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
                "detail": "Problemas ao listar StudentClass",
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
                "detail": "Problemas ao editar StudentPresence",
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

