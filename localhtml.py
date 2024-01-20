root = tk.Tk()
root.resizable(False, False)
root.geometry("450x350")
def paint():
    def start():
        name = entry.get()
        if not name.startswith("https://"):
            name= "https://" + name
        html_code = urllib.request.urlopen(name).read().decode("utf-8")
        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(html_code.encode())
        def run():
            def mess():
                messagebox.showinfo(message="localhost:" + str(port))
                root.destroy()
            port = random.randint(1000, 9999)
            server_address = ('', port)  # Выберите любой доступный порт
            httpd = HTTPServer(server_address, RequestHandler)
            multiprocessing.Process(target=mess()).start()
            stop = multiprocessing.Process(target=quit)
            server =multiprocessing.Process(target=httpd.serve_forever())
            server.start()
        run()
    entry = tk.Entry(root)
    button= tk.Button(root, text="Запустить", command=start)
    entry.place(x=150, y =140)
    button.place(x=175, y=160)
paint()
root.mainloop()
