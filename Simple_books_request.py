import requests


class SimpleBooksRequest:
    BASE_URL = "https://simple-books-api.glitch.me"
    API_STATUS_ENDPOINT = "/status"
    GET_ALL_BOOKS_ENDPOINT = "/books"

    def get_api_status(self):
        api_status_url = self.BASE_URL + self.API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    def get_all_books(self, limit="", book_type=""):
        get_all_books_url = self.BASE_URL + self.GET_ALL_BOOKS_ENDPOINT
        if limit != "" and book_type == "":
            get_all_books_url += f"?limit={limit}"
        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"
        if limit != "" and book_type != "":
            get_all_books_url += f"?limit={limit}&type{book_type}"
        response = requests.get(get_all_books_url)
        return response




