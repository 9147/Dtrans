from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import requests
from gtts import gTTS

model_name = "facebook/nllb-200-distilled-600M"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

translator = pipeline('translation', model=model, tokenizer=tokenizer, max_length=400)

def textModel(TEXT,src_lang_code,tgt_lang_code):
  def TextToSpeech(Text_Audio):
    english_language = "en"
    Indian_gtts_object = gTTS(text = Text_Audio,
                          lang = english_language,
                          slow = True,tld='co.in')
    Indian_gtts_object.save("/content/timepass.wav")

  input_text = TEXT

  translated_text = translator(input_text, src_lang=src_lang_code, tgt_lang=tgt_lang_code)[0]["translation_text"]
  print("Translated Text:")
  print(translated_text)
  # TextToSpeech(translated_text)

