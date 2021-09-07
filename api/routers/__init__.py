'''
Anything we add as router we need put the router here.
'''


import api.routers.v1.survey as survey_routes
import api.routers.v1.users as user_routes

v1_routes = [
    survey_routes.router,
    user_routes.router,
]
