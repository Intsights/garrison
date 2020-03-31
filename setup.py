import setuptools


setuptools.setup(
    name='garrison-server',
    version='0.1.0',
    author='Gal Ben David',
    author_email='gal@intsights.com',
    url='https://github.com/intsights/garrison',
    project_urls={
        'Source': 'https://github.com/intsights/garrison',
    },
    license='MIT',
    description='Queue server base on RocksDB as a KV-Store backend and gRPC as an interface',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='rocksdb db database queue fastapi',
    python_requires='>=3.6',
    zip_safe=True,
    install_requires=[
        'python-rocksdb',
        'grpcio',
        'protobuf',
    ],
    packages=setuptools.find_packages(),
)
