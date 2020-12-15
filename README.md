# estuduff-drf-api

  - Basic implementation of django-rest-framework API with swagger.


Requirements:
  1. Virtual environment runnning with python 3.8.0
  2. Clone project
  3. Run `pip install -r requirements.txt` to install the project dependencies
  3. Start the server `python manage.py runserver`
  
Caso ocorra algum erro na instalação do requirements.txt no Linux:
  1. Digite o seguinte comando no cmd fazer algumas atualizações: `sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev`
  2. Após instale o pyenv: `curl https://pyenv.run/ | bash` e `exec $SHELL`
  3. Atualize o pyenv: 
  
    git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    pyenv update
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    exec "$SHELL"
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
    
  4. Instale o plugin libpq-dev: `sudo apt-get install libpq-dev python-dev`
  5. Instale o pip install psycopg2 na pasta da aplicação: `pip install psycopg2`
  
 
The Swagger endpoints are `/doc/` and `/redoc/`
