import logging
from neo4j import GraphDatabase

logger = logging.getLogger(__name__)

class KnowledgeGraph:
    def __init__(self):
        self.uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
        self.user = "neo4j"  # Replace with your Neo4j username
        self.password = "password"  # Replace with your Neo4j password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

    def add_scheme(self, title, description):
        with self.driver.session() as session:
            session.write_transaction(self._create_scheme, title, description)

    @staticmethod
    def _create_scheme(tx, title, description):
        query = (
            "MERGE (s:Scheme {title: $title}) "
            "ON CREATE SET s.description = $description "
            "ON MATCH SET s.description = $description"
        )
        tx.run(query, title=title, description=description)

    def get_scheme(self, title):
        with self.driver.session() as session:
            return session.read_transaction(self._get_scheme, title)

    @staticmethod
    def _get_scheme(tx, title):
        query = "MATCH (s:Scheme {title: $title}) RETURN s.title, s.description"
        result = tx.run(query, title=title)
        return result.single()
