from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
jc_results = Table('jc_results', post_meta,
    Column('id', String(length=128), primary_key=True, nullable=False),
    Column('jc_id', String(length=64)),
    Column('assay_date', DateTime),
    Column('assay_number1', SmallInteger),
    Column('assay_number2', SmallInteger),
    Column('N1', Float),
    Column('L1', Float),
    Column('M1', Float),
    Column('E1', Float),
    Column('B1', Float),
    Column('WBC1', Float),
    Column('N2', Float),
    Column('L2', Float),
    Column('M2', Float),
    Column('E2', Float),
    Column('B2', Float),
    Column('WBC2', Float),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['jc_results'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['jc_results'].drop()
