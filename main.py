# IMPORT STATEMENTS
from home import page_1
import taipy as tp

page = """
<|navbar|>
Placeholder
"""

# MAIN
if __name__ == "__main__":
    tp.Core().run()
    pages = {
        "Home": page_1,
        "Chatbot": page
    }

    gui = tp.Gui(pages = pages)
    gui.run(use_reloader=True, port=5001)