import tkinter as tk
from plyer import notification

class DeliveryApp:
    def __init__(self, master):
        self.master = master
        master.title("Delivery App")
        master.geometry("400x200")

        self.label = tk.Label(master, text="Delivery App")
        self.label.pack(pady=10)

        self.notification_button = tk.Button(master, text="Notify", command=self.show_notification)
        self.notification_button.pack(pady=10)

    def show_notification(self):
        title = "New Delivery"
        message = "You have a new delivery request."

        # Trigger a desktop notification
        notification.notify(
            title=title,
            message=message,
            app_name="Delivery App",
            app_icon=None,  # You can provide a path to an icon if desired
            timeout=10  # Notification will automatically disappear after 10 seconds
        )

def main():
    root = tk.Tk()
    app = DeliveryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
