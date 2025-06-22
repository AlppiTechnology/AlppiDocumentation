# Internal Note

**Get Internal Note**

---

## **<element class="http-get">GET<element>** - /internal_note/<element class="path-get">pk_internal_note</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de uma notificação interna.

    O campo ``ct_single_attach`` é referente a insformação do Anexo Único  onmde consta o iten de advertência ou bonificação relacionado a nota interna.

    O `ct_deadline` é usada para o prazo final da Nota Interna.

    O `ct_student_deadline` é usada para o prazo final da resposta do aluno a Nota Internal.

    O `ct_cal_statement` é a sugestão do CAL como advertência.

    O `ct_cmdt_statement` é a escolah do COMANDANTE para advertência.

    A `ct_cmdt_answer` é preenchido como 1 ou 0 (True or False) caso o comandante apenas deseja seguir a recomentação do CAL, sem ter nescessidade de preencher os campo anterior.

    O campo `active_fields` contem o nome dos campos que o usuário está habilitado a editar.

    O `regulaments` são os regulamentos que o CAL pode anexar a Nota Internal.

    O `workflow` é o fluxo de movimentações de status a Nota Internal

| Name               | In             | Type   | Default | Nullable | Description                          |
| :----------------- | :------------- | :----- | :------ | :------- | :----------------------------------- |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                |
| `pk_internal_note` | path variables | string | None    | No       | Obtained in **_List Internal Note_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "pk_internal_note": 1,
                "ci_number": "00001",
                "fk_reporter": 1,
                "username": "Patrick Berlatto Piccini",
                "fk_campus": 1,
                "deadline": "2025-06-30",
                "student_deadline": "2025-06-28",
                "fk_student": 20,
                "student_name": "Aluno 1",
                "statement": 0,
                "custom_grade": null,
                "created": "2025-06-13T00:49:36",
                "updated": "2025-06-17T23:52:40",
                "status": 4,
                "attachments": [
                    {
                        "pk_student_single_attach": 2,
                        "fk_internal_note_id": 1,
                        "single_attach": "0005.0002"
                    }
                ],
                "comments": [
                    {
                        "pk_internal_note_comment": 1,
                        "fk_internal_note_id": 1,
                        "fk_user_id": 1,
                        "date": "2025-06-13T03:54:35.890824Z",
                        "comment": "comment save",
                        "group": "superuser",
                        "username": "Patrick Berlatto Piccini"
                    }
                ],
                "regulaments": [
                    {
                        "pk_student_regulament": 3,
                        "fk_internal_note_id": 1,
                        "regulament": "0004.0000"
                    }
                ],
                "active_fields": [
                    "attachments",
                    "deadline,",
                    "student_deadline",
                    "regulaments",
                    "statement",
                    "comments",
                    "status",
                    "custon_grade"
                ],
                "workflows": {
                    "1": [
                        {
                            "name": "Mover para justificar",
                            "fromStatusReference": "1",
                            "fromStatisReferenceName": "Criado",
                            "toStatusReference": "2",
                            "toStatusReferenceName": "Para Justificar"
                        }
                    ],
                    "2": [
                        {
                            "name": "Mover para analize",
                            "fromStatusReference": "2",
                            "fromStatisReferenceName": "Para Justificar",
                            "toStatusReference": "3",
                            "toStatusReferenceName": "Analize de justificativa"
                        }
                    ],
                    "3": [
                        {
                            "name": "Mover para validação",
                            "fromStatusReference": "3",
                            "fromStatisReferenceName": "Analize de justificativa",
                            "toStatusReference": "4",
                            "toStatusReferenceName": "Aguardando validação da analize"
                        }
                    ],
                    "4": [
                        {
                            "name": "Mover para Concluido",
                            "fromStatusReference": "4",
                            "fromStatisReferenceName": "Aguardando validação da analize",
                            "toStatusReference": "5",
                            "toStatusReferenceName": "Concluido"
                        },
                        {
                            "name": "Voltar para analize",
                            "fromStatusReference": "4",
                            "fromStatisReferenceName": "Criado",
                            "toStatusReference": "3",
                            "toStatusReferenceName": "Analize de justificativa"
                        }
                    ],
                    "5": [
                        {
                            "name": "Finalizar",
                            "fromStatusReference": "10004",
                            "fromStatisReferenceName": "Concluido",
                            "toStatusReference": null,
                            "toStatusReferenceName": null
                        }
                    ]
                }
            }

        ```

    ??? info "Schema"

        ```{ .json .no-copy}
            {
                "pk_internal_note": integer,
                "ci_number": string,
                "fk_reporter": integer,
                "username": string,
                "fk_campus": integer,
                "deadline": string,
                "student_deadline": string,
                "fk_student": integer,
                "student_name": string,
                "statement": integer,
                "custom_grade": integer or null,
                "created": string,
                "updated": string,
                "status": integer,
                "attachments": [
                    {
                        "pk_student_single_attach": integer,
                        "fk_internal_note_id": integer,
                        "single_attach": string
                    }
                ],
                "comments": [
                    {
                        "pk_internal_note_comment": integer,
                        "fk_internal_note_id": integer,
                        "fk_user_id": integer,
                        "date": string,
                        "comment": string,
                        "group": string,
                        "username": string
                    }
                ],
                "regulaments": [
                    {
                        "pk_student_regulament": integer,
                        "fk_internal_note_id": integer,
                        "regulament": string
                    }
                ],
                "active_fields": array of strings,
                "workflow": {
                    string: [
                        {
                            "name": string,
                            "fromStatusReference": string,
                            "fromStatisReferenceName": string,
                            "toStatusReference": string,
                            "toStatusReferenceName": string
                        }
                    ]
                }
            }


        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este CTInternalNote.",
                "render": 0
            }
        ```

        ??? info "Schema"

            ``` { .json .no-copy}
                {
                    "detail": string,
                    "render": integer
                }
            ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar Students Internal Note",
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
                "detail": "Problemas ao listar Regulaments",
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
                "detail": "Problemas ao listar Comentarios do Internal Note",
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
                "detail": "Problemas ao visualizar CTInternalNote",
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

