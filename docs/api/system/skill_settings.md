# Skill Settings

**Get Skill Settings**

---

## **<element class="http-get">GET<element>** - /skillsettings/<element class="path-get">pk_skill_setting</element>/

??? note "Description"

    ### Description
    Captura as informações detalhadas de um Habilidade específico.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_skill_setting` | path variables | string | None    | No       | Obtained in **_List Skill Settings_** |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_skill_setting": 1,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "label_name": "Teste 4",
                "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público.",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_skill_setting": integer,
                "fk_campus": integer,
                "campus_name": string,
                "label_name": string,
                "description": string,
                "status": integer
            }
        }
        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao visualizar SkillSettings",
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

**List Skill Settings**

## **<element class="http-get">GET<element>** - /skillsettings/list/

??? note "Description"

    ### Description
    Lista todos os Habilidades cadastrados no sistema.

| Name            | In          | Type   | Default | Nullable | Description                 |
| :-------------- | :---------- | :----- | :------ | :------- | :-------------------------- |
| `Authorization` | header      | string | None    | No       | Obtained in **Login**       |
| `page`          | query param | string | 1       | Yes      |                             |
| `page_size`     | query param | string | 30      | Yes      |                             |
| `search`        | query param | string | None    | Yes      | Name of the skill to search |
| `status`        | query param | string | 1       | Yes      | 1-Active/0-Inative          |

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "navigation": {
                "next": "http://alppi/sys/api/v1/skillsettings/list/?page=3&page_size=20", // link para proxima pagina
                "previous": "http://alppi/sys/api/v1/skillsettings/list/?page=1&page_size=10" // link para pagina anterior
            },
            "next": 3, // numero da proxima pagina
            "previous": 1, // numero na pagina anterior
            "count": 1, // quantidade encontrata
            "results": [
                    {
                        "pk_skill_setting": 4,
                        "label_name": "Fardamento",
                        "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público.",
                        "status": 1
                    },
                    {
                        "pk_skill_setting": 2,
                        "label_name": "Musculação",
                        "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público.",
                        "status": 1
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
        "results": list
        }

        ```

??? danger "500"

    === "Error 1"

        ``` json
            {
                "detail": "Problemas ao visualizar SkillSettings",
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

**Create Skill Settings**

## **<element class="http-post">POST<element>** - /skillsettings/create/

??? note "Description"

    ### Description
    Rota para criação de um novo Habilidade.

| Name            | In     | Type   | Default | Nullable | Description           |
| :-------------- | :----- | :----- | :------ | :------- | :-------------------- |
| `Authorization` | header | string | None    | No       | Obtained in **Login** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "label_name": "teste 5",
        "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público."
    }
    ```

??? info "Body Schema"

    ```{ .json .no-copy}
    {
        "label_name": string,
        "description": string
    }
    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_skill_setting": 6,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "label_name": "Teste 5",
                "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público.",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```{ .json .no-copy}
        {
            "results": {
                "pk_skill_setting": integer,
                "fk_campus": integer,
                "campus_name": string,
                "label_name": string,
                "description": string,
                "status": integer
            }
        }
        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Informe o nome da Habilidade"
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
            "detail": "Informe o descrição da Habilidade"
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
                "detail": "Problemas ao cadastrar SkillSettings Area",
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

**Update Skill Settings**

## **<element class="http-put">PUT<element>** - /skillsettings/<element class="path-put">pk_skill_setting</element>/update/

??? note "Description"

    ### Description
    Rota para a atualização dos dados de um Habilidade.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_skill_setting` | path variables | string | None    | No       | Obtained in **_List Skill Settings_** |

### **Request Body**

=== "application/json"

    ``` json
    {
        "label_name": "fisico",
        "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público. Envolve o domínio da linguagem, expressão facial e corporal, organização de conteúdo e técnicas de persuasão.",
        "status": 0
    }
    ```

??? info "Body Schema"

    ```json
    {
        "label_name": string,
        "description": string,
        "status": integer // 1-True / 0-False
    }

    ```

### **Response Body**

??? success "200"

    === "application/json"

        ``` json
        {
            "results": {
                "pk_skill_setting": 5,
                "fk_campus": 1,
                "campus_name": "Atitus Educação Passo Fundo",
                "label_name": "Fisico",
                "description": "A oratória é a habilidade de comunicar ideias e informações de maneira eficaz através da fala em público. Envolve o domínio da linguagem, expressão facial e corporal, organização de conteúdo e técnicas de persuasão.",
                "status": 1
            }
        }
        ```

    ??? info "Schema"

        ```json
        {
            "results": {
                "pk_skill_setting": integer,
                "fk_campus": integer,
                "campus_name": string,
                "label_name": string,
                "description": string,
                "status": integer
            }
        }


        ```

??? warning "400"

    === "Error 1"

        ``` json
        {
            "detail": "Não foi possivel encontrar este SkillSettings."
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
            "detail": "Informe o nome da Habilidade"
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
                "detail": "Informe a descrição da Habilidade"
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
                "detail": "Problemas ao editar SkillSettings Area",
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

**Change Status Skill Settings**

## **<element class="http-put">PUT<element>** - /skillsettings/<element class="path-put">pk_skill_setting</element>/changestatus/

??? note "Description"

    ### Description
    Rota para a atualização de status de um Habilidade.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_skill_setting` | path variables | string | None    | No       | Obtained in **_List Skill Settings_** |

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
            "results": "Habilidade atualizado com sucesso."
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
                "detail": "Não foi possivel encontrar este SkillSettings."
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
                "detail": "Problemas ao alterar status do skill_settings",
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

**Delete Skill Settings**

## **<element class="http-del">DELL<element>** - /skillsettings/<element class="path-del">pk_skill_setting</element>/delete/

??? note "Description"

    ### Description
    Rota para excluir uma Habilidade.

| Name               | In             | Type   | Default | Nullable | Description                           |
| :----------------- | :------------- | :----- | :------ | :------- | :------------------------------------ |
| `Authorization`    | header         | string | None    | No       | Obtained in **Login**                 |
| `pk_skill_setting` | path variables | string | None    | No       | Obtained in **_List Skill Settings_** |

### **Response Body**

!!! success "204 No Content"

    


??? warning "400"

    === "Error 1"

        ``` json
            {
                "detail": "Não foi possivel encontrar este SkillSettings."
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
                "detail": "Problemas ao deletar SkillSettings",
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
