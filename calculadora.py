import flet as ft

def main(page: ft.Page):
    page.title = "Somador de Números"
    page.theme_mode = "DARK"
    page.window.width = 300
    page.window.height = 400

    # Função de soma
    def somar(e):
        try:
            n1 = float(num1.value)
            n2 = float(num2.value)
            resultado.value = f"Soma: {n1 + n2}"
        except ValueError:
            resultado.value = "Por favor, digite números válidos."
        page.update()

    #Espaçamento superior
    espaco = ft.Container(
        height= 50
    )

    # Campos de entrada
    num1 = ft.TextField(label="Número 1", width=200)
    num2 = ft.TextField(label="Número 2", width=200)

    # Texto para mostrar o resultado
    resultado = ft.Text(value="Digite os números e clique em Somar", size=16)

    # Botão
    btn_somar = ft.ElevatedButton("Somar", on_click=somar)

    # Adicionando os elementos na tela
    page.add(
        espaco,
        num1,
        num2,
        btn_somar,
        resultado
    )

ft.app(target=main)
