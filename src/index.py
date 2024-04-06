from rich.console import Console
import rich.traceback

rich.traceback.install()
console = Console()

data = {
    "Mathew": {
        "id": 1,
        "math": 7.5,
        "english": 8.5,
        "history": 9.5,
        "science": 10.0,
        "geography": 9.5,
        "politics": 9.0,
        "art": 8.0,
        "music": 9.0,
        "sport": 9.0,
    },
    "Sarah": {
        "id": 2,
        "math": 10,
        "english": 7.5,
        "history": 6.5,
        "science": 5.6,
        "geography": 10,
        "politics": 6.3,
        "art": 8.0,
        "music": 10,
        "sport": 10,
    },
}


class BinarySearch:
    """Binary search implementation"""
    def __init__(self, data):
        self.data = data
        self.keys = list(data.keys())

    """Binary search"""
    def search(self, target):
        left, right = 0, len(self.keys) - 1
        while left <= right:
            middle = (left + right) // 2
            if self.keys[middle] == target:
                return self.data[target]
            elif self.keys[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return None

    """Search subject"""
    def search_subject(self, person, subject):
        return self.data.get(person, {}).get(subject)

def main():
    # Example usage
    search_result = BinarySearch(data).search_subject("Sarah", "english")
    console.print(search_result)

if __name__ == "__main__":
    main()
