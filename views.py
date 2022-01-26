from flask import jsonify
from app import app, db, session, logger, docs
from schemas import UserSchema, PhoneSchema, EmailSchema
from models import *
from flask_apispec import use_kwargs, marshal_with


@app.route('/user_search', methods=['POST'])
@use_kwargs(UserSchema(only=('name', 'surname', 'patronymic')))
@marshal_with(UserSchema)
def search_user(**kwargs):
    try:
        user = User.get_user(**kwargs)
    except Exception as e:
        logger.warning(
            f'user search failed with this full name: {kwargs["surname"]} {kwargs["name"]} {kwargs["patronymic"]}'
        )
        return {'message': str(e)}, 400
    return user


@app.route('/create_user', methods=['PUT'])
@use_kwargs(UserSchema)
@marshal_with(UserSchema)
def create_user(**kwargs):
    try:
        new_user = User(**kwargs)
        new_user.save()
    except Exception as e:
        logger.warning(
            f'user create failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return new_user


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
@marshal_with(UserSchema)
def delete_user(user_id):
    try:
        user = User.get_user_by_id(user_id=user_id)
        user.delete()
    except Exception as e:
        logger.warning(
            f'user delete failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return '', 204


@app.route('/update_user/<int:user_id>', methods=['PATCH'])
@use_kwargs(UserSchema)
@marshal_with(UserSchema)
def update_user(user_id, **kwargs):
    try:
        user = User.get_user_by_id(user_id=user_id)
        user.update(**kwargs)
    except Exception as e:
        logger.warning(
            f'user update failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return user


@app.route('/add_phone/<int:user_id>', methods=['PUT'])
@use_kwargs(PhoneSchema)
@marshal_with(PhoneSchema)
def add_phone(user_id, **kwargs):
    try:
        phone = Phone(user_id, **kwargs)
        phone.save()
    except Exception as e:
        logger.warning(
            f'phone add failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return phone


@app.route('/update_phone/<int:user_id>/<int:phone_id>', methods=['PATCH'])
@use_kwargs(PhoneSchema)
@marshal_with(PhoneSchema)
def update_phone(user_id, phone_id, **kwargs):
    try:
        phone = Phone.get(user_id=user_id, phone_id=phone_id)
        phone.update(**kwargs)
    except Exception as e:
        logger.warning(
            f'phone update failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return phone


@app.route('/delete_phone/<int:user_id>/<int:phone_id>', methods=['DELETE'])
@marshal_with(PhoneSchema)
def delete_phone(user_id, phone_id):
    try:
        phone = Phone.get(user_id=user_id, phone_id=phone_id)
        phone.delete()
    except Exception as e:
        logger.warning(
            f'phone delete failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return '', 204


@app.route('/add_email/<int:user_id>', methods=['PUT'])
@use_kwargs(EmailSchema)
@marshal_with(EmailSchema)
def add_email(user_id, **kwargs):
    try:
        email = Email(user_id, **kwargs)
        email.save()
    except Exception as e:
        logger.warning(
            f'email add failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return email


@app.route('/update_email/<int:user_id>/<int:email_id>', methods=['PATCH'])
@use_kwargs(EmailSchema)
@marshal_with(EmailSchema)
def update_email(user_id, email_id, **kwargs):
    try:
        email = Email.get(user_id=user_id, email_id=email_id)
        email.update(**kwargs)
    except Exception as e:
        logger.warning(
            f'email update failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return email


@app.route('/delete_email/<int:user_id>/<int:email_id>', methods=['DELETE'])
@marshal_with(EmailSchema)
def delete_email(user_id, email_id):
    try:
        email = Email.get(user_id=user_id, email_id=email_id)
        email.delete()
    except Exception as e:
        logger.warning(
            f'email delete failed with errors {e}'
        )
        return {'message': str(e)}, 400
    return '', 204


@app.errorhandler(422)
def handle_error(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid Request.'])
    logger.warning(f'Invalid input params: {messages}')
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400
