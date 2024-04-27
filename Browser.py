import tkinter as tk
import requests

def send_request():
    url = entry_url.get()
    method = var_method.get()
    data = entry_data.get() if method == "POST" else None
    username = entry_username.get()  
    password = entry_password.get()  
    
    if not username =="nadia" or not password=="12345":
    
        text_response.config(state=tk.NORMAL)
        text_response.delete('1.0', tk.END)
        text_response.insert(tk.END, "Error: Please enter username and password")
        text_response.config(state=tk.DISABLED)
        return

    auth = (username, password)
    cookies = {'session_id': 'your_session_id'}
    if method == "GET":
        headers = {'Cache-Control': 'max-age=3600'} 
    elif method == "POST":
        headers = {'Cache-Control': 'no-cache'}  
    headers['X-Custom-Header'] = 'Custom Value'
    try:
        if method == "GET":
            response = requests.get(url, auth=auth, cookies=cookies, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=data, auth=auth, cookies=cookies, headers=headers)
        text_response.config(state=tk.NORMAL)
        text_response.delete('1.0', tk.END)
        text_response.insert(tk.END, response.text)
        text_response.config(state=tk.DISABLED)
    except requests.exceptions.RequestException as e:
        text_response.config(state=tk.NORMAL)
        text_response.delete('1.0', tk.END)
        text_response.insert(tk.END, f"Error: {str(e)}")
        text_response.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Browser")


label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*") 
entry_password.pack()

label_url = tk.Label(root, text="URL:")
label_url.pack()

entry_url = tk.Entry(root)
entry_url.pack()

label_method = tk.Label(root, text="Method:")
label_method.pack()

var_method = tk.StringVar(root)
var_method.set("GET")
option_menu = tk.OptionMenu(root, var_method, "GET", "POST")
option_menu.pack()

label_data = tk.Label(root, text="Data (for POST):")
label_data.pack()

entry_data = tk.Entry(root)
entry_data.pack()

button_send = tk.Button(root, text="Send Request", command=send_request)
button_send.pack()

text_response = tk.Text(root, height=20, width=40)
text_response.config(state=tk.DISABLED)
text_response.pack()

root.mainloop()
