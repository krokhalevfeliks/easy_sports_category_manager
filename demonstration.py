from mysql.connector import connect, Error

try:
    # Подключаемся без указания БД, чтобы создать её
    with connect(
        host="localhost",
        user="root",
        password="93uniner"
    ) as connection:
        create_database_query = "CREATE DATABASE IF NOT EXISTS sm_app"
        with connection.cursor() as cursor:
            cursor.execute(create_database_query)
            print("База данных sm_app создана (если не существовала).")


    # Основное подключение к БД sm_app
    with connect(
        host="localhost",
        user="root",
        password="93uniner",
        database="sm_app"
    ) as connection_with_db:
        print("Подключено к базе данных sm_app")
        
        # Создаём таблицу valen_info
        create_table_query = """
        CREATE TABLE IF NOT EXISTS valen_info (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
        """
        with connection_with_db.cursor() as cursor:
            cursor.execute(create_table_query)

        # SELECT из valen_info
        show_table_query = "SELECT * FROM valen_info"
        with connection_with_db.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

        # Создаём таблицу movies
        create_movies_table_query = """
        CREATE TABLE IF NOT EXISTS movies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            release_year YEAR,
            genre VARCHAR(100),
            collection_in_mil INT
        )
        """
        with connection_with_db.cursor() as cursor:
            cursor.execute(create_movies_table_query)
            print("Таблица movies создана (если не существовала).")


        # Создаём таблицу reviewers
        create_reviewers_table_query = """
        CREATE TABLE IF NOT EXISTS reviewers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100)
        )
        """
        with connection_with_db.cursor() as cursor:
            cursor.execute(create_reviewers_table_query)
            connection_with_db.commit()
            print("Таблица reviewers создана (если не существовала).")

        # Создаём таблицу ratings
        create_ratings_table_query = """
        CREATE TABLE IF NOT EXISTS ratings (
            movie_id INT,
            reviewer_id INT,
            rating DECIMAL(2,1),
            FOREIGN KEY(movie_id) REFERENCES movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
            PRIMARY KEY(movie_id, reviewer_id)
        )
        """
        with connection_with_db.cursor() as cursor:
            cursor.execute(create_ratings_table_query)
            connection_with_db.commit()
            print("Таблица ratings создана (если не существовала).")


        # DESCRIBE movies
        describe_query = "DESCRIBE movies"
        with connection_with_db.cursor() as cursor:
            cursor.execute(describe_query)
            result = cursor.fetchall()
            print("Схема таблицы movies:")
            for row in result:
                print(row)

        # ALTER TABLE (исправляем тип поля)
        alter_table_query = """
        ALTER TABLE movies
        MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """
        with connection_with_db.cursor() as cursor:
            cursor.execute(alter_table_query)
            connection_with_db.commit()  # Фиксируем изменения
            print("Поле collection_in_mil изменено на DECIMAL(4,1).")


        # Повторный DESCRIBE после изменений
        with connection_with_db.cursor() as cursor:
            cursor.execute(describe_query)
            result = cursor.fetchall()
            print("\nСхема таблицы movies после изменений:")
            for row in result:
                print(row)

        # Вставляем данные в таблицу movies (внутри блока with!)
        insert_movies_query = """
        INSERT INTO movies (title, release_year, genre, collection_in_mil)
        VALUES
            ('Forrest Gump', 1994, 'Drama', 330.2),
            ('3 Idiots', 2009, 'Drama', 2.4),
            ('Eternal Sunshine of the Spotless Mind', 2004, 'Drama', 34.5),
            ('Good Will Hunting', 1997, 'Drama', 138.1),
            ('Skyfall', 2012, 'Action', 304.6),
            ('Gladiator', 2000, 'Action', 188.7),
            ('Black', 2005, 'Drama', 3.0),
            ('Titanic', 1997, 'Romance', 659.2),
            ('The Shawshank Redemption', 1994, 'Drama', 28.4),
            ('Udaan', 2010, 'Drama', 1.5),
            ('Home Alone', 1990, 'Comedy', 286.9),
            ('Casablanca', 1942, 'Romance', 1.0),
            ('Avengers: Endgame', 2019, 'Action', 858.8),
            ('Night of the Living Dead', 1968, 'Horror', 2.5),
            ('The Godfather', 1972, 'Crime', 135.6),
            ('Haider', 2014, 'Action', 4.2),
            ('Inception', 2010, 'Adventure', 293.7),
            ('Evil', 2003, 'Horror', 1.3),
            ('Toy Story 4', 2019, 'Animation', 434.9),
            ('Air Force One', 1997, 'Drama', 138.1),
            ('The Dark Knight', 2008, 'Action', 535.4),
            ('Bhaag Milkha Bhaag', 2013, 'Sport', 4.1),
            ('The Lion King', 1994, 'Animation', 423.6),
            ('Pulp Fiction', 1994, 'Crime', 108.8),
            ('Kai Po Che', 2013, 'Sport', 6.0),
            ('Beasts of No Nation', 2015, 'War', 1.4),
            ('Andadhun', 2018, 'Thriller', 2.9),
            ('The Silence of the Lambs', 1991, 'Crime', 68.2),
            ('Deadpool', 2016, 'Action', 363.6),
            ('Drishyam', 2015, 'Mystery', 3.0)
        """
        with connection_with_db.cursor() as cursor:
            cursor.execute(insert_movies_query)
            connection_with_db.commit()  # Фиксируем изменения
            print(f"Добавлено {cursor.rowcount} записей в таблицу movies.")


except Error as e:
    print(f"Ошибка: {e}")