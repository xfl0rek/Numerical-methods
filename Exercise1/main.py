import bisection
import secant
import draw_function
from decimal import Decimal as d


def stopping_criterion():
    print("\nChoose stopping criterion:")
    print("1. |xi - xi-1| < ε")
    print("2. |f(xi)| < ε")
    print("3. Execute a specific number of iterations")

    criterion_choice = input()

    if criterion_choice == "1":
        epsilon = float(input("Enter epsilon: "))
        max_iter = 1000
        return criterion_choice, epsilon, max_iter
    elif criterion_choice == "2":
        epsilon = float(input("Enter epsilon: "))
        max_iter = 1000
        return criterion_choice, epsilon, max_iter
    elif criterion_choice == "3":
        max_iter = int(input("Enter the maximum number of iterations: "))
        epsilon = d(0)
        return criterion_choice, epsilon, max_iter


def main():
    menu = True
    while menu:
        print("1. Polynomial (x^2 + 4x - 5)")
        print("2. Trigonometric Function (2sin(4x))")
        print("3. Exponential (2^x - 2)")
        print("4. Composition of Functions (2^(x ^ 2 + 2x + 1) - 2)")
        print("5. Exit\n")

        choice = input("Choose a function: ")

        if choice == "1":
            print("Enter the left endpoint of the interval:")
            a = float(input())
            print("Enter the right endpoint of the interval:")
            b = float(input())
            criterion_choice, epsilon, max_iter = stopping_criterion()
            result = bisection.bisection(a, b, choice, epsilon, max_iter, criterion_choice)
            result2 = secant.secant(a, b, choice, epsilon, max_iter, criterion_choice)
            if result is not None and result2 is not None:
                draw_function.draw_function(choice, a, b, result, result2)
        if choice == "2":
            print("Enter the left endpoint of the interval:")
            a = float(input())
            print("Enter the right endpoint of the interval:")
            b = float(input())
            criterion_choice, epsilon, max_iter = stopping_criterion()
            result = bisection.bisection(a, b, choice, epsilon, max_iter, criterion_choice)
            result2 = secant.secant(a, b, choice, epsilon, max_iter, criterion_choice)
            if result is not None and result2 is not None:
                draw_function.draw_function(choice, a, b, result, result2)
        if choice == "3":
            print("Enter the left endpoint of the interval:")
            a = float(input())
            print("Enter the right endpoint of the interval:")
            b = float(input())
            criterion_choice, epsilon, max_iter = stopping_criterion()
            result = bisection.bisection(a, b, choice, epsilon, max_iter, criterion_choice)
            result2 = secant.secant(a, b, choice, epsilon, max_iter, criterion_choice)
            if result is not None and result2 is not None:
                draw_function.draw_function(choice, a, b, result, result2)
        if choice == "4":
            print("Enter the left endpoint of the interval:")
            a = float(input())
            print("Enter the right endpoint of the interval:")
            b = float(input())
            criterion_choice, epsilon, max_iter = stopping_criterion()
            result = bisection.bisection(a, b, choice, epsilon, max_iter, criterion_choice)
            result2 = secant.secant(a, b, choice, epsilon, max_iter, criterion_choice)
            if result is not None and result2 is not None:
                draw_function.draw_function(choice, a, b, result, result2)
        if choice == "5":
            menu = False


if __name__ == "__main__":
    main()
