# generate prisma models and sync with db schema
python -m prisma generate
python -m prisma db push --force-reset