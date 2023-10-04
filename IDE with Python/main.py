import subprocess
from tkinter import * # Permite criar interfaces gráficas
from tkinter.filedialog import asksaveasfilename, askopenfilename
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file(): # Abrir
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file: # Permite ler todo o conteúdo da página
        code = file.read() # Ler todo o conteúdo do arquivo selecionado
        editor.delete('1.0', END) # Deleta todo o conteúdo antigo do editor
        editor.insert('1.0', code) # Atualiza o editor para o arquivo selecionado
        set_file_path(path) # Pega o último path atualizado

def save_as(): # Salvar como & Salvar
    if file_path == '': # Salvar como
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else: # Salvar
        path = file_path
    with open(path, 'w') as file: # Permite abrir a pasta e escrever todo o texto presente no editor
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run(): # Função habilita quando executado o botão de "Run"
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Salve seu código')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

    code = editor.get('1.0', END) # Permite que o código pegue todas às funções presentes no código
    exec(code) # Permite que execute as funções que foram escritas no código

compiler = Tk() # Cria uma tela para fazer edições
compiler.title("Hello, IDE") # Oferece o nome da IDE

menu_bar = Menu(compiler) # Cria uma barra de menu que está integrada à variável "compiler"

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)


run_bar = Menu(menu_bar, tearoff=0) # Oferece a função de executar o código a partir de uma outra barra de menu, só que no interior da Super()
menu_bar.add_cascade(label='Run', menu=run_bar) # Habilita o efeito cascata, isto é, que desce a página a partir de um texto
run_bar.add_command(label='Run', command=run) # Adiciona o comando e texto na barra de Run

compiler.config(menu=menu_bar)

editor = Text() # Habilita a função de escrever
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
