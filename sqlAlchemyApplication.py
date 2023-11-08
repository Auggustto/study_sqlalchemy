from sqlalchemy import Column, Inspector, Integer, ForeignKey, String, create_engine, inspect, select
import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, Session

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

# Conexão com o banco de dados
engine = create_engine("sqlite://")

# Metadata / Criando as classes como tabelas no banco  de dados
Base.metadata.create_all(engine)

# Depreciado - Será removido em futuro release
# print(engine.table_names())

# Definindo um inspetor
#  insp = Inspector(engine) method on Inspector is deprecated and will be removed in a future release.
# print(insp.has_table("user_account"))

insp = sqlalchemy.inspect(engine)

# Printando os nomes das tabelas
print(insp.get_table_names())

# Printando o mome do esquema OBS: Quando não definimos o nome do esquema a propria aplicação define um  (main)
print(insp.default_schema_name)

# Criando a sessão
with Session(engine) as session:
     leonardo = User(
         name = "leonardo",
         fullname = "Leonardo Augusto",
         address = [Address(email_address = "leonardo@gmail.com")]
         )
     
     laura = User(
         name = "laura",
         fullname = "Laura Rosario",
         address = [Address(email_address = "laura@gmail.com")]
         )
     
     livia = User(
         name = "livia",
         fullname = "Livia Rosario",
         address = [Address(email_address = "livia@gmail.com"),
                    Address(email_address = "liviarosario@gmail.com")]
         )
     
     # Enviando para db
     session.add_all([leonardo, laura, livia])
     session.commit()

# Buscando os dados no db
statements = select(User).where(User.name.in_(["leonardo", "laura","livia"]))

# Preecisamsos tratar os dados antes de printar
# for user in session.scalars(statements):
#     print(user)

# Recuperando os email de livia
stmt_address = select(Address).where(Address.user_id.in_([3]))
for smtaddress in session.scalars(stmt_address):
    print(smtaddress)

# Utilizando outros tipos de filtros
filter_order_by = select(User).order_by(User.fullname.desc())
for filter_order in session.scalars(filter_order_by):
    print(filter_order)

# Usando join, retornando somete o Fullname e email_address
filter_join = select(User.fullname, Address.email_address).join_from(Address, User)
for filter_joins in session.scalars(filter_join): 
    print(filter_joins)

# O metodo scalars pega somente o primeiro resultado, 
# por esse motivo não retornou o Address.email_address para que funcione 
# o filtro devemos usar fetchall
connection = engine.connect()
results = connection.execute(filter_join).fetchall()
for result in results:
    print(result)

# Usando count para contar o numero de instancias
filter_counts = select(funct.count("*")).select_from(User)
for filter_count in filter_counts.scalars(filter_counts):
    print(filter_count)