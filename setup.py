import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kafka_handler",
    version="1.0.0",
    author="Harshit Budhraja",
    author_email="harshitbudhraja1301@gmail.com",
    description="A simple Kafka wrapper based on confluent_kafka python client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshitbudhraja/kafka_handler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['confluent_kafka;python_version>="3.6"'],
    python_requires='>=3.6',
)