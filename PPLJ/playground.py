if __name__ == "__main__":
    dicts = [
        { "name": "Tom", "age": 10 },
        { "name": "Mark", "age": 5 },
        { "name": "Pam", "age": 7 },
        { "name": "Dick", "age": 12 },
        { "name": "Pam", "age": 8 }
    ]

    print(next(item for item in dicts if item["name"] == "Pam"))
    print(next(item for item in dicts if item["name"] == "Pam"))