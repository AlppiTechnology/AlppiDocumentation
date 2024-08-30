# User Authentication
## Login Route

---
## **_POST_** - `/login/`

??? note "Description"
    
    ### Description
    A rota de login é fundamental para autenticar o usuário no sistema, garantindo que ele tenha acesso apenas aos módulos que a instituição associada está autorizada a utilizar e visualizar no frontend. Durante o processo de login, dois tokens JWT são gerados e retornados na resposta:

    **_user_access:_** Este token concede ao usuário a permissão para acessar o sistema, encapsulando informações essenciais, como ID do usuário, nome, status, e o grupo ao qual ele pertence.

    **_system_modules:_** Este token define quais módulos do sistema estão disponíveis para o usuário, com base nas permissões concedidas à instituição.

    ### User Access



    ~~~ json
    {
    "pk_user": 1,
    "registration": "00001",
    "username": "Patrick Berlatto Piccini",
    "status": true,
    "campus_code": 1,
    "pk_campus": 1,
    "ip_adress": "131.221.12.242",
    "group": "superuser",
    "current_school_year": 3,
    "current_term": 2,
    "exp": 2081726873
    }
    ~~~

    ### System Modules

    ~~~ json
    {
    "absence": 1,
    "grade": 1,
    "graphic": 1,
    "home": 1,
    "register": 1,
    "campus_name": "Atiitus Educação Passo Fundo",
    "cnpj": "02353336035",
    "free_trial": "2024-01-29",
    "in_test": false
    }
    ~~~


| Name      | In | Type | Default | Nullable | Description                          |
| :---------- | :----------------------------------- |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |




??? warning "400"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~

??? danger "500"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~


??? abstract "500"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~

??? info "500"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~

??? danger "500"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~


??? danger "500"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~


??? danger "500"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ~~~ python
        import requests
    ~~~