# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calamus']

package_data = \
{'': ['*']}

install_requires = \
['lazy-object-proxy>=1.4.3,<2.0.0',
 'marshmallow>=3.5.1,<4.0.0',
 'pyld>=2.0.2,<3.0.0',
 'rdflib>=6.0.0,<7.0.0']

extras_require = \
{'docs': ['Jinja2>=3.0.0,<3.1.0',
          'sphinx>=3.0.3,<4.0.0',
          'sphinx-rtd-theme>=0.4.3,<0.5.0',
          'sphinxcontrib-spelling>=5.0.0,<6.0.0']}

setup_kwargs = {
    'name': 'calamus',
    'version': '0.4.0',
    'description': 'calamus is a library built on top of marshmallow to allow (de-)Serialization of Python classes to JSON-LD.',
    'long_description': '..\n    Copyright 2017-2020 - Swiss Data Science Center (SDSC)\n    A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and\n    Eidgenössische Technische Hochschule Zürich (ETHZ).\n\n    Licensed under the Apache License, Version 2.0 (the "License");\n    you may not use this file except in compliance with the License.\n    You may obtain a copy of the License at\n\n        http://www.apache.org/licenses/LICENSE-2.0\n\n    Unless required by applicable law or agreed to in writing, software\n    distributed under the License is distributed on an "AS IS" BASIS,\n    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n    See the License for the specific language governing permissions and\n    limitations under the License.\n\n.. image:: https://github.com/SwissDataScienceCenter/calamus/blob/master/docs/reed.png?raw=true\n   :align: center\n\n==================================================\n calamus: JSON-LD Serialization Library for Python\n==================================================\n\n.. image:: https://readthedocs.org/projects/calamus/badge/?version=latest\n   :target: https://calamus.readthedocs.io/en/latest/en/latest/?badge=latest\n   :alt: Documentation Status\n\n.. image:: https://github.com/SwissDataScienceCenter/calamus/workflows/Test,%20Integration%20Tests%20and%20Deploy/badge.svg\n   :target: https://github.com/SwissDataScienceCenter/calamus/actions?query=workflow%3A%22Test%2C+Integration+Tests+and+Deploy%22+branch%3Amaster\n\n.. image:: https://badges.gitter.im/SwissDataScienceCenter/calamus.svg\n   :target: https://gitter.im/SwissDataScienceCenter/calamus?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge\n\ncalamus is a library built on top of marshmallow to allow (de-)Serialization\nof Python classes to JSON-LD\n\n\nInstallation\n============\n\ncalamus releases and development versions are available from `PyPI\n<https://pypi.org/project/calamus/>`_. You can install it using any tool that\nknows how to handle PyPI packages.\n\nWith pip:\n\n::\n\n    $ pip install calamus\n\n\nUsage\n=====\n\nAssuming you have a class like\n\n.. code-block:: python\n\n    class Book:\n        def __init__(self, _id, name):\n            self._id = _id\n            self.name = name\n\nDeclare schemes\n---------------\nYou can declare a schema for serialization like\n\n.. code-block:: python\n\n    from calamus import fields\n    from calamus.schema import JsonLDSchema\n\n    schema = fields.Namespace("http://schema.org/")\n\n    class BookSchema(JsonLDSchema):\n        _id = fields.Id()\n        name = fields.String(schema.name)\n\n        class Meta:\n            rdf_type = schema.Book\n            model = Book\n\nThe ``fields.Namespace`` class represents an ontology namespace.\n\nMake sure to set ``rdf_type`` to the RDF triple type you want get and\n``model`` to the python class this schema applies to.\n\nSerializing objects ("Dumping")\n-------------------------------\n\nYou can now easily serialize python classes to JSON-LD\n\n.. code-block:: python\n\n    book = Book(_id="http://example.com/books/1", name="Ilias")\n    jsonld_dict = BookSchema().dump(book)\n    #{\n    #    "@id": "http://example.com/books/1",\n    #    "@type": "http://schema.org/Book",\n    #    "http://schema.org/name": "Ilias",\n    #}\n\n    jsonld_string = BookSchema().dumps(book)\n    #\'{"@id": "http://example.com/books/1", "http://schema.org/name": "Ilias", "@type": "http://schema.org/Book"}\')\n\nDeserializing objects ("Loading")\n---------------------------------\n\nYou can also easily deserialize JSON-LD to python objects\n\n.. code-block:: python\n\n    data = {\n        "@id": "http://example.com/books/1",\n        "@type": "http://schema.org/Book",\n        "http://schema.org/name": "Ilias",\n    }\n    book = BookSchema().load(data)\n    #<Book(_id="http://example.com/books/1", name="Ilias")>\n\nValidation of properties in a namespace using an OWL ontology\n-------------------------------------------------------------\n\nYou can validate properties in a python class during serialization using an OWL ontology. The ontology used in the example below doesn\'t have ``publishedYear`` defined as a property.\n::\n\n    class Book:\n        def __init__(self, _id, name, author, publishedYear):\n            self._id = _id\n            self.name = name\n            self.author = author\n            self.publishedYear = publishedYear\n\n    class BookSchema(JsonLDSchema):\n        _id = fields.Id()\n        name = fields.String(schema.name)\n        author = fields.String(schema.author)\n        publishedYear = fields.Integer(schema.publishedYear)\n\n        class Meta:\n           rdf_type = schema.Book\n           model = Book\n\n    book = Book(id="http://example.com/books/2", name="Outliers", author="Malcolm Gladwell", publishedYear=2008)\n\n    data = {\n        "@id": "http://example.com/books/3",\n        "@type": "http://schema.org/Book",\n        "http://schema.org/name" : "Harry Potter & The Prisoner of Azkaban",\n        "http://schema.org/author" : "J. K. Rowling",\n        "http://schema.org/publishedYear" : 1999\n    }\n\n    valid_invalid_dict = BookSchema().validate_properties(\n        data,\n        "tests/fixtures/book_ontology.owl"\n    )\n    # The ontology doesn\'t have a publishedYear property\n    # {\'valid\': {\'http://schema.org/author\', \'http://schema.org/name\'}, \'invalid\': {\'http://schema.org/publishedYear\'}}\n\n    validated_json = BookSchema().validate_properties(book, "tests/fixtures/book_ontology.owl", return_valid_data=True)\n    #{\'@id\': \'http://example.com/books/2\', \'@type\': [\'http://schema.org/Book\'], \'http://schema.org/name\': \'Outliers\', \'http://schema.org/author\': \'Malcolm Gladwell\'}\n\n\n\nYou can also use this during deserialization.\n::\n\n    class Book:\n        def __init__(self, _id, name, author):\n            self._id = _id\n            self.name = name\n            self.author = author\n\n    schema = fields.Namespace("http://schema.org/")\n\n    class BookSchema(JsonLDSchema):\n        _id = fields.Id()\n        name = fields.String(schema.name)\n        author = fields.String(schema.author)\n\n        class Meta:\n            rdf_type = schema.Book\n            model = Book\n\n    data = {\n        "@id": "http://example.com/books/1",\n        "@type": "http://schema.org/Book",\n        "http://schema.org/name": "Harry Potter & The Chamber of Secrets",\n        "http://schema.org/author": "J. K. Rowling",\n        "http://schema.org/publishedYear": 1998,\n    }\n\n    verified_data = BookSchema().validate_properties(data, "tests/fixtures/book_ontology.owl", return_valid_data=True)\n\n    book_verified = BookSchema().load(verified_data)\n    #<Book(_id="http://example.com/books/1", name="Harry Potter & The Chamber of Secrets", author="J. K. Rowling")>\n\n\nThe function validate_properties has 3 arguments: ``data``, ``ontology`` and ``return_valid_data``.\n\n``data`` can be a Json-LD, a python object of the schema\'s model class, or a list of either of those.\n\n``ontology`` is a string pointing to the OWL ontology\'s location (path or URI).\n\n``return_valid_data`` is an optional argument with the default value ``False``. Default behavior is to return dictionary with valid and invalid properties. Setting this to True returns the JSON-LD with only validated properties.\n\nAnnotations\n-----------\n\nClasses can also be annotated directly with schema information, removing the need to have a separate schema. This\ncan be done by setting the ``metaclass`` of the model to ``JsonLDAnnotation``.\n\n.. code-block:: python\n\n    import datetime.datetime as dt\n\n    from calamus.schema import JsonLDAnnotation\n    import calamus.fields as fields\n\n    schema = fields.Namespace("http://schema.org/")\n\n    class User(metaclass=JsonLDAnnotation):\n        _id = fields.Id()\n        birth_date = fields.Date(schema.birthDate, default=dt.now)\n        name = fields.String(schema.name, default=lambda: "John")\n\n        class Meta:\n            rdf_type = schema.Person\n\n    user = User()\n\n    # dumping\n    User.schema().dump(user)\n    # or\n    user.dump()\n\n    # loading\n    u = User.schema().load({"_id": "http://example.com/user/1", "name": "Bill", "birth_date": "1970-01-01 00:00"})\n\nSupport\n=======\n\nYou can reach us on our `Gitter Channel <https://gitter.im/SwissDataScienceCenter/calamus>`_.\n',
    'author': 'Swiss Data Science Center',
    'author_email': 'contact@datascience.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SwissDataScienceCenter/calamus/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
