import json
import tkinter as tk
from tkinter import scrolledtext

import requests

# Määritä agentin ID ja API:n URL
AGENT_ID = (
    "agent-78856c01-4e81-4b42-a180-dbbf0ceb58da"  # Korvaa omalla agentin ID:lläsi
)
API_URL = f"http://localhost:8283/v1/agents/{AGENT_ID}/messages"

# Jos käytössä on salasanasuojaus, määritä Authorization-otsake
HEADERS = {
    "Content-Type": "application/json",
    # "Authorization": "Bearer YOUR_PASSWORD"  # Poista kommentti ja korvaa omalla salasanallasi, jos tarvitaan
}


class LettaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Letta-AI Keskustelu")

        # Yläpaneeli, jossa on virtanappula
        top_frame = tk.Frame(root)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        power_button = tk.Button(top_frame, text="⏻", command=self.root.quit)
        power_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Keskustelualue
        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state="disabled", height=20
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Syötekenttä ja Lähetä-painike
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.entry_field = tk.Entry(bottom_frame)
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.entry_field.bind("<Return>", self.send_message)

        send_button = tk.Button(bottom_frame, text="Lähetä", command=self.send_message)
        send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        user_message = self.entry_field.get().strip()
        if not user_message:
            return

        self.display_message("Sinä", user_message)
        self.entry_field.delete(0, tk.END)

        payload = {"messages": [{"role": "user", "content": user_message}]}

        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            response.raise_for_status()
            data = response.json()

            # Etsi ensimmäinen assistant_message-tyyppinen viesti
            assistant_reply = None
            for message in data.get("messages", []):
                if message.get("message_type") == "assistant_message":
                    assistant_reply = message.get("content")
                    break

            if assistant_reply:
                self.display_message("Letta", assistant_reply)
            else:
                self.display_message("Letta", "Ei vastausta.")

        except requests.exceptions.RequestException as e:
            self.display_message("Virhe", f"HTTP-pyyntö epäonnistui: {e}")

    def display_message(self, sender, message):
        self.chat_area.configure(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    gui = LettaGUI(root)
    root.mainloop()
