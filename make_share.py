from PIL import Image,ImageDraw,ImageFont
W,H=1200,630
im=Image.new('RGB',(W,H),'#062b52'); d=ImageDraw.Draw(im)
d.line([(0,126),(230,126),(300,196),(540,196),(612,124),(892,124),(977,209),(1200,209)],fill='#1d5a88',width=3)
d.line([(70,520),(330,520),(400,450),(690,450),(765,525),(1095,525)],fill='#1d5a88',width=3)
d.ellipse((292,188,308,204),fill='#ffc400'); d.ellipse((757,517,773,533),fill='#ffc400')
d.ellipse((86,82,180,176),fill='#ffc400'); d.polygon([(142,92),(109,141),(132,141),(127,179),(162,123),(139,123)],fill='#062b52')
reg='/usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf'; bold='/usr/share/fonts/truetype/noto/NotoSansHebrew-Bold.ttf'
def rtl(text,xy,size,color,font=bold,anchor='ra'):
 f=ImageFont.truetype(font,size,layout_engine=ImageFont.Layout.RAQM)
 d.text(xy,text,font=f,fill=color,anchor=anchor,direction='rtl',language='he')
rtl('חשמל חיים',(1110,145),54,'white')
rtl('חשמלאי מוסמך בדימונה',(1110,255),76,'white')
rtl('עבודות חשמל לבית ועמדות טעינה',(1110,340),40,'#ffc400')
# tagline: drawn dot separators instead of U+2022 (Noto Sans Hebrew lacks the glyph)
f_reg=ImageFont.truetype(reg,31,layout_engine=ImageFont.Layout.RAQM)
phrases=['אבחון ברור','עבודה מדויקת','קשר ישיר']
space_w=f_reg.getlength(' ')
dot_r=4
cy=450+31*0.42  # bullet optical center for 31px ascender-anchored text
x=1110.0
for i,p in enumerate(phrases):
    d.text((x,450),p,font=f_reg,fill='#d9e6f1',anchor='ra',direction='rtl',language='he')
    x-=f_reg.getlength(p)
    if i<len(phrases)-1:
        x-=2*space_w
        d.ellipse((x-2*dot_r,cy-dot_r,x,cy+dot_r),fill='#d9e6f1')
        x-=2*dot_r+2*space_w
d.rounded_rectangle((830,505,1110,567),radius=8,fill='#ffc400')
f=ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf',28)
d.text((970,538),'052-439-7528',font=f,fill='#062b52',anchor='mm')
im.save('/downloads/share-fixed.png',optimize=True)
