from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # Set your default page size here

    def paginate_queryset(self, queryset, request, view=None):
        if request.accepted_renderer.format == 'csv':
            return None  # Disable pagination for CSV format
        return super().paginate_queryset(queryset, request, view)
