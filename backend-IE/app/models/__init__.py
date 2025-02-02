from app import app, db

with app.app_context():
    db.drop_all()  # 仅在非生产环境下更新数据表
    db.create_all()
    print("Database tables created.")
