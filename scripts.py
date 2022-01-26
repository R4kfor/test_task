from app import session, engine


if __name__ == '__main__':
    # with open('email_table_copy.csv', 'w') as f:
    #     conn = engine.raw_connection()
    #     cursor = conn.cursor()
    #     cmd = 'COPY email TO STDIN WITH (FORMAT CSV, HEADER TRUE)'
    #     cursor.copy_expert(cmd, f)
    #     conn.commit()

    with open('user_table_copy.csv', 'r') as f:
        conn = engine.raw_connection()
        cursor = conn.cursor()
        cmd = 'COPY users FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)
        conn.commit()
        f.close()

    with open('phone_table_copy.csv', 'r') as f:
        conn = engine.raw_connection()
        cursor = conn.cursor()
        cmd = 'COPY phones FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)
        conn.commit()
        f.close()

    with open('email_table_copy.csv', 'r') as f:
        conn = engine.raw_connection()
        cursor = conn.cursor()
        cmd = 'COPY email FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
        cursor.copy_expert(cmd, f)
        conn.commit()
        f.close()

# res = client.put('/create_user', json={'name': 'Sabir', 'surname': 'Tagirov', 'patronymic': 'Damirovich', 'gender': 'male', 'birth_day': '1998-06-17', 'address': 'Krasnoyarsk'})
# res = client.put('/create_user', json={'name': 'Sabir', 'surname': 'Tagirov', 'patronymic': 'Damirovich', 'gender': 'male', 'birth_day': '1998-06-17', 'address': 'Krasnoyarsk'})
# res = client.put('/create_user', json={'name': 'Ilya', 'surname': 'Kozyrev', 'patronymic': 'Aleksandrovich', 'gender': 'male', 'birth_day': '2000-12-01', 'address': 'Krasnoyarsk'})
# res = client.put('/create_user', json={'name': 'Margarita', 'surname': 'Tudareva', 'patronymic': 'Aleksyvna', 'gender': 'female', 'birth_day': '1999-05-17', 'address': 'Krasnoyarsk'})
# res = client.put('/create_user', json={'name': 'Elena', 'surname': 'Kolceva', 'patronymic': 'Dmitrievna', 'gender': 'female', 'birth_day': '1999-11-25', 'address': 'Izhevsk'})
# res = client.put('/create_user', json={'name': 'Dmitriy', 'surname': 'Kolcev', 'patronymic': 'Ivanovich', 'gender': 'female', 'birth_day': '1987-08-14', 'address': 'Izhevsk'})
