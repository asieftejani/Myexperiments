myweb: sh -c '> ./myfrappe/logs/access.log' && gunicorn -b 127.0.0.1:8000 -w 2 myfrappe.myapp:myapplication --reload --log-level debug --access-logfile ./myfrappe/logs/access.log

mydb: mariadbd &