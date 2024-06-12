from tkinter import *
import requests

def get_quote():
    """
    Fetch a new quote from the Kanye Rest API and update the canvas text.
    """
    try:
        # Make a request to the Kanye Rest API
        response = requests.get("https://api.kanye.rest")
        response.raise_for_status()  # Ensure we notice bad responses
        
        # Parse the JSON response
        data = response.json()
        quote = data["quote"]
        
        # Update the canvas with the new quote
        canvas.itemconfig(quote_text, text=quote)
    except requests.RequestException as e:
        # Handle any errors that occur during the request
        print(f"Error fetching quote: {e}")
        canvas.itemconfig(quote_text, text="Error fetching quote. Please try again.")

# Initialize the main application window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Create a canvas widget for the background and quote text
canvas = Canvas(width=300, height=500)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# Add a placeholder text for the quote
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Create a button with Kanye's image that fetches a new quote when clicked
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, width=220, height=240)
kanye_button.grid(row=1, column=0)

# Start the Tkinter main event loop
window.mainloop()
