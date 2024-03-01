import subprocess # Executa programas externos
import tkinter
from tkinter import * # Cria interfaces gráficas
from tkinter.filedialog import asksaveasfilename, askopenfilename # Realiza uma seleção de pastas e a função que deseja implementar nela
file_path = ''

def toggle_activated():
    f1 = Frame(compiler, width=300, height=height_editor, bg='black')
    f1.place(x=0, y=0)

    def delete():
        f1.destroy()

    Button(f1, text='close', command=delete).place(x=5, y=10)

def set_file_path(path):
    global file_path
    file_path = path

def open_file(): # Abrir pasta
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file: # Permite ler todo o conteúdo da página
        code = file.read() # Ler todo o conteúdo do arquivo selecionado
        editor.delete('1.0', END) # Deleta todo o conteúdo antigo do editor
        editor.insert('1.0', code) # Atualiza o editor para o arquivo selecionado
        set_file_path(path) # Pega o último path atualizado

def save_as(): # Salvar Como & Salvar
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file: # Permite abrir a pasta e escrever todo o texto presente no editor
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run(): # Botão "Executar"
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

compiler = Tk() # Cria uma janela
compiler.title("Own IDE") # Nome da IDE

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

editor = Text(height=20) # Habilita um local para escrever
editor.pack() # Adiciona o "widget" na página
height_editor = editor.cget('height') + 305

Button(compiler, command=toggle_activated, text='open').place(x=5, y=10)

text_output = Label(text="Output")
text_output.pack()
code_output = Text(height=10) # Output
code_output.pack()

compiler.mainloop()