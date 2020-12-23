import os
from pypi_org.data.package import Package, Release
from pypi_org.data import db_session

def main():
    init_db()
    while True:
        insert_a_package()

def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'pypi.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)

def insert_a_package():
    p = Package()
    p.id = input("package id").strip().lower()
    p.summary = input("sum").strip()
    p.author_name = input("name").strip()
    p.license = input("licence").strip()

    print("Release 1")
    r = Release()
    r.major_ver = int(input("int").strip())
    r.minor_ver= int(input("int").strip())
    r.build_ver = int(input("int").strip())
    r.size= int(input("int").strip())
    p.releases.append(r)

    print("Release 2")
    r = Release()
    r.major_ver = int(input("int").strip())
    r.minor_ver= int(input("int").strip())
    r.build_ver = int(input("int").strip())
    r.size= int(input("int").strip())
    p.releases.append(r)


    session = db_session.factory()
    session.add(p)
    session.commit()

if __name__ == '__main__':
    main()