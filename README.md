# todo sample app based on Flask

## to push the app to pivotal cloud foundry
1. cd webapp
2. cf push todo-rajib -m 128M --random-route

Then access the route from your browser. You should be able to add/delete/edit todo items.
DB integration - In progress!

## to re-deploy the app after source update
1. cd webapp
2. cf push todo-rajib

## to run the app locally
1. cd webapp
2. python todo_app.py
