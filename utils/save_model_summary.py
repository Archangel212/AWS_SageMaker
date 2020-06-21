from PIL import ImageDraw,ImageDraw2,ImageFont, Image, ImageOps

def save_model_summary(model, filepath,  padding=25, font=ImageFont.load_default()):
  string_list = []
  model.summary(print_fn=lambda x: string_list.append(x))
  model_summary = "\n".join(string_list)

  str_length = len(model_summary)
  img = Image.new("RGB",(str_length,str_length), color="white" )

  d = ImageDraw.Draw(img)
  txtWidth, txtHeight = d.textsize(model_summary)
  d.text((padding,padding), model_summary, fill=(0,0,0,100), font=font)
  area_cropped = (0,0,(str_length-txtWidth)-2*padding, (str_length-txtHeight)-2*padding)
  img_cropped = ImageOps.crop(img,area_cropped)

  f = ImageFont.load_default()
  f.font.getsize(model_summary)
  # pyplot.figure(figsize=(10,10))
  # pyplot.imshow(img_cropped)
  img_cropped.save(filepath)
  # print(txtWidth, txtHeight,str_length,img_cropped.size,f.font.getsize(model_summary))