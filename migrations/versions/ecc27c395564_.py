"""empty message

Revision ID: ecc27c395564
Revises: c48cdec0b1db
Create Date: 2021-08-09 14:45:59.960127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecc27c395564'
down_revision = 'c48cdec0b1db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('artic_covid_result_readset_id_fkey', 'artic_covid_result', type_='foreignkey')
    op.create_foreign_key(None, 'artic_covid_result', 'read_set', ['readset_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('covid_confirmatory_pcr_extraction_id_fkey', 'covid_confirmatory_pcr', type_='foreignkey')
    op.create_foreign_key(None, 'covid_confirmatory_pcr', 'extraction', ['extraction_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('extraction_sample_id_fkey', 'extraction', type_='foreignkey')
    op.create_foreign_key(None, 'extraction', 'sample', ['sample_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('mykrobe_readset_id_fkey', 'mykrobe', type_='foreignkey')
    op.create_foreign_key(None, 'mykrobe', 'read_set', ['readset_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('pangolin_result_artic_covid_result_id_fkey', 'pangolin_result', type_='foreignkey')
    op.create_foreign_key(None, 'pangolin_result', 'artic_covid_result', ['artic_covid_result_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('pcr_result_sample_id_fkey', 'pcr_result', type_='foreignkey')
    op.drop_constraint('pcr_result_pcr_assay_id_fkey', 'pcr_result', type_='foreignkey')
    op.create_foreign_key(None, 'pcr_result', 'sample', ['sample_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.create_foreign_key(None, 'pcr_result', 'pcr_assay', ['pcr_assay_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('project_groups_id_fkey', 'project', type_='foreignkey')
    op.create_foreign_key(None, 'project', 'groups', ['groups_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('raw_sequencing_extraction_id_fkey', 'raw_sequencing', type_='foreignkey')
    op.drop_constraint('raw_sequencing_tiling_pcr_id_fkey', 'raw_sequencing', type_='foreignkey')
    op.drop_constraint('raw_sequencing_raw_sequencing_batch_id_fkey', 'raw_sequencing', type_='foreignkey')
    op.create_foreign_key(None, 'raw_sequencing', 'tiling_pcr', ['tiling_pcr_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.create_foreign_key(None, 'raw_sequencing', 'raw_sequencing_batch', ['raw_sequencing_batch_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.create_foreign_key(None, 'raw_sequencing', 'extraction', ['extraction_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('raw_sequencing_illumina_raw_sequencing_id_fkey', 'raw_sequencing_illumina', type_='foreignkey')
    op.create_foreign_key(None, 'raw_sequencing_illumina', 'raw_sequencing', ['raw_sequencing_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('raw_sequencing_nanopore_raw_sequencing_id_fkey', 'raw_sequencing_nanopore', type_='foreignkey')
    op.create_foreign_key(None, 'raw_sequencing_nanopore', 'raw_sequencing', ['raw_sequencing_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('read_set_readset_batch_id_fkey', 'read_set', type_='foreignkey')
    op.drop_constraint('read_set_raw_sequencing_id_fkey', 'read_set', type_='foreignkey')
    op.create_foreign_key(None, 'read_set', 'read_set_batch', ['readset_batch_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.create_foreign_key(None, 'read_set', 'raw_sequencing', ['raw_sequencing_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('read_set_batch_raw_sequencing_batch_id_fkey', 'read_set_batch', type_='foreignkey')
    op.create_foreign_key(None, 'read_set_batch', 'raw_sequencing_batch', ['raw_sequencing_batch_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('read_set_illumina_readset_id_fkey', 'read_set_illumina', type_='foreignkey')
    op.create_foreign_key(None, 'read_set_illumina', 'read_set', ['readset_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('read_set_nanopore_readset_id_fkey', 'read_set_nanopore', type_='foreignkey')
    op.create_foreign_key(None, 'read_set_nanopore', 'read_set', ['readset_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('sample_sample_source_id_fkey', 'sample', type_='foreignkey')
    op.create_foreign_key(None, 'sample', 'sample_source', ['sample_source_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('sample_source_project_project_id_fkey', 'sample_source_project', type_='foreignkey')
    op.drop_constraint('sample_source_project_sample_source_id_fkey', 'sample_source_project', type_='foreignkey')
    op.create_foreign_key(None, 'sample_source_project', 'project', ['project_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.create_foreign_key(None, 'sample_source_project', 'sample_source', ['sample_source_id'], ['id'], onupdate='cascade', ondelete='cascade')
    op.drop_constraint('tiling_pcr_extraction_id_fkey', 'tiling_pcr', type_='foreignkey')
    op.create_foreign_key(None, 'tiling_pcr', 'extraction', ['extraction_id'], ['id'], onupdate='cascade', ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tiling_pcr', type_='foreignkey')
    op.create_foreign_key('tiling_pcr_extraction_id_fkey', 'tiling_pcr', 'extraction', ['extraction_id'], ['id'])
    op.drop_constraint(None, 'sample_source_project', type_='foreignkey')
    op.drop_constraint(None, 'sample_source_project', type_='foreignkey')
    op.create_foreign_key('sample_source_project_sample_source_id_fkey', 'sample_source_project', 'sample_source', ['sample_source_id'], ['id'])
    op.create_foreign_key('sample_source_project_project_id_fkey', 'sample_source_project', 'project', ['project_id'], ['id'])
    op.drop_constraint(None, 'sample', type_='foreignkey')
    op.create_foreign_key('sample_sample_source_id_fkey', 'sample', 'sample_source', ['sample_source_id'], ['id'])
    op.drop_constraint(None, 'read_set_nanopore', type_='foreignkey')
    op.create_foreign_key('read_set_nanopore_readset_id_fkey', 'read_set_nanopore', 'read_set', ['readset_id'], ['id'])
    op.drop_constraint(None, 'read_set_illumina', type_='foreignkey')
    op.create_foreign_key('read_set_illumina_readset_id_fkey', 'read_set_illumina', 'read_set', ['readset_id'], ['id'])
    op.drop_constraint(None, 'read_set_batch', type_='foreignkey')
    op.create_foreign_key('read_set_batch_raw_sequencing_batch_id_fkey', 'read_set_batch', 'raw_sequencing_batch', ['raw_sequencing_batch_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.drop_constraint(None, 'read_set', type_='foreignkey')
    op.drop_constraint(None, 'read_set', type_='foreignkey')
    op.create_foreign_key('read_set_raw_sequencing_id_fkey', 'read_set', 'raw_sequencing', ['raw_sequencing_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.create_foreign_key('read_set_readset_batch_id_fkey', 'read_set', 'read_set_batch', ['readset_batch_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.drop_constraint(None, 'raw_sequencing_nanopore', type_='foreignkey')
    op.create_foreign_key('raw_sequencing_nanopore_raw_sequencing_id_fkey', 'raw_sequencing_nanopore', 'raw_sequencing', ['raw_sequencing_id'], ['id'])
    op.drop_constraint(None, 'raw_sequencing_illumina', type_='foreignkey')
    op.create_foreign_key('raw_sequencing_illumina_raw_sequencing_id_fkey', 'raw_sequencing_illumina', 'raw_sequencing', ['raw_sequencing_id'], ['id'])
    op.drop_constraint(None, 'raw_sequencing', type_='foreignkey')
    op.drop_constraint(None, 'raw_sequencing', type_='foreignkey')
    op.drop_constraint(None, 'raw_sequencing', type_='foreignkey')
    op.create_foreign_key('raw_sequencing_raw_sequencing_batch_id_fkey', 'raw_sequencing', 'raw_sequencing_batch', ['raw_sequencing_batch_id'], ['id'])
    op.create_foreign_key('raw_sequencing_tiling_pcr_id_fkey', 'raw_sequencing', 'tiling_pcr', ['tiling_pcr_id'], ['id'])
    op.create_foreign_key('raw_sequencing_extraction_id_fkey', 'raw_sequencing', 'extraction', ['extraction_id'], ['id'])
    op.drop_constraint(None, 'project', type_='foreignkey')
    op.create_foreign_key('project_groups_id_fkey', 'project', 'groups', ['groups_id'], ['id'])
    op.drop_constraint(None, 'pcr_result', type_='foreignkey')
    op.drop_constraint(None, 'pcr_result', type_='foreignkey')
    op.create_foreign_key('pcr_result_pcr_assay_id_fkey', 'pcr_result', 'pcr_assay', ['pcr_assay_id'], ['id'])
    op.create_foreign_key('pcr_result_sample_id_fkey', 'pcr_result', 'sample', ['sample_id'], ['id'])
    op.drop_constraint(None, 'pangolin_result', type_='foreignkey')
    op.create_foreign_key('pangolin_result_artic_covid_result_id_fkey', 'pangolin_result', 'artic_covid_result', ['artic_covid_result_id'], ['id'])
    op.drop_constraint(None, 'mykrobe', type_='foreignkey')
    op.create_foreign_key('mykrobe_readset_id_fkey', 'mykrobe', 'read_set', ['readset_id'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.drop_constraint(None, 'extraction', type_='foreignkey')
    op.create_foreign_key('extraction_sample_id_fkey', 'extraction', 'sample', ['sample_id'], ['id'])
    op.drop_constraint(None, 'covid_confirmatory_pcr', type_='foreignkey')
    op.create_foreign_key('covid_confirmatory_pcr_extraction_id_fkey', 'covid_confirmatory_pcr', 'extraction', ['extraction_id'], ['id'])
    op.drop_constraint(None, 'artic_covid_result', type_='foreignkey')
    op.create_foreign_key('artic_covid_result_readset_id_fkey', 'artic_covid_result', 'read_set', ['readset_id'], ['id'])
    # ### end Alembic commands ###
