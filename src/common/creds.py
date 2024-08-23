
import os
from dotenv import load_dotenv
load_dotenv()

class Credentials:

    def __init__(self) -> None:
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")


    def __test__(self) --> None:
        for element in self.__dict__.keys():
            