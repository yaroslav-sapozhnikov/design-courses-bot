import psycopg2
import cfg

print("Connecting to DB...")

conn = psycopg2.connect(
    dbname=cfg.DB_NAME,
    host=cfg.DB_HOST,
    user=cfg.DB_USER,
    password=cfg.DB_PASSWORD,
    port=cfg.DB_PORT
)

print("Connection success")
