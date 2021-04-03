import pprint
import datetime
from app import db
from app.models import Isolate, IlluminaReadSet, Mykrobe, NanoporeReadSet


def add_isolate():
    isolate = Isolate(date_collected=datetime.datetime.utcnow(), species='Salmonella',
                            location='blah', isolate_identifier='PMQ124')
    print(isolate)
    #save the model to the database
    # use add_all([list, of, isolates]) to add multiples at the same time
    db.session.add(isolate)
    db.session.commit()


def add_isolate_and_irs():
    irs1 = IlluminaReadSet(read_set_filename='PMQ124_sequencing',
                                        path_r1="/path/to/PMQ124_sequencing_R1.fastq",
                                        path_r2="/path/to/PMQ124_sequencing_R2.fastq")
    irs2 = IlluminaReadSet(read_set_filename='PMQ124_sequencing',
                                        path_r1="/path/to/PMQ124_v2_sequencing_R1.fastq",
                                        path_r2="/path/to/PMQ124_v2_sequencing_R2.fastq")
    isolate = Isolate(date_collected=datetime.datetime.utcnow(), species='Salmonella',
                      location='blah', isolate_identifier='ASH001')
    isolate.illumina_read_sets = [irs1, irs2]
    # print(isolate.illumina_read_sets)
    db.session.add(isolate)
    db.session.commit()


def add_nanopore_read_set():
    nanopore_read_set = NanoporeReadSet(isolate_id=1, read_set_filename='PMQ124_sequencing_nanopore',
                                        path_fast5="/path/to/PMQ124_sequencing.nanopore.fast5",
                                        path_fastq="/path/to/PMQ124_sequencing.nanopore.fastq")
    db.session.add(nanopore_read_set)
    db.session.commit()


def add_illumina_read_set():
    illumina_read_set = IlluminaReadSet(read_set_filename='PMQ124_sequencing',
                                        r1="/path/to/PMQ124_sequencing_R1.fastq",
                                        r2="/path/to/PMQ124_sequencing_R2.fastq")
    db.session.add(illumina_read_set)
    db.session.commit()
    # return nanopore_read_set


def add_mykrobe():
    myk = Mykrobe(nanopore_read_set_id=1, species='Mtb', mykrobe_version="v0.8.0")
    db.session.add(myk)
    db.session.commit()


def query_isolates():
    # or can use db.session.query(Isolate)
    i = Isolate.query.all()
    for x in i:
        print(x.isolate_identifier)
        # pprint.pprint(x.__dict__)
        print([y.path_r1 for y in x.illumina_read_sets])


def query_irs():
    # or can use db.session.query(Isolate)
    i = IlluminaReadSet.query.all()
    pprint.pprint(i[0].isolate)


def query_nrs():
    # or can use db.session.query(Isolate)
    i = NanoporeReadSet.query.all()
    pprint.pprint(i)


def query_mykrobe():
    m = Mykrobe.query.all()
    for x in m:
        print(x)
        print(x.read_set_id)


def query_join():
    ## this one works - it works when teh first outerjoin is on Isolate, but not when it's on IRS
    # a = db.session.query(Isolate, IlluminaReadSet, Mykrobe) \
    #     .outerjoin(Isolate) \
    #     .outerjoin(Mykrobe).all()

    # a = db.session.query(Isolate, IlluminaReadSet, Mykrobe, NanoporeReadSet) \
    #     .outerjoin(Isolate) \
    #     .outerjoin(NanoporeReadSet, Isolate, NanoporeReadSet.isolate_id == Isolate.id) \
    #     .outerjoin(Mykrobe).all()

    # a = db.session.query(Isolate)

    # a = db.session.query(Isolate, IlluminaReadSet, NanoporeReadSet, Mykrobe)\
    #     .join(Isolate, IlluminaReadSet, Isolate.id == IlluminaReadSet.isolate_id, isouter=True)\
    #     .join(Isolate, NanoporeReadSet, Isolate.id == NanoporeReadSet.isolate_id, isouter=True).all()
        # .join(Mykrobe, IlluminaReadSet, IlluminaReadSet.id == Mykrobe.illumina_read_set_id, isouter=True)\
        # .join(Mykrobe, NanoporeReadSet, NanoporeReadSet.id == Mykrobe.nanopore_read_set_id, isouter=True)\

    a = db.session.query(Isolate, IlluminaReadSet, Mykrobe)\
        .join(Isolate, isouter=True)\
        .join(Mykrobe, isouter=True).distinct()

    b = db.session.query(Isolate, NanoporeReadSet, Mykrobe)\
        .join(Isolate, isouter=True)\
        .join(Mykrobe, isouter=True).distinct()

    # c = a.union(b)
        # .join()
        # .join(NanoporeReadSet, isouter=True).all()
        # .join(Isolate, isouter=True).all()
        # .join(Mykrobe, IlluminaReadSet, IlluminaReadSet.id == Mykrobe.illumina_read_set_id, isouter=True)\
        # .join(Mykrobe, NanoporeReadSet, NanoporeReadSet.id == Mykrobe.nanopore_read_set_id, isouter=True)\
    # a = a.extend(b)
    pprint.pprint(a.all())
    print()
    pprint.pprint(b.all())
    # print()
    # pprint.pprint(c.all())


def join_nrs():
    a = db.session.query(Isolate, NanoporeReadSet, Mykrobe)\
        .join(Isolate)\
        .join(Mykrobe) \
        .all()
    pprint.pprint(a)


def create_it():
    db.create_all()


def add_isolate_and_study():
    pass


# create_it()
# add_isolate()
# add_isolate_and_irs()
# add_nanopore_read_set()
# add_mykrobe()
# query_isolates()
# query_irs()
# query_nrs()
# query_mykrobe()
query_join()
# join_nrs()