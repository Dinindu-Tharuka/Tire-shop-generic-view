from rest_framework.pagination import PageNumberPagination

class DefaultPagination(PageNumberPagination):
    page_size = 7

class BillPagination(PageNumberPagination):
    page_size = 5

class ChequePagination(PageNumberPagination):
    page_size = 10