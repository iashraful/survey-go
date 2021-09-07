'''
Anything we add as router we need put the router here.
'''


import api.routers.survey as survey_routes
import api.routers.users as user_routes

routes = [
    survey_routes.router,
    user_routes.router,
]
