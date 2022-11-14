DB_HOST='127.0.0.1'
DB_PORT=3306
DB_USER='root'
DB_PASS='password'

DB_NAME_LIKE='your_dbname%_test'
DB_ADDFIELD_TABLE='your_table'
DB_ADDFIELD_COLUMNS={
    'your_field_1': "DATETIME NULL DEFAULT NULL COMMENT '字段1'",
    'your_field_2': "VARCHAR(10) NULL DEFAULT NULL COMMENT '字段2' AFTER `your_field_1`",
}