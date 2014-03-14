from setuptools import setup

setup(
    name='bugzilla2fedmsg',
    version='0.1.0',
    description='Consume BZ messages over STOMP and republish to fedmsg',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='https://github.com/fedora-infra/bugzilla2fedmsg',
    install_requires=[
        "fedmsg",
        "python-bugzilla",
        "stomper",
    ],
    packages=[],
    entry_points="""
    [moksha.consumer]
    bugzilla2fedmsg = bugzilla2fedmsg:BugzillaConsumer
    """,
)