from marshmallow import Schema, validate, validates, fields, ValidationError


class PhoneSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    phone_number = fields.String()

    @validates("phone_number")
    def validate_phone_number_length(self, value):
        if (len(value) < 12) or (len(value) > 12):
            raise ValidationError('phone number must contain 12 numbers')

    phone_type = fields.String(validate=[
        validate.Length(min=1, max=20),
        validate.OneOf(['home', 'mobile'])
    ])
    message = fields.String(dump_only=True)


class EmailSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    email = fields.String(validate=[
        validate.Length(max=120),
        validate.Email()
    ])
    email_type = fields.String(validate=[
        validate.Length(min=1, max=20),
        validate.OneOf(['job', 'personal'])
    ])
    message = fields.String(dump_only=True)


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(validate=[
        validate.Length(max=50)
    ])
    surname = fields.String(validate=[
        validate.Length(max=50)
    ])
    patronymic = fields.String(validate=[
        validate.Length(max=50)
    ])

    gender = fields.String(validate=[
        validate.Length(max=10),
        validate.OneOf(['male', 'female'])
    ])
    birth_day = fields.Date(format='%Y-%m-%d', error_messages={
        'format': '"{input}" cannot be formatted as a date.',
        'invalid': 'date must be written as: yyyy-mm-d'
    })
    address = fields.String()
    phones = fields.Nested(PhoneSchema, dump_only=True, many=True)
    emails = fields.Nested(EmailSchema, dump_only=True, many=True)
    message = fields.String(dump_only=True)
