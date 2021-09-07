'''
Anything we add as router we need put the router here.
'''

# V1
import api.routers.v1.survey as survey_v1_routes
import api.routers.v1.users as user_v1_routes
# V2
import api.routers.v2.users as user_v2_routes

v1_routes = [
    survey_v1_routes.router,
    user_v1_routes.router,
]

v2_routes = [
    user_v2_routes.router,
]
