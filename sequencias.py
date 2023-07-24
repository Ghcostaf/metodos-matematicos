import matplotlib.pyplot as plt

def a(n):
    return n / (n + 1)

def sequenciaconv(L, epsilon, N_epsilon, nmin, nmax):
    data_points = []
    for n in range(nmin, nmax + 1):
        an = a(n)
        data_points.append((n, an))
        if n >= N_epsilon:
            if abs(an - L) <= epsilon:
                break

    plt.plot(*zip(*data_points), 'bo-', label='an')
    plt.xlabel('n')
    plt.ylabel('a(n)')
    plt.title('Sequência numérica')
    plt.legend()

    plt.show()

def converdesconhecido(nmin, nmax):
    data_points = [(n, a(n)) for n in range(nmin, nmax + 1)]

    plt.plot(*zip(*data_points), 'bo-', label='an')
    plt.xlabel('n')
    plt.ylabel('a(n)')
    plt.title('Sequência numérica')
    plt.legend()

    plt.show()

    return data_points

def main():
    choice = input("Escolha (a) se a sequência é convergente ou (b) se é desconhecido: ")

    if choice == 'a':
        L = float(input("Digite o valor do limite L: "))
        epsilon = float(input("Digite o valor da tolerância epsilon: "))
        N_epsilon = int(input("Digite o índice N(epsilon): "))
        nmin = int(input("Digite o valor de nmin: "))
        nmax = int(input("Digite o valor de nmax: "))

        sequenciaconv(L, epsilon, N_epsilon, nmin, nmax)

        plt.axhline(L - epsilon, color='r', linestyle='--', label='L - epsilon')
        plt.axhline(L, color='g', linestyle='--', label='L')
        plt.axhline(L + epsilon, color='b', linestyle='--', label='L + epsilon')
        plt.legend()
        plt.show()

    elif choice == 'b':
        nmin = int(input("Digite o valor de nmin: "))
        nmax = int(input("Digite o valor de nmax: "))

        converdesconhecido(nmin, nmax)

    else:
        print("Opção inválida. Escolha (a) ou (b).")

if __name__ == "__main__":
    main()

