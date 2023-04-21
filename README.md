# Como rodar o projeto gestao_financeira_engeselt



  - Clone esse repositório.
  
  - Crie um virtualenv com Python 3.11.3
  
  - Ative o virtualenv.
  
  - Instale as dependências.
  
  - Rode as migrações.
  

git clone https://github.com/AlanLima100/gestao_financeira_engeselt

python -m venv venv

pip install django

python -m pip install --upgrade pip (Para atualizar para masi rececente)

pip install -r requirements.txt

.\venv\Scripts\activate

python manage.py migrate

python manage.py runserver