**List Internal Note**

## **<element class="http-get">GET<element>** - /internal_note/list/

??? note "Description"

    ### Description
    Lista todos as notas internas do campus

| Name            | In          | Type   | Default | Nullable | Description           |
| :-------------- | :---------- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header      | string | None    | No       | Obtained in **Login** |
| `page`          | query param | string | 1       | Yes      |                       |
| `page_size`     | query param | string | 30      | Yes      |                       |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/internal_note/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/internal_note/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                {
                    "pk_internal_note": 1,
                    "ci_number": "00001",
                    "deadline": "2025-06-30",
                    "student_deadline": "2025-06-28",
                    "student_name": "Aluno 1",
                    "student_registration": "00011",
                    "created": "2025-06-13T00:49:36",
                    "updated": "2025-06-17T23:52:40",
                    "status": 4
                }
            ]
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "navigation": {
                "next": string
                "previous": string
            },
            "next": integer
            "previous": integer
            "count": integer
            "results": [
                {
                    "pk_internal_note": integer,
                    "ci_number": string,
                    "deadline": string,
                    "student_deadline": string,
                    "student_name": string,
                    "student_registration": string,
                    "created": string,
                    "updated": string,
                    "status": integer
                }
            ]
        }
        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao listar todos os CTInternalNote.",
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

**Create Internal Note**

## **<element class="http-post">POST<element>** - /internal_note/create/

??? note "Description"

    ### Description
    Rota para criação de uma nota internal com status 1 do workflow

    O campo ``ct_single_attach`` é referente a insformação do Anexo Único  onmde consta o iten de advertência ou bonificação relacionado a nota interna.

    O `ct_deadline` é usada para o prazo final da Nota Interna.

    O `ct_student_deadline` é usada para o prazo final da resposta do aluno a Nota Internal.

    O `ct_cal_statement` é a sugestão do CAL como advertência.

    O `ct_cmdt_statement` é a escolah do COMANDANTE para advertência.

    A `ct_cmdt_answer` é preenchido como 1 ou 0 (True or False) caso o comandante apenas deseja seguir a recomentação do CAL, sem ter nescessidade de preencher os campo anterior.

    O campo `active_fields` contem o nome dos campos que o usuário está habilitado a editar.

    O `regulaments` são os regulamentos que o CAL pode anexar a Nota Internal.

    O `workflow` é o fluxo de movimentações de status a Nota Internal

| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |

### **Request Body**

