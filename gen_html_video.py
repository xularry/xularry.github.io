import os
import argparse
import random

def gen_html(data_dirs, out_dir, scale):
  groups = [os.path.basename(o) for o in data_dirs]
  out_path = os.path.join(out_dir, 'index.html')
  print('save', out_path)
  title = 'Video user study'
  fout = open(out_path, 'w')
  lines = []
  lines.append('<!DOCTYPE html>') 
  lines.append('<html>')
  lines.append('<head>')
  lines.append('<title>%s</title>' % title)
  
  lines.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
  lines.append('<script src="FileSaver.js"></script>')
  lines.append('<style>')
  lines.append('* {box-sizing: border-box}')
  lines.append('body {font-family: Verdana, sans-serif; margin:0}')
  lines.append('.mySlides {display: none}')
  lines.append('img {vertical-align: middle;}')
  lines.append('.slideshow-container {')
  lines.append('  max-width: 1920px;')
  lines.append('  position: relative;')
  lines.append('  margin: auto;')
  lines.append('}')
  lines.append('.prev, .next {')
  lines.append('  cursor: pointer;')
  lines.append('  position: absolute;')
  lines.append('  top: 50%;')
  lines.append('  width: auto;')
  lines.append('  padding: -10px;')
  lines.append('  margin-top: -22px;')
  lines.append('  color: blue;')
  lines.append('  font-weight: bold;')
  lines.append('  font-size: 38px;')
  lines.append('  transition: 0.6s ease;')
  lines.append('  border-radius: 0 3px 3px 0;')
  lines.append('}')
  lines.append('.next {')
  lines.append('  right: 0;')
  lines.append('  border-radius: 3px 0 0 3px;')
  lines.append('}')
  lines.append('.prev:hover, .next:hover {')
  lines.append('  background-color: rgba(0,0,0,0);')
  lines.append('}')
  lines.append('.text {')
  lines.append('  text-align: center;')
  lines.append('}')

  lines.append('.numbertext {')
  lines.append('  color: #f2f2f2;')
  lines.append('  font-size: 12px;')
  lines.append('  padding: 8px 12px;')
  lines.append('  position: absolute;')
  lines.append('  top: 0;')
  lines.append('}')
  lines.append('.dot {')
  lines.append('  cursor: pointer;')
  lines.append('  height: 15px;')
  lines.append('  width: 15px;')
  lines.append('  margin: 0 2px;')
  lines.append('  background-color: #bbb;')
  lines.append('  border-radius: 5%;')
  lines.append('  display: inline-block;')
  lines.append('  transition: background-color 0.6s ease;')
  lines.append('}')
  lines.append('.active, .dot:hover {')
  lines.append('  background-color: #717171;')
  lines.append('}')
  lines.append('.fade {')
  lines.append('  -webkit-animation-name: fade;')
  lines.append('  -webkit-animation-duration: 1.5s;')
  lines.append('  animation-name: fade;')
  lines.append('  animation-duration: 1.5s;')
  lines.append('}')

  lines.append('@-webkit-keyframes fade {')
  lines.append('  from {opacity: .4} ')
  lines.append('  to {opacity: 1}')
  lines.append('}')

  lines.append('@keyframes fade {')
  lines.append('  from {opacity: .4} ')
  lines.append('  to {opacity: 1}')
  lines.append('}')
  lines.append('@media only screen and (max-width: 300px) {')
  lines.append('  .prev, .next,.text {font-size: 11px},')
  lines.append('   .column {')
  lines.append('        width: 100%;')
  lines.append('    }')
  lines.append('}')

  lines.append('.column {')
  lines.append('    float: left;')
  lines.append('    width: 32%;')
  lines.append('    padding: 5px;')
  lines.append('}')

  lines.append('.row::after {')
  lines.append('    content: "";')
  lines.append('    clear: both;')
  lines.append('    display: table;')
  lines.append('}')

  lines.append('#div_in {')
  lines.append('    float: left;')
  lines.append('    width: 480px;')
  lines.append('    height: 256px;')
  lines.append('    margin: 1px;')
  lines.append('    padding: 1px;')
  lines.append('    border: 1px dotted black;')
  lines.append('}')

  lines.append('.div {')
  lines.append('    float: left;')
  lines.append('    width: 480px;')
  lines.append('    height: 270px;')
  lines.append('    margin: 1px;')
  lines.append('    padding: 1px;')
  lines.append('    border: 1px solid black;')
  lines.append('}')
  lines.append('</style>')
  lines.append('</head>')

  lines.append('<body>')
  lines.append('<div class="slideshow-container">')

  # lines.append('<p>I\'m KD')
  lines.append('<p>Super-Resolution User Study</p>')
  lines.append('<p>请将视觉效果最好的第一、二、三张图依次拖入最下方的top1、top2、top3的方框中。</p>')
  lines.append('<p>当图较小区分不出区别时，鼠标右键依次点击图像->在新的标签页中打开可查看大图->Ctrl(或command)+数字键可以快捷切换标签便于比较。</p>')
  
  data_dir = data_dirs[0]
  items = [o for o in os.listdir(data_dir)]

  items.sort()
  divin_id=0
  div_id=0
  for item in items:
    print("item:", item)
    rawname, ext = os.path.splitext(item)
    if ext != '.png':  # .m4v
      continue
    else:
      lines.append('<div class="mySlides fade">')

    lines.append('<div class="row">')

    gourps = random.shuffle(groups)

    for g in groups: 
      print("g:", g)
      video_name = g +'/'+item
      divin_id += 1
      lines.append('<div class="column">')
      td0 = '<div id="divIn{}" ondrop="drop(event)" ondragover="allowDrop(event)">'.format(divin_id)
      lines.append(td0)
      # td1 = '<video autoplay muted draggable=true" autoplay="autoplay" ondragstart="drag(event)" id="{}video{}" style="width:70%" controls loop>'.format(g+'/', divin_id)
      # td1 = '<draggable=true"  ondragstart="drag(event)" id="{}video{}" style="width:70%">'.format(g+'/', divin_id)
      #lines.append(td1)
      #td2 = '<img src="{}" type="image/png; width: 100px; height: 100px;">'.format(video_name)
      #td2 = '<img src="{}" style="width: 1000px; height: 500px;">'.format(video_name)
      #td2 = '<img src="{}" style="width: 500px; height: 500px; object-fit: contain;">'.format(video_name)
      # td2 = '<img src="{}" draggable=true ondragstart="drag(event)" id="{}video{}" style="width: 500px; height: 500px; object-fit: contain;">'.format(video_name, g+'/', divin_id)
      td2 = '<img src="{}" draggable=true ondragstart="drag(event)" id="{}video{}" style="width: 500px; height: auto; object-fit: contain;">'.format(video_name, g+'/', divin_id)
      lines.append(td2)
      # lines.append('</video>')
      lines.append('</div>')
      lines.append('</div>')
    lines.append('</div>')

    lines.append('<div class="row">')
    for g in groups:
      div_id += 1
      lines.append('<div class="column">')
      #td1 = '<div class="div" id="div{}" ondrop="drop(event)" ondragover="allowDrop(event)" height="500" width="500">'.format(div_id)
      td1 = '<div class="div" id="div{}" ondrop="drop(event)" ondragover="allowDrop(event)" style="width: 500px; height: 500px; object-fit: contain;">'.format(div_id)
      lines.append(td1)
      lines.append('<input type="hidden" value="t1"/>')
      lines.append('</div>')
      lines.append('</div>')
      if div_id % 3==0:
        break
    lines.append('</div>')

    lines.append('<div class="row">')
    g_index=0
    for g in groups:
      g_index += 1
      lines.append('<div class="column">')
      td1 = '<div class="text">Top {}</div>'.format(str(g_index))
      lines.append(td1)
      lines.append('</div>')
      if g_index % 3==0:
        break
    lines.append('</div>')
    lines.append('</div>')
  
  lines.append('<div class="mySlides fade">')
  lines.append('<h2>Complete : Thank you for your time! Please submit the results as a text file.</h2>')
  lines.append('<input type="button" width="400" height="80" align="center" onclick="myFunction()" value="Submit Result">')
  lines.append('</div>')
  lines.append('</div>')

  lines.append('</div>')

  lines.append('<a class="prev" onclick="plusSlides(-1)">&#10094;</a>')
  lines.append('<a class="next" onclick="plusSlides(1)">&#10095;</a>')

  lines.append('</div>')
  lines.append('<br>')
  lines.append('<div style="text-align:center">')
  lines.append('  <span class="dot" onclick="currentSlide(1)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(2)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(3)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(4)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(5)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(6)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(7)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(8)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(9)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(10)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(11)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(12)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(13)"></span>')
  lines.append('  <span class="dot" onclick="currentSlide(14)"></span>')
  lines.append(' <span class="dot" onclick="currentSlide(15)"></span>')
  lines.append('</div>')


  lines.append('<script>')

  lines.append('var slideIndex = 1;')
  lines.append('showSlides(slideIndex);')

  lines.append('function plusSlides(n) {')
  lines.append('  showSlides(slideIndex += n);')
  lines.append('}')

  lines.append('function currentSlide(n) {')
  lines.append('  showSlides(slideIndex = n);')
  lines.append('}')

  lines.append('function showSlides(n) {')
  lines.append('  var i;')
  lines.append('  var slides = document.getElementsByClassName("mySlides");')
  lines.append('  var dots = document.getElementsByClassName("dot");')
  lines.append('  if (n > slides.length) {slideIndex = 1}    ')
  lines.append('  if (n < 1) {slideIndex = slides.length}')
  lines.append('  for (i = 0; i < slides.length; i++) {')
  lines.append('      slides[i].style.display = "none";  ')
  lines.append('  }')
  lines.append('  for (i = 0; i < dots.length; i++) {')
  lines.append('     dots[i].className = dots[i].className.replace(" active", "");')
  lines.append('  }')
  lines.append('  slides[slideIndex-1].style.display = "block";  ')
  lines.append('  dots[slideIndex-1].className += " active";')
  lines.append('}')

  lines.append('function allowDrop(ev) {')
  lines.append('    ev.preventDefault();')
  lines.append('}')

  lines.append('function drag(ev) {')
  lines.append('    ev.dataTransfer.setData("text", ev.target.id);')
  lines.append('}')

  lines.append('function drop(ev) {')
  lines.append('    ev.preventDefault();')
  lines.append('    var data = ev.dataTransfer.getData("text");')
  lines.append('    ev.target.appendChild(document.getElementById(data));')
      
  lines.append('  if (ev.target.id != "div_in")')
  lines.append('  {')
  lines.append('    var divNode = document.getElementById(ev.target.id);')
  lines.append('    var inputNodes = divNode.getElementsByTagName('+'\'input\''+');')
  lines.append('    inputNodes[0].value = data')
  lines.append('  }')
  lines.append('}')

  lines.append('function myFunction() {')
  lines.append('  var id;')
  lines.append('  var result = "";')
  # lines.append('  for (id = 1; id <= 9; id++) {')
  print(items)
  total_number_text = ('  for (id = 1; id <= {}; id++)'.format(len(items)*3))+' {'
  lines.append(total_number_text)
  lines.append('    divName = "div" + id')
  lines.append('    var divNode = document.getElementById(divName);')
  lines.append('    var inputNodes = divNode.getElementsByTagName('+'\'input\''+');')
  lines.append('    result = result + divName + " " + inputNodes[0].value' + '+'+ '"\\' + 'n"')
  lines.append('  }')
  lines.append('  var file = new File([result], "video_prop_yourname.txt", {type: "text/plain;charset=utf-8"});')
  lines.append('  saveAs(file);')
  lines.append('}')
  lines.append('</script>')

  lines.append('</body>')
  lines.append('<html>')

  fout.write('%s' % ('\n'.join(lines)))
  fout.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dirs', nargs='+', type=str)
  parser.add_argument('--out_dir', type=str)
  parser.add_argument('--scale', type=float, default=1.0)

  args = parser.parse_args()
  if args.data_dirs is not None and len(args.data_dirs) > 0 and args.out_dir is not None:
    gen_html(args.data_dirs, args.out_dir, args.scale)
  else:
    print('Example: python gen_html_video.py --out_dir . --data_dirs input gt single_0930')
