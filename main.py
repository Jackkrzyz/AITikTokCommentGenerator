import tkinter as tk
from pyperclip import copy
from download_mp3 import download_mp3
import openai_implementation, os
window = tk.Tk()
window.title("AI TikTok Comment Generator")
window.geometry("400x500")


frame = tk.Frame(window)
frame.pack()


def generate_comment():
  '''Generates a comment and prints it to the output box'''
  output_box.delete("1.0","end")
  video_link=link_entry.get()
  link_entry.delete("0","end")
  
  api_key = api_entry.get()
  tone = mood_value_inside.get()
  grammar_quality = grammar_value_inside.get()

  print("link", video_link)
  mp3name = download_mp3(video_link)
  
  file_dir = os.path.dirname(os.path.realpath('__file__'))
  file_name = os.path.join(file_dir, f'Content/{mp3name}.mp3')
  output_box.insert( "1.0", openai_implementation.comment(openai_implementation.transcribe(file_name, api_key), tone, grammar_quality))


def copy_text():
  '''Copies the text within the output text box (doesn't work on replit)'''
  copy(output_box.get("1.0", "end"))



# Video Link
api_key_frame = tk.LabelFrame(frame, text="OpenAI API Key")
api_key_frame.grid(row= 0, column= 0, pady=10)

api_entry=tk.Entry(api_key_frame)
api_entry.pack(padx=10,pady=10)

video_link_frame = tk.LabelFrame(frame, text="TikTok Video Link")
video_link_frame.grid(row= 1, column= 0, pady=10)

link_entry=tk.Entry(video_link_frame)
link_entry.pack(padx=10,pady=10)

# Configuration
config_frame = tk.LabelFrame(frame, text="Configuration")
config_frame.grid(row=2, column=0)

mood_label = tk.Label(config_frame, text="Tone")
mood_label.grid(row=0, column=0)

mood_value_inside = tk.StringVar(config_frame)
mood_value_inside.set("Select an Option")
mood_options = [ "Funny", "Insightful", "Angry", "Sympathetic"]
mood_select = tk.OptionMenu(config_frame, mood_value_inside, *mood_options)
mood_select.grid(row=1, column=0,padx=10, pady=10)

grammar_label = tk.Label(config_frame, text="Grammar")
grammar_label.grid(column=1, row=0)

grammar_value_inside = tk.StringVar(config_frame)
grammar_value_inside.set("Select an Option")
grammar_options = ["Improper", "Proper"]
grammar_select = tk.OptionMenu(config_frame, grammar_value_inside, *grammar_options)
grammar_select.grid(row=1, column=1, padx=10, pady=10)

# Output
output_frame = tk.LabelFrame(frame, text="Output")
output_frame.grid(row=3, column=0)

generate_button = tk.Button(output_frame, text="Generate", command=generate_comment)
generate_button.grid(row=0, column = 0 , padx=10, pady=10)

copy_button= tk.Button(output_frame, text="Copy Text", command=copy_text)
copy_button.grid(row=0, column = 2, padx=10, pady=10)
output_box = tk.Text(output_frame,height= 10, width= 25)
output_box.grid(row = 1, column = 0, columnspan=3)



window.mainloop()