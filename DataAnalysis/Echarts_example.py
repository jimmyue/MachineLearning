from pyecharts import Graph
from pyecharts import Line
from pyecharts import Liquid
from pyecharts import Map
from pyecharts import Parallel
#初始化数据
nodes=[{'name':'结点1','symbolSize':10},
	   {'name':'结点2','symbolSize':20},
	   {'name':'结点3','symbolSize':30},
	   {'name':'结点4','symbolSize':40},
	   {'name':'结点5','symbolSize':50},
	   {'name':'结点6','symbolSize':40},
	   {'name':'结点7','symbolSize':30},
	   {'name':'结点8','symbolSize':20}]
attr=['衬衫','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1=[5,20,36,10,10,100]
v2=[55,60,16,20,15,80]
# 关系图,修改为True查看
if False:
	links=[]
	for i in nodes:
		for j in nodes:
			links.append({'source':i.get('name'),'target':j.get('name')})
	graph=Graph('关系图-环形布局示例')
	graph.add('',nodes,links,is_label_show=True,repulsion=8000,layout='circular',label_text_color=None)
	graph.show_config()
	graph.render()
# 折线图,修改为True查看
if False:
	line=Line('折线图示例')
	line.add('商家A',attr,v1,mark_point=['min','average'])
	line.add('商家B',attr,v2,is_smooth=True,mark_point=['max','average'])
	line.show_config()
	line.render()
# 阶梯图,修改为True查看
if False:
	line=Line('折线图-阶梯图示例')
	line.add('商家A',attr,v1,is_strp=True,is_label_show=True)
	line.show_config()
	line.render()
# 面积图,修改为True查看
if False:
	line=Line('折线图-面积图示例')
	line.add('商家A',attr,v1,is_fill=True,line_opacity=0.2,area_opacity=0.4,symbol=None)
	line.add('商家B',attr,v2,is_fill=True,area_color='#000',area_opacity=0.3,is_smooth=True)
	line.show_config()
	line.render()
# 圆形水球图,修改为True查看
if False:
	liquid=Liquid('水球-圆形图示例')
	liquid.add('Liquid',[0.8,0.2],is_liquid_outline_show=True)
	liquid.show_config()
	liquid.render()
# 砖石水球图,修改为True查看
if False:
	liquid=Liquid('水球-砖石图示例')
	liquid.add('Liquid',[0.8,0.2],is_liquid_outline_show=True,shape='diamond')
	liquid.show_config()
	liquid.render()
# 中国地图,修改为True查看
value=[10,20,30,40,50,60,70,80,90,100]
prov=['广西','广东','福建','湖南','江西','云南','贵州','浙江','安徽','湖北']
if False:
	map=Map('Map结合Visualmap示例',width=1200,height=600)
	map.add('',prov,value,maptype='china',is_visualmap=True,visual_text_color='#000')
	map.show_config()
	map.render()
# 广东地图,修改为True查看
city=['汕头市','湛江市','茂名市','江门市','惠州市','中山市','东莞市','佛山市','深圳市','广州市']
if False:
	map=Map('广东地图示例',width=1200,height=600)
	map.add('',city,value,maptype='广东',is_visualmap=True,visual_text_color='#000')
	map.show_config()
	map.render()
# 平行坐标系,修改为True查看
c_schema=[{'dim':0,'name':'data'},
		  {'dim':1,'name':'AQI'},
		  {'dim':2,'name':'pm2.5'},
		  {'dim':3,'name':'pm10'},
		  {'dim':4,'name':'co'},
		  {'dim':5,'name':'no2'},
		  {'dim':6,'name':'co2'},
		  {'dim':7,'name':'等级','type':'category','data':['优','良','轻度污染','中度污染','重度污染','严重污染']}]
data=[[1,91,45,125,0.82,34,23,'良'],
      [2,65,45,125,0.82,34,23,'良'],
      [3,83,45,125,0.82,34,23,'良'],
      [4,102,45,125,0.82,34,23,'轻度污染'],
      [5,88,45,125,0.82,34,23,'轻度污染'],
      [6,89,45,125,0.82,34,23,'轻度污染'],
      [7,81,45,125,0.82,34,23,'轻度污染'],
      [8,97,45,125,0.82,34,23,'良'],
      [9,102,45,125,0.82,34,23,'良'],
      [10,111,45,125,0.82,34,23,'良'],
      [11,98,45,125,0.82,34,23,'轻度污染'],
      [12,89,45,125,0.82,34,23,'良'],
      [13,88,45,125,0.82,34,23,'良'],
      [14,81,45,125,0.82,34,23,'轻度污染']]
if True:
	parallel=Parallel('平行坐标系-用户自定义指示器')
	parallel.config(c_schema=c_schema)
	parallel.add('Parallel',data)
	parallel.show_config()
	parallel.render()