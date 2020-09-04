To make migrations from codebase to Database
python manage.py makemigrations purchase
python manage.py sqlmigrate purchase <migration filename created>
python manage.py migrate

To open a python shell and execute python file 
python manage.py shell
exec(open('purchase/orm_create_purchase_status_data.py').read())
  
