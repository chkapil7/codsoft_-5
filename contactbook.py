import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create buttons
        self.add_button = tk.Button(self.main_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_button = tk.Button(self.main_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.main_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.update_button = tk.Button(self.main_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=3, padx=5, pady=5)

        self.delete_button = tk.Button(self.main_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=4, padx=5, pady=5)

        # Create treeview for displaying contacts
        self.tree = ttk.Treeview(self.main_frame, columns=("Name", "Phone", "Email", "Address"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.grid(row=1, column=0, columnspan=5, sticky="nsew")

        # Add scrollbar
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=5, sticky="ns")

    def add_contact(self):
        contact = self.get_contact_info()
        if contact:
            self.contacts.append(contact)
            self.view_contacts()

    def view_contacts(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for contact in self.contacts:
            self.tree.insert("", "end", values=contact)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
        if search_term:
            found_contacts = [c for c in self.contacts if search_term.lower() in c[0].lower() or search_term in c[1]]
            for i in self.tree.get_children():
                self.tree.delete(i)
            for contact in found_contacts:
                self.tree.insert("", "end", values=contact)

    def update_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Update Contact", "No contact selected!")
            return
        selected_contact = self.tree.item(selected_item[0], 'values')
        updated_contact = self.get_contact_info()
        if updated_contact:
            self.contacts = [updated_contact if c == selected_contact else c for c in self.contacts]
            self.view_contacts()

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Delete Contact", "No contact selected!")
            return
        selected_contact = self.tree.item(selected_item[0], 'values')
        self.contacts.remove(selected_contact)
        self.view_contacts()

    def get_contact_info(self):
        name = simpledialog.askstring("Contact Info", "Enter name:")
        phone = simpledialog.askstring("Contact Info", "Enter phone number:")
        email = simpledialog.askstring("Contact Info", "Enter email:")
        address = simpledialog.askstring("Contact Info", "Enter address:")
        if name and phone and email and address:
            return (name, phone, email, address)
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
