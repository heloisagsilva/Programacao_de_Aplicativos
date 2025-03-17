import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas
import tkinter as tk  # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import ttk  # Importa o módulo ttk do tkinter para usar widgets com estilo
from tkinter import *  # Importa todos os componentes do tkinter
from tkinter.ttk import *  # Importa os componentes do tkinter com estilo (para o uso de combobox e outros widgets estilizados)
from PIL import Image, ImageTk
import tkinter.messagebox as MessageBox
import tkinter.filedialog as filedialog
import os
import shutil
import sys
sys.setrecursionlimit(3000)  # Aumenta o limite para 3000

# Adicione este código no início do programa, após as importações
if not os.path.exists("imagens"):
    os.makedirs("imagens")
    
# Criar uma imagem padrão se não existir
default_path = "imagens/default_product.png"
if not os.path.exists(default_path):
    try:
        # Crie uma imagem colorida simples como padrão
        img = Image.new('RGB', (150, 150), color='#F0D8E8')
        img.save(default_path)
    except Exception as e:
        print(f"Erro ao criar imagem padrão: {e}") 

# Criando a janela principal do aplicativo
janela = tk.Tk()  
janela.title("FLORICULTURA MÃO NA TERRA")  
janela.geometry("1100x600")

# Criando o Canvas e definindo a altura e a largura para o canvas ocupar toda a tela
canvas = tk.Canvas(janela, bg="#F0D8E8")
canvas.pack(side="left", fill="both", expand=True)

# Adicionar a scrollbar personalizada
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=canvas.yview, style="TScrollbar")  # Usando o estilo personalizado
scrollbar.pack(side="right", fill="y")

# Configurar a scrollbar
canvas.config(yscrollcommand=scrollbar.set)

# Criando o frame dentro do canvas
content_frame = tk.Frame(canvas)  
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Cabeçalho (Header)
header = tk.Frame(content_frame, bg="#c1ed74", height=50) 
header.pack(fill="x") 

# Verifica se a imagem da logo existe dentro da pasta 'img'
logo_path = "imagens/logo.PNG"
if os.path.exists(logo_path):  
    img = Image.open(logo_path).resize((120, 120)) 
    logo = ImageTk.PhotoImage(img)  
    logo_label = tk.Label(header, image=logo, bg="#c1ed74") 
    logo_label.image = logo 
    logo_label.pack(side="left", padx=10) 

# Texto do cabeçalho ao lado da logo
tk.Label(header, text="🏵️     Bem-Vindo á Floricultura Mão na Terra          🏵️", fg='#7e0054', bg='#c1ed74', font=("Segoe UI Black", 35, "bold")).pack(side="left", padx=5, pady=10) 

# Barra de Navegação
nav_bar = tk.Frame(content_frame, bg="#c1ed74")  
nav_bar.pack(fill="x") 

# Barra de navegação com "Contato", "Sobre Nós" e "Admin"
btn_frame = tk.Frame(nav_bar, bg="#c1ed74")  
btn_frame.pack(side="right")  # Colocando os botões à direita

# Listando os botões
navigation = ["Contato", "Sobre Nós", "Admin"]  

for item in navigation: 
    btn = tk.Button(btn_frame, text=item, bg="#c1ed74", fg="black", font=("Arial", 10), relief="flat") 
    btn.pack(side="left", padx=10, pady=5) 

# Função para exibir a mensagem sobre a loja
def show_about():
    MessageBox.showinfo("Sobre Nós:", "Na Mão na Terra, somos apaixonados por jardinagem e tudo que envolve o cultivo e cuidado com as plantas. Nossa missão é oferecer os melhores produtos para ajudar você a transformar seu jardim, quintal ou espaço verde.\n\nTrabalhamos com uma seleção cuidadosa de produtos para garantir qualidade e eficiência no cuidado com suas plantas. Seja você um jardineiro experiente ou alguém que está começando agora, temos tudo o que precisa!")

# Função para exibir a mensagem de contato
def show_contact():
    MessageBox.showinfo("Contato:", "Se tiver alguma dúvida, ligue ou mande mensagem para este número: +55 (47) 94002-8922")

