# python_pagination_demo.py

def paginate(data, page=1, per_page=3):
    """
    data: list of items
    page: current page number
    per_page: number of items per page
    """
    total_items = len(data)
    total_pages = (total_items + per_page - 1) // per_page  # ceil division

    if page < 1 or page > total_pages:
        return {
            "page_data": [],
            "current_page": page,
            "total_pages": total_pages,
            "has_previous": False,
            "has_next": False,
            "previous_page": None,
            "next_page": None
        }

    start = (page - 1) * per_page
    end = start + per_page
    page_data = data[start:end]

    return {
        "page_data": page_data,
        "current_page": page,
        "total_pages": total_pages,
        "has_previous": page > 1,
        "has_next": page < total_pages,
        "previous_page": page - 1 if page > 1 else None,
        "next_page": page + 1 if page < total_pages else None
    }


# -------------------------
# CLI Pagination Demo
# -------------------------

data = [
    "John", "Paul", "George", "Ringo",
    "Yoko", "Linda", "Mick", "Keith",
    "Charlie", "Ronnie", "Freddie", "Brian"
]

per_page = 3
current_page = 1

while True:
    result = paginate(data, current_page, per_page)
    print("\n--- Page", result['current_page'], "of", result['total_pages'], "---")
    for item in result['page_data']:
        print(item)

    print("\nNavigation:")
    if result['has_previous']:
        print(f"P: Previous ({result['previous_page']})")
    if result['has_next']:
        print(f"N: Next ({result['next_page']})")
    print("Q: Quit")

    choice = input("\nEnter choice (P/N/Q) or page number: ").strip().upper()

    if choice == "Q":
        print("Exiting...")
        break
    elif choice == "P" and result['has_previous']:
        current_page = result['previous_page']
    elif choice == "N" and result['has_next']:
        current_page = result['next_page']
    elif choice.isdigit():
        page_num = int(choice)
        if 1 <= page_num <= result['total_pages']:
            current_page = page_num
        else:
            print("Invalid page number!")
    else:
        print("Invalid choice!")


# ===================== class based pagination CLI =====================

class Pagination:
    def __init__(self, data, per_page=3):
        self.data = data
        self.per_page = per_page
        self.total_items = len(data)
        self.total_pages = (self.total_items + self.per_page - 1) // self.per_page
        self.page = 1

    def get_page_data(self):
        start = (self.page - 1) * self.per_page
        end = start + self.per_page
        return self.data[start:end]

    def has_previous(self):
        return self.page > 1

    def has_next(self):
        return self.page < self.total_pages

    def previous_page(self):
        return self.page - 1 if self.has_previous() else None

    def next_page(self):
        return self.page + 1 if self.has_next() else None

    def go_to_page(self, page):
        if 1 <= page <= self.total_pages:
            self.page = page
        else:
            print("Invalid page number!")

    def __str__(self):
        return f"Page {self.page} of {self.total_pages}"

    def run_cli(self):
        """Run CLI loop"""
        while True:
            print(f"\n--- {self} ---")
            for item in self.get_page_data():
                print(item)

            print("\nNavigation:")
            if self.has_previous():
                print(f"P: Previous ({self.previous_page()})")
            if self.has_next():
                print(f"N: Next ({self.next_page()})")
            print("Q: Quit")

            choice = input("\nEnter choice (P/N/Q) or page number: ").strip().upper()

            if choice == "Q":
                print("Exiting...")
                break
            elif choice == "P" and self.has_previous():
                self.page = self.previous_page()
            elif choice == "N" and self.has_next():
                self.page = self.next_page()
            elif choice.isdigit():
                self.go_to_page(int(choice))
            else:
                print("Invalid choice!")

# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    data = [
        "John", "Paul", "George", "Ringo",
        "Yoko", "Linda", "Mick", "Keith",
        "Charlie", "Ronnie", "Freddie", "Brian"
    ]

    paginator = Pagination(data, per_page=3)
    paginator.run_cli()
