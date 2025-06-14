import os
import pytest
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv(dotenv_path=BASE_DIR / ".env", override=False)
    load_dotenv(dotenv_path=BASE_DIR / ".env.local", override=True)
