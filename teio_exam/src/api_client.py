import requests

from src.data_models import DocData


class ApiClient:
    def __init__(self, host: str = "localhost", port: int = 36436):
        self.host = host
        self.port = port

    def fetch_questions(self, api_path: str = "/api/get_questions") -> list[DocData]:
        """从API获取题目数据"""
        url = f"http://{self.host}:{self.port}{api_path}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if not data.get("success"):
                raise RuntimeError("目前无法拉取题库")

            docs_data: list[DocData] = []
            for doc in data["data"]["questions"]:
                docs_data.append(DocData(doc["file_name"], doc["questions"]))

            return docs_data
        except Exception as e:
            raise RuntimeError(f"获取题目失败: {str(e)}") from e
