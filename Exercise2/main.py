import file_operations as op
import functions as fun


def main():
    menu = True
    while menu:
        print("1. Load from file")
        print("2. Enter the number of systems")
        print("3. Exit")
        choice = input()
        if choice == "1":
            print("Enter example (*.txt): ")
            example = input()
            print("Choose stopping criterion")
            print("1. Number of iterations")
            print("2. Accuracy")
            choice2 = input()

            if choice2 == "1":
                matrix, b = op.load_matrix(example)
                print("Enter the maximum number of iterations:")
                max_iter = int(input())
                result = fun.gauss_seidel(matrix, b, None, max_iter, None)
                print(result)
            elif choice2 == "2":
                matrix, b = op.load_matrix(example)
                print("Enter accuracy: ")
                epsilon = float(input())
                result = fun.gauss_seidel(matrix, b, None, None, epsilon)
                print(result)
            else:
                print("Invalid choice.")
        elif choice == "2":
            print("Enter how many systems you want to solve:")
            num_systems = int(input())
            if 0 < num_systems <= 10:
                print("Choose stopping criterion")
                print("1. Number of iterations")
                print("2. Accuracy")
                choice2 = input()

                if choice2 == "1":
                    print("Enter the maximum number of iterations:")
                    max_iter = int(input())
                    selected_equations = []
                    results = []
                    for i in range(num_systems):
                        print(f"Enter the name of file {i + 1}:")
                        file_name = input()
                        selected_equations.append(file_name)

                    for i in range(len(selected_equations)):
                        example = selected_equations[i]
                        matrix, b = op.load_matrix(example)
                        print(f"File {i + 1}:")
                        result = fun.gauss_seidel(matrix, b, None, max_iter, None)
                        results.append(result)
                    print(results)
                elif choice2 == "2":
                    print("Enter accuracy:")
                    epsilon = float(input())
                    selected_equations = []
                    results = []
                    for i in range(num_systems):
                        print(f"Enter the name of file {i + 1}:")
                        file_name = input()
                        selected_equations.append(file_name)
                    for i in range(len(selected_equations)):
                        example = selected_equations[i]
                        matrix, b = op.load_matrix(example)
                        print(f"File {i + 1}:")
                        result = fun.gauss_seidel(matrix, b, None, None, epsilon)
                        results.append(result)
                    print(results)
                else:
                    print("Invalid choice.")
            else:
                print("Invalid number of systems provided.")
        else:
            menu = False


if __name__ == "__main__":
    main()
