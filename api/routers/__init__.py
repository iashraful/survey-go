'''
Anything we add as router we need put the router here.
'''


import api.routers.tasks as task_routes
import api.routers.survey as survey_routes

routes = [
    task_routes.router,
    survey_routes.router
]
