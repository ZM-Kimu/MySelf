import argparse
import base64

import requests
from faker import Faker
from werkzeug.security import generate_password_hash

from app import app, db
from app.models.admin import Admin
from app.models.conversation import Conversation
from app.models.user import User

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test", "-t", action="store_true", help="Do a completely insert-delete test."
)
parser.add_argument(
    "--no-fake", "-nf", action="store_true", help="Do not generate fake data."
)
parser.add_argument("--show", "-s", action="store_true", help="Show all conversations.")


faker = Faker("zh_CN")

base_url = "http://localhost:8001"


def generate_data(num_users=35, num_conversations=100):
    print("----------Start Generate Data----------")
    users = []
    for _ in range(num_users):
        user = User(
            name=faker.name(),
            age=faker.random_int(10, 80),
            gender=faker.random_element(("male", "female")),
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    conversations = []
    with open("./app/resources/images/1.jpg", "rb") as img:
        for _ in range(num_conversations):
            user = faker.random_element(users)
            conversation = Conversation(
                user_uuid=user.uuid,
                type=faker.word(),
                question=faker.text(faker.random_int(0, 1536)),
                prompt=faker.text(faker.random_int(0, 1536)),
                image="/img/1",  # 或者生成base64图像数据
                is_processed=faker.boolean(),
            )
            conversations.append(conversation)
    db.session.add_all(conversations)
    db.session.commit()
    print(
        f"----------{len(users)} Users and {len(conversations)} Conversations Generated----------"
    )


with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    if not Admin.query.filter_by(username="admin").first():
        db.session.add(
            Admin(
                username="admin",
                password=generate_password_hash("123456"),
                role="super",
            )
        )
        db.session.commit()

args = parser.parse_args()
with app.app_context():
    if not args.no_fake:
        generate_data()
        print("----------Fake Data Generated----------")

if args.test:
    token = requests.post(
        base_url + "/login",
        timeout=10,
        json={"username": "admin", "password": "123456"},
        headers={"Content-Type": "application/json"},
    ).json()
    if not token["success"]:
        print(f"Error when trying to get token {token['message']}.")
    token = token["data"]["token"]
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    uuid = requests.post(
        base_url + "/create_user",
        headers=headers,
        json={
            "name": faker.name(),
            "age": faker.random_int(10, 80),
            "gender": faker.random_element(("male", "female")),
        },
        timeout=10,
    ).json()["data"]["user_uuid"]
    path = input("Input a picture path: ")
    with open(path, "rb") as img:
        conv_uuid = requests.post(
            base_url + "/create_conversation",
            headers=headers,
            json={
                "user_uuid": uuid,
                "type": faker.word(),
                "question": faker.text(1536),
                "answer": faker.text(12288),
                "prompt": faker.text(1536),
                "image": base64.b64encode(img.read()).decode(),
            },
            timeout=10,
        ).json()["data"]["conversation_uuid"]
    requests.delete(
        base_url + f"/delete_conversation/{conv_uuid}", headers=headers, timeout=10
    )
    print("Completion test complete.")


if args.show:
    print(
        "----------Start Get Conversations Test - From 0 Get 2 conversations----------"
    )
    token = requests.post(
        base_url + "/login",
        timeout=10,
        json={"username": "admin", "password": "123456"},
        headers={"Content-Type": "application/json"},
    ).json()
    if not token["success"]:
        print(f"Error when trying to get token {token['message']}.")
    token = token["data"]["token"]
    print(token)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    conversations = requests.post(
        base_url + "/get_conversations",
        headers=headers,
        json={"start": 0, "count": 2},
        timeout=10,
    ).json()["data"]
    print(conversations)
    print("----------Start Get Conversations Test - Get All Conversation----------")
    conversations = requests.post(
        base_url + "/get_conversations",
        headers=headers,
        timeout=10,
    ).json()["data"]["conversations"]
    print(f"----------Get {len(conversations)} Conversations For All----------")
