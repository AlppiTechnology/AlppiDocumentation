# Skill Grade

**Get Skill Grade**


## **<element class="http-get">GET<element>** - /skillgrade/<element class="path-get">pk_class_setting</element>/<element class="path-get">fk_pedagogical</element>/<element class="path-get">fk_skill</element>

??? note "Description"

    ### Description
    Mostra as notas de uma Habilidade dos alunos de uma Turma e Disciplina especifica, informando tambem a Etapa(Term) que deseja visualizar.

| Name            | In          | Type   | Default | Nullable | Description                   |
|:----------------|:------------|:-------|:--------|:---------|:------------------------------|
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `pk_class_setting`| path param | string | None       | No      |Obtained in **List Class Settings** |
| `fk_pedagogical`| path param | string | None      | No      |Obtained in **List Pedagogical** |
| `fk_skill`      | path param | string | None      | No      |Obtained in **List Skill** |
| `fk_term`       | query param | string | None    | No      |Term you want to see the notes for. Obtained in **List Term**|



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "editable": true,
                "term_grade": 30.0,
                "skill": 1,
                "grades": [
                    {
                        "pk_skill_grade": 1,
                        "fk_student_user": 23,
                        "student_name": "Aluno 1",
                        "registration": "00023",
                        "grade_1": 0.0,
                        "grade_2": 0.0,
                        "grade_3": 0.0,
                        "grade_4": 0.0,
                        "grade_5": 0.0
                    }
                ]
            }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
            {
                "editable": boolean, // parametro para sinalizar se as notas desta Etapa estão disponiveis para edição
                "term_grade": integer, // Nota maxima suportada nesta etapa
                "skill": integer, // Identificador se esta habitado a criação de notas de Habilidades (Rota Skill Grade)
                "grades": [
                    {
                        "pk_skill_grade": integer,
                        "fk_student_user": integer,
                        "student_name": string,
                        "registration": string,
                        "grade_1": integer,
                        "grade_2": integer,
                        "grade_3": integer,
                        "grade_4": integer,
                        "grade_5": integer
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
            "detail": "Essa Etapa não pertece ao ano letivo.",
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
                "detail": "Problemas ao visualizar SubjectGrade.",
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


**Update Skill Grade**

## **<element class="http-put">PUT<element>** - /skillgrade/<element class="path-put">pk_class_setting</element>/<element class="path-put">fk_pedagogical</element>/<element class="path-put">fk_term</element>/<element class="path-put">fk_skill</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma Area do Conhecimento.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization` | header      | string | None    | No       | Obtained in **Login**         |
| `pk_class_setting`| path param | string | None       | No      |Obtained in **List Class Settings** |
| `fk_pedagogical`| path param | string | None      | No      |Obtained in **List Pedagogical** |
| `fk_skill`      | path param | string | None      | No      |Obtained in **List Skill** |
| `fk_term`       | path param | string | None    | No      |Term you want to see the notes for. Obtained in **List Term**|



### **Request Body**

=== "application/json"

    ``` json
        {
            "term_grade": 30.0,
            "grades": [
                {
                    "pk_skill_grade": 1,
                    "fk_student_user": 23,
                    "grade_1": 10.0,
                    "grade_2": 0.0,
                    "grade_3": 0.0,
                    "grade_4": 0.0,
                    "grade_5": 0.0
                } // ... other students
            ]
        }

    ```
    ??? info "Schema"

        ```{ .json .no-copy}
            {
                "term_grade": number,
                "grades": [
                    {
                        "pk_subject_grade": integer,
                        "fk_student_user": integer,
                        "grade_1": number,
                        "grade_2": number,
                        "grade_3": number,
                        "grade_4": number,
                        "grade_5": number
                    }
                ]
            }

                
        ```



### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": "Notas editadas com sucesso"
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
            "detail": "Essa Etapa não pertece ao ano letivo.",
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
            "detail": "A soma das notas do aluno NOME_DO_ALUNO não podem passar de VALOR_DA_NOTA. Verifique as notas e envie novamente.",
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
            "detail": "Não é possivel editar as notas nesse momento.",
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
                "detail": "Problemas ao editar SkillGrade",
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