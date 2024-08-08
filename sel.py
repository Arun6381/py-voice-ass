from googlesearch import search


def google_search(query, num_results=1):
    try:
        search_results = list(search(query, num_results=num_results))
        return search_results
    except Exception as e:
        return str(e)


def main():
    print("Welcome to the Google Search AI!")
    while True:
        user_question = input("Ask me a question (type 'exit' to quit): ")

        if user_question.lower() == 'exit':
            print("Goodbye!")
            break

        search_results = google_search(user_question)

        if isinstance(search_results, list):
            if len(search_results) > 0:
                print("Top search result:")
                print(search_results[0])
            else:
                print("No search results found.")
        else:
            print("An error occurred:", search_results)


if __name__ == "__main__":
    main()