=== "application/json"

    ``` json
        {
            "deadline":"2024-06-30",
            "student_deadline":"2024-06-28",
            "students":{
                "fk_student":21,
                "single_attach":["0001.0002"],// Anexo unico
                "regulaments":["0001.0001"]  // regulamentos
                }
        }
    ```
    ??? info "Body Schema"

        ```{ .json .no-copy}
                {
                    "deadline": string,
                    "student_deadline": string,
                    "students": [
                        {
                            "fk_student": integer,
                            "single_attach":  array of strings,
                            "regulaments":  array of strings,
                        }
                    ]
                }
        ```

### **Response Body**

!!! success "201"



??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar todos os CTRegulament.",
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
                "detail": "Não foi possivel encontrar todos os CTStudentInternalNote.",
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
                    "ct_single_attach": [
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
                "detail": "Problemas ao cadastrar CTInternalNote",
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

**Update Internal Note**

## **<element class="http-put">PUT<element>** - /internal_note/<element class="path-put">pk_internal_note</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de uma internal note

    *OBS:* É obrigatório segir o fluxo do workflow para as edições e os actives_fields.

    O campo ``ct_single_attach`` é referente a insformação do Anexo Único  onmde consta o iten de advertência ou bonificação relacionado a nota interna.

    O `ct_deadline` é usada para o prazo final da Nota Interna.

    O `ct_student_deadline` é usada para o prazo final da resposta do aluno a Nota Internal.

    O `ct_cal_statement` é a sugestão do CAL como advertência.

    O `ct_cmdt_statement` é a escolah do COMANDANTE para advertência.

    A `ct_cmdt_answer` é preenchido como 1 ou 0 (True or False) caso o comandante apenas deseja seguir a recomentação do CAL, sem ter nescessidade de preencher os campo anterior.

    O campo `active_fields` contem o nome dos campos que o usuário está habilitado a editar.

    O `regulaments` são os regulamentos que o CAL pode anexar a Nota Internal.

    O `workflow` é o fluxo de movimentações de status a Nota Internal

| Name               | In             | Type   | Default | Nullable | Description                          |
| :----------------- | :------------- | :----- | :------ | :------- | :----------------------------------- |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                |
| `pk_internal_note` | path variables | string | None    | No       | Obtained in **_List Internal Note_** |

### **Request Body**

=== "application/json"

    ``` json
        {
            "deadline": "2025-06-30",
            "student_deadline": "2025-06-28",
            "statement": 0,
            "status": 5,
            "custom_grade": null, 
            "regulaments": [
                "0004.0000"
            ],
            "attachments": [
                "0005.0002"
            ]
        }
    ```

??? info "Body Schema"

    ```json
    {
    "deadline": string,
    "student_deadline": string,
    "statement": integer,
    "status": integer,
    "custom_grade": floating or null,
    "regulaments": array of strings,
    "attachments": array of strings
    }


    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "deadline": "2025-06-30",
            "student_deadline": "2025-06-28",
            "statement": 0,
            "custom_grade": null,
            "status": 1
        }
        ```

    ??? info "Schema"

        ```json
        {
            "deadline": string,
            "student_deadline": string,
            "statement": integer,
            "custom_grade": integer or null,
            "status": integer
        }

        ```

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este CTInternalNote",
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
                "detail": "Não é possovel cadastrar duas vezes o mesmo regulamento. {regulament}",
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
                "detail": "Não foi possivel encontrar todos os CTRegulament.",
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
                "detail": "Não foi possivel encontrar este CTRegulament.",
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
                "detail": "Não foi possivel encontrar todos os CTStudentInternalNote.",
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
                "detail": "Não foi possivel encontrar este CTStudentInternalNote.",
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
                "detail": "Não é possovel cadastrar duas vezes o mesmo regulamento. {regulament}",
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
                "detail": {
                    "ct_student_deadline": [
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
                "detail": "Problemas ao editar CTInternalNote",
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

**Delete Internal Note**

## **<element class="http-del">DELL<element>** - /internal_note/<element class="path-del">pk_internal_note</element>/delete/

??? note "Description"

    ### Description
    A rota de login é fundamental

    Deletar uma nota interna (apenas Super Usuário)

| Name               | In             | Type   | Default | Nullable | Description                          |
| :----------------- | :------------- | :----- | :------ | :------- | :----------------------------------- |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                |
| `pk_internal_note` | path variables | string | None    | No       | Obtained in **_List Internal Note_** |

### **Response Body**

!!! success "204"

??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este Internal Note.",
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
                "detail": "Problemas ao deletar Internal Note",
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
