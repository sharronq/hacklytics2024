# IMPORT STATEMENTS
from home import page_1
from chatbot import *
import taipy as tp
# from PIL import Image

# image = Image.open("logo.png")
# page = """
# <|navbar|>
# Placeholder
# """

# MAIN
if __name__ == "__main__":
    tp.Core().run()
    # content = image
    pages = {
        "Home": page_1,
        "Chatbot": page_2
    }

    gui = tp.Gui(pages = pages)
    gui.run(use_reloader=True, port=5001)