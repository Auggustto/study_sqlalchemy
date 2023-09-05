from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import declarative_base, relationship

# Definindo uma base
Base = declarative_base()

# Erdando os atributos da classe base
class User(Base):
    __tablename__ = "user_account"

    # Definindo os atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    # Definindo uma representação para classe
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nullable=False Deixa o preenchimento do email como obrigatorio
    email_address = Column(String(30), nullable=False)
    # Chave estrangeira (quando preciso recuperar informações que estão em outras tabelas)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    # Definindo uma representação para classe
    def __repr__(self):
        return f"Addres(id={self.id}, email={self.email_address})"
