# -*- coding: utf-8 -*-

from {{cookiecutter.repo_name}} import create_app

#View function imports

app = create_app()

# Add routes
#app.add_url_rule('/', view_func=index, methods=['GET'])


if __name__ == "__main__":
    app.run(port=3333, debug=True)
