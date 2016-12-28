from setuptools import setup

install_requires = ['eventlet==0.20.0']

setup(
    name="rtsp", version="0.0.1", packages=['rtsp'], include_package_data=True, zip_safe=False,
    install_requires=install_requires
)
