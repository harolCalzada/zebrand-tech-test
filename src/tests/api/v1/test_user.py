from http import HTTPStatus


def test_user_list_api(api_client, admin_user, superadmin_user):
    api_client.force_authenticate(user=superadmin_user)
    response = api_client.get('/api/v1/user/')
    total_users = len([superadmin_user, admin_user])
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['count'] == total_users
    assert response_data['results'][0]['id'] == admin_user.id
    assert response_data['results'][0]['username'] == admin_user.username
    assert response_data['results'][0]['email'] == admin_user.email
    assert response_data['results'][0]['first_name'] == admin_user.first_name
    assert response_data['results'][0]['last_name'] == admin_user.last_name
    assert response_data['results'][0]['is_staff'] == admin_user.is_staff
    assert response_data['results'][0]['is_superuser'] == admin_user.is_superuser


def test_user_list_api_unauthorized(api_client):
    response = api_client.get('/api/v1/user/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_user_list_api_forbidden(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.get('/api/v1/user/')
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_user_detail_api(api_client, admin_user, superadmin_user):
    api_client.force_authenticate(user=superadmin_user)
    response = api_client.get(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['id'] == admin_user.id
    assert response_data['username'] == admin_user.username
    assert response_data['email'] == admin_user.email
    assert response_data['first_name'] == admin_user.first_name
    assert response_data['last_name'] == admin_user.last_name
    assert response_data['is_staff'] == admin_user.is_staff
    assert response_data['is_superuser'] == admin_user.is_superuser


def test_user_detail_api_unauthorized(api_client, admin_user):
    response = api_client.get(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_user_detail_api_forbidden(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.get(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_user_create_api(api_client, superadmin_user):
    api_client.force_authenticate(user=superadmin_user)
    username = 'admintest'
    email = 'admintest@zebrand.mx'
    password = 'password'
    is_staff = True
    is_superuser = True
    data = {
        'username': username,
        'email': email,
        'password': password,
        'is_staff': True,
        'is_superuser': True
    }
    response = api_client.post('/api/v1/user/', data=data)
    assert response.status_code == HTTPStatus.CREATED
    response_data = response.json()
    assert response_data['username'] == username
    assert response_data['email'] == email
    assert response_data['is_staff'] == is_staff
    assert response_data['is_superuser'] == is_superuser


def test_user_create_api_unauthorized(api_client):
    response = api_client.post('/api/v1/user/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_user_create_api_forbidden(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post('/api/v1/user/')
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_user_update_api(api_client, superadmin_user, admin_user):
    api_client.force_authenticate(user=superadmin_user)
    new_username = 'admintest'
    new_email = 'admintest@zebrand.mx'
    new_password = 'password'
    data = {
        'username': new_username,
        'email': new_email,
        'password': new_password
    }
    response = api_client.put(f'/api/v1/user/{admin_user.id}/', data=data)
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['username'] == new_username
    assert response_data['email'] == new_email


def test_user_update_api_unauthorized(api_client, admin_user):
    response = api_client.put(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_user_update_api_forbidden(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.put(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.FORBIDDEN

def test_user_delete_api(api_client, admin_user, superadmin_user):
    api_client.force_authenticate(user=superadmin_user)
    response = api_client.delete(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_user_delete_api_unauthorized(api_client, admin_user):
    response = api_client.delete(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_user_delete_api_forbidden(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(f'/api/v1/user/{admin_user.id}/')
    assert response.status_code == HTTPStatus.FORBIDDEN
