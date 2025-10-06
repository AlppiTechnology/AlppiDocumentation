import re

def define_env(env):
    """
    Define macros customizadas para MkDocs.
    """

    @env.macro
    def route(method, path, new=False, upd=False):
        """
        Gera documentação de rota no formato customizado.

        Exemplo:
            {{ route("PUT", "/student/change-password/", new=True) }}
        """

        method = method.upper()
        method_lower = method.lower()

        # Classe de cor HTTP (trata 'DELETE' como 'del')
        color_class = f"http-del" if method_lower == "delete" else f"http-{method_lower}"
        path_class = f"path-del" if method_lower == "delete" else f"path-{method_lower}"

        # Substitui {param} por spans coloridos
        def replace_param(match):
            return f'<span class="{path_class}">{match.group(1)}</span>'
        path_html = re.sub(r"\{([^}]+)\}", replace_param, path)

        # Ícone "novo"
        new_icon = ":material-new-box:{ .new-alert }" if new else ""

        upd_icon = ":material-star-box:{ .upd-alert }" if upd else ""

        # HTML final
        if new_icon:
            html = f'**{new_icon} <span class="{color_class}">{method}</span>** - {path_html}'

        elif upd_icon:
            html = f'**{upd_icon} <span class="{color_class}">{method}</span>** - {path_html}'
        
        else:
            html = f'**<span class="{color_class}">{method}</span>** - {path_html}'
            

        return html


    @env.macro
    def superuser():
        """
        Tag de Super usuario

        Exemplo:
            {{ superuser() }}
        """
        html = '<span class="superuser">SuperUser</span>'
        return html

    @env.macro
    def admin():
        """
        Tag de Super usuario

        Exemplo:
            {{ admin() }}
        """
        html = '<span class="administrator">Administrator</span>'
        return html

    @env.macro
    def coordinator():
        """
        Tag de Super usuario

        Exemplo:
            {{ coordinator() }}
        """

        html = '<span class="coordinator">Coordinator</span>'
        return html

    @env.macro
    def evaluator():
        """
        Tag de Super usuario

        Exemplo:
            {{ evaluator() }}
        """
        html = '<span class="evaluator">Evaluator</span>'
        return html

    @env.macro
    def teacher():
        """
        Tag de Super usuario

        Exemplo:
            {{ teacher() }}
        """
        html = '<span class="teacher">Teacher</span>'
        return html


    @env.macro
    def student():
        """
        Tag de Super usuario

        Exemplo:
            {{ student() }}
        """
        html = '<span class="student">Student</span> '
        return html