# Função para abrir a janela de login do admin
def show_admin_login():
    login_window = tk.Toplevel(janela)
    login_window.title("Login de Administrador")
    login_window.geometry("300x250")

    tk.Label(login_window, text="Nome do Usuário:", font=("Arial", 12)).pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Arial", 12))
    username_entry.pack(pady=10)

    tk.Label(login_window, text="Senha do Usuário:", font=("Arial", 12)).pack(pady=10)
    password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
    password_entry.pack(pady=10)

    def login():
        if username_entry.get() == "admin" and password_entry.get() == "admin":
            login_window.destroy()
            open_admin_panel()
        else:
            MessageBox.showerror("Erro", "Usuário ou senha inválidos!")

    login_button = tk.Button(login_window, text="Entrar", bg="green", fg="white", font=("Arial", 12), command=login)
    login_button.pack(pady=10)

def search_product():
    search_term = search_entry.get().lower()
    results = [p for p in products if search_term in p["name"].lower()]
    
    # Limpar os resultados anteriores (se houver)
    for widget in product_frame.winfo_children():
        widget.destroy()
    
    # Mostrar os resultados encontrados
    for product in results:
        frame = tk.Frame(product_frame, relief="groove", borderwidth=4, padx=10, pady=10)
        frame.pack(side="left", padx=10, pady=10)
        
        img = load_image(product["image"], (150, 150))
        if img:
            label_img = tk.Label(frame, image=img)
            label_img.image = img
            label_img.pack()

        tk.Label(frame, text=product["name"], font=("Arial", 10, "bold")).pack()
        tk.Label(frame, text=product["price"], font=("Arial", 10)).pack()
        
        add_to_cart_button = tk.Button(frame, text="Adicionar ao Carrinho", bg="green", fg="white", font=("Arial", 8))
        add_to_cart_button.pack(pady=5)

# Barra de pesquisa no topo
search_frame = tk.Frame(content_frame, bg="#F5F5F5")
search_frame.pack(fill="x", padx=20, pady=10)

search_label = tk.Label(search_frame, text="🔍 Pesquisar Produto:", font=("Arial", 14), bg="#F5F5F5")
search_label.pack(side="left", padx=10)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=40)
search_entry.pack(side="left", padx=10)

search_button = tk.Button(search_frame, text="Pesquisar", bg="#c1ed74", fg="black", font=("Arial", 12, 'bold'), relief="solid", bd=2, command=search_product)
search_button.pack(side="left", padx=10)




