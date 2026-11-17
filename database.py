
import sqlite3

DATABASE_NAME = "kpk.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS riwayat_kpk (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bilangan1 INTEGER NOT NULL,
            bilangan2 INTEGER NOT NULL,
            hasil INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_kpk(a, b, hasil):
    conn = get_connection()

    cursor = conn.execute("""
        INSERT INTO riwayat_kpk
        (bilangan1, bilangan2, hasil)
        VALUES (?, ?, ?)
    """, (a, b, hasil))

    record_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return record_id


def get_all_history():
    conn = get_connection()

    rows = conn.execute("""
        SELECT * FROM riwayat_kpk
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def get_history_by_id(record_id):
    conn = get_connection()

    row = conn.execute("""
        SELECT * FROM riwayat_kpk
        WHERE id = ?
    """, (record_id,)).fetchone()

    conn.close()

    return dict(row) if row else None


def delete_history(record_id):
    conn = get_connection()

    cursor = conn.execute("""
        DELETE FROM riwayat_kpk
        WHERE id = ?
    """, (record_id,))

    conn.commit()

    deleted = cursor.rowcount > 0

    conn.close()

    return deleted
