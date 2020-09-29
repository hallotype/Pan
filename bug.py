fontFile = "Pan_drawbotBug.ttf"
font(fontFile,1000)
print(listFontVariations())
fontVariations(ANGL=210, wght=30, SHAP=1, STEP=40)
print(fontVariations())
text("A",(100,100))

newPage(1000,1000)
font(fontFile,1000)
fontVariations(ANGL=0, wght=30, SHAP=2, STEP=60)
print(fontVariations())
text("A",(100,100))
