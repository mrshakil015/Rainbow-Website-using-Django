#!/usr/bin/python

import sys, sqlite3

class sqlMerge(object):
    """Basic python script to merge data of 2 !!!IDENTICAL!!!! SQL tables"""

    def __init__(self, parent=None):
        super(sqlMerge, self).__init__()

        self.db_a = None
        self.db_b = None

    def loadTables(self, file_a, file_b):
        self.db_a = sqlite3.connect(file_a)
        self.db_b = sqlite3.connect(file_b)

        cursor_a = self.db_a.cursor()
        cursor_a.execute("SELECT name FROM sqlite_master WHERE type='table';")

        table_counter = 0
        print("SQL Tables available: \n===================================================\n")
        for table_item in cursor_a.fetchall():
            current_table = table_item[0]
            table_counter += 1
            print("-> " + current_table)
        print("\n===================================================\n")

        if table_counter == 1:
            table_to_merge = current_table
        else:
            table_to_merge = input("Table to Merge: ")

        return table_to_merge

    def merge(self, table_name):
        cursor_a = self.db_a.cursor()
        cursor_b = self.db_b.cursor()

        new_table_name = table_name + "_new"

        try:
            # Create the new table by copying the original
            cursor_a.execute(f"CREATE TABLE IF NOT EXISTS {new_table_name} AS SELECT * FROM {table_name} WHERE 1=0")

            # Get the column count to match the number of placeholders
            cursor_a.execute(f"PRAGMA table_info({table_name})")
            column_count = len(cursor_a.fetchall())

            # Prepare the INSERT statement with placeholders
            placeholders = ",".join("?" * column_count)
            insert_query = f"INSERT INTO {new_table_name} VALUES ({placeholders})"

            # Insert rows from db_b into the new table in db_a
            for row in cursor_b.execute(f"SELECT * FROM {table_name}"):
                print(row)
                cursor_a.execute(insert_query, row)

            # Rename the new table to replace the old table
            cursor_a.execute(f"DROP TABLE IF EXISTS {table_name}")
            cursor_a.execute(f"ALTER TABLE {new_table_name} RENAME TO {table_name}")
            self.db_a.commit()

            print("\n\nMerge Successful!\n")

        except sqlite3.OperationalError as e:
            print(f"ERROR!: Merge Failed - {e}")
            cursor_a.execute(f"DROP TABLE IF EXISTS {new_table_name}")

        finally:
            self.db_a.close()
            self.db_b.close()

        return


    def main(self):
        print("Please enter name of db file")
        file_name_a = input("File Name A:")
        file_name_b = input("File Name B:")

        table_name = self.loadTables(file_name_a, file_name_b)
        self.merge(table_name)

        return

if __name__ == '__main__':
    app = sqlMerge()
    app.main()