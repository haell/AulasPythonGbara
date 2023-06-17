try:
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero.")
except KeyboardInterrupt:
    print("O usuário interrompeu a execução.")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print('Muito obrigado, volte sempre!')
