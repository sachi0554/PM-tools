## project setup for windows machine

create virtual environment 
cmd -> py -m venv .

activate virtual environment
cmd -> .\Scripts\activate

install from requirements.text 
cmd-> pip install -r requirements.txt


## Run app
cmd-> py manage.py runserver 

note- make sure active directory will be src/


## update requirements.text  file 
cmd-> pip freeze > requirements.txt
