from pydantic import BaseModel, Field

class LoginFormRequestDTO(BaseModel):
    username: str = Field(description="User Name")
    password: str = Field(description="Password")
