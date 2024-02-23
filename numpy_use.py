
import matplotlib
import matplotlib.font_manager

mf_fn = sorted(matplotlib.font_manager.findSystemFonts(fontpaths='C:\\Windows\\Fonts', fontext='ttf'))
list_font = []
print("可用的系统字体：", len(mf_fn))
for i in mf_fn[0:365]:
    list_font.append(i)


print(list_font)
print("上传成功")
