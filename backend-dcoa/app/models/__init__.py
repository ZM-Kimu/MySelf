from flask import Flask
from flask_migrate import revision, upgrade

from app.utils.constant import DataStructure as D
from app.utils.database import CRUD
from app.utils.logger import Log

from . import daily_report, department, member, period_task, verification
from .department import Department
from .member import Member


def dev_init(app: Flask) -> None:
    try:
        with app.app_context():
            upgrade(revision="head")  # 更新db结构
            revision(message="init", autogenerate=True)

            with CRUD(Department, name="开发组") as d:
                if not d.query_key():
                    d.add()

            with CRUD(Department, name="开发组") as d:
                if not d.query_key(name="AI开发组"):
                    instance = d.create_instance(no_attach=True)
                    d.update(
                        instance, name="AI开发组", parent_id=d.query_key().first().id
                    )
                    d.add(instance)

            with CRUD(Department, name="AI开发组") as d:
                dep_id = d.query_key().first().id

            with CRUD(Department, name="美术组") as d:
                if not d.query_key():
                    d.add()

            with CRUD(Department, name="美术组") as d:
                art_id = d.query_key().first().id

            with CRUD(Member, id="1145141919") as k:
                if not k.query_key():
                    k.add(name="ki", major="empty", role=D.admin, learning="None")
                    k.instance.set_password()
                else:
                    k.update(
                        name="ki",
                        major="empty",
                        role=D.admin,
                        learning="None",
                        phone="19191919",
                        email="0",
                        department_id=dep_id,
                    )

    except Exception as e:
        Log.error(f"Failed to initialize the db: {e}")
