from telebot import TeleBot
import psycopg
import os

bot = TeleBot('<TOKEN>', threaded=False)
DB_URL = os.environ['POSTGRES_URL']
with psycopg.connect(DB_URL) as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY,
        ts TIMESTAMP DEFAULT NOW()
    )
    """)


@bot.message_handler()
def main(msg):
    user_id = msg.from_user.id
    with psycopg.connect(DB_URL) as conn:
        conn.execute(
            'INSERT INTO users VALUES (%s)'
            'ON CONFLICT DO NOTHING', (user_id,),
        )
        sign_up_ts = conn.execute(
            'SELECT ts FROM users WHERE id = %s',
            (user_id,),
        ).fetchone()[0]
    bot.send_message(
        user_id, 'Час твоєї реєстрації: '
        f'{sign_up_ts:%d.%m.%Y %H:%M:%S}'
    )
