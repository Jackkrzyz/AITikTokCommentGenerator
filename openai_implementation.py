import openai, json

def transcribe(file):
  f = open('api_key.json', 'r')
  key = json.load(f)
  openai.api_key = key['api_key']
  audio_file= open(file, "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file)["text"]
  return transcript


def comment(transcription, tone, grammar_style):
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[

        {"role": "user", "content": f"Create a {tone} TikTok comment of less than 100 characters with {grammar_style} grammar for a video with the following transcript: {transcription}"},

    ]
  )
  return response['choices'][0]['message']['content']