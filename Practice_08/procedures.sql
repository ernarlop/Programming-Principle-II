CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE name = p_name AND surname = p_surname
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO contacts(name, surname, phone)
        VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_surnames TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    names_len INT;
    surnames_len INT;
    phones_len INT;
BEGIN
    names_len := array_length(p_names, 1);
    surnames_len := array_length(p_surnames, 1);
    phones_len := array_length(p_phones, 1);

    IF names_len IS NULL OR surnames_len IS NULL OR phones_len IS NULL THEN
        RAISE EXCEPTION 'Input arrays must not be empty';
    END IF;

    IF names_len <> surnames_len OR names_len <> phones_len THEN
        RAISE EXCEPTION 'All input arrays must have the same length';
    END IF;

    DROP TABLE IF EXISTS incorrect_data;

    CREATE TEMP TABLE incorrect_data (
        name TEXT,
        surname TEXT,
        phone TEXT
    ) ON COMMIT DROP;

    FOR i IN 1..names_len LOOP
        IF p_phones[i] ~ '^\+?[0-9]{10,15}$' THEN
            IF EXISTS (
                SELECT 1
                FROM contacts
                WHERE name = p_names[i] AND surname = p_surnames[i]
            ) THEN
                UPDATE contacts
                SET phone = p_phones[i]
                WHERE name = p_names[i] AND surname = p_surnames[i];
            ELSE
                INSERT INTO contacts(name, surname, phone)
                VALUES (p_names[i], p_surnames[i], p_phones[i]);
            END IF;
        ELSE
            INSERT INTO incorrect_data(name, surname, phone)
            VALUES (p_names[i], p_surnames[i], p_phones[i]);
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value
       OR surname = p_value
       OR phone = p_value
       OR (name || ' ' || surname) = p_value;
END;
$$;