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

| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_internal_note`| path variables| string | None | No | Obtained in **_List Internal Note_**|


### **Response Body**

??? success "200"

    === "application/json"

        ``` json
            {
                "results": {
                    "pk_ct_internal_note": 1,
                    "title": "Titulo da Ocorrência",
                    "fk_reporter": 1,
                    "username": "Patrick Berlatto Piccini",
                    "fk_campus": 1,
                    "ct_single_attach": "003.015",
                    "ct_deadline": "2024-06-30",
                    "ct_student_deadline": "2024-06-28",
                    "ct_cal_statement": 3,
                    "ct_cmdt_statement": 0,
                    "ct_cmdt_answer": 0,
                    "created": "2024-11-16T18:58:04",
                    "updated": "2024-12-04T00:28:42",
                    "status": 4,
                    "active_fields": [
                        "ct_single_attach",
                        "ct_deadline,",
                        "ct_student_deadline",
                        "regulaments",
                        "students",
                        "comments",
                        "status"
                    ],
                    "regulaments": [
                        "004.001.001",
                        "004.001.002",
                        "004.001.003",
                        "004.001.004"
                    ],
                    "students": [
                        {
                            "pk_ct_student_internal_note": 7,
                            "fk_student": 20,
                            "username": "Aluno 1",
                            "registration": "00011"
                        },
                        {
                            "pk_ct_student_internal_note": 20,
                            "fk_student": 21,
                            "username": "Aluno 2",
                            "registration": "00012"
                        }
                    ],
                    "comments": [
                        {
                            "pk_ct_comment": 1,
                            "fk_user": 1,
                            "date": "2024-11-16T21:58:37.321015Z",
                            "comment": "TESTE COMENTARIO",
                            "username": "Patrick Berlatto Piccini",
                            "registration": "00001",
                            "group": "superuser"
                        },
                        {
                            "pk_ct_comment": 2,
                            "fk_user": 5,
                            "date": "2024-12-12T03:25:42.102104Z",
                            "comment": "UPDATE 2",
                            "username": "Sargento 3",
                            "registration": "00005",
                            "group": "avaliador"
                        },
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
                }

        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
            {
                    "results": {
                        "pk_ct_internal_note": integer,
                        "title": string,
                        "fk_reporter": integer,
                        "username": string,
                        "fk_campus": integer,
                        "ct_single_attach": string,
                        "ct_deadline": string,
                        "ct_student_deadline": string,
                        "ct_cal_statement": integer,
                        "ct_cmdt_statement": integer,
                        "ct_cmdt_answer": integer,
                        "created": string,
                        "updated": string,
                        "status": integer,
                        "active_fields": array of strings,
                        "regulaments": array of strings,
                        "students": [
                            {
                                "pk_ct_student_internal_note": integer,
                                "fk_student": integer,
                                "username": string,
                                "registration": string
                            }
                        ],
                        "comments": [
                            {
                                "pk_ct_comment": integer,
                                "fk_user": integer,
                                "date": string,
                                "comment": string,
                                "username": string,
                                "registration": string,
                                "group": string or null
                            }
                        ],
                        "workflows": {
                            "1": [
                                {
                                    "name": string,
                                    "fromStatusReference": integer,
                                    "fromStatusReferenceName": string,
                                    "toStatusReference": integer,
                                    "toStatusReferenceName": string
                                }
                            ],
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


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `page`   | query param |string | 1 | Yes | |
| `page_size`   | query param |string | 30 | Yes | |



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
                    "pk_ct_internal_note": 1,
                    "title": "Titulo da Ocorrência",
                    "ct_deadline": "2024-06-30",
                    "ct_student_deadline": "2024-06-28",
                    "created": "2024-11-16T18:58:04",
                    "updated": "2024-12-04T00:28:42",
                    "status": 4
                },
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
                    "pk_ct_internal_note": integer,
                    "title": string,
                    "ct_deadline": string,
                    "ct_student_deadline": string,
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


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |



### **Request Body**


=== "application/json"

    ``` json
    {
        "title":"Titulo da Ocorrência LOCAL",
        "ct_single_attach":"0001.0002", // Anexo unico
        "ct_deadline":"2024-06-30",
        "ct_student_deadline":"2024-06-28",
        "ct_cal_statement":0, // opção "Parecer do CAL"
        "ct_cmdt_statement":0, // opção "Parecer do CMDT"
        "ct_cmdt_answer":0,
        "regulaments":["0001.0001","0002.0002"],
        "students":[
            21,22,23
        ]
    }
    ```
??? info "Body Schema"
    
    ```{ .json .no-copy}
        {
            "title": string,
            "ct_single_attach": string,
            "ct_deadline": string,
            "ct_student_deadline": string,
            "ct_cal_statement": integer,
            "ct_cmdt_statement": integer,
            "ct_cmdt_answer": integer,
            "regulaments": array of strings,
            "students": array of integers
        }

    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_ct_internal_note": 6,
                "title": "Titulo da Ocorrência",
                "fk_reporter": 1,
                "username": "Patrick Berlatto Piccini",
                "fk_campus": 1,
                "ct_single_attach": "0001.0002",
                "ct_deadline": "2025-06-30",
                "ct_student_deadline": "2025-06-28",
                "ct_cal_statement": 0,
                "ct_cmdt_statement": 0,
                "ct_cmdt_answer": 0,
                "created": "2025-01-20T23:53:11",
                "updated": "2025-01-20T23:53:11",
                "status": 1
            }
        }
        ```

    ??? info "Schema"
    
        ```{ .json .no-copy}
        {
            "results": {
                "pk_ct_internal_note": integer,
                "title": string,
                "fk_reporter": integer,
                "username": string,
                "fk_campus": integer,
                "ct_single_attach": string,
                "ct_deadline": string,
                "ct_student_deadline": string,
                "ct_cal_statement": integer,
                "ct_cmdt_statement": integer,
                "ct_cmdt_answer": integer,
                "created": string,
                "updated": string,
                "status": integer
            }
        }
        ```

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


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header | string | None | No | Obtained in **Login** |
| `pk_internal_note`| path variables| string | None | No | Obtained in **_List Internal Note_**|



### **Request Body**


=== "application/json"

    ``` json
        {
            "title": "Titulo da Ocorrência",
            "username": "Patrick Berlatto Piccini",
            "fk_campus": 1,
            "ct_single_attach": "003.015",
            "ct_deadline": "2025-06-30",
            "ct_student_deadline": "2025-06-28",
            "ct_cal_statement": 3,
            "ct_cmdt_statement": 0,
            "ct_cmdt_answer": 0,
            "created": "2025-11-16T18:58:04",
            "updated": "2025-12-04T00:28:42",
            "status": 4,
            "regulaments": [
                "004.001.001",
                "004.001.002",
                "004.001.003",
                "004.001.004"
            ],
            "students": [
                20,22,23,21
            ]
        }

    ```
??? info "Body Schema"
    
    ```json
    {
        "title": string,
        "username": string,
        "fk_campus": integer,
        "ct_single_attach": string,
        "ct_deadline": string,
        "ct_student_deadline": string,
        "ct_cal_statement": integer,
        "ct_cmdt_statement": integer,
        "ct_cmdt_answer": integer,
        "created": string,
        "updated": string,
        "status": integer,
        "regulaments": array of strings,
        "students": array of integers
    }

    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_ct_internal_note": 6,
                "title": "Titulo da Ocorrência excluir",
                "fk_reporter": 1,
                "username": "Patrick Berlatto Piccini",
                "fk_campus": 1,
                "ct_single_attach": "0001.0002",
                "ct_deadline": "2024-06-30",
                "ct_student_deadline": "2024-06-28",
                "ct_cal_statement": 0,
                "ct_cmdt_statement": 0,
                "ct_cmdt_answer": 0,
                "created": "2025-01-20T23:53:11",
                "updated": "2025-01-20T23:53:11",
                "status": 1
            }
        }
        ```

    ??? info "Schema"
    
        ```json
        {
            "results":{
                "pk_ct_internal_note": integer,
                "title": string,
                "fk_reporter": integer,
                "username": string,
                "fk_campus": integer,
                "ct_single_attach": string,
                "ct_deadline": string,
                "ct_student_deadline": string,
                "ct_cal_statement": integer,
                "ct_cmdt_statement": integer,
                "ct_cmdt_answer": integer,
                "created": string,
                "updated": string,
                "status": integer
            }
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


| Name              | In | Type | Default | Nullable | Description                          |
| :-----------------|:---|:-----|:--------|:---------|:------------------------------------ |
| `Authorization`   | header |string | None | No | Obtained in **Login** |
| `pk_internal_note`| path variables| string | None | No | Obtained in **_List Internal Note_**|


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



