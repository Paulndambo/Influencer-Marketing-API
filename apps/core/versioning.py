from rest_framework import versioning


class HeaderVersioning(versioning.AcceptHeaderVersioning):
    default_version = '1.0'