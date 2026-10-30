from linked_queue import LinkedQueue


def main():
    jobs = LinkedQueue()
    while True:
        print("\nPRINT QUEUE")
        print("1. Add print job")
        print("2. Print next job")
        print("3. Show waiting jobs")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            job_id = input("Job ID: ").strip()
            try:
                pages = int(input("Number of pages: "))
                if pages <= 0:
                    print("Pages must be greater than zero.")
                    continue
            except ValueError:
                print("Enter a whole number for pages.")
                continue
            jobs.enqueue({"id": job_id, "pages": pages})
            print("Job added.")
        elif choice == "2":
            try:
                job = jobs.dequeue()
                print(f"Printing job {job['id']} ({job['pages']} page(s)).")
            except IndexError as error:
                print("Error:", error)
        elif choice == "3":
            print("Waiting jobs:", jobs)
        elif choice == "0":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
