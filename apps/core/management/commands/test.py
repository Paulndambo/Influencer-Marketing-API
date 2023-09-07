# yourapp/management/commands/custom_test_all.py

from django.core.management.base import BaseCommand
from django.test.runner import DiscoverRunner


class Command(BaseCommand):
    help = 'Run tests for specific test modules'

    def handle(self, *args, **options):
        test_modules = ['apps/products/tests']

        test_runner = DiscoverRunner(verbosity=1)

        failures = test_runner.run_tests(test_modules)

        if failures:
            self.stderr.write(self.style.ERROR("Some tests failed."))
            exit(1)
        else:
            self.stdout.write(self.style.SUCCESS("All tests passed."))