# Função para abrir o painel do administrador melhorado
def open_admin_panel():
    admin_panel = tk.Toplevel(janela)
    admin_panel.title("Painel de Administração")
    admin_panel.geometry("800x600")
    admin_panel.configure(bg="#F0D8E8")

    # Cabeçalho do painel de administração
    admin_header = tk.Frame(admin_panel, bg="#c1ed74", height=50)
    admin_header.pack(fill="x", pady=10)
    
    tk.Label(admin_header, text="Painel de Administração - MÃO NA TERRA", 
             fg='#7e0054', bg='#c1ed74', font=("Segoe UI Black", 24, "bold")).pack(pady=10)

    # Notebook para abas (adicionar produto, gerenciar estoque, etc.)
    notebook = ttk.Notebook(admin_panel)
    notebook.pack(fill="both", expand=True, padx=20, pady=20)

    # Aba para adicionar produto
    add_product_tab = tk.Frame(notebook, bg="#F0D8E8")
    notebook.add(add_product_tab, text="Adicionar Produto")

    # Aba para gerenciar estoque
    manage_stock_tab = tk.Frame(notebook, bg="#F0D8E8")
    notebook.add(manage_stock_tab, text="Gerenciar Estoque")

    # Frame para adicionar produto
    tk.Label(add_product_tab, text="Adicionar Novo Produto", font=("Arial", 16, "bold"), bg="#F0D8E8").pack(pady=10)

    form_frame = tk.Frame(add_product_tab, bg="#F0D8E8")
    form_frame.pack(pady=10)

    # Campos do formulário
    tk.Label(form_frame, text="Nome do Produto:", font=("Arial", 12), bg="#F0D8E8").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    product_name_entry = tk.Entry(form_frame, font=("Arial", 12), width=40)
    product_name_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Preço (R$):", font=("Arial", 12), bg="#F0D8E8").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    price_entry = tk.Entry(form_frame, font=("Arial", 12), width=40)
    price_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Quantidade em Estoque:", font=("Arial", 12), bg="#F0D8E8").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    stock_entry = tk.Entry(form_frame, font=("Arial", 12), width=40)
    stock_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(form_frame, text="Categoria:", font=("Arial", 12), bg="#F0D8E8").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    category_combobox = ttk.Combobox(form_frame, font=("Arial", 12), width=38, 
                                      values=["Sementes", "Ferramentas", "Vasos", "Insumos", "Decoração", "Outros"])
    category_combobox.grid(row=3, column=1, padx=10, pady=5)
    category_combobox.current(0)

    tk.Label(form_frame, text="Descrição:", font=("Arial", 12), bg="#F0D8E8").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    description_text = tk.Text(form_frame, font=("Arial", 12), width=40, height=5)
    description_text.grid(row=4, column=1, padx=10, pady=5)

    # Frame para imagem
    image_frame = tk.Frame(form_frame, bg="#F0D8E8")
    image_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    image_path_var = tk.StringVar()
    image_preview_label = tk.Label(image_frame, text="Pré-visualização da Imagem", bg="#F0D8E8", width=20, height=10, relief="solid")
    image_preview_label.pack(side="left", padx=10)

    def select_image():
        file_path = filedialog.askopenfilename(
            title="Selecionar Imagem", 
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if file_path:
            image_path_var.set(file_path)
            # Exibir pré-visualização
            try:
                img = Image.open(file_path)
                img = img.resize((150, 150), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                image_preview_label.config(image=photo)
                image_preview_label.image = photo
            except Exception as e:
                MessageBox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")

    image_button = tk.Button(image_frame, text="Selecionar Imagem", bg="#c1ed74", fg="black", 
                             font=("Arial", 12), command=select_image)
    image_button.pack(side="right", padx=10)

    def add_product():
        # Validar os campos
        if not product_name_entry.get() or not price_entry.get() or not stock_entry.get():
            MessageBox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return
        
        # Validar preço e estoque (devem ser números)
        try:
            price = float(price_entry.get().replace(',', '.'))
            stock = int(stock_entry.get())
        except ValueError:
            MessageBox.showerror("Erro", "Preço e estoque devem ser valores numéricos!")
            return
        
        # Verificar se uma imagem foi selecionada
        if not image_path_var.get():
            MessageBox.showerror("Erro", "Selecione uma imagem para o produto!")
            return
        
        # Copiar a imagem para a pasta "imagens"
        try:
            if not os.path.exists("imagens"):
                os.makedirs("imagens")
            
            # Gerar nome de arquivo baseado no nome do produto
            product_name_normalized = product_name_entry.get().lower().replace(' ', '_')
            file_extension = os.path.splitext(image_path_var.get())[1]
            new_image_name = f"{product_name_normalized}{file_extension}"
            new_image_path = os.path.join("imagens", new_image_name)
            
            # Copiar o arquivo
            shutil.copy2(image_path_var.get(), new_image_path)
            
            # Adicionar o produto à lista
            new_product = {
                "name": product_name_entry.get(),
                "price": f"R$ {price:.2f}".replace('.', ','),
                "image": new_image_path,
                "stock": stock,
                "category": category_combobox.get(),
                "description": description_text.get("1.0", tk.END).strip()
            }
            
            products.append(new_product)
            
            # Limpar os campos após adicionar
            product_name_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            stock_entry.delete(0, tk.END)
            description_text.delete("1.0", tk.END)
            image_path_var.set("")
            image_preview_label.config(image=None)
            
            MessageBox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            
            # Atualizar a exibição dos produtos
            refresh_product_display()
            
        except Exception as e:
            MessageBox.showerror("Erro", f"Não foi possível salvar o produto: {e}")

    # Botão para adicionar produto
    add_button = tk.Button(add_product_tab, text="Adicionar Produto", bg="green", fg="white", 
                           font=("Arial", 14, "bold"), command=add_product)
    add_button.pack(pady=20)

    # Configuração da aba de gerenciamento de estoque
    tk.Label(manage_stock_tab, text="Gerenciar Estoque de Produtos", font=("Arial", 16, "bold"), bg="#F0D8E8").pack(pady=10)
    
    # Frame para pesquisar produtos
    search_stock_frame = tk.Frame(manage_stock_tab, bg="#F0D8E8")
    search_stock_frame.pack(fill="x", pady=10)
    
    tk.Label(search_stock_frame, text="Pesquisar Produto:", font=("Arial", 12), bg="#F0D8E8").pack(side="left", padx=10)
    search_stock_entry = tk.Entry(search_stock_frame, font=("Arial", 12), width=30)
    search_stock_entry.pack(side="left", padx=5)
    
    # Tabela para exibir produtos
    stock_table_frame = tk.Frame(manage_stock_tab, bg="white")
    stock_table_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Criando o Treeview para a tabela de estoque
    columns = ("ID", "Nome", "Preço", "Estoque", "Categoria")
    stock_table = ttk.Treeview(stock_table_frame, columns=columns, show="headings")
    
    # Definindo as colunas
    stock_table.heading("ID", text="ID")
    stock_table.heading("Nome", text="Nome do Produto")
    stock_table.heading("Preço", text="Preço")
    stock_table.heading("Estoque", text="Estoque")
    stock_table.heading("Categoria", text="Categoria")
    
    # Configurando larguras das colunas
    stock_table.column("ID", width=50)
    stock_table.column("Nome", width=200)
    stock_table.column("Preço", width=100)
    stock_table.column("Estoque", width=100)
    stock_table.column("Categoria", width=150)
    
    # Adicionando scrollbar à tabela
    stock_scrollbar = ttk.Scrollbar(stock_table_frame, orient="vertical", command=stock_table.yview)
    stock_table.configure(yscrollcommand=stock_scrollbar.set)
    
    stock_scrollbar.pack(side="right", fill="y")
    stock_table.pack(side="left", fill="both", expand=True)
    
    # Função para carregar produtos na tabela
    def load_products_to_table():
        # Limpar a tabela
        for item in stock_table.get_children():
            stock_table.delete(item)
        
        # Adicionar produtos à tabela
        for i, product in enumerate(products):
            stock = product.get("stock", "N/A")
            category = product.get("category", "N/A")
            stock_table.insert("", "end", values=(i+1, product["name"], product["price"], stock, category))
    
    # Função para pesquisar produtos na tabela
    def search_stock():
        search_term = search_stock_entry.get().lower()
        
        # Limpar a tabela
        for item in stock_table.get_children():
            stock_table.delete(item)
        
        # Filtrar e adicionar produtos correspondentes
        for i, product in enumerate(products):
            if search_term in product["name"].lower():
                stock = product.get("stock", "N/A")
                category = product.get("category", "N/A")
                stock_table.insert("", "end", values=(i+1, product["name"], product["price"], stock, category))
    
    # Botão para pesquisar
    search_stock_button = tk.Button(search_stock_frame, text="Pesquisar", bg="#c1ed74", fg="black", 
                                    font=("Arial", 10, "bold"), command=search_stock)
    search_stock_button.pack(side="left", padx=10)
    
    # Frame para atualizar estoque
    update_stock_frame = tk.Frame(manage_stock_tab, bg="#F0D8E8")
    update_stock_frame.pack(fill="x", pady=10)
    
    tk.Label(update_stock_frame, text="Atualizar Estoque do Produto Selecionado:", font=("Arial", 12), bg="#F0D8E8").grid(row=0, column=0, columnspan=2, pady=5)
    
    tk.Label(update_stock_frame, text="Nova Quantidade:", font=("Arial", 12), bg="#F0D8E8").grid(row=1, column=0, padx=10, pady=5)
    new_stock_entry = tk.Entry(update_stock_frame, font=("Arial", 12), width=10)
    new_stock_entry.grid(row=1, column=1, padx=10, pady=5)
    
    def update_stock():
        selected = stock_table.selection()
        if not selected:
            MessageBox.showerror("Erro", "Selecione um produto para atualizar o estoque!")
            return
        
        try:
            new_stock = int(new_stock_entry.get())
            if new_stock < 0:
                raise ValueError("O estoque não pode ser negativo")
                
            # Obter o ID do item selecionado
            item_id = stock_table.item(selected[0])['values'][0]
            
            # Atualizar o estoque no dicionário do produto
            products[item_id-1]["stock"] = new_stock
            
            # Atualizar a tabela
            stock_table.item(selected[0], values=(item_id, products[item_id-1]["name"], 
                                                products[item_id-1]["price"], new_stock, 
                                                products[item_id-1].get("category", "N/A")))
            
            MessageBox.showinfo("Sucesso", "Estoque atualizado com sucesso!")
            new_stock_entry.delete(0, tk.END)
            
        except ValueError as e:
            MessageBox.showerror("Erro", f"Valor inválido para estoque: {e}")
    
    # Botão para atualizar estoque
    update_stock_button = tk.Button(update_stock_frame, text="Atualizar Estoque", bg="blue", fg="white", 
                                   font=("Arial", 12), command=update_stock)
    update_stock_button.grid(row=1, column=2, padx=10, pady=5)
    
    # Carregar produtos na tabela
    load_products_to_table()
    
    # Botão para voltar à página inicial
    back_button = tk.Button(admin_panel, text="Voltar à Página Inicial", bg="#c1ed74", fg="black", 
                           font=("Arial", 14), command=admin_panel.destroy)
    back_button.pack(pady=15)

# Função para atualizar a exibição dos produtos na tela principal
def refresh_product_display():
    # Limpar a exibição atual
    for widget in product_frame.winfo_children():
        widget.destroy()
    
    # Reexibir produtos
    cols = 6  
    rows = (len(products) + cols - 1) // cols

    for i, product in enumerate(products):
        frame = tk.Frame(product_frame, relief="groove", borderwidth=4, padx=10, pady=10)
        row = i // cols  
        col = i % cols 
        frame.grid(row=row, column=col, padx=10, pady=10)  

        # Usar uma abordagem simplificada para imagens
        img = None
        try:
            path = product["image"]
            if path.startswith("img/"):
                path = "imagens/" + path.split("/")[1]
                
            if os.path.exists(path):
                pil_img = Image.open(path).resize((150, 150), Image.LANCZOS)
                img = ImageTk.PhotoImage(pil_img)
        except Exception as e:
            print(f"Erro ao carregar imagem {product['image']}: {e}")
            
        if img:
            label_img = tk.Label(frame, image=img)
            label_img.image = img
            label_img.pack()
        else:
            # Usar um label simples caso a imagem não seja carregada
            placeholder = tk.Label(frame, text="Imagem não\ndisponível", width=20, height=8, 
                                 bg="#F0D8E8", relief="solid")
            placeholder.pack()

        # Resto do código para exibir informações do produto...
        tk.Label(frame, text=product["name"], font=("Arial", 10, "bold")).pack() 
        price_label = tk.Label(frame, text=product["price"], font=("Arial", 10))
        price_label.pack()
        
        # Verificar disponibilidade de estoque
        if "stock" in product:
            stock_text = f"Em estoque: {product['stock']} unid." if product["stock"] > 0 else "Fora de estoque"
            stock_color = "green" if product["stock"] > 0 else "red"
            tk.Label(frame, text=stock_text, font=("Arial", 8), fg=stock_color).pack()

        # Botão de adicionar ao carrinho
        add_to_cart_button = tk.Button(frame, text="Adicionar ao Carrinho", bg="green", fg="white", 
                                     font=("Arial", 8), command=lambda p=product: add_to_cart(p))
        add_to_cart_button.pack(pady=5) 

# Alterando os botões para chamar as funções corretas
btn_contato = btn_frame.winfo_children()[0]  # O botão "Contato" é o primeiro na lista
btn_contato.config(command=show_contact)

btn_sobre_nos = btn_frame.winfo_children()[1]  # O botão "Sobre Nós" é o segundo
btn_sobre_nos.config(command=show_about)

btn_admin = btn_frame.winfo_children()[2]  # O botão "Admin" é o terceiro
btn_admin.config(command=show_admin_login)

# Área de Produtos
product_frame = tk.Frame(content_frame)
product_frame.pack(fill="both", expand=True)  

# Função para carregar e redimensionar imagens - melhorada para tratar erros
# Função melhorada para carregar e redimensionar imagens
def load_image(path, size):
    try:
        # Converter caminhos img/ para imagens/
        if path.startswith("img/"):
            path = "imagens/" + path.split("/")[1]
            
        if os.path.exists(path):
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        else:
            # Use uma imagem padrão simples sem chamar load_image novamente
            default_path = "imagens/default_product.png"
            if os.path.exists(default_path):
                img = Image.open(default_path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            else:
                # Criar uma imagem em branco diretamente
                img = Image.new('RGB', size, color='#F0D8E8')
                return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Erro ao carregar imagem {path}: {e}")
        # Criar uma imagem em branco sem recursão
        img = Image.new('RGB', size, color='#F0D8E8')
        return ImageTk.PhotoImage(img)
# Lista de produtos com preços e informações de estoque
products = [
    {"name": "Saco de Terra", "price": "R$ 30,99", "image": "img/terra.jpg", "stock": 25, "category": "Insumos"},
    {"name": "Saco de Esterco", "price": "R$ 32,99", "image": "img/esterco.png", "stock": 15, "category": "Insumos"},
    {"name": "Vaso", "price": "R$ 15,99", "image": "img/vaso.png", "stock": 40, "category": "Vasos"},
    {"name": "Bandejas de Cultivo", "price": "R$ 12,99", "image": "img/bandeja.png", "stock": 30, "category": "Ferramentas"},
    {"name": "Regador", "price": "R$ 29,99", "image": "img/regador.png", "stock": 18, "category": "Ferramentas"},
    {"name": "Mangueira", "price": "R$ 59,99", "image": "img/mangueira.png", "stock": 10, "category": "Ferramentas"},
    {"name": "Inseticidas", "price": "R$ 20,80", "image": "img/inceticida.png", "stock": 22, "category": "Insumos"},
    {"name": "Pulverizador", "price": "R$ 49,99", "image": "img/pulverizador.png", "stock": 12, "category": "Ferramentas"},
    {"name": "Enxadinha", "price": "R$ 49,99", "image": "img/enxadinha.png", "stock": 8, "category": "Ferramentas"},
    {"name": "Pá de Mão", "price": "R$ 42,99", "image": "img/pa.png", "stock": 15, "category": "Ferramentas"},
    {"name": "Tesoura de Poda", "price": "R$ 23,99", "image": "img/tesoura_poda.png", "stock": 20, "category": "Ferramentas"},
    {"name": "Tesoura de Colheita", "price": "R$ 24,99", "image": "img/tesoura.png", "stock": 18, "category": "Ferramentas"},
    {"name": "Serrote de Poda", "price": "R$ 129,99", "image": "img/serrote.png", "stock": 5, "category": "Ferramentas"},
    {"name": "Faca de Enxertia", "price": "R$ 18,99", "image": "img/canivete.png", "stock": 7, "category": "Ferramentas"},
    {"name": "Garfo de Mão", "price": "R$ 8,99", "image": "img/garfo.png", "stock": 25, "category": "Ferramentas"},
    {"name": "Luvas de Jardinagem", "price": "R$ 18,99", "image": "img/luva.png", "stock": 30, "category": "Ferramentas"},
    {"name": "Avental impermeável", "price": "R$ 18,99", "image": "img/avental.png", "stock": 14, "category": "Ferramentas"},
    {"name": "Estacas e tutores", "price": "R$ 57,99", "image": "img/estacas.png", "stock": 3, "category": "Ferramentas"},
    {"name": "Sementes de Tulipa", "price": "R$ 2,90", "image": "img/vaso.png", "stock": 15, "category": "Ferramentas"},
    {"name": "Sementes de Lírio", "price": "R$ 2,90", "image": "img/vaso.png", "stock": 10, "category": "Ferramentas"},
    {"name": "Sementes de Dente de Leão", "price": "R$ 2,90", "image": "img/vaso.png", "stock": 7, "category": "Ferramentas"},
    {"name": "Sementes de Violeta", "price": "R$ 2,90", "image": "img/vaso.png","stock": 78, "category": "Ferramentas"},
    {"name": "Sementes de Orquídea", "price": "R$ 2,90", "image": "img/vaso.png","stock": 21, "category": "Ferramentas"},
    {"name": "Sementes de Jasmin", "price": "R$ 2,90", "image": "img/vaso.png","stock": 61, "category": "Ferramentas"},
    {"name": "Sementes de Margarida", "price": "R$ 2,90", "image": "img/vaso.png","stock": 39, "category": "Ferramentas"},
    {"name": "Sementes de Camélia", "price": "R$ 2,90", "image": "img/vaso.png","stock": 27, "category": "Ferramentas"},
    {"name": "Sementes de Cravo", "price": "R$ 2,90", "image": "img/vaso.png","stock": 45, "category": "Ferramentas"},
    {"name": "Sementes de Azaléia", "price": "R$ 2,90", "image": "img/vaso.png","stock": 11, "category": "Ferramentas"},
    {"name": "Sementes de Hibisco", "price": "R$ 10,40", "image": "img/vaso.png","stock": 25, "category": "Ferramentas"},
    {"name": "Sementes de Pitaya", "price": "R$ 10,40", "image": "img/vaso.png", "stock": 2, "category": "Ferramentas"},                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
]

# Organizando os produtos em um grid
cols = 6  
rows = (len(products) + cols - 1) // cols

for i, product in enumerate(products):
    frame = tk.Frame(product_frame, relief="groove", borderwidth=4, padx=10, pady=10, highlightbackground="black", highlightthickness=2)  # Definindo borda preta
    row = i // cols  
    col = i % cols 
    frame.grid(row=row, column=col, padx=10, pady=10)  

    # Carregar imagem do produto
    img = load_image(product["image"], (150, 150))  # Carrega a imagem com o tamanho desejado
    if img:  # Só exibe a imagem se ela foi carregada corretamente
        label_img = tk.Label(frame, image=img)
        label_img.image = img  # Mantém uma referência para a imagem
        label_img.pack()  
    else:
        tk.Label(frame, text="Imagem não encontrada", font=("Arial", 10, "italic"), fg="red").pack()  

    # Exibe as informações do produto: nome, preço e desconto
    tk.Label(frame, text=product["name"], font=("Arial", 10, "bold")).pack() 
    
    # Preço antigo riscado
    price_label = tk.Label(frame, text=product["price"], font=("Arial", 10))
    price_label.pack()

    # Botão de adicionar ao carrinho
    add_to_cart_button = tk.Button(frame, text="Adicionar ao Carrinho", bg="green", fg="white", font=("Arial", 8), command=lambda product=product: add_to_cart(product))
    add_to_cart_button.pack(pady=5)  


# Carrinho de compras (Listbox) com melhorias
carrinho_frame = tk.Frame(content_frame, bg="white", bd=2, relief="sunken", padx=20, pady=20)
carrinho_frame.pack(side="bottom", fill="x", padx=10, pady=10)  # Carrinho na parte de baixo

tk.Label(carrinho_frame, text="Carrinho de Compras:", font=("Arial", 12, "bold")).pack(pady=10)


# Frame para mostrar os itens do carrinho
cart_list_frame = tk.Frame(carrinho_frame)
cart_list_frame.pack(fill="both", padx=10, pady=10)

# Lista para os itens
lista_carrinho = tk.Listbox(cart_list_frame, width=50, height=10, selectmode=tk.SINGLE)
lista_carrinho.pack(side="left", fill="y")

# Scrollbar
cart_scrollbar = tk.Scrollbar(cart_list_frame, orient="vertical", command=lista_carrinho.yview)
cart_scrollbar.pack(side="right", fill="y")
lista_carrinho.config(yscrollcommand=cart_scrollbar.set)

# Função para adicionar item ao carrinho
def add_to_cart(product):
    lista_carrinho.insert(tk.END, f"{product['name']} - {product['price']}")
    update_total()

# Área do total do carrinho
total_frame = tk.Frame(carrinho_frame)
total_frame.pack(fill="x", padx=10, pady=10)

# Exibindo o total
total_label = tk.Label(total_frame, text="Total: R$ 0,00", font=("Arial", 12, "bold"))
total_label.pack(side="left")

def remove_from_cart():
    selected = lista_carrinho.curselection()
    if selected:
        lista_carrinho.delete(selected)
        update_total()
    else:
        MessageBox.showinfo("Aviso", "Selecione um item para remover")

# Botão para remover item do carrinho
remove_button = tk.Button(cart_list_frame, text="Remover Item", bg="red", fg="white", 
                          font=("Arial", 10), command=remove_from_cart)
remove_button.pack(side="bottom", pady=5)

# Função para atualizar o total
def update_total():
    total = 0
    for item in lista_carrinho.get(0, tk.END):
        price = item.split('-')[-1].strip()
        price = price.replace('R$', '').replace(',', '.').strip()
        total += float(price)
    
    total_label.config(text=f"Total: R$ {total:.2f}")

# Função para finalizar a compra
# Função para finalizar a compra com opções de pagamento
def finalizar_compra():
    if lista_carrinho.size() == 0:
        MessageBox.showinfo("Aviso", "Seu carrinho está vazio!")
        return
    
    # Criar janela de pagamento
    pagamento_window = tk.Toplevel(janela)
    pagamento_window.title("Opções de Pagamento")
    pagamento_window.geometry("400x400")
    pagamento_window.configure(bg="#F0D8E8")
    
    # Título
    tk.Label(pagamento_window, text="Escolha a forma de pagamento", 
             font=("Arial", 14, "bold"), bg="#F0D8E8").pack(pady=15)
    
    # Calcular total
    total = 0
    for item in lista_carrinho.get(0, tk.END):
        price = item.split('-')[-1].strip()
        price = price.replace('R$', '').replace(',', '.').strip()
        total += float(price)
    
    # Mostrar total
    tk.Label(pagamento_window, text=f"Total da compra: R$ {total:.2f}", 
             font=("Arial", 12), bg="#F0D8E8").pack(pady=10)
    
    # Frame para as opções de pagamento
    payment_frame = tk.Frame(pagamento_window, bg="#F0D8E8")
    payment_frame.pack(pady=10)
    
    # Variável para armazenar a opção de pagamento selecionada
    payment_option = tk.StringVar()
    payment_option.set("credito")  # Padrão: cartão de crédito
    
    # Opções de pagamento
    tk.Radiobutton(payment_frame, text="Cartão de Crédito", variable=payment_option, 
                  value="credito", bg="#F0D8E8", font=("Arial", 11),
                  command=lambda: show_parcelas_frame()).pack(anchor="w", pady=5)
    
    tk.Radiobutton(payment_frame, text="Cartão de Débito", variable=payment_option, 
                  value="debito", bg="#F0D8E8", font=("Arial", 11),
                  command=lambda: hide_parcelas_frame()).pack(anchor="w", pady=5)
    
    tk.Radiobutton(payment_frame, text="PIX", variable=payment_option, 
                  value="pix", bg="#F0D8E8", font=("Arial", 11),
                  command=lambda: hide_parcelas_frame()).pack(anchor="w", pady=5)
    
    # Frame para as parcelas (visível apenas quando cartão de crédito é selecionado)
    parcelas_frame = tk.Frame(pagamento_window, bg="#F0D8E8")
    parcelas_frame.pack(pady=10)
    
    tk.Label(parcelas_frame, text="Número de parcelas:", 
             font=("Arial", 11), bg="#F0D8E8").pack(side="left", padx=5)
    
    # Dropdown para escolher número de parcelas
    parcelas = ttk.Combobox(parcelas_frame, values=[f"{i}x" for i in range(1, 13)], width=5)
    parcelas.current(0)  # 1x como padrão
    parcelas.pack(side="left", padx=5)
    
    # Função para mostrar o frame de parcelas
    def show_parcelas_frame():
        parcelas_frame.pack(pady=10)
    
    # Função para esconder o frame de parcelas
    def hide_parcelas_frame():
        parcelas_frame.pack_forget()
    
    # Função para processar o pagamento
    def process_payment():
        payment_type = payment_option.get()
        
        if payment_type == "credito":
            num_parcelas = parcelas.get().replace("x", "")
            valor_parcela = total / int(num_parcelas)
            MessageBox.showinfo("Pagamento Realizado", 
                               f"Pagamento com Cartão de Crédito em {num_parcelas}x de R$ {valor_parcela:.2f} realizado com sucesso!")
        elif payment_type == "debito":
            MessageBox.showinfo("Pagamento Realizado", 
                               f"Pagamento com Cartão de Débito no valor de R$ {total:.2f} realizado com sucesso!")
        else:  # pix
            # Gerar um código PIX fictício
            pix_code = "12345678901234567890"
            
            pix_window = tk.Toplevel(pagamento_window)
            pix_window.title("Pagamento via PIX")
            pix_window.geometry("300x200")
            pix_window.configure(bg="#F0D8E8")
            
            tk.Label(pix_window, text="Código PIX gerado:", 
                    font=("Arial", 12), bg="#F0D8E8").pack(pady=10)
            
            pix_entry = tk.Entry(pix_window, font=("Arial", 10), width=25)
            pix_entry.insert(0, pix_code)
            pix_entry.config(state="readonly")
            pix_entry.pack(pady=10)
            
            tk.Label(pix_window, text="Use o código acima para pagar\nvia seu aplicativo bancário.", 
                    font=("Arial", 10), bg="#F0D8E8", justify="center").pack(pady=10)
            
            tk.Button(pix_window, text="Confirmar Pagamento", bg="green", fg="white", 
                     font=("Arial", 10), command=lambda: [pix_window.destroy(), 
                                                         MessageBox.showinfo("Pagamento Realizado", 
                                                                            "Pagamento via PIX realizado com sucesso!")]).pack(pady=10)
            
            return
        
        tk.Label(cart_list_frame, text="Clique em um item para selecioná-lo e removê-lo:", 
         font=("Arial", 10)).pack(anchor="w")
        
        # Limpar o carrinho e fechar a janela de pagamento
        lista_carrinho.delete(0, tk.END)
        update_total()
        pagamento_window.destroy()
    
    # Botão para confirmar pagamento
    confirm_button = tk.Button(pagamento_window, text="Confirmar Pagamento", bg="green", fg="white", 
                              font=("Arial", 12, "bold"), command=process_payment)
    confirm_button.pack(pady=20)
    
    # Botão para cancelar
    cancel_button = tk.Button(pagamento_window, text="Cancelar", bg="red", fg="white", 
                             font=("Arial", 10), command=pagamento_window.destroy)
    cancel_button.pack(pady=5)

# Botão para finalizar a compra
finalizar_button = tk.Button(carrinho_frame, text="Finalizar Compra", bg="blue", fg="white", 
                            font=("Arial", 10, "bold"), command=finalizar_compra)
finalizar_button.pack(pady=10)

# Atualizando a região visível
content_frame.update_idletasks() 
canvas.config(scrollregion=canvas.bbox("all"))

# Inicia o loop principal da interface gráfica
janela.mainloop()