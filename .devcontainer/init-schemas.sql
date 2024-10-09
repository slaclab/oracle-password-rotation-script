CREATE USER schema_one IDENTIFIED BY password_one;
GRANT CONNECT, RESOURCE TO schema_one;

CREATE USER schema_two IDENTIFIED BY password_two;
GRANT CONNECT, RESOURCE TO schema_two;
