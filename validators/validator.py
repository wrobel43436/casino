import user
from gbl_const import handled_servers


def validate_return_json(request):




    json = request.json
    response = {'missing': [], 'wrong': []}

    if 'email' not in json:
        response['missing'].append['email']
    else:
        email = json['email']
    splited_email = email.split('@')

    if len(splited_email) != 2:
        response['wrong'].append('email')

    email_server = splited_email[1]
    server = email_server.split('.')

    if server[0] not in handled_servers:
        response['wrong'].append('email not supported')

    if 'firstName' not in json:
        response['missing'].append('first_name')

    if 'lastName' not in json:
        response['missing'].append('last_name')

    if 'isAdmin' not in json:
        response['missing'].append('is_admin')

    if 'isActive' not in json:
        response['missing'].append('is_active')

    if 'lastLogin' not in json:
        response['missing'].append('last_lgoin')

    if 'password' not in json:
        response['missing'].append('password')

    if len(response['missing']) + len(response['wrong']) > 0:
        return response, 400

    return None
