import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class Elevator:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.maintenance_records = []
        self.repair_records = []

    def add_maintenance_record(self, date, description):
        record = {'date': date, 'description': description}
        self.maintenance_records.append(record)

    def add_repair_record(self, date, description):
        record = {'date': date, 'description': description}
        self.repair_records.append(record)

    def get_maintenance_records(self):
        return self.maintenance_records

    def get_repair_records(self):
        return self.repair_records

    def __str__(self):
        return f"Elevator ID: {self.id}, Location: {self.location}"

class ElevatorManagementSystem:
    def __init__(self):
        self.elevators = {}

    def add_elevator(self, id, location):
        if id not in self.elevators:
            self.elevators[id] = Elevator(id, location)
        else:
            return f"Elevator with ID {id} already exists."

    def record_maintenance(self, id, date, description):
        if id in self.elevators:
            self.elevators[id].add_maintenance_record(date, description)
        else:
            return f"No elevator found with ID {id}."

    def record_repair(self, id, date, description):
        if id in self.elevators:
            self.elevators[id].add_repair_record(date, description)
        else:
            return f"No elevator found with ID {id}."

    def get_elevator_info(self, id):
        if id in self.elevators:
            elevator = self.elevators[id]
            return {
                'info': str(elevator),
                'maintenance_records': elevator.get_maintenance_records(),
                'repair_records': elevator.get_repair_records()
            }
        else:
            return f"No elevator found with ID {id}."

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elevator Maintenance and Repair Tracking System")
        self.geometry("600x400")
        self.system = ElevatorManagementSystem()
        self.create_widgets()

    def create_widgets(self):
        self.label_id = tk.Label(self, text="Elevator ID")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)

        self.entry_id = tk.Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_location = tk.Label(self, text="Location")
        self.label_location.grid(row=1, column=0, padx=10, pady=10)

        self.entry_location = tk.Entry(self)
        self.entry_location.grid(row=1, column=1, padx=10, pady=10)

        self.button_add_elevator = tk.Button(self, text="Add Elevator", command=self.add_elevator)
        self.button_add_elevator.grid(row=2, column=0, columnspan=2, pady=10)

        self.button_record_maintenance = tk.Button(self, text="Record Maintenance", command=self.record_maintenance)
        self.button_record_maintenance.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_record_repair = tk.Button(self, text="Record Repair", command=self.record_repair)
        self.button_record_repair.grid(row=4, column=0, columnspan=2, pady=10)

        self.button_get_info = tk.Button(self, text="Get Elevator Info", command=self.get_elevator_info)
        self.button_get_info.grid(row=5, column=0, columnspan=2, pady=10)

    def add_elevator(self):
        id = self.entry_id.get()
        location = self.entry_location.get()
        result = self.system.add_elevator(id, location)
        if result:
            messagebox.showinfo("Info", result)
        else:
            messagebox.showinfo("Info", f"Elevator {id} added successfully.")

    def record_maintenance(self):
        id = self.entry_id.get()
        date = simpledialog.askstring("Input", "Enter Maintenance Date:")
        description = simpledialog.askstring("Input", "Enter Maintenance Description:")
        result = self.system.record_maintenance(id, date, description)
        if result:
            messagebox.showinfo("Info", result)
        else:
            messagebox.showinfo("Info", "Maintenance recorded successfully.")

    def record_repair(self):
        id = self.entry_id.get()
        date = simpledialog.askstring("Input", "Enter Repair Date:")
        description = simpledialog.askstring("Input", "Enter Repair Description:")
        result = self.system.record_repair(id, date, description)
        if result:
            messagebox.showinfo("Info", result)
        else:
            messagebox.showinfo("Info", "Repair recorded successfully.")

    def get_elevator_info(self):
        id = self.entry_id.get()
        info = self.system.get_elevator_info(id)
        if isinstance(info, dict):
            message = f"Info: {info['info']}\n\nMaintenance Records:\n"
            for record in info['maintenance_records']:
                message += f"{record['date']}: {record['description']}\n"
            message += "\nRepair Records:\n"
            for record in info['repair_records']:
                message += f"{record['date']}: {record['description']}\n"
            messagebox.showinfo("Elevator Info", message)
        else:
            messagebox.showinfo("Info", info)

if __name__ == "__main__":
    app = Application()
    app.mainloop()

