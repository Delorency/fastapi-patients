set -e
alembic upgrade head
python start.py