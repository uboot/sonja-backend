import connexion
import sqlalchemy.exc

from sonja import database
from sonja.database import logger
from sonja.ssh import hash_password, test_password
from flask import abort
from flask_login import current_user
from swagger_server import models

permission_label_table = {
    "read": database.PermissionLabel.read,
    "write": database.PermissionLabel.write,
    "admin": database.PermissionLabel.admin
}


def __create_user(record: database.User):
    return models.User(
        id=str(record.id),
        type="users",
        attributes=models.UserAttributes(
            user_name=record.user_name,
            last_name=record.last_name,
            first_name=record.first_name,
            email=record.email,
            permissions=[models.UserAttributesPermissions(p.label.name) for p in record.permissions]
        )
    )


def add_user(body=None):
    if connexion.request.is_json:
        body = models.UserData.from_dict(connexion.request.get_json())  # noqa: E501

    if not body.data.attributes.user_name:
        abort(400)

    record = database.User()
    record.user_name = body.data.attributes.user_name
    record.last_name = body.data.attributes.last_name
    record.first_name = body.data.attributes.first_name
    record.email = body.data.attributes.email
    if body.data.attributes.password:
        record.password = hash_password(body.data.attributes.password)
    record.permissions.clear()
    if body.data.attributes.permissions:
        for p in body.data.attributes.permissions:
            permission = database.Permission()
            permission.label = permission_label_table[p.permission]
            record.permissions.append(permission)
    try:
        with database.session_scope() as session:
            session.add(record)
            session.commit()
            return models.UserData(data=__create_user(record)), 201
    except sqlalchemy.exc.IntegrityError as e:
        if e.orig.args[0] == database.ErrorCodes.DUPLICATE_ENTRY:
            abort(409)
        abort(400)


def delete_user(user_id):
    with database.session_scope() as session:
        try:
            database.remove_but_last_user(user_id)
        except database.OperationFailed:
            abort(400)
        except database.NotFound:
            abort(404)
    return None


def get_user(user_id):
    with database.session_scope() as session:
        record = session.query(database.User).filter_by(id=user_id).first()
        if not record:
            abort(404)
        return models.UserData(data=__create_user(record))


def get_users():
    with database.session_scope() as session:
        return models.UserList(
            data=[__create_user(record) for record in session.query(database.User).all()]
        )


def update_user(user_id, body=None):
    if connexion.request.is_json:
        body = models.UserData.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        with database.session_scope() as session:
            record = session.query(database.User).filter_by(id=user_id).first()
            if not record:
                abort(404)

            if body.data.attributes.password:
                if user_id == current_user.id:
                    # the password of the current user can only be changed if the "old" password is provided
                    if body.data.attributes.old_password and test_password(body.data.attributes.old_password, record.password):
                        record.password = hash_password(body.data.attributes.password)
                    else:
                        abort(400)
                else:
                    # passwords of other users can always be changed
                    record.password = hash_password(body.data.attributes.password)

            record.user_name = body.data.attributes.user_name
            record.last_name = body.data.attributes.last_name
            record.first_name = body.data.attributes.first_name
            record.email = body.data.attributes.email

            record.permissions.clear()
            if body.data.attributes.permissions:
                for p in body.data.attributes.permissions:
                    permission = database.Permission()
                    permission.label = permission_label_table[p.permission]
                    record.permissions.append(permission)

            return models.EcosystemData(data=__create_user(record))
    except sqlalchemy.exc.IntegrityError as e:
        if e.orig.args[0] == database.ErrorCodes.DUPLICATE_ENTRY:
            abort(409)
        abort(400)
